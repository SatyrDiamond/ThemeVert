
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
	
	def get_prop(self):
		prop = {}
		prop['supported_types'] = ['gtk']
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		import configparser
		theme_obj.supported_types.append('gtk')

		config = configparser.ConfigParser()
		config.read(themeverter_intent.input_file)

		maincolors = config['main']

		gtk_colors = theme_obj.colors_gtk

		for k, v in maincolors.items(): gtk_colors.set(k, hex_to_int(v))