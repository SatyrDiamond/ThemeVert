
import plugins

def hex_to_int(val):
	h = val.lstrip('#')
	return list(int(h[i:i+2], 16) for i in (0, 2, 4))

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'gtk_color_scheme'
	
	def get_name(self):
		return 'gtk color scheme INI'
	
	def parse(self, theme_obj, themeverter_intent):
		import configparser

		config = configparser.ConfigParser()
		config.read(themeverter_intent.input_file)

		maincolors = config['main']

		theme_obj.add_color('fg_color', hex_to_int(maincolors['fg_color']) )
		theme_obj.add_color('bg_color', hex_to_int(maincolors['bg_color']) )
		theme_obj.add_color('base_color', hex_to_int(maincolors['base_color']) )
		theme_obj.add_color('text_color', hex_to_int(maincolors['text_color']) )
		theme_obj.add_color('selected_bg_color', hex_to_int(maincolors['selected_bg_color']) )
		theme_obj.add_color('selected_fg_color', hex_to_int(maincolors['selected_fg_color']) )

		globalstyle = theme_obj.style_global
		globalstyle.add_color_named('control', None, 'bg', 'bg_color')
		globalstyle.add_color_named('control', None, 'fg', 'fg_color')
		globalstyle.add_color_named('text', None, 'bg', 'base_color')
		globalstyle.add_color_named('text', None, 'fg', 'text_color')
		globalstyle.add_color_named('text', 'active', 'bg', 'selected_bg_color')
		globalstyle.add_color_named('text', 'active', 'fg', 'selected_fg_color')
