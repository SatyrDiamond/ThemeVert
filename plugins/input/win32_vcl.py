
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
		#vcl_theme_obj.to_xml('vcl_out.xml')

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

		def vcl_get_font(stylename, fontname, state, colorname1, colorname2):
			if fontname in vcl_theme_obj.fonts:
				f_name, f_size, f_unk, f_r, f_g, f_b = vcl_theme_obj.fonts[fontname].split(',')

				font_obj = theme_obj.add_font(stylename, state, colorname1)
				font_obj.used = True
				font_obj.face = f_name
				font_obj.size = int(f_size)

				outcolor = state+':'+colorname1+colorname2

				theme_obj.add_color(stylename, outcolor, [int(f_r), int(f_g), int(f_b)])

		theme_obj.add_stylecontrol('menubar')
		theme_obj.add_stylecontrol('checkbox')
		theme_obj.add_stylecontrol('radiobutton')
		theme_obj.add_stylecontrol('groupbox')
		theme_obj.add_stylecontrol('menuitem')
		theme_obj.add_stylecontrol('editbox')
		theme_obj.add_stylecontrol('treeitem')
		theme_obj.add_stylecontrol('griditem')

		vcl_get_font('menubar', 'ButtonTextNormal', 'main', 'control', '_font_fg')
		vcl_get_font('menubar', 'ButtonTextPressed', 'active', 'control', '_font_fg')
		vcl_get_font('menubar', 'ButtonTextHot', 'hot', 'control', '_font_fg')
		vcl_get_font('menubar', 'ButtonTextFocused', 'focused', 'control', '_font_fg')
		vcl_get_font('menubar', 'ButtonTextDisabled', 'inactive', 'control', '_font_fg')

		vcl_get_font('checkbox', 'CheckBoxTextNormal', 'main', 'control', '_font_fg')
		vcl_get_font('checkbox', 'CheckBoxTextPressed', 'active', 'control', '_font_fg')
		vcl_get_font('checkbox', 'CheckBoxTextHot', 'hot', 'control', '_font_fg')
		vcl_get_font('checkbox', 'CheckBoxTextFocused', 'focused', 'control', '_font_fg')
		vcl_get_font('checkbox', 'CheckBoxTextDisabled', 'inactive', 'control', '_font_fg')

		vcl_get_font('radiobutton', 'RadioButtonTextNormal', 'main', 'control', '_font_fg')
		vcl_get_font('radiobutton', 'RadioButtonTextPressed', 'active', 'control', '_font_fg')
		vcl_get_font('radiobutton', 'RadioButtonTextHot', 'hot', 'control', '_font_fg')
		vcl_get_font('radiobutton', 'RadioButtonTextFocused', 'focused', 'control', '_font_fg')
		vcl_get_font('radiobutton', 'RadioButtonTextDisabled', 'inactive', 'control', '_font_fg')

		vcl_get_font('groupbox', 'GroupBoxTextNormal', 'main', 'control', '_font_fg')
		vcl_get_font('groupbox', 'GroupBoxTextDisabled', 'inactive', 'control', '_font_fg')

		vcl_get_font('menu', 'MenuItemTextNormal', 'main', 'control', '_font_fg')
		vcl_get_font('menu', 'MenuItemTextSelected', 'active', 'control', '_font_fg')
		vcl_get_font('menu', 'MenuItemTextHot', 'hot', 'control', '_font_fg')
		vcl_get_font('menu', 'MenuItemTextDisabled', 'inactive', 'control', '_font_fg')

		vcl_get_font('editbox', 'EditBoxTextNormal', 'main', 'edit', '_font_fg')
		vcl_get_font('editbox', 'EditBoxTextFocused', 'focused', 'edit', '_font_fg')
		vcl_get_font('editbox', 'EditBoxTextHot', 'hot', 'edit', '_font_fg')
		vcl_get_font('editbox', 'EditBoxTextDisabled', 'inactive', 'edit', '_font_fg')
		vcl_get_font('editbox', 'EditBoxTextSelected', 'active', 'edit', '_font_fg')

		vcl_get_font('treeitem', 'TreeItemTextNormal', 'main', 'edit', '_font_fg')
		vcl_get_font('treeitem', 'TreeItemTextHot', 'hot', 'edit', '_font_fg')
		vcl_get_font('treeitem', 'TreeItemTextSelected', 'selected', 'edit', '_font_fg')
		vcl_get_font('treeitem', 'TreeItemTextFocused', 'focused', 'edit', '_font_fg')
		vcl_get_font('treeitem', 'TreeItemTextDisabled', 'inactive', 'edit', '_font_fg')

		vcl_get_font('griditem', 'GridItemNormal', 'main', 'edit', '_font_fg')
		vcl_get_font('griditem', 'GridItemSelected', 'active', 'edit', '_font_fg')