
import xml.etree.ElementTree as ET
from objects import visual
from functions import color as colorfunc

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
			part.set('scrollbar', colorfunc.writestr(self.scrollbar) )
			part.set('background', colorfunc.writestr(self.background) )
			part.set('activetitle', colorfunc.writestr(self.activetitle) )
			part.set('inactivetitle', colorfunc.writestr(self.inactivetitle) )
			part.set('menu', colorfunc.writestr(self.menu) )
			part.set('window', colorfunc.writestr(self.window) )
			part.set('windowframe', colorfunc.writestr(self.windowframe) )
			part.set('menutext', colorfunc.writestr(self.menutext) )
			part.set('windowtext', colorfunc.writestr(self.windowtext) )
			part.set('titletext', colorfunc.writestr(self.titletext) )
			part.set('activeborder', colorfunc.writestr(self.activeborder) )
			part.set('inactiveborder', colorfunc.writestr(self.inactiveborder) )
			part.set('appworkspace', colorfunc.writestr(self.appworkspace) )
			part.set('hilight', colorfunc.writestr(self.hilight) )
			part.set('hilighttext', colorfunc.writestr(self.hilighttext) )
			part.set('buttonface', colorfunc.writestr(self.buttonface) )
			part.set('buttonshadow', colorfunc.writestr(self.buttonshadow) )
			part.set('graytext', colorfunc.writestr(self.graytext) )
			part.set('buttontext', colorfunc.writestr(self.buttontext) )
			part.set('inactivetitletext', colorfunc.writestr(self.inactivetitletext) )
			part.set('buttonhilight', colorfunc.writestr(self.buttonhilight) )
			part.set('buttondkshadow', colorfunc.writestr(self.buttondkshadow) )
			part.set('buttonlight', colorfunc.writestr(self.buttonlight) )
			part.set('infotext', colorfunc.writestr(self.infotext) )
			part.set('infowindow', colorfunc.writestr(self.infowindow) )
			part.set('buttonalternateface', colorfunc.writestr(self.buttonalternateface) )
			part.set('hottrackingcolor', colorfunc.writestr(self.hottrackingcolor) )
			part.set('gradientactivetitle', colorfunc.writestr(self.gradientactivetitle) )
			part.set('gradientinactivetitle', colorfunc.writestr(self.gradientinactivetitle) )
			part.set('menuhilight', colorfunc.writestr(self.menuhilight) )
			part.set('menubar', colorfunc.writestr(self.menubar) )

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

			theme_obj.add_color_named(None, 'main:control_bg', 'win32__buttonface')
			theme_obj.add_color_named(None, 'main:control_bg_alt', 'win32__buttonalternateface')
			theme_obj.add_color_named(None, 'main:control_fg', 'win32__windowtext')
			theme_obj.add_color_named(None, 'main:edit_bg', 'win32__window')
			theme_obj.add_color_named(None, 'main:edit_fg', 'win32__windowtext')
			theme_obj.add_color_named(None, 'inactive:control_bg', 'win32__buttonface')
			theme_obj.add_color_named(None, 'inactive:control_fg', 'win32__graytext')
			theme_obj.add_color_named(None, 'inactive:edit_bg', 'win32__buttonface')
			theme_obj.add_color_named(None, 'inactive:edit_fg', 'win32__graytext')
			theme_obj.add_color_named(None, 'hot:edit_bg', 'win32__hottrackingcolor')
			theme_obj.add_color_named(None, 'main:edit_bg_selected', 'win32__hilight')
			theme_obj.add_color_named(None, 'main:edit_fg_selected', 'win32__hilighttext')

			# ------ titlebar -----
			theme_obj.add_stylecontrol('titlebar')
			theme_obj.add_color_named('titlebar', 'main:control_bg', 'win32__activetitle')
			theme_obj.add_color_named('titlebar', 'main:control_fg', 'win32__titletext')
			theme_obj.add_color_named('titlebar', 'main:control_bg_second', 'win32__gradientactivetitle')
			theme_obj.add_color_named('titlebar', 'main:user_gradent', 'win32__gradientactivetitle')
			theme_obj.add_color_named('titlebar', 'inactive:control_bg', 'win32__inactivetitle')
			theme_obj.add_color_named('titlebar', 'inactive:control_fg', 'win32__inactivetitletext')
			theme_obj.add_color_named('titlebar', 'inactive:control_bg_second', 'win32__gradientinactivetitle')
			theme_obj.add_color_named('titlebar', 'main:user_gradent', 'win32__gradientinactivetitle')
			theme_obj.add_prop('titlebar', 'main', 'color_fx', 'gradent')
			theme_obj.add_prop('titlebar', 'main', 'gradent_color', 'user_gradent')
			theme_obj.add_prop('titlebar', 'main', 'color_fx', 'gradent')
			theme_obj.add_prop('titlebar', 'main', 'gradent_color', 'user_gradent')

			# ------ desktop -----
			theme_obj.add_stylecontrol('desktop')
			theme_obj.add_color_named('desktop', 'main:control_bg', 'win32__background')

			# ------ tooltip -----
			theme_obj.add_stylecontrol('tooltip')
			theme_obj.add_color_named('tooltip', 'main:control_bg', 'win32__infowindow')
			theme_obj.add_color_named('tooltip', 'main:control_fg', 'win32__infotext')

			# ------ menubar -----
			theme_obj.add_stylecontrol('menubar')
			theme_obj.add_color_named('menubar', 'main:control_bg', 'win32__menubar')
			theme_obj.add_color_named('menubar', 'main:control_fg', 'win32__menutext')

			# ------ menu -----
			theme_obj.add_stylecontrol('menu')
			theme_obj.add_color_named('menu', 'main:control_bg', 'win32__menu')
			theme_obj.add_color_named('menu', 'main:control_fg', 'win32__menutext')
			theme_obj.add_color_named('menu', 'focused:control_bg', 'win32__hilight')
			theme_obj.add_color_named('menu', 'focused:control_fg', 'win32__hilighttext')

			# ------ scrollbar -----
			theme_obj.add_stylecontrol('scrollbar')
			theme_obj.add_color_named('scrollbar', 'main:control_bg', 'win32__scrollbar')

			# ------ window -----
			theme_obj.add_stylecontrol('window')
			theme_obj.add_color_named('window', 'main:border', 'win32__activeborder')
			theme_obj.add_color_named('window', 'inactive:border', 'win32__inactiveborder')

	def export_colors(self, theme_obj):
		if self.used == False and 'win32' not in theme_obj.supported_types:
			theme_obj.supported_types.append('win32')

			globalstyle = theme_obj.style_global
			ctrl_main_bg = theme_obj.get_color_rgb(None, 'main:control_bg')
			ctrl_main_fg = theme_obj.get_color_rgb(None, 'main:control_fg')
			text_main_bg = theme_obj.get_color_rgb(None, 'main:edit_bg')
			text_main_fg = theme_obj.get_color_rgb(None, 'main:edit_fg')
			text_sel_bg = theme_obj.get_color_rgb(None, 'main:edit_bg_selected')
			text_sel_fg = theme_obj.get_color_rgb(None, 'main:edit_fg_selected')

			maxv = 1-(max(ctrl_main_bg.get_int())/255)

			mulctrl = 1.3+((maxv**2)/1.5)

			threed_shadow = ctrl_main_bg.copy()*(1/mulctrl)
			threed_light = ctrl_main_bg.copy()*(mulctrl/1)

			threed_mid_shadow = colorfunc.mix_color(threed_shadow, ctrl_main_bg, 0.5)
			threed_mid_light = colorfunc.mix_color(threed_light, ctrl_main_bg, 0.5)

			self.set('buttonface', ctrl_main_bg.get_int() )
			self.set('buttondkshadow', threed_shadow.get_int() )
			self.set('buttonshadow', threed_mid_shadow.get_int() )
			self.set('buttonhilight', threed_light.get_int() )
			self.set('buttonlight', threed_mid_light.get_int() )

			altface = theme_obj.get_color_rgb(None, 'main:control_bg_alt')
			self.set('buttonalternateface', altface.get_int())

			self.set('buttontext', ctrl_main_fg.get_int() )

			self.set('window', text_main_bg.get_int() )
			self.set('windowtext', text_main_fg.get_int() )

			self.set('hilight', text_sel_bg.get_int() )
			self.set('hilighttext', text_sel_fg.get_int() )

			self.set('activeborder', ctrl_main_bg.get_int() )
			self.set('inactiveborder', ctrl_main_bg.get_int() )
			self.set('windowframe', ctrl_main_bg.get_int() )

			color = theme_obj.get_color_rgb(None, 'inactive:control_fg')
			self.set('graytext', color.get_int() )

			# ------ titlebar -----
			color = theme_obj.get_color_rgb('titlebar', 'main:control_bg')
			self.set('activetitle', color.get_int() )
			self.set('gradientactivetitle', color.get_int() )
			cfx_type = theme_obj.get_prop('titlebar', 'main', 'color_fx')
			if cfx_type=='gradent':
				gradent_color = theme_obj.get_prop('titlebar', 'main', 'gradent_color')
				gcolor = theme_obj.get_color_rgb('titlebar', 'main:'+gradent_color)
				if gcolor: self.set('gradientactivetitle', gcolor.get_int() )
			else:
				gcolor = theme_obj.get_color_rgb('titlebar', 'main:control_bg_second')
				if gcolor: self.set('gradientactivetitle', gcolor.get_int() )

			color = theme_obj.get_color_rgb('titlebar', 'inactive:control_bg')
			self.set('inactivetitle', color.get_int() )
			self.set('gradientinactivetitle', color.get_int() )
			cfx_type = theme_obj.get_prop('titlebar', 'inactive', 'color_fx')
			if cfx_type=='gradent':
				gradent_color = theme_obj.get_prop('titlebar', 'inactive', 'gradent_color')
				gcolor = theme_obj.get_color_rgb('titlebar', 'inactive:'+gradent_color)
				if gcolor: self.set('gradientinactivetitle', gcolor.get_int() )
			else:
				gcolor = theme_obj.get_color_rgb('titlebar', 'inactive:control_bg_second')
				if gcolor: self.set('gradientinactivetitle', gcolor.get_int() )

			color = theme_obj.get_color_rgb('titlebar', 'main:control_fg')
			self.set('titletext', color.get_int() )

			color = theme_obj.get_color_rgb('titlebar', 'inactive:control_fg')
			self.set('inactivetitletext', color.get_int() )

			# ------ desktop -----
			color_bg = theme_obj.get_color_rgb('desktop', 'main:control_bg')
			self.set('background', color_bg.get_int() )

			# ------ tooltip -----
			color_bg = theme_obj.get_color_rgb('tooltip', 'main:control_bg')
			color_fg = theme_obj.get_color_rgb('tooltip', 'main:control_fg')
			self.set('infowindow', color_bg.get_int() )
			self.set('infotext', color_fg.get_int() )

			# ------ menubar -----
			color_bg = theme_obj.get_color_rgb('menubar', 'main:control_bg')
			self.set('menubar', color_bg.get_int() )

			# ------ menu -----
			color_bg = theme_obj.get_color_rgb('menu', 'main:control_bg')
			color_fg = theme_obj.get_color_rgb('menu', 'main:control_fg')
			self.set('menu', color_bg.get_int() )
			self.set('menutext', color_fg.get_int() )

			# ------ scrollbar -----
			scrollbar = theme_obj.get_color_rgb('scrollbar', 'main:control_bg')
			self.set('scrollbar', scrollbar.get_int() )

			# ------ window -----
			border = theme_obj.get_color_rgb('window', 'main:border')
			#self.set('activeborder', border.get_int() )
			border = theme_obj.get_color_rgb('window', 'inactive:border')
			#self.set('inactiveborder', border.get_int() )