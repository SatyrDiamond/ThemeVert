
import plugins
from functions import color as colorfunc

class output_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'output'
	
	def get_shortname(self):
		return 'win32_theme'
	
	def get_name(self):
		return '[Win32] Windows .theme'
	
	def get_prop(self):
		prop = {}
		prop['supported_types'] = ['win32']
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		from objects.file_theme import windows_theme

		win32_colors = theme_obj.colors_win32

		wintheme = windows_theme.wintheme()
		win32colf = wintheme.colors
		win32colf['ActiveBorder'] = colorfunc.writestr(win32_colors.activeborder)
		win32colf['ActiveTitle'] = colorfunc.writestr(win32_colors.activetitle)
		win32colf['AppWorkSpace'] = colorfunc.writestr(win32_colors.appworkspace)
		win32colf['Background'] = colorfunc.writestr(win32_colors.background)
		win32colf['ButtonAlternateFace'] = colorfunc.writestr(win32_colors.buttonalternateface)
		win32colf['ButtonDkShadow'] = colorfunc.writestr(win32_colors.buttondkshadow)
		win32colf['ButtonFace'] = colorfunc.writestr(win32_colors.buttonface)
		win32colf['ButtonHilight'] = colorfunc.writestr(win32_colors.buttonhilight)
		win32colf['ButtonLight'] = colorfunc.writestr(win32_colors.buttonlight)
		win32colf['ButtonShadow'] = colorfunc.writestr(win32_colors.buttonshadow)
		win32colf['ButtonText'] = colorfunc.writestr(win32_colors.buttontext)
		win32colf['GradientActiveTitle'] = colorfunc.writestr(win32_colors.gradientactivetitle)
		win32colf['GradientInactiveTitle'] = colorfunc.writestr(win32_colors.gradientinactivetitle)
		win32colf['GrayText'] = colorfunc.writestr(win32_colors.graytext)
		win32colf['Hilight'] = colorfunc.writestr(win32_colors.hilight)
		win32colf['HilightText'] = colorfunc.writestr(win32_colors.hilighttext)
		win32colf['HotTrackingColor'] = colorfunc.writestr(win32_colors.hottrackingcolor)
		win32colf['InactiveBorder'] = colorfunc.writestr(win32_colors.inactiveborder)
		win32colf['InactiveTitle'] = colorfunc.writestr(win32_colors.inactivetitle)
		win32colf['InactiveTitleText'] = colorfunc.writestr(win32_colors.inactivetitletext)
		win32colf['InfoText'] = colorfunc.writestr(win32_colors.infotext)
		win32colf['InfoWindow'] = colorfunc.writestr(win32_colors.infowindow)
		win32colf['Menu'] = colorfunc.writestr(win32_colors.menu)
		win32colf['MenuBar'] = colorfunc.writestr(win32_colors.menubar)
		win32colf['MenuHilight'] = colorfunc.writestr(win32_colors.menuhilight)
		win32colf['MenuText'] = colorfunc.writestr(win32_colors.menutext)
		win32colf['Scrollbar'] = colorfunc.writestr(win32_colors.scrollbar)
		win32colf['TitleText'] = colorfunc.writestr(win32_colors.titletext)
		win32colf['Window'] = colorfunc.writestr(win32_colors.window)
		win32colf['WindowFrame'] = colorfunc.writestr(win32_colors.windowframe)
		win32colf['WindowText'] = colorfunc.writestr(win32_colors.windowtext)

		wintheme.write(themeverter_intent.output_file)
