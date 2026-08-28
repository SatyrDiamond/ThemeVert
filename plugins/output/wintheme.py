
import plugins

def writecol(c): return ' '.join([str(x) for x in c.get_int()])

class output_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'output'
	
	def get_shortname(self):
		return 'win32_theme'
	
	def get_name(self):
		return 'Windows .theme'
	
	def parse(self, theme_obj, themeverter_intent):
		import configparser
		win32_colors = theme_obj.win32_colors

		config = configparser.ConfigParser()
		config.read(themeverter_intent.output_file)
		win32colf = {}
		win32colf['ActiveBorder'] = writecol(win32_colors.activeborder)
		win32colf['ActiveTitle'] = writecol(win32_colors.activetitle)
		win32colf['AppWorkSpace'] = writecol(win32_colors.appworkspace)
		win32colf['Background'] = writecol(win32_colors.background)
		win32colf['ButtonAlternateFace'] = writecol(win32_colors.buttonalternateface)
		win32colf['ButtonDkShadow'] = writecol(win32_colors.buttondkshadow)
		win32colf['ButtonFace'] = writecol(win32_colors.buttonface)
		win32colf['ButtonHilight'] = writecol(win32_colors.buttonhilight)
		win32colf['ButtonLight'] = writecol(win32_colors.buttonlight)
		win32colf['ButtonShadow'] = writecol(win32_colors.buttonshadow)
		win32colf['ButtonText'] = writecol(win32_colors.buttontext)
		win32colf['GradientActiveTitle'] = writecol(win32_colors.gradientactivetitle)
		win32colf['GradientInactiveTitle'] = writecol(win32_colors.gradientinactivetitle)
		win32colf['GrayText'] = writecol(win32_colors.graytext)
		win32colf['Hilight'] = writecol(win32_colors.hilight)
		win32colf['HilightText'] = writecol(win32_colors.hilighttext)
		win32colf['HotTrackingColor'] = writecol(win32_colors.hottrackingcolor)
		win32colf['InactiveBorder'] = writecol(win32_colors.inactiveborder)
		win32colf['InactiveTitle'] = writecol(win32_colors.inactivetitle)
		win32colf['InactiveTitleText'] = writecol(win32_colors.inactivetitletext)
		win32colf['InfoText'] = writecol(win32_colors.infotext)
		win32colf['InfoWindow'] = writecol(win32_colors.infowindow)
		win32colf['Menu'] = writecol(win32_colors.menu)
		win32colf['MenuBar'] = writecol(win32_colors.menubar)
		win32colf['MenuHilight'] = writecol(win32_colors.menuhilight)
		win32colf['MenuText'] = writecol(win32_colors.menutext)
		win32colf['Scrollbar'] = writecol(win32_colors.scrollbar)
		win32colf['TitleText'] = writecol(win32_colors.titletext)
		win32colf['Window'] = writecol(win32_colors.window)
		win32colf['WindowFrame'] = writecol(win32_colors.windowframe)
		win32colf['WindowText'] = writecol(win32_colors.windowtext)
		config['Control Panel\\Colors'] = win32colf

		with open(themeverter_intent.output_file, 'w') as configfile:
		    config.write(configfile)
