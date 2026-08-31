
import plugins
from functions import color as colorfunc

class output_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'output'
	
	def get_shortname(self):
		return 'icewm'
	
	def get_name(self):
		return '[Unix] IceWM'
	
	def get_prop(self):
		prop = {}
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		from objects.file_theme import icewm
		icewmtheme = icewm.icewm_theme()
		themedata = icewmtheme.data

		themedata['ThemeDescription'] = ['string', "Converted Theme"]

		themedata['ThemeAuthor'] = ['string', "Software"]

		themedata['Look'] = ['type', 'pixmap']
		themedata['TitleBarHeight'] = ['int', 19]
		themedata['TitleBarJustify'] = ['int', 50]

		themedata['BorderSizeX'] = ['int', 5]
		themedata['BorderSizeY'] = ['int', 5]
		themedata['CornerSizeX'] = ['int', 16]
		themedata['CornerSizeY'] = ['int', 16]
		themedata['DlgBorderSizeX'] = ['int', 2]
		themedata['DlgBorderSizeY'] = ['int', 2]

		ctrl_main_bg = theme_obj.get_color_rgb(None, 'main:control_bg')
		ctrl_main_fg = theme_obj.get_color_rgb(None, 'main:control_fg')
		text_main_bg = theme_obj.get_color_rgb(None, 'main:edit_bg')
		text_main_fg = theme_obj.get_color_rgb(None, 'main:edit_fg')
		text_sel_bg = theme_obj.get_color_rgb(None, 'main:edit_bg_selected')
		text_sel_fg = theme_obj.get_color_rgb(None, 'main:edit_fg_selected')

		themedata['BorderSizeX'] = ['int', 5]
		themedata['BorderSizeY'] = ['int', 5]
		themedata['CornerSizeX'] = ['int', 16]
		themedata['CornerSizeY'] = ['int', 16]
		themedata['DlgBorderSizeX'] = ['int', 2]
		themedata['DlgBorderSizeY'] = ['int', 2]

		#Border
		o_color_bg = theme_obj.get_color_rgb('window', 'main:control_bg')
		i_color_bg = theme_obj.get_color_rgb('window', 'inactive:control_bg')
		themedata['ColorActiveBorder'] = ['string', o_color_bg.get_hex()]
		themedata['ColorNormalBorder'] = ['string', i_color_bg.get_hex()]

		#Button
		o_color_bg = theme_obj.get_color_rgb('button', 'main:control_bg')
		o_color_fg = theme_obj.get_color_rgb('button', 'main:control_fg')
		pressed_color_bg = theme_obj.get_color_rgb('button', 'pressed:control_bg')
		pressed_color_fg = theme_obj.get_color_rgb('button', 'pressed:control_fg')
		themedata['ColorNormalButton'] = ['string', o_color_bg.get_hex()]
		themedata['ColorNormalButtonText'] = ['string', o_color_fg.get_hex()]
		themedata['ColorActiveButton'] = ['string', pressed_color_bg.get_hex()]
		themedata['ColorActiveButtonText'] = ['string', pressed_color_fg.get_hex()]

		#TitleButton
		o_color_bg = theme_obj.get_color_rgb('titlebar_button', 'main:control_bg')
		o_color_fg = theme_obj.get_color_rgb('titlebar_button', 'main:control_fg')
		themedata['ColorNormalTitleButton'] = ['string', o_color_bg.get_hex()]
		themedata['ColorNormalTitleButtonText'] = ['string', o_color_fg.get_hex()]

		# ScrollBar
		o_color_bg = theme_obj.get_color_rgb('scrollbar', 'main:control_bg')
		themedata['ColorScrollBar'] = ['string', o_color_fg.get_hex()]

		o_color_bg = theme_obj.get_color_rgb('scrollbar_slider', 'main:control_bg')
		themedata['ColorScrollBarSlider'] = ['string', o_color_fg.get_hex()]

		o_color_bg = theme_obj.get_color_rgb('scrollbar_button', 'main:control_bg')
		o_color_fg = theme_obj.get_color_rgb('scrollbar_button', 'main:control_fg')
		i_color_fg = theme_obj.get_color_rgb('scrollbar_button', 'inactive:control_fg')
		themedata['ColorScrollBarButton'] = ['string', o_color_bg.get_hex()]
		themedata['ColorScrollBarArrow'] = ['string', o_color_bg.get_hex()]
		themedata['ColorScrollBarInactiveArrow'] = ['string', i_color_fg.get_hex()]
		themedata['ColorScrollBarButtonArrow'] = ['string', o_color_fg.get_hex()]

		# MenuItem
		main_control_bg = theme_obj.get_color_rgb('menu', 'main:control_bg')
		main_control_fg = theme_obj.get_color_rgb('menu', 'main:control_fg')
		focused_control_bg = theme_obj.get_color_rgb('menu', 'focused:control_bg')
		focused_control_fg = theme_obj.get_color_rgb('menu', 'focused:control_fg')
		inactive_control_fg = theme_obj.get_color_rgb('menu', 'inactive:control_fg')

		themedata['ColorNormalMenu'] = ['string', main_control_bg.get_hex()]
		themedata['ColorNormalMenuItemText'] = ['string', main_control_fg.get_hex()]
		themedata['ColorActiveMenuItem'] = ['string', focused_control_bg.get_hex()]
		themedata['ColorActiveMenuItemText'] = ['string', focused_control_fg.get_hex()]
		themedata['ColorDisabledMenuItemText'] = ['string', inactive_control_fg.get_hex()]

		# TitleBar
		main_control_bg = theme_obj.get_color_rgb('titlebar', 'main:control_bg')
		main_control_fg = theme_obj.get_color_rgb('titlebar', 'main:control_fg')
		inactive_control_bg = theme_obj.get_color_rgb('titlebar', 'inactive:control_bg')
		inactive_control_fg = theme_obj.get_color_rgb('titlebar', 'inactive:control_fg')

		themedata['ColorActiveTitleBar'] = ['string', main_control_bg.get_hex()]
		themedata['ColorActiveTitleBarText'] = ['string', main_control_fg.get_hex()]
		themedata['ColorNormalTitleBar'] = ['string', inactive_control_bg.get_hex()]
		themedata['ColorNormalTitleBarText'] = ['string', inactive_control_fg.get_hex()]
		
		# Apm

		# CPUStatus

		# Input
		themedata["ColorInput"] = ['string', text_main_bg.get_hex()]
		themedata["ColorInputText"] = ['string', text_main_fg.get_hex()]
		themedata["ColorInputSelection"] = ['string', text_sel_bg.get_hex()]
		themedata["ColorInputSelectionText"] = ['string', text_sel_fg.get_hex()]

		# MinimizedWindow
		themedata["ColorActiveMinimizedWindow"] = ['string', text_main_bg.get_hex()]
		themedata["ColorActiveMinimizedWindowText"] = ['string', text_main_fg.get_hex()]
		themedata["ColorNormalMinimizedWindow"] = ['string', ctrl_main_bg.get_hex()]
		themedata["ColorNormalMinimizedWindowText"] = ['string', ctrl_main_fg.get_hex()]

		# TaskBar
		themedata["ColorDefaultTaskBar"] = ['string', ctrl_main_bg.get_hex()]
		themedata["ColorActiveTaskBarApp"] = ['string', ctrl_main_bg.get_hex()]
		themedata["ColorActiveTaskBarAppText"] = ['string', ctrl_main_fg.get_hex()]
		themedata["ColorInvisibleTaskBarApp"] = ['string', ctrl_main_bg.get_hex()]
		themedata["ColorInvisibleTaskBarAppText"] = ['string', ctrl_main_fg.get_hex()]
		themedata["ColorMinimizedTaskBarApp"] = ['string', ctrl_main_bg.get_hex()]
		themedata["ColorMinimizedTaskBarAppText"] = ['string', ctrl_main_fg.get_hex()]
		themedata["ColorNormalTaskBarApp"] = ['string', ctrl_main_bg.get_hex()]
		themedata["ColorNormalTaskBarAppText"] = ['string', ctrl_main_fg.get_hex()]

		# Label
		themedata['ColorLabel'] = ['string', ctrl_main_bg.get_hex()]
		themedata['ColorLabelText'] = ['string', ctrl_main_fg.get_hex()]

		# ListBox
		themedata['ColorListBox'] = ['string', text_main_bg.get_hex()]
		themedata['ColorListBoxText'] = ['string', text_main_fg.get_hex()]
		themedata['ColorListBoxSelection'] = ['string', text_sel_bg.get_hex()]
		themedata['ColorListBoxSelectionText'] = ['string', text_sel_fg.get_hex()]

		# TitleBar
		col1 = theme_obj.get_color_rgb('tooltip', 'main:control_bg')
		col2 = theme_obj.get_color_rgb('tooltip', 'main:control_fg')
		themedata['ColorToolTip'] = ['string', col1.get_hex()]
		themedata['ColorToolTipText'] = ['string', col2.get_hex()]
		
		# Desktop
		desktop = theme_obj.get_color_rgb('desktop', 'main:control_bg')
		themedata['DesktopBackgroundColor'] = ['string', desktop.get_hex()]

		icewmtheme.write(themeverter_intent.output_file)
