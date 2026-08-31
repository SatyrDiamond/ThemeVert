
import plugins
from objects import visual

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
			color = fluxboxtheme.get_data(name)
			if color: 
				color = fluxbox.get_color(color)
				theme_obj.add_color(control, colloc, color)

		def get_flux_color_merge(name1, name2, control, colloc):
			color1 = fluxboxtheme.get_data(name1)
			color2 = fluxboxtheme.get_data(name2)

			if color1 and color2: 
				outcolor1 = visual.visual_color().from_int(fluxbox.get_color(color1))
				outcolor2 = visual.visual_color().from_int(fluxbox.get_color(color2))
				outcol = color.mix_color(outcolor1, outcolor2, 0.5)
				theme_obj.add_color(control, colloc, outcol.get_int())

		get_flux_color('menu.frame.color', None, 'main:control_bg')
		get_flux_color('menu.frame.color', None, 'main:edit_bg')
		get_flux_color_merge('menu.frame.color', 'menu.frame.colorto', None, 'main:control_bg')
		get_flux_color_merge('menu.frame.color', 'menu.frame.colorto', None, 'main:edit_bg')

		get_flux_color('menu.frame.textColor', None, 'main:control_fg')
		get_flux_color('menu.frame.textColor', None, 'main:edit_fg')
		get_flux_color('menu.frame.disableColor', None, 'inactive:edit_fg')

		get_flux_color('menu.hilite.color', None, 'main:edit_bg_selected')
		get_flux_color('menu.hilite.textColor', None, 'main:edit_fg_selected')

		get_flux_color('toolbar.button.color', None, 'main:control_bg')
		get_flux_color('toolbar.button.picColor', None, 'main:control_fg')

		# desktop
		theme_obj.add_stylecontrol('desktop')
		get_flux_color('background.color', 'desktop', 'main:control_bg')

		# titlebar
		theme_obj.add_stylecontrol('titlebar')
		get_flux_color('window.title.color', 'titlebar', 'main:control_bg')
		get_flux_color('window.title.colorTo', 'titlebar', 'main:control_bg_second')

		get_flux_color('window.title.focus.color', 'titlebar', 'main:control_bg')
		get_flux_color('window.title.focus.colorTo', 'titlebar', 'main:control_bg_second')
		get_flux_color('window.label.focus.textColor', 'titlebar', 'main:control_fg')

		get_flux_color('window.title.unfocus.color', 'titlebar', 'inactive:control_bg')
		get_flux_color('window.title.unfocus.colorTo', 'titlebar', 'inactive:control_bg_second')
		get_flux_color('window.label.unfocus.textColor', 'titlebar', 'inactive:control_fg')

		# titlebar_button
		theme_obj.add_stylecontrol('titlebar_button')
		get_flux_color('window.button.focus.color', 'titlebar_button', 'main:control_bg')
		get_flux_color('window.button.focus.picColor', 'titlebar_button', 'main:control_fg')
		get_flux_color('window.button.unfocus.Color', 'titlebar_button', 'inactive:control_bg')
		get_flux_color('window.button.unfocus.picColor', 'titlebar_button', 'inactive:control_fg')

		# menu
		theme_obj.add_stylecontrol('menu')
		get_flux_color('menu.frame.color', 'menu', 'main:control_bg')
		get_flux_color('menu.frame.textColor', 'menu', 'main:control_fg')
		get_flux_color('menu.frame.disableColor', 'menu', 'inactive:control_fg')
		get_flux_color('menu.hilite.color', 'menu', 'main:control_bg_selected')
		get_flux_color('menu.hilite.textColor', 'menu', 'main:control_fg_selected')
		get_flux_color_merge('menu.frame.color', 'menu.frame.colorto', 'menu', 'main:control_bg_selected')