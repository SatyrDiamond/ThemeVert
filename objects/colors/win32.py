
import xml.etree.ElementTree as ET
from objects import visual

def writecol(c): return ' '.join([str(x) for x in c.get_int()])

class colors_win32():
	__slots__ = ['used', 'scrollbar', 'background', 'activetitle', 'inactivetitle', 'menu', 'window', 'windowframe', 'menutext', 'windowtext', 'titletext', 'activeborder', 'inactiveborder', 'appworkspace', 'hilight', 'hilighttext', 'buttonface', 'buttonshadow', 'graytext', 'buttontext', 'inactivetitletext', 'buttonhilight', 'buttondkshadow', 'buttonlight', 'infotext', 'infowindow', 'buttonalternateface', 'hottrackingcolor', 'gradientactivetitle', 'gradientinactivetitle', 'menuhilight', 'menubar']

	def __init__(self):
		self.used = False

		self.scrollbar = visual.visual_color()
		self.background = visual.visual_color()
		self.activetitle = visual.visual_color()
		self.inactivetitle = visual.visual_color()
		self.menu = visual.visual_color()
		self.window = visual.visual_color()
		self.windowframe = visual.visual_color()
		self.menutext = visual.visual_color()
		self.windowtext = visual.visual_color()
		self.titletext = visual.visual_color()
		self.activeborder = visual.visual_color()
		self.inactiveborder = visual.visual_color()
		self.appworkspace = visual.visual_color()
		self.hilight = visual.visual_color()
		self.hilighttext = visual.visual_color()
		self.buttonface = visual.visual_color()
		self.buttonshadow = visual.visual_color()
		self.graytext = visual.visual_color()
		self.buttontext = visual.visual_color()
		self.inactivetitletext = visual.visual_color()
		self.buttonhilight = visual.visual_color()
		self.buttondkshadow = visual.visual_color()
		self.buttonlight = visual.visual_color()
		self.infotext = visual.visual_color()
		self.infowindow = visual.visual_color()
		self.buttonalternateface = visual.visual_color()
		self.hottrackingcolor = visual.visual_color()
		self.gradientactivetitle = visual.visual_color()
		self.gradientinactivetitle = visual.visual_color()
		self.menuhilight = visual.visual_color()
		self.menubar = visual.visual_color()

		self.scrollbar.set_int([200,200,200])
		self.background.set_int([59,110,165])
		self.activetitle.set_int([153,180,209])
		self.inactivetitle.set_int([191,205,219])
		self.menu.set_int([240,240,240])
		self.window.set_int([255,255,255])
		self.windowframe.set_int([100,100,100])
		self.menutext.set_int([0,0,0])
		self.windowtext.set_int([0,0,0])
		self.titletext.set_int([0,0,0])
		self.activeborder.set_int([180,180,180])
		self.inactiveborder.set_int([244,247,252])
		self.appworkspace.set_int([171,171,171])
		self.hilight.set_int([0,120,215])
		self.hilighttext.set_int([255,255,255])
		self.buttonface.set_int([240,240,240])
		self.buttonshadow.set_int([160,160,160])
		self.graytext.set_int([109,109,109])
		self.buttontext.set_int([0,0,0])
		self.inactivetitletext.set_int([0,0,0])
		self.buttonhilight.set_int([255,255,255])
		self.buttondkshadow.set_int([105,105,105])
		self.buttonlight.set_int([227,227,227])
		self.infotext.set_int([0,0,0])
		self.infowindow.set_int([255,255,225])
		self.buttonalternateface.set_int([0,0,0])
		self.hottrackingcolor.set_int([0,102,204])
		self.gradientactivetitle.set_int([185,209,234])
		self.gradientinactivetitle.set_int([215,228,242])
		self.menuhilight.set_int([0,120,215])
		self.menubar.set_int([240,240,240])

	def set(self, c, v):
		if v:
			self.used = True
			match c.lower():
				case 'scrollbar': self.scrollbar.set_int(v)
				case 'background': self.background.set_int(v)
				case 'activetitle': self.activetitle.set_int(v)
				case 'inactivetitle': self.inactivetitle.set_int(v)
				case 'menu': self.menu.set_int(v)
				case 'window': self.window.set_int(v)
				case 'windowframe': self.windowframe.set_int(v)
				case 'menutext': self.menutext.set_int(v)
				case 'windowtext': self.windowtext.set_int(v)
				case 'titletext': self.titletext.set_int(v)
				case 'activeborder': self.activeborder.set_int(v)
				case 'inactiveborder': self.inactiveborder.set_int(v)
				case 'appworkspace': self.appworkspace.set_int(v)
				case 'hilight': self.hilight.set_int(v)
				case 'hilighttext': self.hilighttext.set_int(v)
				case 'buttonface': self.buttonface.set_int(v)
				case 'buttonshadow': self.buttonshadow.set_int(v)
				case 'graytext': self.graytext.set_int(v)
				case 'buttontext': self.buttontext.set_int(v)
				case 'inactivetitletext': self.inactivetitletext.set_int(v)
				case 'buttonhilight': self.buttonhilight.set_int(v)
				case 'buttondkshadow': self.buttondkshadow.set_int(v)
				case 'buttonlight': self.buttonlight.set_int(v)
				case 'infotext': self.infotext.set_int(v)
				case 'infowindow': self.infowindow.set_int(v)
				case 'buttonalternateface': self.buttonalternateface.set_int(v)
				case 'hottrackingcolor': self.hottrackingcolor.set_int(v)
				case 'gradientactivetitle': self.gradientactivetitle.set_int(v)
				case 'gradientinactivetitle': self.gradientinactivetitle.set_int(v)
				case 'menuhilight': self.menuhilight.set_int(v)
				case 'menubar': self.menubar.set_int(v)
				case _: print('unknown color type', c)

	def to_xml(self, part, name):
		if self.used:
			part = ET.SubElement(part, name)
			part.set('scrollbar', writecol(self.scrollbar) )
			part.set('background', writecol(self.background) )
			part.set('activetitle', writecol(self.activetitle) )
			part.set('inactivetitle', writecol(self.inactivetitle) )
			part.set('menu', writecol(self.menu) )
			part.set('window', writecol(self.window) )
			part.set('windowframe', writecol(self.windowframe) )
			part.set('menutext', writecol(self.menutext) )
			part.set('windowtext', writecol(self.windowtext) )
			part.set('titletext', writecol(self.titletext) )
			part.set('activeborder', writecol(self.activeborder) )
			part.set('inactiveborder', writecol(self.inactiveborder) )
			part.set('appworkspace', writecol(self.appworkspace) )
			part.set('hilight', writecol(self.hilight) )
			part.set('hilighttext', writecol(self.hilighttext) )
			part.set('buttonface', writecol(self.buttonface) )
			part.set('buttonshadow', writecol(self.buttonshadow) )
			part.set('graytext', writecol(self.graytext) )
			part.set('buttontext', writecol(self.buttontext) )
			part.set('inactivetitletext', writecol(self.inactivetitletext) )
			part.set('buttonhilight', writecol(self.buttonhilight) )
			part.set('buttondkshadow', writecol(self.buttondkshadow) )
			part.set('buttonlight', writecol(self.buttonlight) )
			part.set('infotext', writecol(self.infotext) )
			part.set('infowindow', writecol(self.infowindow) )
			part.set('buttonalternateface', writecol(self.buttonalternateface) )
			part.set('hottrackingcolor', writecol(self.hottrackingcolor) )
			part.set('gradientactivetitle', writecol(self.gradientactivetitle) )
			part.set('gradientinactivetitle', writecol(self.gradientinactivetitle) )
			part.set('menuhilight', writecol(self.menuhilight) )
			part.set('menubar', writecol(self.menubar) )

	def import_colors(self, theme_obj):
		if self.used == True and 'basic' not in theme_obj.supported_types:
			theme_obj.supported_types.append('basic')
			theme_obj.add_global_color('win32__activeborder', self.activeborder.get_int() )
			theme_obj.add_global_color('win32__activetitle', self.activetitle.get_int() )
			theme_obj.add_global_color('win32__appworkspace', self.appworkspace.get_int() )
			theme_obj.add_global_color('win32__background', self.background.get_int() )
			theme_obj.add_global_color('win32__buttonalternateface', self.buttonalternateface.get_int() )
			theme_obj.add_global_color('win32__buttondkshadow', self.buttondkshadow.get_int() )
			theme_obj.add_global_color('win32__buttonface', self.buttonface.get_int() )
			theme_obj.add_global_color('win32__buttonhilight', self.buttonhilight.get_int() )
			theme_obj.add_global_color('win32__buttonlight', self.buttonlight.get_int() )
			theme_obj.add_global_color('win32__buttonshadow', self.buttonshadow.get_int() )
			theme_obj.add_global_color('win32__buttontext', self.buttontext.get_int() )
			theme_obj.add_global_color('win32__gradientactivetitle', self.gradientactivetitle.get_int() )
			theme_obj.add_global_color('win32__gradientinactivetitle', self.gradientinactivetitle.get_int() )
			theme_obj.add_global_color('win32__graytext', self.graytext.get_int() )
			theme_obj.add_global_color('win32__hilight', self.hilight.get_int() )
			theme_obj.add_global_color('win32__hilighttext', self.hilighttext.get_int() )
			theme_obj.add_global_color('win32__hottrackingcolor', self.hottrackingcolor.get_int() )
			theme_obj.add_global_color('win32__inactiveborder', self.inactiveborder.get_int() )
			theme_obj.add_global_color('win32__inactivetitle', self.inactivetitle.get_int() )
			theme_obj.add_global_color('win32__inactivetitletext', self.inactivetitletext.get_int() )
			theme_obj.add_global_color('win32__infotext', self.infotext.get_int() )
			theme_obj.add_global_color('win32__infowindow', self.infowindow.get_int() )
			theme_obj.add_global_color('win32__menu', self.menu.get_int() )
			theme_obj.add_global_color('win32__menubar', self.menubar.get_int() )
			theme_obj.add_global_color('win32__menuhilight', self.menuhilight.get_int() )
			theme_obj.add_global_color('win32__menutext', self.menutext.get_int() )
			theme_obj.add_global_color('win32__scrollbar', self.scrollbar.get_int() )
			theme_obj.add_global_color('win32__titletext', self.titletext.get_int() )
			theme_obj.add_global_color('win32__window', self.window.get_int() )
			theme_obj.add_global_color('win32__windowframe', self.windowframe.get_int() )
			theme_obj.add_global_color('win32__windowtext', self.windowtext.get_int() )

			globalstyle = theme_obj.style_global
			globalstyle.add_color_named('main:control_bg', 'win32__buttonface')
			globalstyle.add_color_named('main:control_fg', 'win32__windowtext')
			globalstyle.add_color_named('main:edit_bg', 'win32__window')
			globalstyle.add_color_named('main:edit_fg', 'win32__windowtext')
			globalstyle.add_color_named('disabled:control_bg', 'win32__buttonface')
			globalstyle.add_color_named('disabled:control_fg', 'win32__graytext')
			globalstyle.add_color_named('disabled:edit_bg', 'win32__buttonface')
			globalstyle.add_color_named('disabled:edit_fg', 'win32__graytext')
			globalstyle.add_color_named('hot:edit_bg', 'win32__hottrackingcolor')
			globalstyle.add_color_named('selected:edit_bg', 'win32__hilight')
			globalstyle.add_color_named('selected:edit_fg', 'win32__hilighttext')

			# ------ desktop -----
			curstyle, curctrl = theme_obj.add_stylecontrol('desktop')
			curstyle.add_color_named('main:control_bg', 'win32__Background')

			# ------ tooltip -----
			curstyle, curctrl = theme_obj.add_stylecontrol('tooltip')
			curstyle.add_color_named('main:control_bg', 'win32__infowindow')
			curstyle.add_color_named('main:control_fg', 'win32__infotext')

			# ------ menubar -----
			curstyle, curctrl = theme_obj.add_stylecontrol('menubar')
			curstyle.add_color_named('main:control_bg', 'win32__menubar')
			curstyle.add_color_named('main:control_fg', 'win32__menutext')

			# ------ menu -----
			curstyle, curctrl = theme_obj.add_stylecontrol('menu')
			curstyle.add_color_named('main:control_bg', 'win32__menu')
			curstyle.add_color_named('main:control_fg', 'win32__menutext')

			# ------ scrollbar -----
			#curstyle, curctrl = theme_obj.add_stylecontrol('scrollbar')
			#curstyle.add_color_named('scrollbar:main:bg', 'win32__scrollbar')
			#curstyle.add_color_named('scrollbar:main:fg', 'win32__buttonface')

	def export_colors(self, theme_obj):
		if self.used == False and 'win32' not in theme_obj.supported_types:
			theme_obj.supported_types.append('win32')

			globalstyle = theme_obj.style_global
			ctrl_main_bg = theme_obj.get_color(None, 'main:control_bg', True)
			ctrl_main_fg = theme_obj.get_color(None, 'main:control_fg', True)
			text_main_bg = theme_obj.get_color(None, 'main:edit_bg', True)
			text_main_fg = theme_obj.get_color(None, 'main:edit_fg', True)
			text_sel_bg = theme_obj.get_color(None, 'selected:edit_bg', True)
			text_sel_fg = theme_obj.get_color(None, 'selected:edit_fg', True)

			threed_dark = ctrl_main_bg.copy()*0.5
			threed_light = ctrl_main_bg.copy()*1.5

			self.set('buttonface', ctrl_main_bg.get_int() )
			self.set('buttondkshadow', threed_dark.get_int() )
			self.set('buttonshadow', threed_dark.get_int() )
			self.set('buttonhilight', threed_light.get_int() )
			self.set('buttonlight', threed_light.get_int() )

			self.set('buttontext', ctrl_main_fg.get_int() )
			self.set('menutext', ctrl_main_fg.get_int() )

			self.set('window', text_main_bg.get_int() )
			self.set('windowtext', text_main_fg.get_int() )

			self.set('hilight', text_sel_fg.get_int() )
			self.set('hilighttext', text_sel_bg.get_int() )

			self.set('activeborder', ctrl_main_bg.get_int() )
			self.set('activetitle', ctrl_main_bg.get_int() )
			self.set('gradientactivetitle', ctrl_main_bg.get_int() )
			self.set('gradientinactivetitle', ctrl_main_bg.get_int() )
			self.set('inactiveborder', ctrl_main_bg.get_int() )
			self.set('inactivetitle', ctrl_main_bg.get_int() )
			self.set('windowframe', ctrl_main_bg.get_int() )

			self.set('inactivetitletext', ctrl_main_fg.get_int() )
			self.set('titletext', ctrl_main_fg.get_int() )

			# ------ desktop -----
			color_bg = theme_obj.get_color('desktop', 'main:control_bg', True)
			self.set('background', color_bg.get_int() )

			# ------ tooltip -----
			color_bg = theme_obj.get_color('tooltip', 'main:control_bg', True)
			color_fg = theme_obj.get_color('tooltip', 'main:edit_fg', True)
			self.set('infowindow', color_bg.get_int() )
			self.set('infotext', color_fg.get_int() )

			# ------ menubar -----
			color_bg = theme_obj.get_color('menubar', 'main:control_bg', True)
			self.set('menubar', color_bg.get_int() )

			# ------ menu -----
			color_bg = theme_obj.get_color('menu', 'main:control_bg', True)
			color_fg = theme_obj.get_color('menu', 'main:edit_fg', True)
			self.set('menu', color_bg.get_int() )
			self.set('menutext', color_fg.get_int() )

			# ------ scrollbar -----
			#scrollbar = theme_obj.get_color('scrollbar', 'main:control_bg', True)
			#self.set('scrollbar', scrollbar.get_int() )
