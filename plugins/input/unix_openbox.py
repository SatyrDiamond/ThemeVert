
import plugins
from objects import visual
from functions import color

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'openbox'
	
	def get_name(self):
		return '[Unix] OpenBox'
	
	def get_prop(self):
		prop = {}
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		from objects.file_theme import manybox
		manyboxtheme = manybox.manybox_theme()
		manyboxtheme.set_openbox()
		manyboxtheme.read(themeverter_intent.input_file)

		def get_box_color_dual(name, control, colloc, bordercolloc):
			incolor = manyboxtheme.get_data(name)
			if incolor:
				#print(incolor)
				assert type(incolor)==dict
				if '_root' in incolor and 'color' in incolor:
					colordata = incolor['_root'].lower().split(' ') if incolor else []
					color1 = manybox.get_color(incolor['color'])

					if 'parentrelative' in colordata: return False
					if 'border.color' in incolor and bordercolloc:
						border = manybox.get_color(incolor['color'])
						theme_obj.add_color(control, bordercolloc, border)
						
					if color1 and ('colorto' in incolor) and ('gradient' in colordata) and control: 
						color2 = manybox.get_color(incolor['colorto'])

						gradtype = None
						if 'horizontal' in colordata: gradtype = 'horizontal'
						if 'vertical' in colordata: gradtype = 'vertical'
						if 'diagonal' in colordata: gradtype = 'diagonal'
						if 'crossdiagonal' in colordata: gradtype = 'crossdiagonal'
						if 'pipecross' in colordata: gradtype = 'pipecross'
						if 'mirrorhorizontal' in colordata: gradtype = 'mirrorhorizontal'
						if 'splitvertical' in colordata: gradtype = 'splitvertical'
						if 'pyramid' in colordata: gradtype = 'pyramid'

						outcolor1 = visual.visual_color().from_int(color1)
						outcolor2 = visual.visual_color().from_int(color2)
						outcol = color.mix_color(outcolor1, outcolor2, 0.5)
						theme_obj.add_color(control, colloc, outcol.get_int())

						state, name = colloc.split(':')

						theme_obj.add_prop_color(control, state, name, 'color_fx', 'gradent')
						if gradtype: theme_obj.add_prop_color(control, state, name, 'gradent_type', gradtype)
						theme_obj.add_prop_color(control, state, name, 'gradent_colors', 'gradent1,gradent2')
						theme_obj.add_color(control, state+':gradent1', color1)
						theme_obj.add_color(control, state+':gradent2', color2)
					else:
						theme_obj.add_color(control, colloc, color1)
					return True
			return False

		def get_box_color(name, control, colloc):
			incolor = manyboxtheme.get_data(name)
			if incolor: 
				incolor = manybox.get_color(incolor)
				theme_obj.add_color(control, colloc, incolor)
				return True
			else:
				return False

		def add_data(name, control, state, prop, valtype):
			ival = manyboxtheme.get_data(name)
			if ival:
				if valtype=='int': ival = int(ival)
				theme_obj.add_prop(control, state, prop, ival)

		#for x in manyboxtheme.data.items():
		#	print(x)

		# -------- menu
		theme_obj.add_stylecontrol('menu')

		get_box_color('menu.border.color', 'menu', 'main:border')
		add_data('menu.border.width', 'menu', 'main', 'border_width', 'int')

		# -------- menu.items
		get_box_color_dual('menu.items.bg', 'menu', 'main:control_bg', 'main:border')
		get_box_color('menu.items.text.color', 'menu', 'main:control_fg')
		get_box_color('menu.items.text.color', 'menu', 'main:control_font_fg')
		get_box_color('menu.items.disabled.text.color', 'menu', 'inactive:control_fg')
		get_box_color('menu.items.disabled.text.color', 'menu', 'inactive:control_font_fg')

		# -------- menu.items.active
		get_box_color_dual('menu.items.active.bg', 'menu', 'focused:control_bg', 'focused:border')
		get_box_color('menu.items.active.text.color', 'menu', 'focused:control_fg')
		get_box_color('menu.items.active.text.color', 'menu', 'focused:control_font_fg')

		# -------- menu.separator
		get_box_color('menu.separator.color', 'menu', 'main:separator')
		add_data('menu.separator.padding.height', 'menu', 'main', 'separator_padding_height', 'int')
		add_data('menu.separator.padding.width', 'menu', 'main', 'separator_padding_width', 'int')

		# -------- menu.title
		theme_obj.add_stylecontrol('menu_header')
		get_box_color_dual('menu.title.bg', 'menu_header', 'main:control_bg', 'main:border')
		get_box_color('menu.title.text.color', 'menu_header', 'main:control_fg')
		get_box_color('menu.title.text.color', 'menu_header', 'main:control_font_fg')
		add_data('menu.title.text.justify', 'menu_header', 'main', 'text_alignment', 'string')

		# -------- window
		theme_obj.add_stylecontrol('window')
		theme_obj.add_stylecontrol('window_button')
		theme_obj.add_stylecontrol('window_grip')
		theme_obj.add_stylecontrol('window_handle')
		theme_obj.add_stylecontrol('window_back')
		theme_obj.add_stylecontrol('titlebar')

		add_data('window.label.text.justify', 'window', 'main', 'text_alignment', 'string')

		# -------- window.active.border
		get_box_color('window.active.border.color', 'window', 'main:border')
		get_box_color('window.inactive.border.color', 'window', 'inactive:border')

		get_box_color_dual('window.inactive.button.unpressed.bg', 'window_button', 'inactive:control_bg', 'inactive:border')
		get_box_color('window.inactive.button.unpressed.image.color', 'window_button', 'inactive:control_fg')
		get_box_color_dual('window.active.button.unpressed.bg', 'window_button', 'main:control_bg', 'main:border')
		get_box_color('window.active.button.unpressed.image.color', 'window_button', 'main:control_fg')
		get_box_color_dual('window.active.button.disabled.bg', 'window_button', 'disabled:control_bg', 'disabled:border')
		get_box_color('window.active.button.disabled.image.color', 'window_button', 'disabled:control_fg')
		get_box_color_dual('window.active.button.hover.bg', 'window_button', 'focused:control_bg', 'focused:border')
		get_box_color('window.active.button.hover.image.color', 'window_button', 'focused:control_fg')
		get_box_color_dual('window.active.button.pressed.bg', 'window_button', 'pressed:control_bg', 'pressed:border')
		get_box_color('window.active.button.pressed.image.color', 'window_button', 'pressed:control_fg')

		get_box_color_dual('window.active.grip.bg', 'window_grip', 'main:control_bg', 'main:border')
		get_box_color_dual('window.active.handle.bg', 'window_handle', 'main:control_bg', 'main:border')
		if not get_box_color_dual('window.active.label.bg', 'titlebar', 'main:control_bg', 'main:border'):
			get_box_color_dual('window.active.title.bg', 'titlebar', 'main:control_bg', 'main:border')
		get_box_color('window.active.label.text.color', 'titlebar', 'main:control_fg')
		get_box_color('window.active.label.text.color', 'titlebar', 'main:control_font_fg')
		get_box_color_dual('window.active.title.bg', 'window_back', 'main:control_bg', 'main:border')

		get_box_color_dual('window.inactive.grip.bg', 'window_grip', 'inactive:control_bg', 'inactive:border')
		get_box_color_dual('window.inactive.handle.bg', 'window_handle', 'inactive:control_bg', 'inactive:border')
		if not get_box_color_dual('window.inactive.label.bg', 'titlebar', 'inactive:control_bg', 'inactive:border'):
			get_box_color_dual('window.inactive.title.bg', 'titlebar', 'inactive:control_bg', 'inactive:border')
		get_box_color('window.inactive.label.text.color', 'titlebar', 'inactive:control_fg')
		get_box_color('window.inactive.label.text.color', 'titlebar', 'inactive:control_font_fg')
		get_box_color_dual('window.inactive.title.bg', 'window_back', 'inactive:control_bg', 'inactive:border')

		add_data('window.handle.width', 'window', 'main', 'handle_height', 'int')

		# -------- maincolors
		get_box_color_dual('menu.items.bg', None, 'main:control_bg', None)
		get_box_color('menu.items.text.color', None, 'main:control_fg')
		get_box_color('menu.items.text.color', None, 'main:control_font_fg')
		get_box_color('menu.items.disabled.text.color', None, 'inactive:control_fg')
		get_box_color('menu.items.disabled.text.color', None, 'inactive:control_font_fg')
		get_box_color('border.color', None, 'main:border')

		isedit1 = get_box_color_dual('window.active.label.bg', None, 'main:edit_bg', None)
		isedit2 = get_box_color('window.active.label.text.color', None, 'main:edit_fg')
		if not (isedit1 and isedit2):
			get_box_color_dual('menu.items.bg', None, 'main:edit_bg', None)
			get_box_color('menu.items.text.color', None, 'main:edit_fg')
			get_box_color('menu.items.text.color', None, 'main:edit_font_fg')
			get_box_color('menu.items.disabled.text.color', None, 'inactive:edit_fg')
			get_box_color('menu.items.disabled.text.color', None, 'inactive:edit_font_fg')

			get_box_color_dual('menu.items.active.bg', None, 'main:edit_bg_selected', None)
			get_box_color('menu.items.active.text.color', None, 'main:edit_fg_selected')