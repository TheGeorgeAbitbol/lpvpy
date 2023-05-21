# -*- coding: utf-8 -*-
"""
Package lpvpy : python for LPV (lapassionduvin.com)

Example of script to run wine_review.transpose_wine_reviews() function

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

import wine_review

review_dir_path = 'CR-par-auteur'
author_ref = 'MathiasB'
header_file = 'header_example.txt'
wine_review.transpose_wine_reviews(review_dir_path, author_ref, header_file)
