
import plugins
from functions import color as colorfunc

class output_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'output'
	
	def get_shortname(self):
		return 'blackbox'
	
	def get_name(self):
		return '[Unix] blackbox'
	
	def get_prop(self):
		prop = {}
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		from objects.file_theme import fluxbox
		fluxboxtheme = fluxbox.fluxbox_theme()
		themedata = fluxboxtheme.data

		def do_color(name, control, colloc):
			outcol = theme_obj.get_color_rgb(control, colloc)
			if outcol: 
				themedata[name] = outcol.get_hex()
				return True
			return False

		def do_color_spec(name, control, colloc):
			outcol = theme_obj.get_color_rgb_spec(control, colloc)
			if outcol: 
				themedata[name] = outcol.get_hex()
				return True
			return False

		def do_color_dual(isspec, name, control, colloc, props):
			state, colname = colloc.split(':')
			
			color_fx = theme_obj.get_prop_color(control, state, colname, 'color_fx')
			themedata[name] = 'raised border' if not props else props

			if color_fx=='gradent':
				gradent_colors = theme_obj.get_prop_color(control, state, colname, 'gradent_colors')
				themedata[name] += ' gradient'
				gradent_colors = gradent_colors.split(',')
				do_color(name+'.color1', control, state+':'+gradent_colors[0])
				do_color(name+'.color2', control, state+':'+gradent_colors[-1])
				return True
			else:
				themedata[name] += ' solid'
				if isspec: return do_color_spec(name+'.backgroundColor', control, colloc)
				else: return do_color(name+'.backgroundColor', control, colloc)
			return False

		def do_data(name, control, state, prop, fallback):
			outdata = theme_obj.get_prop(control, state,prop)
			themedata[name] = str(outdata) if outdata else fallback

		# -------- menu.title
		do_color_dual(False, 'menu.title', 'menu_header', 'main:control_bg', None)
		do_color('menu.title.foregroundColor', 'menu_header', 'main:control_fg')
		do_color('menu.title.textColor', 'menu_header', 'main:control_font_fg')
		do_data('menu.title.alignment', 'menu_header', 'main', 'text_alignment', 'center')
		do_data('menu.title.marginwidth', 'menu_header', 'main', 'margin_width', '2')
		themedata['menu.title.font'] = 'Bitstream Vera Sans-12:style=Bold'

		# -------- menu.frame
		do_color_dual(False, 'menu.frame', 'menu', 'main:control_bg', None)
		do_color('menu.frame.foregroundColor', 'menu', 'main:control_fg')
		do_color('menu.frame.textColor', 'menu', 'main:control_font_fg')
		do_color('menu.frame.disabledColor', 'menu', 'inactive:control_fg')
		do_data('menu.frame.alignment', 'menu', 'main', 'text_alignment', 'left')
		do_data('menu.frame.marginwidth', 'menu', 'main', 'margin_width', '2')

		# -------- menu.active
		do_color_dual(False, 'menu.active', None, 'main:edit_bg_selected', None)
		do_color('menu.active.foregroundColor', None, 'main:edit_fg_selected')
		do_color('menu.active.textColor', None, 'main:edit_font_fg_selected')

		do_color_dual(False, 'menu.active', 'menu', 'focused:control_bg', None)
		do_color('menu.active.foregroundColor', 'menu', 'focused:control_fg')
		do_color('menu.active.textColor', 'menu', 'focused:control_font_fg')
		
		# -------- slit
		do_color_dual(False, 'slit', 'slit', 'main:edit_bg_selected', None)
		do_data('slit.marginwidth', 'slit', 'main', 'margin_width', '2')

		# -------- toolbar
		do_color_dual(False, 'toolbar', 'taskbar', 'main:control_bg', None)
		do_data('toolbar.alignment', 'taskbar', 'main', 'text_alignment', 'left')
		do_data('toolbar.marginwidth', 'taskbar', 'main', 'margin_width', '2')
		themedata['toolbar.font'] = 'Bitstream Vera Sans-9:style=Bold'

		# -------- toolbar.label
		do_color_dual(False, 'toolbar.label', 'taskbar_label', 'main:control_bg', None)
		do_color('toolbar.label.textColor', 'taskbar_label', 'main:control_fg')
		do_data('toolbar.label.marginwidth', 'taskbar_label', 'main', 'margin_width', '2')

		# -------- toolbar.windowLabel
		do_color_dual(False, 'toolbar.windowLabel', 'taskbar_button_app', 'main:control_bg', None)
		do_color('toolbar.windowLabel.textColor', 'taskbar_button_app', 'main:control_fg')

		# -------- toolbar.clock
		do_color_dual(False, 'toolbar.clock', 'clock', 'main:control_bg', None)
		do_color('toolbar.clock.textColor', 'clock', 'main:control_fg')

		# -------- toolbar.button
		do_color_dual(False, 'toolbar.button', 'taskbar_button', 'main:control_bg', None)
		do_color_dual(False, 'toolbar.button.pressed', 'taskbar_button', 'pressed:control_bg', 'sunken border')
		do_color('toolbar.button.foregroundColor', 'taskbar_button', 'main:control_fg')
		do_data('toolbar.button.marginwidth', 'taskbar_button', 'main', 'margin_width', '2')

		# -------- window.title
		# focus
		do_color_dual(False, 'window.title.focus', 'window_back', 'main:control_bg', None)
		# unfocus
		do_color_dual(False, 'window.title.unfocus', 'window_back', 'inactive:control_bg', None)

		do_data('window.title.marginwidth', 'window_back', 'main', 'margin_width', '2')

		# -------- window.label
		# focus
		do_color_dual(False, 'window.label.focus', 'titlebar', 'main:control_bg', None)
		do_color('window.label.focus.textColor', 'titlebar', 'main:control_fg')
		# unfocus
		do_color_dual(False, 'window.label.unfocus', 'titlebar', 'inactive:control_bg', None)
		do_color('window.label.unfocus.textColor', 'titlebar', 'inactive:control_fg')

		do_data('window.label.marginwidth', 'titlebar', 'main', 'margin_width', '2')

		# -------- window.button
		# focus
		do_color_dual(False, 'window.button.focus', 'window_button', 'main:control_bg', None)
		do_color('window.button.focus.foregroundColor', 'window_button', 'main:control_fg')
		# unfocus
		do_color_dual(False, 'window.button.unfocus', 'window_button', 'inactive:control_bg', None)
		do_color('window.button.unfocus.foregroundColor', 'window_button', 'inactive:control_fg')
		# pressed
		do_color_dual(False, 'window.button.pressed', 'window_button', 'pressed:control_bg', 'sunken border')
		do_color('window.button.focus.foregroundColor', 'window_button', 'pressed:control_fg')

		do_data('window.button.marginwidth', 'window_button', 'main', 'margin_width', '2')

		# -------- window.handle
		# focus
		do_color_dual(False, 'window.handle.focus', 'window_handle', 'main:control_bg', None)
		# unfocus
		do_color_dual(False, 'window.handle.unfocus', 'window_handle', 'inactive:control_bg', None)

		# -------- window.grip
		# focus
		do_color_dual(False, 'window.grip.focus', 'window_grip', 'main:control_bg', None)
		# unfocus
		do_color_dual(False, 'window.grip.unfocus', 'window_grip', 'inactive:control_bg', None)

		# -------- window.frame
		do_data('window.frame.borderWidth', 'window', 'main', 'border_width', '1')
		# focus
		do_color('window.frame.focus.borderColor', 'window', 'main:border')
		# unfocus
		do_color('window.frame.unfocus.borderColor', 'window', 'inactive:border')

		# -------- window
		do_data('window.alignment', 'window', 'main', 'text_alignment', 'left')
		do_data('window.handleHeight', 'window', 'main', 'border_width', '8')







		# -------- desktop
		outcol = theme_obj.get_color_rgb('desktop', 'main:control_bg')
		if outcol:
			themedata['rootCommand'] = 'bsetroot -solid '+('rgb:%02x/%02x/%02x' % tuple(outcol.get_int()))

		fluxboxtheme.write(themeverter_intent.output_file)
