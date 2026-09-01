
import plugins

from functions import color

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
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
		icewmtheme.read(themeverter_intent.input_file)

		def add_color(name, default):
			incolor = default
			if name in icewmtheme.data:
				valtype, val = icewmtheme.data[name]
				if valtype=='string':
					incolor = val

			if default:
				if incolor.startswith('rgb:'):
					r, g, b = incolor.strip('rgb:').split('/')
					r = int(r, 16)
					g = int(g, 16)
					b = int(b, 16)
					theme_obj.add_global_color(name, [r,g,b])
					return True
				if incolor.startswith('#'):
					theme_obj.add_global_color(name, color.hex_to_int(incolor))
					return True

		# Border
		add_color("ColorNormalBorder", "rgb:C0/C0/C0")
		add_color("ColorActiveBorder", "rgb:C0/C0/C0")
		theme_obj.add_stylecontrol('window')
		theme_obj.add_color_named('window', 'main:border', 'ColorActiveBorder')
		theme_obj.add_color_named('window', 'inactive:border', 'ColorNormalBorder')

		# Button
		add_color("ColorActiveButton", "rgb:E0/E0/E0")
		add_color("ColorActiveButtonText", "rgb:00/00/00")
		add_color("ColorNormalButton", "rgb:C0/C0/C0")
		add_color("ColorNormalButtonText", "rgb:00/00/00")
		theme_obj.add_color_named(None, 'main:control_bg', 'ColorNormalButton')
		theme_obj.add_color_named(None, 'main:control_fg', 'ColorNormalButtonText')
		theme_obj.add_color_named(None, 'pressed:control_bg', 'ColorActiveButton')
		theme_obj.add_color_named(None, 'pressed:control_fg', 'ColorActiveButtonText')

		# TitleButton
		add_color("ColorNormalTitleButton", "rgb:C0/C0/C0")
		add_color("ColorNormalTitleButtonText", "rgb:00/00/00")
		theme_obj.add_stylecontrol('titlebar_button')
		theme_obj.add_color_named('titlebar_button', 'main:control_bg', 'ColorNormalTitleButton')
		theme_obj.add_color_named('titlebar_button', 'main:control_fg', 'ColorNormalTitleButtonText')

		# ScrollBar
		add_color("ColorScrollBar", "rgb:A0/A0/A0")
		theme_obj.add_stylecontrol('scrollbar')
		theme_obj.add_color_named('scrollbar', 'main:control_bg', 'ColorScrollBar')

		add_color("ColorScrollBarSlider", "rgb:C0/C0/C0")
		theme_obj.add_stylecontrol('scrollbar_slider')
		theme_obj.add_color_named('scrollbar_slider', 'main:control_bg', 'ColorScrollBarSlider')

		add_color("ColorScrollBarButton", "rgb:C0/C0/C0")
		add_color("ColorScrollBarArrow", "rgb:C0/C0/C0")
		add_color("ColorScrollBarInactiveArrow", "rgb:80/80/80")
		add_color("ColorScrollBarButtonArrow", "rgb:00/00/00")
		theme_obj.add_stylecontrol('scrollbar_button')
		theme_obj.add_color_named('scrollbar_button', 'main:control_bg', 'ColorScrollBarButton')
		theme_obj.add_color_named('scrollbar_button', 'main:control_fg', 'ColorScrollBarButtonArrow')
		theme_obj.add_color_named('scrollbar_button', 'inactive:control_fg', 'ColorScrollBarInactiveArrow')

		# MenuItem
		add_color("ColorNormalMenu", "rgb:C0/C0/C0")
		add_color("ColorNormalMenuItemText", "rgb:00/00/00")
		add_color("ColorActiveMenuItem", "rgb:A0/A0/A0")
		add_color("ColorActiveMenuItemText", "rgb:00/00/00")
		add_color("ColorDisabledMenuItemText", "rgb:80/80/80")
		theme_obj.add_stylecontrol('menu')
		theme_obj.add_color_named('menu', 'main:control_bg', 'ColorNormalMenu')
		theme_obj.add_color_named('menu', 'main:control_fg', 'ColorNormalMenuItemText')
		theme_obj.add_color_named('menu', 'focused:control_bg', 'ColorActiveMenuItem')
		theme_obj.add_color_named('menu', 'focused:control_fg', 'ColorActiveMenuItemText')
		theme_obj.add_color_named('menu', 'inactive:control_fg', 'ColorDisabledMenuItemText')

		# TitleBar
		add_color("ColorActiveTitleBar", "rgb:00/00/A0")
		add_color("ColorActiveTitleBarText", "rgb:FF/FF/FF")
		add_color("ColorNormalTitleBar", "rgb:80/80/80")
		add_color("ColorNormalTitleBarText", "rgb:00/00/00")
		#theme_obj.add_stylecontrol('titlebar')
		#theme_obj.add_color_named('main:control_bg', 'ColorActiveTitleBar')
		#theme_obj.add_color_named('main:control_fg', 'ColorActiveTitleBarText')
		#theme_obj.add_color_named('inactive:control_bg', 'ColorNormalTitleBar')
		#theme_obj.add_color_named('inactive:control_fg', 'ColorNormalTitleBarText')

		# Apm
		add_color("ColorApm", "rgb:00/00/00")
		add_color("ColorApmBattary", "rgb:FF/FF/00")
		add_color("ColorApmBattery", "rgb:FF/FF/00")
		add_color("ColorApmGraphBg", "rgb:00/00/00")
		add_color("ColorApmLine", "rgb:00/FF/00")
		add_color("ColorApmText", "rgb:00/FF/00")

		# CPUStatus
		add_color("ColorCPUStatusIdle", "rgb:00/00/00")
		add_color("ColorCPUStatusInterrupts", "rgb:FF/FF/00")
		add_color("ColorCPUStatusIoWait", "rgb:60/00/60")
		add_color("ColorCPUStatusNice", "rgb:00/00/FF")
		add_color("ColorCPUStatusSoftIrq", "rgb:00/FF/FF")
		add_color("ColorCPUStatusSteal", "rgb:FF/8A/91")
		add_color("ColorCPUStatusSystem", "rgb:FF/00/00")
		add_color("ColorCPUStatusTemp", "rgb:60/60/C0")
		add_color("ColorCPUStatusUser", "rgb:00/FF/00")
		theme_obj.add_stylecontrol('graphstat_cpu')
		theme_obj.add_color_named('graphstat_cpu', 'main:edit_bg', 'ColorCPUStatusIdle')
		theme_obj.add_color_named('graphstat_cpu', 'main:edit_fg_interrupts', 'ColorCPUStatusInterrupts')
		theme_obj.add_color_named('graphstat_cpu', 'main:edit_fg_iowait', 'ColorCPUStatusIoWait')
		theme_obj.add_color_named('graphstat_cpu', 'main:edit_fg_nice', 'ColorCPUStatusNice')
		theme_obj.add_color_named('graphstat_cpu', 'main:edit_fg_softirq', 'ColorCPUStatusSoftIrq')
		theme_obj.add_color_named('graphstat_cpu', 'main:edit_fg_steal', 'ColorCPUStatusSteal')
		theme_obj.add_color_named('graphstat_cpu', 'main:edit_fg_system', 'ColorCPUStatusSystem')
		theme_obj.add_color_named('graphstat_cpu', 'main:edit_fg_temp', 'ColorCPUStatusTemp')
		theme_obj.add_color_named('graphstat_cpu', 'main:edit_fg_user', 'ColorCPUStatusUser')

		# Input
		add_color("ColorInputText", "rgb:00/00/00")
		add_color("ColorInput", "rgb:FF/FF/FF")
		add_color("ColorInputSelection", "rgb:80/80/80")
		add_color("ColorInputSelectionText", "rgb:00/00/00")
		theme_obj.add_color_named('input', 'main:edit_bg', 'ColorInput')
		theme_obj.add_color_named('input', 'main:edit_fg', 'ColorInputText')
		theme_obj.add_color_named('input', 'main:edit_bg_selected', 'ColorInputSelection')
		theme_obj.add_color_named('input', 'main:edit_fg_selected', 'ColorInputSelectionText')

		# MinimizedWindow
		add_color("ColorActiveMinimizedWindow", "rgb:E0/E0/E0")
		add_color("ColorActiveMinimizedWindowText", "rgb:00/00/00")
		add_color("ColorNormalMinimizedWindow", "rgb:C0/C0/C0")
		add_color("ColorNormalMinimizedWindowText", "rgb:00/00/00")

		# TaskBar
		theme_obj.add_stylecontrol('taskbar')
		add_color("ColorDefaultTaskBar", "rgb:C0/C0/C0")
		theme_obj.add_color_named('taskbar', 'active:control_bg', 'ColorDefaultTaskBar')

		theme_obj.add_stylecontrol('taskbar_button_app')
		add_color("ColorActiveTaskBarApp", "rgb:E0/E0/E0")
		add_color("ColorActiveTaskBarAppText", "rgb:00/00/00")
		add_color("ColorInvisibleTaskBarApp", "rgb:80/80/80")
		add_color("ColorInvisibleTaskBarAppText", "rgb:00/00/00")
		add_color("ColorMinimizedTaskBarApp", "rgb:A0/A0/A0")
		add_color("ColorMinimizedTaskBarAppText", "rgb:00/00/00")
		add_color("ColorNormalTaskBarApp", "rgb:C0/C0/C0")
		add_color("ColorNormalTaskBarAppText", "rgb:00/00/00")
		theme_obj.add_color_named('taskbar_button_app', 'active:control_bg', 'ColorActiveTaskBarApp')
		theme_obj.add_color_named('taskbar_button_app', 'active:control_fg', 'ColorActiveTaskBarAppText')
		theme_obj.add_color_named('taskbar_button_app', 'invisible:control_bg', 'ColorInvisibleTaskBarApp')
		theme_obj.add_color_named('taskbar_button_app', 'invisible:control_fg', 'ColorInvisibleTaskBarAppText')
		theme_obj.add_color_named('taskbar_button_app', 'minimized:control_bg', 'ColorMinimizedTaskBarApp')
		theme_obj.add_color_named('taskbar_button_app', 'minimized:control_fg', 'ColorMinimizedTaskBarAppText')
		theme_obj.add_color_named('taskbar_button_app', 'main:control_bg', 'ColorNormalTaskBarApp')
		theme_obj.add_color_named('taskbar_button_app', 'main:control_fg', 'ColorNormalTaskBarAppText')

		# Label
		add_color("ColorLabel", "rgb:C0/C0/C0")
		add_color("ColorLabelText", "rgb:00/00/00")
		theme_obj.add_stylecontrol('label')
		theme_obj.add_color_named('label', 'main:control_bg', 'ColorLabel')
		theme_obj.add_color_named('label', 'main:control_fg', 'ColorLabelText')

		# ListBox
		add_color("ColorListBox", "rgb:C0/C0/C0")
		add_color("ColorListBoxSelection", "rgb:80/80/80")
		add_color("ColorListBoxSelectionText", "rgb:00/00/00")
		add_color("ColorListBoxText", "rgb:00/00/00")
		theme_obj.add_stylecontrol('listbox')
		theme_obj.add_color_named('listbox', 'main:edit_bg', 'ColorListBox')
		theme_obj.add_color_named('listbox', 'main:edit_fg', 'ColorListBoxText')
		theme_obj.add_color_named('listbox', 'main:edit_bg_selected', 'ColorListBoxSelection')
		theme_obj.add_color_named('listbox', 'main:edit_fg_selected', 'ColorListBoxSelectionText')

		theme_obj.add_color_named(None, 'main:edit_bg', 'ColorListBox')
		theme_obj.add_color_named(None, 'main:edit_fg', 'ColorListBoxText')
		theme_obj.add_color_named(None, 'main:edit_bg_selected', 'ColorListBoxSelection')
		theme_obj.add_color_named(None, 'main:edit_fg_selected', 'ColorListBoxSelectionText')
		
		# MEMStatus
		add_color("ColorMEMStatusFree", "rgb:00/00/00")
		add_color("ColorMEMStatusBuffers", "rgb:60/60/C0")
		add_color("ColorMEMStatusCached", "rgb:80/80/FF")
		add_color("ColorMEMStatusUser", "rgb:40/40/80")
		theme_obj.add_stylecontrol('graphstat_memory')
		theme_obj.add_color_named('graphstat_memory', 'main:edit_bg', 'ColorMEMStatusFree')
		theme_obj.add_color_named('graphstat_memory', 'main:edit_fg_buffers', 'ColorMEMStatusBuffers')
		theme_obj.add_color_named('graphstat_memory', 'main:edit_fg_cached', 'ColorMEMStatusCached')
		theme_obj.add_color_named('graphstat_memory', 'main:edit_fg_user', 'ColorMEMStatusUser')

		# MoveSize
		add_color("ColorMoveSizeStatus", "rgb:C0/C0/C0")
		add_color("ColorMoveSizeStatusText", "rgb:00/00/00")
		theme_obj.add_stylecontrol('move_size_status')
		theme_obj.add_color_named('move_size_status', 'main:control_bg', 'ColorMoveSizeStatus')
		theme_obj.add_color_named('move_size_status', 'main:control_fg', 'ColorMoveSizeStatusText')

		# Net
		add_color("ColorNetIdle", "rgb:00/00/00")
		add_color("ColorNetReceive", "rgb:FF/00/FF")
		add_color("ColorNetSend", "rgb:FF/FF/00")
		theme_obj.add_stylecontrol('graphstat_network')
		theme_obj.add_color_named('graphstat_network', 'main:edit_bg', 'ColorNetIdle')
		theme_obj.add_color_named('graphstat_network', 'main:edit_fg_rx', 'ColorNetReceive')
		theme_obj.add_color_named('graphstat_network', 'main:edit_fg_tx', 'ColorNetSend')
		
		# Clock
		add_color("ColorClock", "rgb:00/00/00")
		add_color("ColorClockText", "rgb:00/FF/00")
		theme_obj.add_stylecontrol('clock')
		theme_obj.add_color_named('clock', 'main:control_bg', 'ColorClock')
		theme_obj.add_color_named('clock', 'main:control_fg', 'ColorClockText')
		theme_obj.add_color_named('clock', 'main:edit_bg', 'ColorClock')
		theme_obj.add_color_named('clock', 'main:edit_fg', 'ColorClockText')
		
		# QuickSwitch
		add_color("ColorQuickSwitch", "rgb:C0/C0/C0")
		add_color("ColorQuickSwitchText", "rgb:00/00/00")
		theme_obj.add_stylecontrol('quick_switch')
		theme_obj.add_color_named('quick_switch', 'main:control_bg', 'ColorQuickSwitch')
		theme_obj.add_color_named('quick_switch', 'main:control_fg', 'ColorQuickSwitchText')

		# ToolTip
		add_color("ColorToolTip", "rgb:E0/E0/00")
		add_color("ColorToolTipText", "rgb:00/00/00")
		theme_obj.add_stylecontrol('tooltip')
		theme_obj.add_color_named('tooltip', 'main:control_bg', 'ColorToolTip')
		theme_obj.add_color_named('tooltip', 'main:control_fg', 'ColorToolTipText')

		# Other
		add_color("ColorDialog", "rgb:C0/C0/C0")
		if add_color("DesktopBackgroundColor", None):
			theme_obj.add_stylecontrol('desktop')
			theme_obj.add_color_named('desktop', 'main:control_bg', 'DesktopBackgroundColor')
