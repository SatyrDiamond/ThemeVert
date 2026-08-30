
import plugins
from objects.file_theme import vcl_theme
from objects.file_theme import vcl_colors

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'vcl_theme'
	
	def get_name(self):
		return '[Win32] Delphi VCL'
	
	def get_prop(self):
		prop = {}
		prop['supported_types'] = ['win32']
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		theme_obj.supported_types.append('win32')
		vcl_theme_obj = vcl_theme.masterstyle_data(themeverter_intent.input_file)
		vcl_theme_obj.to_xml('vcl_out.xml')

		def vcl_get_w32_color(vclname):
			c = vcl_theme_obj.get_color_w32(vclname)
			d, c = vcl_theme.get_color_int(c)
			#print(d, vclname, c)
			return c

		win32_colors = theme_obj.colors_win32
		
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
		
		win32_colors.import_colors(theme_obj)

		def vcl_get_font(curstyle, fontname, proploc, propcol):
			if fontname in vcl_theme_obj.fonts:
				f_name, f_size, f_unk, f_r, f_g, f_b = vcl_theme_obj.fonts[fontname].split(',')

				font_obj = curstyle.add_font(proploc)
				font_obj.used = True
				font_obj.face = f_name
				font_obj.size = int(f_size)
				curstyle.add_color(proploc+':'+propcol, [int(f_r), int(f_g), int(f_b)])

		curstyle, curctrl = theme_obj.add_stylecontrol('menubar')
		vcl_get_font(curstyle, 'ButtonTextNormal', 'main:control', 'text')
		vcl_get_font(curstyle, 'ButtonTextPressed', 'active:control', 'text')
		vcl_get_font(curstyle, 'ButtonTextHot', 'hot:control', 'text')
		vcl_get_font(curstyle, 'ButtonTextFocused', 'focused:control', 'text')
		vcl_get_font(curstyle, 'ButtonTextDisabled', 'inactive:control', 'text')

		curstyle, curctrl = theme_obj.add_stylecontrol('checkbox')
		vcl_get_font(curstyle, 'CheckBoxTextNormal', 'main:control', 'text')
		vcl_get_font(curstyle, 'CheckBoxTextPressed', 'active:control', 'text')
		vcl_get_font(curstyle, 'CheckBoxTextHot', 'hot:control', 'text')
		vcl_get_font(curstyle, 'CheckBoxTextFocused', 'focused:control', 'text')
		vcl_get_font(curstyle, 'CheckBoxTextDisabled', 'inactive:control', 'text')

		curstyle, curctrl = theme_obj.add_stylecontrol('radiobutton')
		vcl_get_font(curstyle, 'RadioButtonTextNormal', 'main:control', 'text')
		vcl_get_font(curstyle, 'RadioButtonTextPressed', 'active:control', 'text')
		vcl_get_font(curstyle, 'RadioButtonTextHot', 'hot:control', 'text')
		vcl_get_font(curstyle, 'RadioButtonTextFocused', 'focused:control', 'text')
		vcl_get_font(curstyle, 'RadioButtonTextDisabled', 'inactive:control', 'text')

		curstyle, curctrl = theme_obj.add_stylecontrol('groupbox')
		vcl_get_font(curstyle, 'GroupBoxTextNormal', 'main:control', 'text')
		vcl_get_font(curstyle, 'GroupBoxTextDisabled', 'inactive:control', 'text')

		curstyle, curctrl = theme_obj.add_stylecontrol('menuitem')
		vcl_get_font(curstyle, 'MenuItemTextNormal', 'main:control', 'text')
		vcl_get_font(curstyle, 'MenuItemTextSelected', 'active:control', 'text')
		vcl_get_font(curstyle, 'MenuItemTextHot', 'hot:control', 'text')
		vcl_get_font(curstyle, 'MenuItemTextDisabled', 'inactive:control', 'text')

		curstyle, curctrl = theme_obj.add_stylecontrol('editbox')
		vcl_get_font(curstyle, 'EditBoxTextNormal', 'main:text', 'fg')
		vcl_get_font(curstyle, 'EditBoxTextFocused', 'focused:text', 'fg')
		vcl_get_font(curstyle, 'EditBoxTextHot', 'hot:text', 'fg')
		vcl_get_font(curstyle, 'EditBoxTextDisabled', 'inactive:text', 'fg')
		vcl_get_font(curstyle, 'EditBoxTextSelected', 'active:text', 'fg')

		curstyle, curctrl = theme_obj.add_stylecontrol('treeitem')
		vcl_get_font(curstyle, 'TreeItemTextNormal', 'main:text', 'fg')
		vcl_get_font(curstyle, 'TreeItemTextHot', 'hot:text', 'fg')
		vcl_get_font(curstyle, 'TreeItemTextSelected', 'selected:text', 'fg')
		vcl_get_font(curstyle, 'TreeItemTextFocused', 'focused:text', 'fg')
		vcl_get_font(curstyle, 'TreeItemTextDisabled', 'inactive:text', 'fg')

		curstyle, curctrl = theme_obj.add_stylecontrol('griditem')
		vcl_get_font(curstyle, 'GridItemNormal', 'main:text', 'fg')
		vcl_get_font(curstyle, 'GridItemSelected', 'active:text', 'fg')