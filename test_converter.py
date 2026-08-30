
from objects import core

import logging
logFormatter = logging.Formatter(fmt='%(levelname)8s | %(name)12s | %(message)s')
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(logFormatter)
logger_plugins = logging.getLogger('plugins')
logger_plugins.addHandler(consoleHandler)
logger_plugins.setLevel(logging.INFO)

themeverter_intent = core.themeverter_intent()

themeconv_core = core.core()
themeconv_core.input_load_plugins(None)
themeconv_core.output_load_plugins(None)

if 1:
	themeverter_intent.set_file_input('themes/win_theme/Windows 2000.theme')
	themeconv_core.input_set('win32_theme')
else:
	themeverter_intent.set_file_input('themes/tcl/ONYXBLUE')
	themeconv_core.input_set('vcl_theme')

themeconv_core.parse_input(themeverter_intent)

themeverter_intent.set_file_output('out.theme')
themeconv_core.output_set('win32_theme')

themeconv_core.parse_output(themeverter_intent)