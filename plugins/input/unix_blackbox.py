
import plugins
from objects import visual
from functions import color

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'blackbox'
	
	def get_name(self):
		return '[Unix] blackbox'
	
	def get_prop(self):
		prop = {}
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		from objects.file_theme import fluxbox
		blackboxtheme = fluxbox.fluxbox_theme()
		blackboxtheme.read(themeverter_intent.input_file)

		def get_flux_color(name, control, colloc):
			name = name.lower()
			icolor = blackboxtheme.get_data(name)
			if icolor: 
				icolor = fluxbox.get_color(icolor)
				theme_obj.add_color(control, colloc, icolor)

		def get_flux_color_merge(name1, name2, control, colloc):
			name = name.lower()
			color1 = blackboxtheme.get_data(name1)
			color2 = blackboxtheme.get_data(name2)

			if color1 and color2: 
				outcolor1 = visual.visual_color().from_int(fluxbox.get_color(color1))
				outcolor2 = visual.visual_color().from_int(fluxbox.get_color(color2))
				outcol = color.mix_color(outcolor1, outcolor2, 0.5)
				theme_obj.add_color(control, colloc, outcol.get_int())

		def get_flux_color_dual(name, control, colloc):

			while True:
				colord = blackboxtheme.get_data(name+'.appearance')
				colordata = colord.split(' ') if colord else []
				if not colordata: break
				if 'parentrelative' in colordata:
					splname = name.split('.')
					newname = '.'.join(splname[0:-1])
					if newname!=name: name = newname
					else: break
				else: break

			color0 = blackboxtheme.get_data(name+'.backgroundColor')
			color1 = blackboxtheme.get_data(name+'.color1')
			color2 = blackboxtheme.get_data(name+'.color2')

			if color1 and color2 and 'gradient' in colordata and control: 
				outcolor1 = visual.visual_color().from_int(fluxbox.get_color(color1))
				outcolor2 = visual.visual_color().from_int(fluxbox.get_color(color2))
				outcol = color.mix_color(outcolor1, outcolor2, 0.5)
				theme_obj.add_color(control, colloc, outcol.get_int())

				state, name = colloc.split(':')

				theme_obj.add_prop_color(control, state, name, 'color_fx', 'gradent')
				theme_obj.add_prop_color(control, state, name, 'gradent_colors', 'gradent1,gradent2')
				theme_obj.add_color(control, state+':gradent1', fluxbox.get_color(color1))
				theme_obj.add_color(control, state+':gradent2', fluxbox.get_color(color2))
			else:
				if color0:
					outcolor0 = fluxbox.get_color(color0)
					theme_obj.add_color(control, colloc, outcolor0)

		def add_data(name, control, state, prop, valtype):
			ival = blackboxtheme.get_data(name)
			if ival:
				if valtype=='int': ival = int(ival)
				theme_obj.add_prop(control, state, prop, ival)

		# -------- menu.title
		theme_obj.add_stylecontrol('menu_header')
		get_flux_color_dual('menu.title', 'menu_header', 'main:control_bg')
		get_flux_color('menu.title.foregroundColor', 'menu_header', 'main:control_fg')
		get_flux_color('menu.title.textColor', 'menu_header', 'main:control_font_fg')
		# skipped menu.title.font
		add_data('menu.title.alignment', 'menu_header', 'main', 'text_alignment', 'string')
		add_data('menu.title.marginwidth', 'menu_header', 'main', 'margin_width', 'int')

		get_flux_color_dual('menu.title', None, 'main:edit_bg')
		get_flux_color('menu.title.foregroundColor', None, 'main:edit_fg')
		get_flux_color('menu.title.textColor', None, 'main:control_font_fg')

		# -------- menu.frame
		theme_obj.add_stylecontrol('menu')
		get_flux_color_dual('menu.frame', 'menu', 'main:control_bg')
		get_flux_color('menu.frame.foregroundColor', 'menu', 'main:control_fg')
		get_flux_color('menu.frame.textColor', 'menu', 'main:control_font_fg')
		get_flux_color('menu.frame.disabledColor', 'menu', 'inactive:control_fg')
		add_data('menu.frame.alignment', 'menu', 'main', 'text_alignment', 'string')
		add_data('menu.frame.marginwidth', 'menu', 'main', 'margin_width', 'int')

		get_flux_color_dual('menu.frame', None, 'main:control_bg')
		get_flux_color('menu.frame.foregroundColor', None, 'main:control_fg')
		get_flux_color('menu.frame.textColor', None, 'main:control_fg')
		get_flux_color('menu.frame.disabledColor', None, 'inactive:control_fg')

		# -------- menu.active
		get_flux_color_dual('menu.active', None, 'main:edit_bg_selected')
		get_flux_color('menu.active.foregroundColor', None, 'main:edit_fg_selected')
		get_flux_color('menu.active.textColor', None, 'main:edit_font_fg_selected')

		get_flux_color_dual('menu.active', 'menu', 'focused:control_bg')
		get_flux_color('menu.active.foregroundColor', 'menu', 'focused:control_fg')
		get_flux_color('menu.active.textColor', 'menu', 'focused:control_font_fg')

		# -------- slit
		theme_obj.add_stylecontrol('slit')
		get_flux_color_dual('slit', 'slit', 'main:control_bg')
		add_data('slit.marginwidth', 'slit', 'main', 'margin_width', 'int')

		# -------- toolbar
		theme_obj.add_stylecontrol('taskbar')
		get_flux_color_dual('toolbar', 'taskbar', 'main:control_bg')
		add_data('toolbar.alignment', 'taskbar', 'main', 'text_alignment', 'string')
		add_data('toolbar.marginwidth', 'taskbar', 'main', 'margin_width', 'int')

		# -------- toolbar.label
		theme_obj.add_stylecontrol('taskbar_label')
		get_flux_color_dual('toolbar.label', 'taskbar_label', 'main:control_bg')
		get_flux_color('toolbar.label.textColor', 'taskbar_label', 'main:control_fg')
		add_data('toolbar.label.marginwidth', 'taskbar_label', 'main', 'margin_width', 'int')

		# -------- toolbar.windowLabel
		theme_obj.add_stylecontrol('taskbar_button_app')
		get_flux_color_dual('toolbar.windowLabel', 'taskbar_button_app', 'main:control_bg')
		get_flux_color('toolbar.windowLabel.textColor', 'taskbar_button_app', 'main:control_fg')

		# -------- toolbar.clock
		theme_obj.add_stylecontrol('clock')
		get_flux_color_dual('toolbar.clock', 'clock', 'main:control_bg')
		get_flux_color('toolbar.clock.textColor', 'clock', 'main:control_fg')

		# -------- toolbar.button
		theme_obj.add_stylecontrol('taskbar_button')
		get_flux_color_dual('toolbar.button', 'taskbar_button', 'main:control_bg')
		get_flux_color_dual('toolbar.button.pressed', 'taskbar_button', 'pressed:control_bg')
		get_flux_color('toolbar.button.foregroundColor', 'taskbar_button', 'main:control_fg')
		add_data('toolbar.button.marginwidth', 'taskbar_button', 'main', 'margin_width', 'int')

		get_flux_color_dual('toolbar.button', None, 'main:control_bg')

		# -------- window.title
		theme_obj.add_stylecontrol('window_back')
		# focus
		get_flux_color_dual('window.title.focus', 'window_back', 'main:control_bg')
		# unfocus
		get_flux_color_dual('window.title.unfocus', 'window_back', 'inactive:control_bg')

		add_data('window.title.marginwidth', 'window_back', 'main', 'margin_width', 'int')

		# -------- window.label
		theme_obj.add_stylecontrol('titlebar')
		# focus
		get_flux_color_dual('window.label.focus', 'titlebar', 'main:control_bg')
		get_flux_color('window.label.focus.textColor', 'titlebar', 'main:control_fg')
		# unfocus
		get_flux_color_dual('window.label.unfocus', 'titlebar', 'inactive:control_bg')
		get_flux_color('window.label.unfocus.textColor', 'titlebar', 'inactive:control_fg')

		add_data('window.label.marginwidth', 'titlebar', 'main', 'margin_width', 'int')

		# -------- window.button
		theme_obj.add_stylecontrol('window_button')
		# focus
		get_flux_color_dual('window.button.focus', 'window_button', 'main:control_bg')
		get_flux_color('window.button.focus.foregroundColor', 'window_button', 'main:control_fg')
		# unfocus
		get_flux_color_dual('window.button.unfocus', 'window_button', 'inactive:control_bg')
		get_flux_color('window.button.unfocus.foregroundColor', 'window_button', 'inactive:control_fg')
		# pressed
		get_flux_color_dual('window.button.pressed', 'window_button', 'pressed:control_bg')
		get_flux_color('window.button.focus.foregroundColor', 'window_button', 'pressed:control_fg')

		add_data('window.button.marginwidth', 'window_button', 'main', 'margin_width', 'int')

		# -------- window.handle
		theme_obj.add_stylecontrol('window_handle')
		# focus
		get_flux_color_dual('window.handle.focus', 'window_handle', 'main:control_bg')
		# unfocus
		get_flux_color_dual('window.handle.unfocus', 'window_handle', 'inactive:control_bg')

		# -------- window.grip
		theme_obj.add_stylecontrol('window_grip')
		# focus
		get_flux_color_dual('window.grip.focus', 'window_grip', 'main:control_bg')
		# unfocus
		get_flux_color_dual('window.grip.unfocus', 'window_grip', 'inactive:control_bg')

		# -------- window.frame
		theme_obj.add_stylecontrol('window')
		add_data('window.frame.borderWidth', 'window', 'main', 'border_width', 'int')
		# focus
		get_flux_color('window.frame.focus.borderColor', 'window', 'main:border')
		# unfocus
		get_flux_color('window.frame.unfocus.borderColor', 'window', 'inactive:border')

		# -------- window
		add_data('window.alignment', 'window', 'main', 'text_alignment', 'string')
		add_data('window.handleHeight', 'window', 'main', 'handle_height', 'int')







		# -------- desktop
		theme_obj.add_stylecontrol('desktop')
		get_flux_color('slit.backgroundColor', 'desktop', 'main:control_bg')

		# -------- toolbar.button
		theme_obj.add_stylecontrol('taskbar_button')
