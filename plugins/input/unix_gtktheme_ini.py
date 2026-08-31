
import plugins

from functions import color

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return 'gtk_color_scheme'
	
	def get_name(self):
		return '[Unix] GTK Colors .INI'
	
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

		for k, v in maincolors.items(): gtk_colors.set(k, color.hex_to_int(v))