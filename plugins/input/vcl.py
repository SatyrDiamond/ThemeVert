
import plugins
from objects.file_theme import vcl_theme
from objects.file_theme import vcl_colors

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'vcl_theme'
	
	def get_name(self):
		return 'Delphi VCL'
	
	def parse(self, theme_obj, themeverter_intent):

		vcl_theme_obj = vcl_theme.masterstyle_data(themeverter_intent.input_file)
		#vcl_theme_obj.to_xml('out_o.xml')

		def vcl_get_w32_color(vclname):
			c = vcl_theme_obj.get_color_w32(vclname)
			c = vcl_theme.get_color_int(c)
			return c

		win32_colors = theme_obj.win32_colors
		
		win32_colors.set('ActiveBorder', vcl_get_w32_color('clActiveBorder') ) # ActiveBorder
		win32_colors.set('ActiveTitle', vcl_get_w32_color('clActiveCaption') ) # ActiveTitle
		win32_colors.set('AppWorkSpace', vcl_get_w32_color('clAppWorkSpace') ) # AppWorkSpace
		win32_colors.set('Background', vcl_get_w32_color('clBackground') ) # Background
		win32_colors.set('ButtonAlternateFace', vcl_get_w32_color('clDefault') )# ButtonAlternateFace
		win32_colors.set('ButtonDkShadow', vcl_get_w32_color('cl3DDkShadow') ) # ButtonDkShadow
		win32_colors.set('ButtonFace', vcl_get_w32_color('clBtnFace') ) # ButtonFace
		win32_colors.set('ButtonHilight', vcl_get_w32_color('clBtnHighlight') ) # ButtonHilight
		win32_colors.set('ButtonLight', vcl_get_w32_color('cl3DLight') ) # ButtonLight
		win32_colors.set('ButtonShadow', vcl_get_w32_color('clBtnShadow') ) # ButtonShadow
		win32_colors.set('ButtonText', vcl_get_w32_color('clBtnText') ) # ButtonText
		win32_colors.set('GradientActiveTitle', vcl_get_w32_color('clGradientActiveCaption') ) # GradientActiveTitle
		win32_colors.set('GradientInactiveTitle', vcl_get_w32_color('clGradientInactiveCaption') ) # GradientInactiveTitle
		win32_colors.set('GrayText', vcl_get_w32_color('clGrayText') ) # GrayText
		win32_colors.set('Hilight', vcl_get_w32_color('clHighlight') ) # Hilight
		win32_colors.set('HilightText', vcl_get_w32_color('clHighlightText') ) # HilightText
		win32_colors.set('HotTrackingColor', vcl_get_w32_color('clHotLight') ) # HotTrackingColor
		win32_colors.set('InactiveBorder', vcl_get_w32_color('clInactiveBorder') ) # InactiveBorder
		win32_colors.set('InactiveTitle', vcl_get_w32_color('clInactiveCaption') ) # InactiveTitle
		win32_colors.set('InactiveTitleText', vcl_get_w32_color('clInactiveCaptionText') ) # InactiveTitleText
		win32_colors.set('InfoText', vcl_get_w32_color('clInfoText') ) # InfoText
		win32_colors.set('InfoWindow', vcl_get_w32_color('clInfoBk') ) # InfoWindow
		win32_colors.set('Menu', vcl_get_w32_color('clMenu') ) # Menu
		win32_colors.set('MenuBar', vcl_get_w32_color('clMenuBar') ) # MenuBar
		win32_colors.set('MenuHilight', vcl_get_w32_color('clMenuHighlight') ) # MenuHilight
		win32_colors.set('MenuText', vcl_get_w32_color('clMenuText') ) # MenuText
		win32_colors.set('Scrollbar', vcl_get_w32_color('clScrollBar') ) # Scrollbar
		win32_colors.set('TitleText', vcl_get_w32_color('clCaptionText') ) # TitleText
		win32_colors.set('Window', vcl_get_w32_color('clWindow') ) # Window
		win32_colors.set('WindowFrame', vcl_get_w32_color('clWindowFrame') ) # WindowFrame
		win32_colors.set('WindowText', vcl_get_w32_color('clWindowText') ) # WindowText
		
		theme_obj.import_win32_colors()
		
		theme_obj.to_xml('out.xml')