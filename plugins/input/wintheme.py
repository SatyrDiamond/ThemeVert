
import plugins
from objects.file_theme import windows_theme

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'win32_theme'
	
	def get_name(self):
		return 'Windows .theme'
	
	def parse(self, theme_obj, themeverter_intent):
		win32_colors = theme_obj.win32_colors
		wintheme = windows_theme.wintheme(themeverter_intent.input_file)
		for k, v in wintheme.colors.items(): win32_colors.set(k, v)
		theme_obj.import_win32_colors()
