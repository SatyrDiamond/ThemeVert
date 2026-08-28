
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
		theme_obj.supported_types.append('basic')

		config = configparser.ConfigParser()
		config.read(themeverter_intent.input_file)

		maincolors = config['main']

		globalstyle = theme_obj.style_global

		def add_color(curstype, name, collocs):
			if name in maincolors:
				color = hex_to_int(maincolors[name])
				theme_obj.add_global_color(name, color)
				for cl in collocs:
					curstype.add_color_named(cl, name)

		add_color(globalstyle, 'bg_color', ['control:main:bg'] )
		add_color(globalstyle, 'fg_color', ['control:main:fg'] )
		add_color(globalstyle, 'base_color', ['text:main:bg'] )
		add_color(globalstyle, 'text_color', ['text:main:fg'] )
		add_color(globalstyle, 'selected_bg_color', ['control:selected:bg'] )
		add_color(globalstyle, 'selected_fg_color', ['control:selected:fg'] )
		add_color(globalstyle, 'inactive_fg_color', ['control:disabled:fg'] )
		add_color(globalstyle, 'selected_base_color', ['text:selected:bg'] )
		add_color(globalstyle, 'selected_text_color', ['text:selected:fg'] )
		add_color(globalstyle, 'inactive_text_color', ['text:disabled:fg'] )

		curstyle, curctrl = theme_obj.add_stylecontrol('tooltip')
		add_color(curstyle, 'tooltip_color', ['control:main:bg'] )

		curstyle, curctrl = theme_obj.add_stylecontrol('infobar_error')
		add_color(curstyle, 'error_bg_color', ['control:main:bg'] )
		add_color(curstyle, 'error_fg_color', ['control:main:fg', 'text:main:fg'] )

		curstyle, curctrl = theme_obj.add_stylecontrol('infobar_warning')
		add_color(curstyle, 'warning_bg_color', ['control:main:bg'] )
		add_color(curstyle, 'warning_fg_color', ['control:main:fg', 'text:main:fg'] )

		curstyle, curctrl = theme_obj.add_stylecontrol('infobar_info')
		add_color(curstyle, 'info_bg_color', ['control:main:bg'] )
		add_color(curstyle, 'info_fg_color', ['control:main:fg', 'text:main:fg'] )

		curstyle, curctrl = theme_obj.add_stylecontrol('infobar_question')
		add_color(curstyle, 'question_bg_color', ['control:main:bg'] )
		add_color(curstyle, 'question_fg_color', ['control:main:fg', 'text:main:fg'] )

		curstyle, curctrl = theme_obj.add_stylecontrol('infobar_other')
		add_color(curstyle, 'question_bg_color', ['control:main:bg'] )
		add_color(curstyle, 'question_fg_color', ['control:main:fg', 'text:main:fg'] )

		curstyle, curctrl = theme_obj.add_stylecontrol('url')
		add_color(curstyle, 'url_color', ['text:main:fg'] )
		add_color(curstyle, 'visited_url_color', ['text:visited:fg'] )

		theme_obj.complete_incomplete()
		theme_obj.to_xml('out.xml')