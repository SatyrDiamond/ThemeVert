
import plugins
from functions import color as colorfunc

class output_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'output'
	
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

		def do_color(name, control, colloc):
			outcol = theme_obj.get_color_rgb(control, colloc)
			if outcol: 
				manyboxtheme.add_data(name, outcol.get_hex())
				return True
			return False

		def do_color_spec(name, control, colloc):
			outcol = theme_obj.get_color_rgb_spec(control, colloc)
			if outcol: 
				manyboxtheme.add_data(name, outcol.get_hex())
				return True
			return False

		def do_color_dual(isspec, name, control, colloc, props):
			state, colname = colloc.split(':')
			
			color_fx = theme_obj.get_prop_color(control, state, colname, 'color_fx')
			outprops = 'raised' if not props else props

			if color_fx=='gradent':
				gradent_colors = theme_obj.get_prop_color(control, state, colname, 'gradent_colors')
				gradent_type = theme_obj.get_prop_color(control, state, colname, 'gradent_type')
				outprops += ' gradient'

				if gradent_type=='horizontal': outprops += 'horizontal'
				if gradent_type=='vertical': outprops += 'vertical'
				if gradent_type=='diagonal': outprops += 'diagonal'
				if gradent_type=='crossdiagonal': outprops += 'crossdiagonal'
				if gradent_type=='pipecross': outprops += 'pipecross'
				if gradent_type=='mirrorhorizontal' in gradent_type: outprops += 'mirrorhorizontal'
				if gradent_type=='splitvertical': outprops += 'splitvertical'
				if gradent_type=='pyramid': outprops += 'pyramid'

				gradent_colors = gradent_colors.split(',')
				do_color(name+'.color', control, state+':'+gradent_colors[0])
				do_color(name+'.colorto', control, state+':'+gradent_colors[-1])
				manyboxtheme.add_data(name, outprops)
				return True
			else:
				outprops += ' solid'
				manyboxtheme.add_data(name, outprops)
				if isspec: return do_color_spec(name+'.color', control, colloc)
				else: return do_color(name+'.color', control, colloc)
			return False

		def do_data(name, control, state, prop, fallback):
			outdata = theme_obj.get_prop(control, state,prop)
			manyboxtheme.add_data(name, str(outdata) if outdata else fallback)

		# -------- menu

		do_color('menu.border.color', 'menu', 'main:border')
		#add_data('menu.border.width', 'menu', 'main', 'border_width', 'int')

		# -------- menu.items
		do_color_dual(False, 'menu.items.bg', 'menu', 'main:control_bg', None)
		do_color('menu.items.text.color', 'menu', 'main:control_font_fg')
		do_color('menu.items.disabled.text.color', 'menu', 'inactive:control_font_fg')

		# -------- menu.items.active
		do_color_dual(False, 'menu.items.active.bg', 'menu', 'focused:control_bg', None)
		do_color('menu.items.active.text.color', 'menu', 'focused:control_font_fg')

		# -------- menu.separator
		do_color('menu.separator.color', 'menu', 'main:separator')
		#add_data('menu.separator.padding.height', 'menu', 'main', 'separator_padding_height', 'int')
		#add_data('menu.separator.padding.width', 'menu', 'main', 'separator_padding_width', 'int')

		# -------- menu.title
		theme_obj.add_stylecontrol('menu_header')
		do_color_dual(False, 'menu.title.bg', 'menu_header', 'main:control_bg', None)
		do_color('menu.title.text.color', 'menu_header', 'main:control_font_fg')
		do_data('menu.title.text.justify', 'menu_header', 'main', 'text_alignment', 'left')

		# -------- window.active.border
		do_color('window.active.border.color', 'window', 'main:border')
		do_color('window.inactive.border.color', 'window', 'inactive:border')

		do_color_dual(False, 'window.inactive.button.unpressed.bg', 'window_button', 'inactive:control_bg', None)
		do_color('window.inactive.button.unpressed.image.color', 'window_button', 'inactive:control_fg')
		do_color_dual(False, 'window.active.button.unpressed.bg', 'window_button', 'main:control_bg', None)
		do_color('window.active.button.unpressed.image.color', 'window_button', 'main:control_fg')
		do_color_dual(False, 'window.active.button.disabled.bg', 'window_button', 'disabled:control_bg', None)
		do_color('window.active.button.disabled.image.color', 'window_button', 'disabled:control_fg')
		do_color_dual(False, 'window.active.button.hover.bg', 'window_button', 'focused:control_bg', None)
		do_color('window.active.button.hover.image.color', 'window_button', 'focused:control_fg')
		do_color_dual(False, 'window.active.button.pressed.bg', 'window_button', 'pressed:control_bg', 'sunken')
		do_color('window.active.button.pressed.image.color', 'window_button', 'pressed:control_fg')

		do_color_dual(False, 'window.active.grip.bg', 'window_grip', 'main:control_bg', None)
		do_color_dual(False, 'window.active.handle.bg', 'window_handle', 'main:control_bg', None)
		do_color_dual(False, 'window.active.label.bg', 'titlebar', 'main:control_bg', None)
		do_color('window.active.label.text.color', 'titlebar', 'main:control_font_fg')
		do_color_dual(False, 'window.active.title.bg', 'window_back', 'main:control_bg', None)

		do_color_dual(False, 'window.inactive.grip.bg', 'window_grip', 'inactive:control_bg', None)
		do_color_dual(False, 'window.inactive.handle.bg', 'window_handle', 'inactive:control_bg', None)
		do_color_dual(False, 'window.inactive.label.bg', 'titlebar', 'inactive:control_bg', None)
		do_color('window.inactive.label.text.color', 'titlebar', 'inactive:control_font_fg')
		do_color_dual(False, 'window.inactive.title.bg', 'window_back', 'inactive:control_bg', None)

		do_data('window.label.text.justify', 'window', 'main', 'text_alignment', 'left')
		#add_data('window.handle.width', 'window', 'main', 'handle_height', 'int')

		# -------- maincolors

		manyboxtheme.write(themeverter_intent.output_file)
