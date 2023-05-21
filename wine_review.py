# -*- coding: utf-8 -*-
"""
Package lpvpy : python for LPV (lapassionduvin.com)

Module transpose_reviews for the transposition of wine tasting reviews
    Inputs are text files containing several reviews of the same wine list, each review written by a single author
    Outputs are text files, one for each wine, containing reviews from all authors

Copyright (C) 2023 Mathias Bouquerel
mbouquerel (arobas) yahoo (point) fr
https://github.com/TheGeorgeAbitbol

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import io
import os.path
import re


# Generic input / output functions

def import_txt_as_list(input_file):
    """
    Import a text file as a list of strings
    :param input_file: Path of the input text file
    :return: a list
    """
    with io.open(input_file, 'r', encoding='utf8') as text_file:
        all_lines = text_file.readlines()
    text_list = [line.strip() for line in all_lines]
    return text_list


def export_list_as_txt_file(output_file, output_list):
    """
    Export a list of string as a text file
    Each element of the list is a line of the text file
    :param output_file: path of the output text file
    :param output_list: list to be exported
    :return: None
    """
    output_txt = str('\n'.join(output_list))
    with io.open(output_file, 'w', encoding='utf8') as text_file:
        text_file.write(output_txt)


def dict_from_text_files(directory):
    """
    Extract data from text files stored in directory
    Generate a dictionary containing filenames as keys and files' content as values
    :param directory: path of the directory containing the text files
    :return: a dictionary
    """
    dict_review = {}
    for text_file in os.listdir(directory):
        file_name = text_file.rsplit('.')[0]
        file_path = os.path.join(directory, text_file)
        with io.open(file_path, 'r', encoding='utf8') as file:
            all_lines = file.readlines()
        dict_review[file_name] = [line.strip() for line in all_lines]
        # use import txt_as_list() !
    return dict_review


# Specific wine review functions

def is_a_wine_name_string(string):
    """
    Use regular expression package to detect if 'Vin X' is in the string (X can be literally 'X' or a number)
    :param string: the input string
    :return: a boolean
    """
    reg_str = 'Vin [0123456789X]{1}'
    test = re.search(reg_str, string)
    return bool(test)


def extract_wine_list(review_as_a_list):
    """
    Read a review as a list of string and extract a list of strings corresponding to wine names,
    the list of line index, and the number of wines
    :param review_as_a_list: wine tasting review stored as list of strings
    :return: list of wine names as strings, list of the row id where the wine review starts, and number of wines
    """
    wine_list = []
    id_list = []
    picture_list = []
    for ii, line in enumerate(review_as_a_list):
        if is_a_wine_name_string(line):
            wine_list.append(line)
            id_list.append(ii)
            if '[attachment=' in review_as_a_list[ii-1]:
                picture_list.append(review_as_a_list[ii-1])
            elif '[attachment=' in review_as_a_list[ii+1]:
                picture_list.append(review_as_a_list[ii+1])
            else:
                picture_list.append(None)
    return wine_list, id_list, picture_list


# Main function for wine review transposition

def transpose_wine_reviews(review_dir, author_ref, header):
    """
    Main function for the transposition of wine tasting reviews from one review per author to one review per wine
    All files containing wine tasting reviews per author named 'author_name' shall be named author_name.txt
    One review is used to get the wine names : the one name named author-ref.txt
    All wine tasting reviews shall contain a paragraph per wine, starting by a line to give the wine name.
        This line shall start by "Vin X", X being a number of X letter
        A line for picture can be inserted above or below this wine title list in the review author_ref.txt
    :param review_dir: path of the directory where all reviews per author are stored
    :param author_ref: name of the author whose review is used to get the wine list
    :param header: path of the text files to be used as header part for all reviews per wine
    (containing a link to the main wine tasting review for instance)
    """
    # Dictionary containing wine reviews per author
    review_per_author = dict_from_text_files(review_dir)

    # Extraction of wine names and associated information
    wine_list, id_list, picture_list = extract_wine_list(review_per_author[author_ref])

    # Review per wine
    review_per_wine = [{'name': wine_name} for wine_name in wine_list]
    for author_name, review in review_per_author.items():
        review_no_pict = [line for line in review if not('[attachment=' in line)]
        wine_list, id_list, useless_list = extract_wine_list(review_no_pict)
        for ii, line_id in enumerate(id_list):
            line_start = line_id
            try:
                line_stop = id_list[ii+1]
            except IndexError:
                line_stop = len(review_no_pict)
            review_per_wine[ii][author_name] = [line for line in review_no_pict[line_start+1:line_stop] if not(line == '')]

    # Formatting and exporting review per wine
    for ww, wine in enumerate(review_per_wine):
        txt_list = import_txt_as_list(header)
        if picture_list[ww]:
            txt_list.extend(['', picture_list[ww]])
        for author_name, review in wine.items():
            if author_name == 'name':
                txt_list.extend(['', '[b]CR: %s[/b]' % review])
                filename_raw = review + '.txt'
                filename = filename_raw.replace(',', ' -').replace(':', '-')
            else:
                txt_list.extend(['', '[i]%s[/i]' % author_name, *review])
        print(txt_list)
        export_list_as_txt_file(filename, txt_list)
