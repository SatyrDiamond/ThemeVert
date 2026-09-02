
import plugins
from objects import visual
from functions import color

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'fluxbox'
	
	def get_name(self):
		return '[Unix] FluxBox'
	
	def get_prop(self):
		prop = {}
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		from objects.file_theme import manybox
		manyboxtheme = manybox.manybox_theme()
		manyboxtheme.set_fluxbox()
		manyboxtheme.read(themeverter_intent.input_file)

		def add_data(name, control, state, prop, valtype):
			ival = manyboxtheme.get_data(name)
			if ival:
				if valtype=='int': ival = int(ival)
				theme_obj.add_prop(control, state, prop, ival)

		def get_box_color_dual(name, control, colloc):
			incolor = manyboxtheme.get_data(name)
			if incolor:
				assert type(incolor)==dict
				if '_root' in incolor and 'color' in incolor:
					colordata = incolor['_root'].lower().split(' ') if incolor else []
					color1 = manybox.get_color(incolor['color'])

					if color1 and ('colorto' in incolor) and ('gradient' in colordata) and control: 
						color2 = manybox.get_color(incolor['colorto'])

						outcolor1 = visual.visual_color().from_int(color1)
						outcolor2 = visual.visual_color().from_int(color2)
						outcol = color.mix_color(outcolor1, outcolor2, 0.5)
						theme_obj.add_color(control, colloc, outcol.get_int())

						state, name = colloc.split(':')

						gradtype = None
						if 'horizontal' in colordata: gradtype = 'horizontal'
						if 'vertical' in colordata: gradtype = 'vertical'
						if 'diagonal' in colordata: gradtype = 'diagonal'
						if 'crossdiagonal' in colordata: gradtype = 'crossdiagonal'
						if 'pipecross' in colordata: gradtype = 'pipecross'
						if 'elliptic' in colordata: gradtype = 'elliptic'
						if 'rectangle' in colordata: gradtype = 'rectangle'
						if 'pyramid' in colordata: gradtype = 'pyramid'

						theme_obj.add_prop_color(control, state, name, 'color_fx', 'gradent')
						if gradtype: theme_obj.add_prop_color(control, state, name, 'gradent_type', gradtype)
						theme_obj.add_prop_color(control, state, name, 'gradent_colors', 'gradent1,gradent2')
						theme_obj.add_color(control, state+':gradent1', color1)
						theme_obj.add_color(control, state+':gradent2', color2)
					else:
						theme_obj.add_color(control, colloc, color1)

		def get_box_color(name, control, colloc):
			incolor = manyboxtheme.get_data(name)
			if incolor: 
				incolor = manybox.get_color(incolor)
				theme_obj.add_color(control, colloc, incolor)

		# -------- desktop
		theme_obj.add_stylecontrol('desktop')
		get_box_color('background.color', 'desktop', 'main:control_bg')

		# -------- window.button
		theme_obj.add_stylecontrol('window_button')
		get_box_color_dual('window.button.unfocus', 'window_button', 'inactive:control_bg')
		get_box_color_dual('window.button.focus', 'window_button', 'main:control_bg')
		get_box_color_dual('window.button.pressed', 'window_button', 'pressed:control_bg')
		get_box_color('window.button.unfocus.piccolor', 'window_button', 'inactive:control_fg')
		get_box_color('window.button.focus.piccolor', 'window_button', 'main:control_fg')
		get_box_color('window.button.pressed.piccolor', 'window_button', 'pressed:control_fg')

		# -------- window.title
		theme_obj.add_stylecontrol('window_back')
		get_box_color_dual('window.title.focus', 'window_back', 'main:control_bg')
		get_box_color_dual('window.title.unfocus', 'window_back', 'inactive:control_bg')

		# -------- window.label
		theme_obj.add_stylecontrol('titlebar')
		get_box_color_dual('window.label.focus', 'titlebar', 'main:control_bg')
		get_box_color('window.label.textColor', 'titlebar', 'main:control_fg')
		get_box_color('window.label.textColor', 'titlebar', 'main:control_font_fg')
		get_box_color_dual('window.label.unfocus', 'titlebar', 'inactive:control_bg')
		get_box_color('window.label.unfocus.textColor', 'titlebar', 'inactive:control_fg')
		get_box_color('window.label.unfocus.textColor', 'titlebar', 'inactive:control_font_fg')
		add_data('window.label.focus.justify', 'titlebar', 'main', 'titlebar', 'string')
		add_data('window.label.unfocus.justify', 'titlebar', 'inactive', 'titlebar', 'string')

		# -------- window.handle
		theme_obj.add_stylecontrol('window_handle')
		get_box_color_dual('window.handle.focus', 'window_handle', 'main:control_bg')
		get_box_color_dual('window.handle.unfocus', 'window_handle', 'inactive:control_bg')
		add_data('handleWidth', 'window', 'main', 'border_width', 'int')

		# -------- window.grip
		theme_obj.add_stylecontrol('window_grip')
		get_box_color_dual('window.grip.focus', 'window_grip', 'main:control_bg')
		get_box_color_dual('window.grip.unfocus', 'window_grip', 'inactive:control_bg')

		theme_obj.add_stylecontrol('window')
		add_data('window.justify', 'window', 'main', 'text_alignment', 'string')
		get_box_color('window.borderColor', 'window', 'main:border')
		add_data('window.borderWidth', 'window', 'main', 'border_width', 'int')

		# -------- menu
		theme_obj.add_stylecontrol('menu')
		get_box_color('menu.borderColor', 'menu', 'main:border')
		add_data('menu.borderWidth', 'menu', 'main', 'border_width', 'int')

		# -------- menu.frame
		get_box_color_dual('menu.frame', 'menu', 'main:control_bg')
		get_box_color('menu.frame.textColor', 'menu', 'main:control_fg')
		get_box_color('menu.frame.textColor', 'menu', 'main:control_font_fg')
		get_box_color('menu.frame.disableColor', 'menu', 'inactive:control_fg')
		get_box_color('menu.frame.disableColor', 'menu', 'inactive:control_font_fg')
		add_data('menu.frame.justify', 'menu', 'main', 'text_alignment', 'string')

		# -------- menu.hilite
		get_box_color_dual('menu.hilite', 'menu', 'focused:control_bg')
		get_box_color('menu.hilite.textColor', 'menu', 'focused:control_fg')
		get_box_color('menu.hilite.textColor', 'menu', 'focused:control_font_fg')

		# -------- menu.title
		theme_obj.add_stylecontrol('menu_header')
		get_box_color_dual('menu.title', 'menu_header', 'main:control_bg')
		get_box_color('menu.title.textColor', 'menu_header', 'main:control_fg')
		get_box_color('menu.title.textColor', 'menu_header', 'main:control_font_fg')
		add_data('menu.title.justify', 'menu_header', 'main', 'text_alignment', 'string')

		# -------- toolbar
		theme_obj.add_stylecontrol('taskbar')
		get_box_color_dual('toolbar', 'taskbar', 'main:control_bg')
		get_box_color('toolbar.textColor', 'taskbar', 'main:control_fg')
		get_box_color('toolbar.textColor', 'taskbar', 'main:control_font_fg')
		add_data('toolbar.justify', 'taskbar', 'main', 'text_alignment', 'string')

		# -------- toolbar.clock
		theme_obj.add_stylecontrol('clock')
		get_box_color_dual('toolbar.clock', 'clock', 'main:control_bg')
		get_box_color('toolbar.clock.textColor', 'clock', 'main:control_fg')
		get_box_color('toolbar.clock.textColor', 'clock', 'main:control_font_fg')

		# -------- toolbar.button
		theme_obj.add_stylecontrol('taskbar_button')
		get_box_color_dual('toolbar.button', 'taskbar_button', 'main:control_bg')
		get_box_color('toolbar.button.piccolor', 'taskbar_button', 'main:control_fg')
		get_box_color_dual('toolbar.button.pressed', 'taskbar_button', 'pressed:control_bg')
		#get_box_color('toolbar.button.pressed.piccolor', 'taskbar_button', 'pressed:control_fg')

		# -------- toolbar.label
		theme_obj.add_stylecontrol('taskbar_label')
		get_box_color_dual('toolbar.label', 'taskbar_label', 'main:control_bg')
		get_box_color('toolbar.label.textColor', 'taskbar_label', 'main:control_fg')

		# -------- toolbar.windowLabel
		theme_obj.add_stylecontrol('taskbar_button_app')
		get_box_color_dual('toolbar.windowLabel', 'taskbar_button_app', 'main:control_bg')
		get_box_color('toolbar.windowLabel.textColor', 'taskbar_button_app', 'main:control_fg')
		get_box_color('toolbar.windowLabel.textColor', 'taskbar_button_app', 'main:control_font_fg')

		# -------- maincolors
		get_box_color_dual('menu.frame', None, 'main:edit_bg')
		get_box_color('menu.frame.textColor', None, 'main:edit_fg')
		get_box_color('menu.frame.textColor', None, 'main:edit_font_fg')

		get_box_color_dual('menu.frame', None, 'main:control_bg')
		get_box_color('menu.frame.textColor', None, 'main:control_fg')
		get_box_color('menu.frame.textColor', None, 'main:control_font_fg')
		get_box_color('menu.frame.disableColor', None, 'inactive:edit_fg')
		get_box_color('menu.frame.disableColor', None, 'inactive:control_font_fg')
		
		get_box_color('menu.hilite.color', None, 'main:edit_bg_selected')
		get_box_color('menu.hilite.textColor', None, 'main:edit_fg_selected')

		get_box_color('toolbar.button.color', None, 'main:control_bg')
		get_box_color('toolbar.button.piccolor', None, 'main:control_fg')

		get_box_color('bordercolor', None, 'main:border')

		theme_obj.add_stylecontrol('button')
		get_box_color_dual('window.button.unfocus', 'button', 'inactive:control_bg')
		get_box_color_dual('window.button.focus', 'button', 'main:control_bg')
		get_box_color_dual('window.button.pressed', 'button', 'pressed:control_bg')
		get_box_color('window.button.unfocus.piccolor', 'button', 'inactive:control_fg')
		get_box_color('window.button.focus.piccolor', 'button', 'main:control_fg')
		get_box_color('window.button.pressed.piccolor', 'button', 'pressed:control_fg')
