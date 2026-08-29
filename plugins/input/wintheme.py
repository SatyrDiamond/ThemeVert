
import plugins
from objects.file_theme import windows_theme

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'win32_theme'
	
	def get_name(self):
		return 'Windows .theme'
	
	def get_prop(self):
		prop = {}
		prop['supported_types'] = ['win32']
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		theme_obj.supported_types.append('win32')
		win32_colors = theme_obj.colors_win32
		wintheme = windows_theme.wintheme(themeverter_intent.input_file)
		for k, v in wintheme.colors.items(): win32_colors.set(k, v)

		def get_font(curstyle, LOGFONTA):
			font_obj = curstyle.add_font('main:control')
			font_obj.used = True
			font_obj.face = LOGFONTA.lfFaceName
			if LOGFONTA.lfWeight>400: font_obj.fx.append('bold')
			if LOGFONTA.lfItalic: font_obj.fx.append('italic')
			if LOGFONTA.lfUnderline: font_obj.fx.append('underline')
			if LOGFONTA.lfStrikeOut: font_obj.fx.append('strikeout')

		if wintheme.NonclientMetrics:
			NonclientMetrics = wintheme.NonclientMetrics
			lfMenuFont = NonclientMetrics.lfMenuFont

			curstyle, curctrl = theme_obj.add_stylecontrol('menubar')
			get_font(curstyle, lfMenuFont)
