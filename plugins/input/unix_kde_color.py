
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
		return '[Unix] KDE/Plasma Color Scheme'
	
	def get_prop(self):
		prop = {}
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		import configparser

		config = configparser.ConfigParser()
		config.read(themeverter_intent.input_file)

		theme_obj.add_stylecontrol('button')
		theme_obj.add_stylecontrol('tooltip')
		theme_obj.add_stylecontrol('complementary')
		theme_obj.add_stylecontrol('titlebar')

		def add_kde_color(kcolorset, colorcat, kcolorname, stylepart, colloc):
			if kcolorname in kcolorset:
				color_id = 'kde_%s_%s' % (colorcat, kcolorname)
				color = conv_color(kcolorset[kcolorname])
				theme_obj.add_global_color(color_id, color)
				theme_obj.add_color_named(stylepart, colloc, color_id)

		if 'Colors:Window' in config:
			colorset = config['Colors:Window']
			add_kde_color(colorset, 'win', 'BackgroundNormal', None, 'main:control_bg')
			add_kde_color(colorset, 'win', 'BackgroundAlternate', None, 'main:control_bg_alt')
			add_kde_color(colorset, 'win', 'ForegroundNormal', None, 'main:control_fg')
			add_kde_color(colorset, 'win', 'ForegroundInactive', None, 'main:control_fg_inactive')
			add_kde_color(colorset, 'win', 'ForegroundLink', None, 'main:control_fg_url')
			add_kde_color(colorset, 'win', 'ForegroundVisited', None, 'main:control_fg_url_visited')
			add_kde_color(colorset, 'win', 'ForegroundActive', None, 'main:control_fg_active')
			add_kde_color(colorset, 'win', 'ForegroundNegative', None, 'main:control_fg_negative')
			add_kde_color(colorset, 'win', 'ForegroundNeutral', None, 'main:control_fg_neutral')
			add_kde_color(colorset, 'win', 'ForegroundPositive', None, 'main:control_fg_positive')

		if 'Colors:Button' in config:
			colorset = config['Colors:Button']
			add_kde_color(colorset, 'button', 'BackgroundNormal', 'button', 'main:control_bg')
			add_kde_color(colorset, 'button', 'BackgroundAlternate', 'button', 'main:control_bg_alt')
			add_kde_color(colorset, 'button', 'ForegroundNormal', 'button', 'main:control_fg')
			add_kde_color(colorset, 'button', 'ForegroundInactive', 'button', 'main:control_fg_inactive')
			add_kde_color(colorset, 'button', 'ForegroundLink', 'button', 'main:control_fg_url')
			add_kde_color(colorset, 'button', 'ForegroundVisited', 'button', 'main:control_fg_url_visited')
			add_kde_color(colorset, 'button', 'ForegroundActive', 'button', 'main:control_fg_active')
			add_kde_color(colorset, 'button', 'ForegroundNegative', 'button', 'main:control_fg_negative')
			add_kde_color(colorset, 'button', 'ForegroundNeutral', 'button', 'main:control_fg_neutral')
			add_kde_color(colorset, 'button', 'ForegroundPositive', 'button', 'main:control_fg_positive')

		if 'Colors:Tooltip' in config:
			colorset = config['Colors:Tooltip']
			add_kde_color(colorset, 'tooltip', 'BackgroundNormal', 'tooltip', 'main:control_bg')
			add_kde_color(colorset, 'tooltip', 'BackgroundAlternate', 'tooltip', 'main:control_bg_alt')
			add_kde_color(colorset, 'tooltip', 'ForegroundNormal', 'tooltip', 'main:control_fg')
			add_kde_color(colorset, 'tooltip', 'ForegroundInactive', 'tooltip', 'main:control_fg_inactive')
			add_kde_color(colorset, 'tooltip', 'ForegroundLink', 'tooltip', 'main:control_fg_url')
			add_kde_color(colorset, 'tooltip', 'ForegroundVisited', 'tooltip', 'main:control_fg_url_visited')
			add_kde_color(colorset, 'tooltip', 'ForegroundActive', 'tooltip', 'main:control_fg_active')
			add_kde_color(colorset, 'tooltip', 'ForegroundNegative', 'tooltip', 'main:control_fg_negative')
			add_kde_color(colorset, 'tooltip', 'ForegroundNeutral', 'tooltip', 'main:control_fg_neutral')
			add_kde_color(colorset, 'tooltip', 'ForegroundPositive', 'tooltip', 'main:control_fg_positive')
			
		if 'Colors:Complementary' in config:
			colorset = config['Colors:Tooltip']
			add_kde_color(colorset, 'complementary', 'BackgroundNormal', 'complementary', 'main:control_bg')
			add_kde_color(colorset, 'complementary', 'BackgroundAlternate', 'complementary', 'main:control_bg_alt')
			add_kde_color(colorset, 'complementary', 'ForegroundNormal', 'complementary', 'main:control_fg')
			add_kde_color(colorset, 'complementary', 'ForegroundInactive', 'complementary', 'main:control_fg_inactive')
			add_kde_color(colorset, 'complementary', 'ForegroundLink', 'complementary', 'main:control_fg_url')
			add_kde_color(colorset, 'complementary', 'ForegroundVisited', 'complementary', 'main:control_fg_url_visited')
			add_kde_color(colorset, 'complementary', 'ForegroundActive', 'complementary', 'main:control_fg_active')
			add_kde_color(colorset, 'complementary', 'ForegroundNegative', 'complementary', 'main:control_fg_negative')
			add_kde_color(colorset, 'complementary', 'ForegroundNeutral', 'complementary', 'main:control_fg_neutral')
			add_kde_color(colorset, 'complementary', 'ForegroundPositive', 'complementary', 'main:control_fg_positive')
			
		if 'Colors:View' in config:
			colorset = config['Colors:Tooltip']
			add_kde_color(colorset, 'view', 'BackgroundNormal', None, 'main:edit_bg')
			add_kde_color(colorset, 'view', 'BackgroundAlternate', None, 'main:edit_bg_alt')
			add_kde_color(colorset, 'view', 'ForegroundNormal', None, 'main:edit_fg')
			add_kde_color(colorset, 'view', 'ForegroundInactive', None, 'main:edit_fg_inactive')
			add_kde_color(colorset, 'view', 'ForegroundLink', None, 'main:edit_fg_url')
			add_kde_color(colorset, 'view', 'ForegroundVisited', None, 'main:edit_fg_url_visited')
			add_kde_color(colorset, 'view', 'ForegroundActive', None, 'main:edit_fg_active')
			add_kde_color(colorset, 'view', 'ForegroundNegative', None, 'main:edit_fg_negative')
			add_kde_color(colorset, 'view', 'ForegroundNeutral', None, 'main:edit_fg_neutral')
			add_kde_color(colorset, 'view', 'ForegroundPositive', None, 'main:edit_fg_positive')

		if 'Colors:Selection' in config:
			colorset = config['Colors:Selection']
			add_kde_color(colorset, 'selection', 'BackgroundNormal', None, 'main:edit_bg_selected')
			add_kde_color(colorset, 'selection', 'BackgroundAlternate', None, 'main:edit_bg_selected_alt')
			add_kde_color(colorset, 'selection', 'ForegroundNormal', None, 'main:edit_fg_selected')
			add_kde_color(colorset, 'selection', 'ForegroundInactive', None, 'main:edit_fg_selected_inactive')
			add_kde_color(colorset, 'selection', 'ForegroundLink', None, 'main:edit_fg_selected_url')
			add_kde_color(colorset, 'selection', 'ForegroundVisited', None, 'main:edit_fg_selected_url_visited')
			add_kde_color(colorset, 'selection', 'ForegroundActive', None, 'main:edit_fg_selected_active')
			add_kde_color(colorset, 'selection', 'ForegroundNegative', None, 'main:edit_fg_selected_negative')
			add_kde_color(colorset, 'selection', 'ForegroundNeutral', None, 'main:edit_fg_selected_neutral')
			add_kde_color(colorset, 'selection', 'ForegroundPositive', None, 'main:edit_fg_selected_positive')

		if 'WM' in config:
			colorset = config['WM']
			add_kde_color(colorset, 'wm', 'activeBackground', 'titlebar', 'main:control_bg')
			add_kde_color(colorset, 'wm', 'activeBlend', 'titlebar', 'main:control_bg_second')
			add_kde_color(colorset, 'wm', 'activeForeground', 'titlebar', 'main:control_fg')
			add_kde_color(colorset, 'wm', 'inactiveBackground', 'titlebar', 'inactive:control_bg')
			add_kde_color(colorset, 'wm', 'inactiveBlend', 'titlebar', 'inactive:control_fg')
			add_kde_color(colorset, 'wm', 'inactiveForeground', 'titlebar', 'inactive:control_bg_second')

			theme_obj.add_global_color('wm_activeBackground', conv_color(colorset['activeBackground']) )
			theme_obj.add_global_color('wm_activeBlend', conv_color(colorset['activeBlend']) )
			theme_obj.add_global_color('wm_activeForeground', conv_color(colorset['activeForeground']) )
			theme_obj.add_global_color('wm_inactiveBackground', conv_color(colorset['inactiveBackground']) )
			theme_obj.add_global_color('wm_inactiveBlend', conv_color(colorset['inactiveBlend']) )
			theme_obj.add_global_color('wm_inactiveForeground', conv_color(colorset['inactiveForeground']) )

			#curstyle.add_prop('main', 'color_fx', 'gradent')
			#curstyle.add_prop('main', 'gradent_color', 'user_gradent')
			#curstyle.add_color_named('main:user_gradent', 'wm_activeBlend')

			#curstyle.add_prop('inactive', 'color_fx', 'gradent')
			#curstyle.add_prop('inactive', 'gradent_color', 'user_gradent')
			#curstyle.add_color_named('inactive:user_gradent', 'wm_inactiveBlend')
