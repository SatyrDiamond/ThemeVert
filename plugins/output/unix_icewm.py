
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

		def do_color(name, control, colloc):
			outcol = theme_obj.get_color_rgb(control, colloc)
			if outcol: themedata[name] = ['string', outcol.get_hex()]

		def do_color_spec(name, control, colloc):
			outcol = theme_obj.get_color_rgb_spec(control, colloc)
			if outcol: themedata[name] = ['string', outcol.get_hex()]

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
		do_color('ColorActiveBorder', 'window', 'main:control_bg')
		do_color('ColorNormalBorder', 'window', 'inactive:control_bg')

		#Button
		do_color('ColorNormalButton', 'button', 'main:control_bg')
		do_color('ColorNormalButtonText', 'button', 'main:control_fg')
		do_color('ColorActiveButton', 'button', 'pressed:control_bg')
		do_color('ColorActiveButtonText', 'button', 'pressed:control_fg')

		#TitleButton
		do_color('ColorNormalTitleButton', 'titlebar_button', 'main:control_bg')
		do_color('ColorNormalTitleButtonText', 'titlebar_button', 'main:control_fg')

		# ScrollBar
		do_color('ColorScrollBar', 'scrollbar', 'main:control_bg')

		do_color('ColorScrollBarSlider', 'scrollbar_slider', 'main:control_bg')

		do_color('ColorScrollBarButton', 'scrollbar_button', 'main:control_bg')
		do_color('ColorScrollBarArrow', 'scrollbar_button', 'main:control_fg')
		do_color('ColorScrollBarInactiveArrow', 'scrollbar_button', 'inactive:control_fg')
		do_color('ColorScrollBarButtonArrow', 'scrollbar_button', 'main:control_fg')

		# MenuItem
		do_color('ColorNormalMenu', 'menu', 'main:control_bg')
		do_color('ColorNormalMenuItemText', 'menu', 'main:control_fg')
		do_color('ColorActiveMenuItem', 'menu', 'focused:control_bg')
		do_color('ColorActiveMenuItemText', 'menu', 'focused:control_fg')
		do_color('ColorDisabledMenuItemText', 'menu', 'inactive:control_fg')

		# TitleBar
		do_color('ColorActiveTitleBar', 'titlebar', 'main:control_bg')
		do_color('ColorActiveTitleBarText', 'titlebar', 'main:control_fg')
		do_color('ColorNormalTitleBar', 'titlebar', 'inactive:control_bg')
		do_color('ColorNormalTitleBarText', 'titlebar', 'inactive:control_fg')

		# Apm

		# CPUStatus
		do_color("ColorCPUStatusIdle", 'graphstat_cpu', 'main:edit_bg')
		do_color_spec("ColorCPUStatusInterrupts", 'graphstat_cpu', 'main:edit_fg_interrupts')
		do_color_spec("ColorCPUStatusIoWait", 'graphstat_cpu', 'main:edit_fg_iowait')
		do_color_spec("ColorCPUStatusNice", 'graphstat_cpu', 'main:edit_fg_nice')
		do_color_spec("ColorCPUStatusSoftIrq", 'graphstat_cpu', 'main:edit_fg_softirq')
		do_color_spec("ColorCPUStatusSteal", 'graphstat_cpu', 'main:edit_fg_steal')
		do_color_spec("ColorCPUStatusSystem", 'graphstat_cpu', 'main:edit_fg_system')
		do_color_spec("ColorCPUStatusTemp", 'graphstat_cpu', 'main:edit_fg_temp')
		do_color_spec("ColorCPUStatusUser", 'graphstat_cpu', 'main:edit_fg_user')

		# Input
		do_color("ColorInput", 'input', 'main:edit_bg')
		do_color("ColorInputText", 'input', 'main:edit_fg')
		do_color("ColorInputSelection", 'input', 'main:edit_bg_selected')
		do_color("ColorInputSelectionText", 'input', 'main:edit_fg_selected')

		# MinimizedWindow
		do_color("ColorActiveMinimizedWindow", None, 'main:edit_bg')
		do_color("ColorActiveMinimizedWindowText", None, 'main:edit_fg')
		do_color("ColorNormalMinimizedWindow", None, 'main:control_bg')
		do_color("ColorNormalMinimizedWindowText", None, 'main:control_fg')

		# TaskBar
		do_color("ColorDefaultTaskBar", 'taskbar', 'main:control_bg')

		do_color("ColorActiveTaskBarApp", 'taskbar_button_app', 'active:control_bg')
		do_color("ColorActiveTaskBarAppText", 'taskbar_button_app', 'active:control_fg')
		do_color("ColorInvisibleTaskBarApp", 'taskbar_button_app', 'invisible:control_bg')
		do_color("ColorInvisibleTaskBarAppText", 'taskbar_button_app', 'invisible:control_fg')
		do_color("ColorMinimizedTaskBarApp", 'taskbar_button_app', 'minimized:control_bg')
		do_color("ColorMinimizedTaskBarAppText", 'taskbar_button_app', 'minimized:control_fg')
		do_color("ColorNormalTaskBarApp", 'taskbar_button_app', 'main:control_bg')
		do_color("ColorNormalTaskBarAppText", 'taskbar_button_app', 'main:control_fg')

		# Label
		do_color('ColorLabel', 'label', 'main:control_bg')
		do_color('ColorLabelText', 'label', 'main:control_fg')

		# ListBox
		do_color('ColorListBox', 'listbox', 'main:edit_bg')
		do_color('ColorListBoxText', 'listbox', 'main:edit_fg')
		do_color('ColorListBoxSelection', 'listbox', 'main:edit_bg_selected')
		do_color('ColorListBoxSelectionText', 'listbox', 'main:edit_fg_selected')

		# MEMStatus
		do_color('ColorMEMStatusFree', 'graphstat_memory', 'main:edit_bg')
		do_color_spec('ColorMEMStatusBuffers', 'graphstat_memory', 'main:edit_fg_buffers')
		do_color_spec('ColorMEMStatusCached', 'graphstat_memory', 'main:edit_fg_cached')
		do_color_spec('ColorMEMStatusUser', 'graphstat_memory', 'main:edit_fg_user')

		# MoveSize
		do_color('ColorMoveSizeStatus', 'move_size_status', 'main:control_bg')
		do_color('ColorMoveSizeStatusText', 'move_size_status', 'main:control_fg')
		
		# Net
		do_color('ColorNetIdle', 'graphstat_network', 'main:edit_bg')
		do_color_spec('ColorNetReceive', 'graphstat_network', 'main:edit_fg_rx')
		do_color_spec('ColorNetSend', 'graphstat_network', 'main:edit_fg_tx')

		# Clock
		do_color('ColorClock', 'clock', 'main:control_bg')
		do_color('ColorClockText', 'clock', 'main:control_fg')
		
		# QuickSwitch
		do_color('ColorQuickSwitch', 'quick_switch', 'main:control_bg')
		do_color('ColorQuickSwitchText', 'quick_switch', 'main:control_fg')

		# ToolTip
		do_color('ColorToolTip', 'tooltip', 'main:control_bg')
		do_color('ColorToolTipText', 'tooltip', 'main:control_fg')
		
		# Desktop
		do_color('DesktopBackgroundColor', 'desktop', 'main:control_bg')

		icewmtheme.write(themeverter_intent.output_file)
