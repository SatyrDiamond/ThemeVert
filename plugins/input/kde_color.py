
import plugins

from functions import color

def conv_color(c): 
	if c.startswith('#'): return color.hex_to_int(c)
	else: return [int(x) for x in c.split(',')]

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'kde_color'
	
	def get_name(self):
		return 'KDE/Plasma Color Scheme'
	
	def get_prop(self):
		prop = {}
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		import configparser

		config = configparser.ConfigParser()
		config.read(themeverter_intent.input_file)

		def do_colors(tstyle, colorset, name):
			txt_backgroundnormal = 'kde_%s_BackgroundNormal' % name
			txt_backgroundalternate = 'kde_%s_BackgroundAlternate' % name
			txt_foregroundnormal = 'kde_%s_ForegroundNormal' % name
			txt_foregroundinactive = 'kde_%s_ForegroundInactive' % name
			txt_foregroundlink = 'kde_%s_ForegroundLink' % name
			txt_foregroundvisited = 'kde_%s_ForegroundVisited' % name
			txt_foregroundactive = 'kde_%s_ForegroundActive' % name
			txt_foregroundnegative = 'kde_%s_ForegroundNegative' % name
			txt_foregroundneutral = 'kde_%s_ForegroundNeutral' % name
			txt_foregroundpositive = 'kde_%s_ForegroundPositive' % name

			theme_obj.add_global_color(txt_backgroundnormal, conv_color(colorset['BackgroundNormal']) )
			tstyle.add_color_named('main:control_bg', txt_backgroundnormal)
			if 'BackgroundAlternate' in colorset:
				theme_obj.add_global_color(txt_backgroundalternate, conv_color(colorset['BackgroundAlternate']) )
				tstyle.add_color_named('main:control_bg_alt', txt_backgroundalternate)

			theme_obj.add_global_color(txt_foregroundnormal, conv_color(colorset['ForegroundNormal']) )
			tstyle.add_color_named('main:control_fg', txt_foregroundnormal)

			if 'ForegroundInactive' in colorset:
				theme_obj.add_global_color(txt_foregroundinactive, conv_color(colorset['ForegroundInactive']) )
				tstyle.add_color_named('inactive:control_fg', txt_foregroundinactive)

			if 'ForegroundLink' in colorset:
				theme_obj.add_global_color(txt_foregroundlink, conv_color(colorset['ForegroundLink']) )
				tstyle.add_color_named('main:control_fg_url', txt_foregroundlink)

			if 'ForegroundVisited' in colorset:
				theme_obj.add_global_color(txt_foregroundvisited, conv_color(colorset['ForegroundVisited']) )
				tstyle.add_color_named('main:control_fg_url_visited', txt_foregroundvisited)

			if 'ForegroundActive' in colorset:
				theme_obj.add_global_color(txt_foregroundactive, conv_color(colorset['ForegroundActive']) )
				tstyle.add_color_named('main:control_fg_active', txt_foregroundactive)

			if 'ForegroundNegative' in colorset:
				theme_obj.add_global_color(txt_foregroundnegative, conv_color(colorset['ForegroundNegative']) )
				tstyle.add_color_named('main:control_fg_negative', txt_foregroundnegative)

			if 'ForegroundNeutral' in colorset:
				theme_obj.add_global_color(txt_foregroundneutral, conv_color(colorset['ForegroundNeutral']) )
				tstyle.add_color_named('main:control_fg_neutral', txt_foregroundneutral)

			if 'ForegroundPositive' in colorset:
				theme_obj.add_global_color(txt_foregroundpositive, conv_color(colorset['ForegroundPositive']) )
				tstyle.add_color_named('main:control_fg_positive', txt_foregroundpositive)
		
		style_glob = theme_obj.style_global
		if 'Colors:Window' in config:
			do_colors(style_glob, config['Colors:Window'], 'win')

		if 'Colors:Button' in config:
			curstyle, curctrl = theme_obj.add_stylecontrol('button')
			do_colors(curstyle, config['Colors:Button'], 'button')

		if 'Colors:Tooltip' in config:
			curstyle, curctrl = theme_obj.add_stylecontrol('tooltip')
			do_colors(curstyle, config['Colors:Tooltip'], 'tooltip')
			
		if 'Colors:Complementary' in config:
			curstyle, curctrl = theme_obj.add_stylecontrol('complementary')
			do_colors(curstyle, config['Colors:Complementary'], 'complementary')
			
		if 'Colors:View' in config:
			name = 'view'
			colorset = config['Colors:View']
			tstyle = style_glob
			txt_backgroundnormal = 'kde_%s_BackgroundNormal' % name
			txt_backgroundalternate = 'kde_%s_BackgroundAlternate' % name
			txt_foregroundnormal = 'kde_%s_ForegroundNormal' % name
			txt_foregroundinactive = 'kde_%s_ForegroundInactive' % name
			txt_foregroundlink = 'kde_%s_ForegroundLink' % name
			txt_foregroundvisited = 'kde_%s_ForegroundVisited' % name
			txt_foregroundactive = 'kde_%s_ForegroundActive' % name
			txt_foregroundnegative = 'kde_%s_ForegroundNegative' % name
			txt_foregroundneutral = 'kde_%s_ForegroundNeutral' % name
			txt_foregroundpositive = 'kde_%s_ForegroundPositive' % name

			theme_obj.add_global_color(txt_backgroundnormal, conv_color(colorset['BackgroundNormal']) )
			theme_obj.add_global_color(txt_backgroundalternate, conv_color(colorset['BackgroundAlternate']) )
			tstyle.add_color_named('main:edit_bg', txt_backgroundnormal)
			tstyle.add_color_named('main:edit_bg_alt', txt_backgroundalternate)

			theme_obj.add_global_color(txt_foregroundnormal, conv_color(colorset['ForegroundNormal']) )
			theme_obj.add_global_color(txt_foregroundinactive, conv_color(colorset['ForegroundInactive']) )
			tstyle.add_color_named('main:edit_fg', txt_foregroundnormal)
			tstyle.add_color_named('inactive:edit_fg', txt_foregroundinactive)

			theme_obj.add_global_color(txt_foregroundlink, conv_color(colorset['ForegroundLink']) )
			theme_obj.add_global_color(txt_foregroundvisited, conv_color(colorset['ForegroundVisited']) )
			tstyle.add_color_named('main:edit_fg_url', txt_foregroundlink)
			tstyle.add_color_named('main:edit_fg_url_visited', txt_foregroundvisited)

			theme_obj.add_global_color(txt_foregroundactive, conv_color(colorset['ForegroundActive']) )
			theme_obj.add_global_color(txt_foregroundnegative, conv_color(colorset['ForegroundNegative']) )
			theme_obj.add_global_color(txt_foregroundneutral, conv_color(colorset['ForegroundNeutral']) )
			theme_obj.add_global_color(txt_foregroundpositive, conv_color(colorset['ForegroundPositive']) )
			tstyle.add_color_named('main:edit_fg_active', txt_foregroundactive)
			tstyle.add_color_named('main:edit_fg_negative', txt_foregroundnegative)
			tstyle.add_color_named('main:edit_fg_neutral', txt_foregroundneutral)
			tstyle.add_color_named('main:edit_fg_positive', txt_foregroundpositive)

		if 'Colors:Selection' in config:
			name = 'selection'
			colorset = config['Colors:Selection']
			tstyle = style_glob
			txt_backgroundnormal = 'kde_%s_BackgroundNormal' % name
			txt_backgroundalternate = 'kde_%s_BackgroundAlternate' % name
			txt_foregroundnormal = 'kde_%s_ForegroundNormal' % name
			txt_foregroundinactive = 'kde_%s_ForegroundInactive' % name
			txt_foregroundlink = 'kde_%s_ForegroundLink' % name
			txt_foregroundvisited = 'kde_%s_ForegroundVisited' % name
			txt_foregroundactive = 'kde_%s_ForegroundActive' % name
			txt_foregroundnegative = 'kde_%s_ForegroundNegative' % name
			txt_foregroundneutral = 'kde_%s_ForegroundNeutral' % name
			txt_foregroundpositive = 'kde_%s_ForegroundPositive' % name

			theme_obj.add_global_color(txt_backgroundnormal, conv_color(colorset['BackgroundNormal']) )
			theme_obj.add_global_color(txt_backgroundalternate, conv_color(colorset['BackgroundAlternate']) )
			tstyle.add_color_named('main:edit_bg_selected', txt_backgroundnormal)
			tstyle.add_color_named('main:edit_bg_selected_alt', txt_backgroundalternate)

			theme_obj.add_global_color(txt_foregroundnormal, conv_color(colorset['ForegroundNormal']) )
			theme_obj.add_global_color(txt_foregroundinactive, conv_color(colorset['ForegroundInactive']) )
			tstyle.add_color_named('main:edit_fg_selected', txt_foregroundnormal)
			tstyle.add_color_named('inactive:edit_fg_selected', txt_foregroundinactive)

			if 'ForegroundLink' in colorset:
				theme_obj.add_global_color(txt_foregroundlink, conv_color(colorset['ForegroundLink']) )
				tstyle.add_color_named('main:edit_fg_selected_url', txt_foregroundlink)

			if 'ForegroundVisited' in colorset:
				theme_obj.add_global_color(txt_foregroundvisited, conv_color(colorset['ForegroundVisited']) )
				tstyle.add_color_named('main:edit_fg_selected_url_visited', txt_foregroundvisited)

			if 'ForegroundVisited' in colorset:
				theme_obj.add_global_color(txt_foregroundvisited, conv_color(colorset['ForegroundVisited']) )
				tstyle.add_color_named('main:control_fg_url_visited', txt_foregroundvisited)

			if 'ForegroundActive' in colorset:
				theme_obj.add_global_color(txt_foregroundactive, conv_color(colorset['ForegroundActive']) )
				tstyle.add_color_named('main:edit_fg_selected_active', txt_foregroundactive)

			if 'ForegroundNegative' in colorset:
				theme_obj.add_global_color(txt_foregroundnegative, conv_color(colorset['ForegroundNegative']) )
				tstyle.add_color_named('main:edit_fg_selected_negative', txt_foregroundnegative)

			if 'ForegroundNeutral' in colorset:
				theme_obj.add_global_color(txt_foregroundneutral, conv_color(colorset['ForegroundNeutral']) )
				tstyle.add_color_named('main:edit_fg_selected_neutral', txt_foregroundneutral)

			if 'ForegroundPositive' in colorset:
				theme_obj.add_global_color(txt_foregroundpositive, conv_color(colorset['ForegroundPositive']) )
				tstyle.add_color_named('main:edit_fg_selected_positive', txt_foregroundpositive)
				
		if 'WM' in config:
			colorset = config['WM']

			theme_obj.add_global_color('wm_activeBackground', conv_color(colorset['activeBackground']) )
			theme_obj.add_global_color('wm_activeBlend', conv_color(colorset['activeBlend']) )
			theme_obj.add_global_color('wm_activeForeground', conv_color(colorset['activeForeground']) )
			theme_obj.add_global_color('wm_inactiveBackground', conv_color(colorset['inactiveBackground']) )
			theme_obj.add_global_color('wm_inactiveBlend', conv_color(colorset['inactiveBlend']) )
			theme_obj.add_global_color('wm_inactiveForeground', conv_color(colorset['inactiveForeground']) )

			curstyle, curctrl = theme_obj.add_stylecontrol('titlebar')
			curstyle.add_color_named('main:control_bg', 'wm_activeBackground')
			curstyle.add_color_named('main:control_bg_second', 'wm_activeBlend')
			curstyle.add_color_named('main:control_fg', 'wm_activeForeground')
			curstyle.add_prop('main', 'color_fx', 'gradent')
			curstyle.add_prop('main', 'gradent_color', 'user_gradent')
			curstyle.add_color_named('main:user_gradent', 'wm_activeBlend')

			curstyle.add_color_named('inactive:control_bg', 'wm_inactiveBackground')
			curstyle.add_color_named('inactive:control_fg', 'wm_inactiveForeground')
			curstyle.add_color_named('inactive:control_bg_second', 'wm_activeBlend')
			curstyle.add_prop('inactive', 'color_fx', 'gradent')
			curstyle.add_prop('inactive', 'gradent_color', 'user_gradent')
			curstyle.add_color_named('inactive:user_gradent', 'wm_inactiveBlend')
