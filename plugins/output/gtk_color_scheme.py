
import plugins
from functions import color as colorfunc

class output_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'output'
	
	def get_shortname(self):
		return 'gtk_color_scheme'
	
	def get_name(self):
		return 'Gtk Colors .INI'
	
	def get_prop(self):
		prop = {}
		prop['supported_types'] = ['gtk']
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		import configparser

		config = configparser.ConfigParser()
		maindata = {}

		gtk_colors = theme_obj.colors_gtk

		if gtk_colors.base_color: maindata['base_color'] = gtk_colors.base_color.get_hex()
		if gtk_colors.bg_color: maindata['bg_color'] = gtk_colors.bg_color.get_hex()
		if gtk_colors.fg_color: maindata['fg_color'] = gtk_colors.fg_color.get_hex()
		if gtk_colors.text_color: maindata['text_color'] = gtk_colors.text_color.get_hex()

		if gtk_colors.error_bg_color: maindata['error_bg_color'] = gtk_colors.error_bg_color.get_hex()
		if gtk_colors.error_color: maindata['error_color'] = gtk_colors.error_color.get_hex()
		if gtk_colors.error_fg_color: maindata['error_fg_color'] = gtk_colors.error_fg_color.get_hex()
		if gtk_colors.inactive_fg_color: maindata['inactive_fg_color'] = gtk_colors.inactive_fg_color.get_hex()
		if gtk_colors.inactive_text_color: maindata['inactive_text_color'] = gtk_colors.inactive_text_color.get_hex()
		if gtk_colors.info_bg_color: maindata['info_bg_color'] = gtk_colors.info_bg_color.get_hex()
		if gtk_colors.info_fg_color: maindata['info_fg_color'] = gtk_colors.info_fg_color.get_hex()
		if gtk_colors.other_bg_color: maindata['other_bg_color'] = gtk_colors.other_bg_color.get_hex()
		if gtk_colors.other_fg_color: maindata['other_fg_color'] = gtk_colors.other_fg_color.get_hex()
		if gtk_colors.question_bg_color: maindata['question_bg_color'] = gtk_colors.question_bg_color.get_hex()
		if gtk_colors.question_fg_color: maindata['question_fg_color'] = gtk_colors.question_fg_color.get_hex()
		if gtk_colors.selected_base_color: maindata['selected_base_color'] = gtk_colors.selected_base_color.get_hex()
		if gtk_colors.selected_bg_color: maindata['selected_bg_color'] = gtk_colors.selected_bg_color.get_hex()
		if gtk_colors.selected_fg_color: maindata['selected_fg_color'] = gtk_colors.selected_fg_color.get_hex()
		if gtk_colors.selected_text_color: maindata['selected_text_color'] = gtk_colors.selected_text_color.get_hex()
		if gtk_colors.tooltip_color: maindata['tooltip_color'] = gtk_colors.tooltip_color.get_hex()
		if gtk_colors.url_color: maindata['url_color'] = gtk_colors.url_color.get_hex()
		if gtk_colors.visited_url_color: maindata['visited_url_color'] = gtk_colors.visited_url_color.get_hex()
		if gtk_colors.warning_bg_color: maindata['warning_bg_color'] = gtk_colors.warning_bg_color.get_hex()
		if gtk_colors.warning_fg_color: maindata['warning_fg_color'] = gtk_colors.warning_fg_color.get_hex()

		config['main'] = maindata

		with open(themeverter_intent.output_file, 'w') as configfile:
		    config.write(configfile)