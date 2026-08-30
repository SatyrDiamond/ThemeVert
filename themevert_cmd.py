#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 SatyrDiamond
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import argparse
import os
import logging
from objects import core

logger_core = logging.getLogger('core')

scriptfiledir = os.path.dirname(os.path.realpath(__file__))

print('ThemeVerter: a Theme/ColorScheme Conversion Tool')

parser = argparse.ArgumentParser()
parser.add_argument("-i", default=None)
parser.add_argument("-it", default=None)
parser.add_argument("-o", default=None)
parser.add_argument("-ot", default=None)
args = parser.parse_args()

dawvert_core = core.core()

if not args.i:
	logger_core.error('Input File Not Specified.')
	exit()
elif not os.path.exists(args.i):
	logger_core.error('Input File Not Found.')
	exit()

if not args.o:
	logger_core.error('Output File Not Specified.')
	exit()


themeconv_core = core.core()
themeconv_core.input_load_plugins(None)
themeconv_core.output_load_plugins(None)

themeconv_core.input_set(args.it)
themeconv_core.output_set(args.ot)

themeverter_intent = core.themeverter_intent()
themeverter_intent.set_file_input(args.i)
themeconv_core.parse_input(themeverter_intent)

themeverter_intent.set_file_output(args.o)
themeconv_core.parse_output(themeverter_intent)