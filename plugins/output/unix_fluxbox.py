
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
		from objects.file_theme import manybox
		manyboxtheme = manybox.manybox_theme()
		manyboxtheme.set_fluxbox()

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

				if gradent_type=='horizontal': outprops += ' horizontal'
				if gradent_type=='vertical': outprops += ' vertical'
				if gradent_type=='diagonal': outprops += ' diagonal'
				if gradent_type=='crossdiagonal': outprops += ' crossdiagonal'
				if gradent_type=='pipecross': outprops += ' pipecross'
				if gradent_type=='elliptic': outprops += ' elliptic'
				if gradent_type=='rectangle': outprops += ' rectangle'
				if gradent_type=='pyramid': outprops += ' pyramid'

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

		# -------- desktop
		do_color_dual(False, 'background', 'desktop', 'main:control_bg', 'flat')

		# -------- window.button
		do_color_dual(False, 'window.button.unfocus', 'window_button', 'inactive:control_bg', None)
		do_color_dual(False, 'window.button.focus', 'window_button', 'main:control_bg', None)
		do_color_dual(False, 'window.button.pressed', 'window_button', 'pressed:control_bg', 'sunken')
		do_color('window.button.unfocus.picColor', 'window_button', 'inactive:control_fg')
		do_color('window.button.focus.picColor', 'window_button', 'main:control_fg')
		#do_color('window.button.pressed.picColor', 'window_button', 'pressed:control_fg')

		# -------- window.title
		do_color_dual(False, 'window.title.focus', 'window_back', 'main:control_bg', None)
		do_color_dual(False, 'window.title.unfocus', 'window_back', 'inactive:control_bg', None)

		# -------- window.label
		do_color_dual(False, 'window.label.focus', 'titlebar', 'main:control_bg', None)
		do_color('window.label.focus.textColor', 'titlebar', 'main:control_font_fg')
		do_color_dual(False, 'window.label.unfocus', 'titlebar', 'inactive:control_bg', None)
		do_color('window.label.unfocus.textColor', 'titlebar', 'inactive:control_font_fg')
		do_data('window.label.focus.justify', 'titlebar', 'main', 'text_alignment', 'left')
		do_data('window.label.unfocus.justify', 'titlebar', 'inactive', 'text_alignment', 'left')

		# -------- window.handle
		do_color_dual(False, 'window.handle.focus', 'window_handle', 'main:control_bg', None)
		do_color_dual(False, 'window.handle.unfocus', 'window_handle', 'inactive:control_bg', None)

		# -------- window.grip
		do_color_dual(False, 'window.grip.focus', 'window_grip', 'main:control_bg', None)
		do_color_dual(False, 'window.grip.unfocus', 'window_grip', 'inactive:control_bg', None)

		# -------- window
		if not do_color('window.borderColor', 'window', 'main:border'):
			do_color('window.borderColor', None, 'main:control_bg')
		do_data('window.borderWidth', 'window', 'main', 'border_width', '1')

		do_color('window.frame.focusColor', None, 'main:control_bg')
		do_color('window.frame.unfocusColor', None, 'inactive:control_bg')
		
		manyboxtheme.add_data('window.title.height', '24')
		manyboxtheme.add_data('window.font', 'lucidasans-12')
		do_data('window.justify', 'window', 'main', 'text_alignment', 'left')

		# -------- menu
		#manyboxtheme.add_data('menu.bevelWidth', '1')
		#if not do_color('menu.borderColor', 'menu', 'main:border'):
		#	do_color('menu.borderColor', None, 'main:control_bg')
		#do_data('menu.borderWidth', 'menu', 'main', 'border_width', '1')

		# -------- menu.bullet
		manyboxtheme.add_data('menu.bullet.position', 'right')
		manyboxtheme.add_data('menu.bullet', 'triangle')

		# -------- menu.frame
		do_color_dual(False, 'menu.frame', 'menu', 'main:control_bg', None)
		do_color('menu.frame.disableColor', 'menu', 'inactive:control_fg')
		manyboxtheme.add_data('menu.frame.font', 'lucidasans-12')
		do_data('menu.frame.justify', 'menu_header', 'main', 'text_alignment', 'left')
		do_color('menu.frame.textColor', 'menu', 'main:control_font_fg')

		# -------- menu.hilite
		colc1 = do_color_dual(False, 'menu.hilite', 'menu', 'focused:control_bg', None)
		colc2 = do_color('menu.hilite.textcolor', 'menu', 'focused:control_font_fg')
		if (not colc1) or (not colc2):
			do_color_dual(False, 'menu.hilite', None, 'main:edit_bg_selected', None)
			do_color('menu.hilite.textcolor', None, 'main:edit_fg_selected')

		# -------- menu.title
		if not do_color_dual(True, 'menu.title', 'menu_header', 'main:control_bg', None):
			do_color_dual(False, 'menu.title', 'titlebar', 'main:control_bg', None)
		if not do_color_spec('menu.title.textColor', 'menu_header', 'main:control_fg'):
			do_color('menu.title.textColor', 'titlebar', 'main:control_font_fg')

		manyboxtheme.add_data('menu.title.font', 'lucidasans-12')
		do_data('menu.title.justify', 'menu_header', 'main', 'text_alignment', 'center')
		manyboxtheme.add_data('menu.titleHeight', '30')

		# -------- toolbar
		do_color_dual(False, 'toolbar', 'taskbar', 'main:control_bg', None)
		do_color('toolbar.textColor', 'taskbar', 'main:control_fg')
		do_color('toolbar.textColor', 'taskbar', 'main:control_font_fg')
		manyboxtheme.add_data('toolbar.height', '24')
		do_data('toolbar.justify', 'taskbar', 'main', 'text_alignment', 'left')
		manyboxtheme.add_data('toolbar.font', 'lucidasans-12')

		# -------- toolbar.clock
		do_color_dual(False, 'toolbar.clock', 'clock', 'main:control_bg', None)
		do_color('toolbar.clock.textColor', 'clock', 'main:control_fg')

		# -------- toolbar.button
		do_color_dual(False, 'toolbar.button', 'taskbar_button', 'main:control_bg', None)
		do_color('toolbar.button.picColor', 'taskbar_button', 'main:control_fg')
		do_color_dual(False, 'toolbar.button.pressed', 'taskbar_button', 'pressed:control_bg', 'sunken')
		#do_color('toolbar.button.pressed.picColor', 'taskbar_button', 'pressed:control_fg')

		# -------- toolbar.label
		do_color_dual(False, 'toolbar.label', 'taskbar_label', 'main:control_bg', None)
		do_color('toolbar.label.textColor', 'taskbar_label', 'main:control_fg')

		# -------- toolbar.windowLabel
		colorv1 = do_color_dual(True, 'toolbar.windowLabel', 'taskbar_button_app', 'main:control_bg', None)
		colorv2 = do_color_spec('toolbar.windowLabel.textColor', 'taskbar_button_app', 'main:control_fg')
		if not (colorv1 and colorv2):
			colorv1 = do_color_dual(False, 'toolbar.windowLabel', 'titlebar', 'main:control_bg', None)
			colorv2 = do_color('toolbar.windowLabel.textColor', 'titlebar', 'main:control_font_fg')

		# -------- others
		if not do_color('borderColor', 'window', 'main:border'):
			do_color('borderColor', None, 'main:control_bg')
		#manyboxtheme.add_data('bevelWidth', '2')
		do_data('borderWidth', 'window', 'main', 'border_width', '1')
		do_data('framewidth', 'window', 'main', 'handle_height', '0')
		do_data('bevelWidth', 'window', 'main', 'handle_height', '1')
		do_data('handleWidth', 'window', 'main', 'handle_height', '5')

		#themedata = fluxboxtheme.data_wildcard

		#do_color_dual(False, '*button.pressed', None, 'pressed:control_bg', 'sunken border')
		#do_color_dual(False, '*button.pressed.picColor', None, 'pressed:control_fg', None)

		#manyboxtheme.add_data_wild('*font', 'lucidasans-12')

		#do_color('*textColor', None, 'main:control_fg')

		manyboxtheme.write(themeverter_intent.output_file)
