
import plugins
from functions import color as colorfunc

class output_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'output'
	
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

		def do_color_dual(isspec, name, control, colloc):
			state, colname = colloc.split(':')
			
			color_fx = theme_obj.get_prop(control, state, 'color_fx:'+colname)
			themedata[name] = 'raised'

			if color_fx=='gradent':
				gradent_colors = theme_obj.get_prop(control, state, 'gradent_colors:'+colname)
				themedata[name] += ' gradient'
				gradent_colors = gradent_colors.split(',')
				do_color(name+'.color', control, state+':'+gradent_colors[0])
				do_color(name+'.colorTo', control, state+':'+gradent_colors[-1])
				return True
			else:
				themedata[name] += ' solid'
				if isspec: return do_color_spec(name+'.color', control, colloc)
				else: return do_color(name+'.color', control, colloc)
			return False

		# window
		do_color_dual(False, 'window.button.unfocus', 'titlebar_button', 'main:control_bg')
		do_color_dual(False, 'window.button.focus', 'titlebar_button', 'main:control_bg')
		do_color_dual(False, 'window.button.pressed', 'titlebar_button', 'pressed:control_bg')
		do_color('window.button.unfocus.picColor', 'titlebar_button', 'main:control_fg')
		do_color('window.button.focus.picColor', 'titlebar_button', 'main:control_fg')
		do_color('window.button.pressed.picColor', 'titlebar_button', 'pressed:control_fg')
		do_color_dual(False, 'window.grip.focus', 'titlebar', 'main:control_bg')
		do_color_dual(False, 'window.grip.unfocus', 'titlebar', 'main:control_bg')
		do_color_dual(False, 'window.handle.focus', 'titlebar', 'main:control_bg')
		do_color_dual(False, 'window.handle.unfocus', 'titlebar', 'main:control_bg')
		do_color_dual(False, 'window.label.focus', 'titlebar', 'main:control_bg')
		do_color('window.label.focus.textColor', 'titlebar', 'main:control_fg')
		do_color_dual(False, 'window.label.unfocus', 'titlebar', 'inactive:control_bg')
		do_color('window.label.unfocus.textColor', 'titlebar', 'inactive:control_fg')
		do_color_dual(False, 'window.title.focus', 'titlebar', 'main:control_bg')
		do_color_dual(False, 'window.title.unfocus', 'titlebar', 'main:control_bg')
		do_color('window.frame.focusColor', None, 'main:control_bg')
		do_color('window.frame.unfocusColor', None, 'main:control_bg')
		themedata['window.title.height'] = '24'
		themedata['window.font'] = 'lucidasans-12'
		themedata['window.justify'] = 'left'
		do_color('window.borderColor', None, 'main:control_fg')
		themedata['window.borderWidth'] = '1'

		# menu
		themedata['menu.bevelWidth'] = '1'
		themedata['menu.borderWidth'] = '1'

		# menu.bullet
		themedata['menu.bullet.position'] = 'right'
		themedata['menu.bullet'] = 'triangle'

		# menu.frame
		do_color_dual(False, 'menu.frame', 'menu', 'main:control_bg')
		do_color('menu.frame.disableColor', 'menu', 'inactive:control_fg')
		themedata['menu.frame.font'] = 'lucidasans-12'
		themedata['menu.frame.justify'] = 'center'
		do_color('menu.frame.textColor', 'menu', 'main:control_fg')

		# menu.hilite
		colc1 = do_color_dual(False, 'menu.hilite', 'menu', 'main:control_bg_selected')
		colc2 = do_color('menu.hilite.textcolor', 'menu', 'main:control_fg_selected')
		if (not colc1) or (not colc2):
			do_color_dual(False, 'menu.hilite', None, 'main:edit_bg_selected')
			do_color('menu.hilite.textcolor', None, 'main:edit_fg_selected')

		# menu.title
		if not do_color_dual(True, 'menu.title', 'menu_header', 'main:control_bg'):
			do_color_dual(False, 'menu.title', 'titlebar', 'main:control_bg')
		if not do_color_spec('menu.title.textColor', 'menu_header', 'main:control_fg'):
			do_color('menu.title.textColor', 'titlebar', 'main:control_fg')

		themedata['menu.title.font'] = 'lucidasans-12'
		themedata['menu.title.justify'] = 'center'
		themedata['menu.titleHeight'] = '30'

		# toolbar
		do_color_dual(False, 'toolbar', 'taskbar', 'main:control_bg')
		themedata['toolbar.height'] = '24'
		themedata['toolbar.justify'] = 'left'
		themedata['toolbar.font'] = 'lucidasans-12'

		# toolbar.clock
		do_color_dual(False, 'toolbar.clock', 'clock', 'main:control_bg')
		do_color('toolbar.clock.textColor', 'clock', 'main:control_fg')

		# toolbar.button
		do_color_dual(False, 'toolbar.button', 'taskbar_button', 'main:control_bg')
		do_color('toolbar.button.picColor', 'taskbar_button', 'main:control_fg')

		# toolbar.label
		do_color_dual(False, 'toolbar.label', 'taskbar_label', 'main:control_bg')
		do_color('toolbar.label.textColor', 'taskbar_label', 'main:control_fg')

		# toolbar.windowLabel
		do_color_dual(False, 'toolbar.windowLabel', 'taskbar_button_app', 'main:control_bg')
		do_color('toolbar.windowLabel.textColor', 'taskbar_button_app', 'main:control_fg')


		# others
		do_color('borderColor', None, 'main:control_fg')
		do_color('background', 'desktop', 'main:control_bg')
		themedata['bevelWidth'] = '2'
		themedata['borderWidth'] = '1'
		themedata['handleWidth'] = '2'

		themedata = fluxboxtheme.data_wildcard

		do_color_dual(False, '*button.pressed', None, 'pressed:control_bg')
		do_color_dual(False, '*button.pressed.picColor', None, 'pressed:control_fg')

		do_color('*textColor', None, 'main:control_fg')
		themedata['*Font'] = 'lucidasans-12'


		fluxboxtheme.write(themeverter_intent.output_file)
