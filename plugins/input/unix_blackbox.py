
import plugins
from objects import visual

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
			color = blackboxtheme.get_data(name)
			if color: 
				color = fluxbox.get_color(color)
				theme_obj.add_color(control, colloc, color)

		def get_flux_color_merge(name1, name2, control, colloc):
			color1 = blackboxtheme.get_data(name1)
			color2 = blackboxtheme.get_data(name2)

			if color1 and color2: 
				outcolor1 = visual.visual_color().from_int(fluxbox.get_color(color1))
				outcolor2 = visual.visual_color().from_int(fluxbox.get_color(color2))
				outcol = color.mix_color(outcolor1, outcolor2, 0.5)
				theme_obj.add_color(control, colloc, outcol.get_int())

		get_flux_color('menu.frame.backgroundColor', None, 'main:control_bg')
		get_flux_color('menu.frame.textColor', None, 'main:control_fg')
		get_flux_color('menu.frame.disabledColor', None, 'inactive:edit_fg')
		get_flux_color('menu.active.backgroundColor', None, 'main:edit_bg_selected')
		get_flux_color('menu.active.foregroundColor', None, 'main:edit_fg_selected')
		get_flux_color('toolbar.button.color', None, 'main:control_bg')
		get_flux_color('toolbar.button.picColor', None, 'main:control_fg')

		get_flux_color('menu.title.backgroundColor', None, 'main:edit_bg')
		get_flux_color('menu.title.textColor', None, 'main:edit_fg')

		# desktop
		theme_obj.add_stylecontrol('desktop')
		get_flux_color('slit.backgroundColor', 'desktop', 'main:control_bg')

		# titlebar
		theme_obj.add_stylecontrol('titlebar')
		get_flux_color('window.title.color1', 'titlebar', 'main:control_bg')
		get_flux_color('window.title.color2', 'titlebar', 'main:control_bg_second')

		get_flux_color('window.title.focus.color1', 'titlebar', 'main:control_bg')
		get_flux_color('window.title.focus.color2', 'titlebar', 'main:control_bg_second')
		get_flux_color('window.label.focus.textColor', 'titlebar', 'main:control_fg')

		get_flux_color('window.title.unfocus.color1', 'titlebar', 'inactive:control_bg')
		get_flux_color('window.title.unfocus.color2', 'titlebar', 'inactive:control_bg_second')
		get_flux_color('window.label.unfocus.textColor', 'titlebar', 'inactive:control_fg')

		# titlebar_button
		theme_obj.add_stylecontrol('titlebar_button')
		get_flux_color('window.button.focus.foregroundColor', 'titlebar_button', 'main:control_fg')
		get_flux_color('window.button.unfocus.foregroundColor', 'titlebar_button', 'inactive:control_fg')

		# menu
		theme_obj.add_stylecontrol('menu')
		get_flux_color('menu.frame.foregroundColor', 'menu', 'main:control_bg')
		get_flux_color('menu.frame.textColor', 'menu', 'main:control_fg')
		get_flux_color('menu.frame.disabledColor', 'menu', 'inactive:control_fg')
		get_flux_color('menu.active.backgroundColor', 'menu', 'main:control_bg_selected')
		get_flux_color('menu.active.foregroundColor', 'menu', 'main:control_fg_selected')
		get_flux_color_merge('menu.frame.foregroundColor', 'menu.frame.foregroundColorto', 'menu', 'main:control_bg_selected')
