
import plugins

class output_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'output'
		
	def get_shortname(self):
		return 'kde_color'
	
	def get_name(self):
		return '[Unix] KDE/Plasma Color Scheme'
	
	def get_prop(self):
		prop = {}
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		config = {}
		def do_color(control, colloc, name, idict):
			outcol = theme_obj.get_color_rgb(control, colloc)
			if outcol: idict[name] = outcol.get_hex()
		general = {}
		general['ColorScheme'] = "Converted Theme"
		general['Name'] = "ThemeVert"
		general['shadeSortColumn'] = "true"
		config['General'] = general

		colors = {}
		do_color(None, 'main:control_bg', 'BackgroundNormal', colors)
		do_color(None, 'main:control_bg_alt', 'BackgroundAlternate', colors)
		do_color(None, 'main:control_fg', 'ForegroundNormal', colors)
		do_color(None, 'main:control_fg_inactive', 'ForegroundInactive', colors)
		do_color(None, 'main:control_fg_active', 'ForegroundActive', colors)
		do_color(None, 'main:control_fg_url', 'ForegroundLink', colors)
		do_color(None, 'main:control_fg_url_visited', 'ForegroundVisited', colors)
		do_color(None, 'main:control_fg_negative', 'ForegroundNegative', colors)
		do_color(None, 'main:control_fg_neutral', 'ForegroundNeutral', colors)
		do_color(None, 'main:control_fg_positive', 'ForegroundPositive', colors)
		config['Colors:Window'] = colors

		colors = {}
		do_color('button', 'main:control_bg', 'BackgroundNormal', colors)
		do_color('button', 'main:control_bg_alt', 'BackgroundAlternate', colors)
		do_color('button', 'main:control_fg', 'ForegroundNormal', colors)
		do_color('button', 'main:control_fg_inactive', 'ForegroundInactive', colors)
		do_color('button', 'main:control_fg_active', 'ForegroundActive', colors)
		do_color('button', 'main:control_fg_url', 'ForegroundLink', colors)
		do_color('button', 'main:control_fg_url_visited', 'ForegroundVisited', colors)
		do_color('button', 'main:control_fg_negative', 'ForegroundNegative', colors)
		do_color('button', 'main:control_fg_neutral', 'ForegroundNeutral', colors)
		do_color('button', 'main:control_fg_positive', 'ForegroundPositive', colors)
		config['Colors:Button'] = colors

		colors = {}
		do_color('tooltip', 'main:control_bg', 'BackgroundNormal', colors)
		do_color('tooltip', 'main:control_bg_alt', 'BackgroundAlternate', colors)
		do_color('tooltip', 'main:control_fg', 'ForegroundNormal', colors)
		do_color('tooltip', 'main:control_fg_inactive', 'ForegroundInactive', colors)
		do_color('tooltip', 'main:control_fg_active', 'ForegroundActive', colors)
		do_color('tooltip', 'main:control_fg_url', 'ForegroundLink', colors)
		do_color('tooltip', 'main:control_fg_url_visited', 'ForegroundVisited', colors)
		do_color('tooltip', 'main:control_fg_negative', 'ForegroundNegative', colors)
		do_color('tooltip', 'main:control_fg_neutral', 'ForegroundNeutral', colors)
		do_color('tooltip', 'main:control_fg_positive', 'ForegroundPositive', colors)
		config['Colors:Complementary'] = colors

		colors = {}
		do_color('complementary', 'main:control_bg', 'BackgroundNormal', colors)
		do_color('complementary', 'main:control_bg_alt', 'BackgroundAlternate', colors)
		do_color('complementary', 'main:control_fg', 'ForegroundNormal', colors)
		do_color('complementary', 'main:control_fg_inactive', 'ForegroundInactive', colors)
		do_color('complementary', 'main:control_fg_active', 'ForegroundActive', colors)
		do_color('complementary', 'main:control_fg_url', 'ForegroundLink', colors)
		do_color('complementary', 'main:control_fg_url_visited', 'ForegroundVisited', colors)
		do_color('complementary', 'main:control_fg_negative', 'ForegroundNegative', colors)
		do_color('complementary', 'main:control_fg_neutral', 'ForegroundNeutral', colors)
		do_color('complementary', 'main:control_fg_positive', 'ForegroundPositive', colors)
		config['Colors:Tooltip'] = colors

		colors = {}
		do_color(None, 'main:edit_bg', 'BackgroundNormal', colors)
		do_color(None, 'main:edit_bg_alt', 'BackgroundAlternate', colors)
		do_color(None, 'main:edit_fg', 'ForegroundNormal', colors)
		do_color(None, 'main:edit_fg_inactive', 'ForegroundInactive', colors)
		do_color(None, 'main:edit_fg_active', 'ForegroundActive', colors)
		do_color(None, 'main:edit_fg_url', 'ForegroundLink', colors)
		do_color(None, 'main:edit_fg_url_visited', 'ForegroundVisited', colors)
		do_color(None, 'main:edit_fg_negative', 'ForegroundNegative', colors)
		do_color(None, 'main:edit_fg_neutral', 'ForegroundNeutral', colors)
		do_color(None, 'main:edit_fg_positive', 'ForegroundPositive', colors)
		config['Colors:View'] = colors

		colors = {}
		do_color(None, 'main:edit_bg_selected', 'BackgroundNormal', colors)
		do_color(None, 'main:edit_bg_selected_alt', 'BackgroundAlternate', colors)
		do_color(None, 'main:edit_fg_selected', 'ForegroundNormal', colors)
		do_color(None, 'main:edit_fg_selected_inactive', 'ForegroundInactive', colors)
		do_color(None, 'main:edit_fg_selected_url', 'ForegroundActive', colors)
		do_color(None, 'main:edit_fg_selected_url_visited', 'ForegroundLink', colors)
		do_color(None, 'main:edit_fg_selected_active', 'ForegroundVisited', colors)
		do_color(None, 'main:edit_fg_selected_negative', 'ForegroundNegative', colors)
		do_color(None, 'main:edit_fg_selected_neutral', 'ForegroundNeutral', colors)
		do_color(None, 'main:edit_fg_selected_positive', 'ForegroundPositive', colors)
		config['Colors:Selection'] = colors

		colors = {}
		do_color('titlebar', 'main:control_bg', 'activeBackground', colors)
		do_color('titlebar', 'main:control_bg_second', 'activeBlend', colors)
		do_color('titlebar', 'main:control_fg', 'activeForeground', colors)
		do_color('titlebar', 'inactive:control_bg', 'inactiveBackground', colors)
		do_color('titlebar', 'inactive:control_bg_second', 'inactiveBlend', colors)
		do_color('titlebar', 'inactive:control_fg', 'inactiveForeground', colors)
		config['WM'] = colors

		f = open(themeverter_intent.output_file, 'w')
		for c in config:
			f.write('[%s]\n' % c)
			for k, v in config[c].items():
				f.write('%s=%s\n' % (k, v))
			f.write('\n')