
import xml.etree.ElementTree as ET
from objects import win32_colors
from objects import visual

# =============================================== DATA ===============================================

class data_color():
	def __init__(self):
		self.used = False
		self.type = ''
		self.color = visual.visual_color()
		self.index_name = None

	def __bool__(self):
		return self.used

	def set_manual(self, rgb):
		self.used = True
		self.type = 'manual'
		self.color.set_int(rgb)

	def set_named(self, name):
		self.used = True
		self.type = 'name'
		self.index_name = name

	def to_xml(self, part, name):
		if self.used:
			part = ET.SubElement(part, name)
			if self.type: part.set('source', self.type)
			if self.color: part.set('color', ','.join([str(x) for x in self.color.get_int()]))
			if self.index_name: part.set('name', self.index_name)

class data_text():
	def __init__(self):
		self.used = False
		self.face = None
		self.size = None
		self.bold = None
		self.italic = None
		#self.color = data_color()
	def set_face(self, part, face):
		self.used = True
		self.face = face
	def to_xml(self, part, name):
		if self.used:
			part = ET.SubElement(part, face)
			if self.face: part.set('face', self.face)
			if self.size: part.set('size', self.size)
			if self.bold: part.set('bold', self.bold)
			if self.italic: part.set('italic', self.italic)
			#if self.color.used: self.color.to_xml(part, 'color')

# =============================================== STYLE ===============================================

class basstyle_stateprop():
	def __init__(self):
		self.prop = {}
		self.bg = data_color()
		self.fg = data_color()
		self.font = data_text()
	def __bool__(self): return bool(self.bg) or bool(self.fg)
	def to_xml(self, part, name):
		cpart = ET.SubElement(part, name)
		self.font.to_xml(part, 'font')
		self.bg.to_xml(cpart, 'bg')
		self.fg.to_xml(cpart, 'fg')
		if self.prop:
			cpart = ET.SubElement(cpart, 'prop')
			for k, v in self.prop.items(): cpart.set(k, str(v))

class basstyle_state():
	def __init__(self):
		self.styleprop = {}

	def add_color(self, stylpropname, name, rgb):
		self._internal_add_color(stylpropname, name, rgb, False)

	def add_color_named(self, stylpropname, name, val):
		self._internal_add_color(stylpropname, name, val, True)

	def _internal_add_color(self, stylpropname, name, val, isname):
		if stylpropname not in self.styleprop: self.styleprop[stylpropname] = basstyle_stateprop()
		styleprop = self.styleprop[stylpropname]
		if name=='bg': colorobj = styleprop.bg
		if name=='fg': colorobj = styleprop.fg
		if not isname: colorobj.set_manual(val)
		else: colorobj.set_named(val)

	def to_xml(self, part, name):
		part = ET.SubElement(part, name)
		for k, v in self.styleprop.items(): 
			if v:
				v.to_xml(part, k)

class basstyle_main():
	def __init__(self):
		self.states = {}
		self.colfrom = []

	def add_color(self, ctrlcat, state, name, rgb):
		if not state: state = 'main'
		if ctrlcat not in self.states: self.states[ctrlcat] = basstyle_state()
		cstate = self.states[ctrlcat]
		cstate.add_color(state, name, rgb)

	def add_color_named(self, ctrlcat, state, name, colname):
		if not state: state = 'main'
		if ctrlcat not in self.states: self.states[ctrlcat] = basstyle_state()
		cstate = self.states[ctrlcat]
		cstate.add_color_named(state, name, colname)

	def to_xml(self, part, name):
		cpart = ET.SubElement(part, name)
		if self.colfrom: cpart.set('color_from', '|'.join(self.colfrom))
		for k, v in self.states.items(): 
			if v:
				v.to_xml(cpart, k)

# =============================================== CTRL ===============================================

class data_control():
	def __init__(self):
		self.styles = []

	def to_xml(self, part, name):
		part = ET.SubElement(part, name)
		part.set('styles', ':'.join(self.styles))

# =============================================== STYLE ===============================================

