
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
		from objects.file_theme import fluxbox
		fluxboxtheme = fluxbox.fluxbox_theme()
		fluxboxtheme.read(themeverter_intent.input_file)

		def get_flux_color(name, control, colloc):
			incolor = fluxboxtheme.get_data(name)
			if incolor: 
				incolor = fluxbox.get_color(incolor)
				theme_obj.add_color(control, colloc, incolor)

		def get_flux_color_dual(name, control, colloc):
			colord = fluxboxtheme.get_data(name)
			color1 = fluxboxtheme.get_data(name+'.color')
			color2 = fluxboxtheme.get_data(name+'.colorTo')

			colordata = colord.split(' ') if colord else []

			if color1 and color2 and 'gradient' in colordata: 
				outcolor1 = visual.visual_color().from_int(fluxbox.get_color(color1))
				outcolor2 = visual.visual_color().from_int(fluxbox.get_color(color2))
				outcol = color.mix_color(outcolor1, outcolor2, 0.5)
				theme_obj.add_color(control, colloc, outcol.get_int())

				state, name = colloc.split(':')

				theme_obj.add_prop(control, state, 'color_fx:'+name, 'gradent')
				theme_obj.add_prop(control, state, 'gradent_colors:'+name, 'gradent1,gradent2')
				theme_obj.add_color(control, state+':gradent1', fluxbox.get_color(color1))
				theme_obj.add_color(control, state+':gradent2', fluxbox.get_color(color2))
			else:
				if color1:
					color1 = fluxbox.get_color(color1)
					theme_obj.add_color(control, colloc, color1)


		# window
		theme_obj.add_stylecontrol('titlebar')
		theme_obj.add_stylecontrol('titlebar_button')
		get_flux_color_dual('window.button.unfocus', 'titlebar_button', 'main:control_bg')
		get_flux_color_dual('window.button.focus', 'titlebar_button', 'hover:control_bg')
		get_flux_color_dual('window.button.pressed', 'titlebar_button', 'pressed:control_bg')
		get_flux_color('window.button.unfocus.picColor', 'titlebar_button', 'main:control_fg')
		get_flux_color('window.button.focus.picColor', 'titlebar_button', 'hover:control_fg')
		get_flux_color('window.button.pressed.picColor', 'titlebar_button', 'pressed:control_fg')
		get_flux_color_dual('window.title', 'titlebar', 'main:control_bg')
		get_flux_color_dual('window.label', 'titlebar', 'main:control_bg')
		get_flux_color('window.label.textColor', 'titlebar', 'main:control_fg')
		get_flux_color_dual('window.label.unfocus', 'titlebar', 'inactive:control_bg')
		get_flux_color('window.label.unfocus.textColor', 'titlebar', 'inactive:control_fg')

		# menu.frame
		theme_obj.add_stylecontrol('menu')
		get_flux_color_dual('menu.frame', None, 'main:control_bg')
		get_flux_color_dual('menu.frame', None, 'main:edit_bg')
		get_flux_color('menu.frame.textColor', None, 'main:control_fg')
		get_flux_color('menu.frame.textColor', None, 'main:edit_fg')
		get_flux_color('menu.frame.disableColor', None, 'inactive:edit_fg')
		get_flux_color_dual('menu.frame', 'menu', 'main:control_bg')
		get_flux_color('menu.frame.textColor', 'menu', 'main:control_fg')
		get_flux_color('menu.frame.disableColor', 'menu', 'inactive:control_fg')

		# menu.hilite
		get_flux_color('menu.hilite.color', None, 'main:edit_bg_selected')
		get_flux_color('menu.hilite.textColor', None, 'main:edit_fg_selected')
		get_flux_color_dual('menu.hilite', 'menu', 'main:control_bg_selected')
		get_flux_color('menu.hilite.textColor', 'menu', 'main:control_fg_selected')

		# menu.title
		theme_obj.add_stylecontrol('menu_header')
		get_flux_color_dual('menu.title', 'menu_header', 'main:control_bg')
		get_flux_color('menu.title.textColor', 'menu_header', 'inactive:control_fg')

		# toolbar
		theme_obj.add_stylecontrol('taskbar')
		get_flux_color_dual('toolbar', 'taskbar', 'main:control_bg')

		# toolbar.clock
		theme_obj.add_stylecontrol('clock')
		get_flux_color_dual('toolbar.clock', 'clock', 'main:control_bg')
		get_flux_color('toolbar.clock.textColor', 'clock', 'main:control_fg')

		# toolbar.button
		get_flux_color('toolbar.button.color', None, 'main:control_bg')
		get_flux_color('toolbar.button.picColor', None, 'main:control_fg')
		theme_obj.add_stylecontrol('taskbar_button')
		get_flux_color_dual('toolbar.button', 'taskbar_button', 'main:control_bg')
		get_flux_color('toolbar.button.picColor', 'taskbar_button', 'main:control_fg')

		# toolbar.label
		theme_obj.add_stylecontrol('taskbar_label')
		get_flux_color_dual('toolbar.label', 'taskbar_label', 'main:control_bg')
		get_flux_color('toolbar.label.textColor', 'taskbar_label', 'main:control_fg')

		# toolbar.windowLabel
		theme_obj.add_stylecontrol('taskbar_button_app')
		get_flux_color_dual('toolbar.windowLabel', 'taskbar_button_app', 'main:control_bg')
		get_flux_color('toolbar.windowLabel.textColor', 'taskbar_button_app', 'main:control_fg')



		# desktop
		theme_obj.add_stylecontrol('desktop')
		get_flux_color('background.color', 'desktop', 'main:control_bg')

		# menu_header

		# menu
		theme_obj.add_stylecontrol('menu')