class data_theme():
	def __init__(self):
		self.controls = {}
		self.style_part = {}
		self.style_global = basstyle_main()
		self.colors = {}
		self.win32_colors = win32_colors.win32_colors()

	def import_win32_colors(self):
		win32_colors = self.win32_colors

		self.add_color('scrollbar', win32_colors.scrollbar.get_int() )
		self.add_color('background', win32_colors.background.get_int() )
		self.add_color('activetitle', win32_colors.activetitle.get_int() )
		self.add_color('inactivetitle', win32_colors.inactivetitle.get_int() )
		self.add_color('menu', win32_colors.menu.get_int() )
		self.add_color('window', win32_colors.window.get_int() )
		self.add_color('windowframe', win32_colors.windowframe.get_int() )
		self.add_color('menutext', win32_colors.menutext.get_int() )
		self.add_color('windowtext', win32_colors.windowtext.get_int() )
		self.add_color('titletext', win32_colors.titletext.get_int() )
		self.add_color('activeborder', win32_colors.activeborder.get_int() )
		self.add_color('inactiveborder', win32_colors.inactiveborder.get_int() )
		self.add_color('appworkspace', win32_colors.appworkspace.get_int() )
		self.add_color('hilight', win32_colors.hilight.get_int() )
		self.add_color('hilighttext', win32_colors.hilighttext.get_int() )
		self.add_color('buttonface', win32_colors.buttonface.get_int() )
		self.add_color('buttonshadow', win32_colors.buttonshadow.get_int() )
		self.add_color('graytext', win32_colors.graytext.get_int() )
		self.add_color('buttontext', win32_colors.buttontext.get_int() )
		self.add_color('inactivetitletext', win32_colors.inactivetitletext.get_int() )
		self.add_color('buttonhilight', win32_colors.buttonhilight.get_int() )
		self.add_color('buttondkshadow', win32_colors.buttondkshadow.get_int() )
		self.add_color('buttonlight', win32_colors.buttonlight.get_int() )
		self.add_color('infotext', win32_colors.infotext.get_int() )
		self.add_color('infowindow', win32_colors.infowindow.get_int() )
		self.add_color('buttonalternateface', win32_colors.buttonalternateface.get_int() )
		self.add_color('hottrackingcolor', win32_colors.hottrackingcolor.get_int() )
		self.add_color('gradientactivetitle', win32_colors.gradientactivetitle.get_int() )
		self.add_color('gradientinactivetitle', win32_colors.gradientinactivetitle.get_int() )
		self.add_color('menuhilight', win32_colors.menuhilight.get_int() )
		self.add_color('menubar', win32_colors.menubar.get_int() )

		globalstyle = self.style_global
		globalstyle.add_color_named('control', None, 'bg', 'buttonface')
		globalstyle.add_color_named('control', None, 'fg', 'windowtext')
		globalstyle.add_color_named('control', 'disabled', 'bg', 'buttonface')
		globalstyle.add_color_named('control', 'disabled', 'fg', 'graytext')
		globalstyle.add_color_named('text', None, 'bg', 'window')
		globalstyle.add_color_named('text', None, 'fg', 'windowtext')
		globalstyle.add_color_named('text', 'selected', 'bg', 'hilight')
		globalstyle.add_color_named('text', 'selected', 'fg', 'hilighttext')
		globalstyle.add_color_named('text', 'disabled', 'bg', 'buttonface')
		globalstyle.add_color_named('text', 'disabled', 'fg', 'graytext')

		curstyle, curctrl = self.add_stylecontrol('tooltip')
		curstyle.add_color_named('control', None, 'bg', 'infowindow')
		curstyle.add_color_named('control', None, 'fg', 'infotext')

		curstyle, curctrl = self.add_stylecontrol('menubar')
		curstyle.add_color_named('control', None, 'bg', 'menu')
		curstyle.add_color_named('control', None, 'fg', 'menutext')

		curstyle, curctrl = self.add_stylecontrol('menu')
		curstyle.add_color_named('control', None, 'bg', 'menu')
		curstyle.add_color_named('control', None, 'fg', 'menutext')

	def add_color(self, name, rgb):
		c_obj = data_color()
		c_obj.set_manual(rgb)
		self.colors[name] = c_obj

	def add_stylecontrol(self, name):
		s_obj = basstyle_main()
		self.style_part[name] = s_obj
		c_obj = data_control()
		c_obj.styles.append(name)
		self.controls[name] = c_obj
		return s_obj, c_obj

	def add_style(self, name):
		c_obj = basstyle_main()
		self.style[name] = c_obj
		return c_obj

	def add_control(self, name):
		c_obj = data_control()
		self.controls[name] = c_obj
		return c_obj

	def to_xml(self, out_file):
		outx = ET.Element("theme")

		part = ET.SubElement(outx, 'colors')
		for k, v in self.colors.items(): v.to_xml(part, k)
		self.style_global.to_xml(outx, 'style_global')
		part = ET.SubElement(outx, 'style_part')
		for k, v in self.style_part.items(): v.to_xml(part, k)
		part = ET.SubElement(outx, 'controls')
		for k, v in self.controls.items(): v.to_xml(part, k)

		outfile = ET.ElementTree(outx)
		ET.indent(outfile, space="\t", level=0)
		outfile.write(out_file, xml_declaration = True)
