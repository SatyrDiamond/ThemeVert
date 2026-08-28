
import xml.etree.ElementTree as ET
from objects import win32_colors
from objects import visual
from objects import valobjs

triplestr = valobjs.triplestr

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

	def get_simp(self):
		if self.used:
			if self.type=='name': return True, self.index_name
			if self.manual=='manual': return False, self.color

class data_text():
	def __init__(self):
		self.used = False
		self.face = None
		self.size = 0
		self.fx = []
		#self.color = data_color()
	def set_face(self, part, face):
		self.used = True
		self.face = face
	def to_xml(self, part, name):
		if self.used:
			part = ET.SubElement(part, 'font')
			if self.face: part.set('face', self.face)
			if self.size: part.set('size', self.size)
			if self.fx: part.set('fx', '|'.join(self.fx))
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
		self.font.to_xml(cpart, 'font')
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

	def add_prop(self, stylpropname):
		if stylpropname not in self.styleprop: self.styleprop[stylpropname] = basstyle_stateprop()
		return self.styleprop[stylpropname]

	def _internal_add_color(self, stylpropname, name, val, isname):
		styleprop = self.add_prop(stylpropname)
		if name=='bg': colorobj = styleprop.bg
		elif name=='fg': colorobj = styleprop.fg
		if not isname: colorobj.set_manual(val)
		else: colorobj.set_named(val)

	def to_xml(self, part, name):
		part = ET.SubElement(part, name)
		for k, v in self.styleprop.items(): 
			if v:
				v.to_xml(part, k)

	def get_color(self, stylpropname, name):
		if stylpropname in self.styleprop: 
			cd = self.styleprop[stylpropname]
			if name=='bg': return cd.bg.get_simp()
			elif name=='fg': return cd.fg.get_simp()

class basstyle_main():
	def __init__(self):
		self.states = {}
		self.colfrom = []

	def add_state(self, state):
		if state not in self.states: self.states[state] = basstyle_state()
		return self.states[state]

	def add_color(self, colloc, rgb):
		calloc_val = triplestr.from_str(colloc)
		ctrlcat = calloc_val.category
		state = calloc_val.type
		name = calloc_val.subtype

		cstate = self.add_state(ctrlcat)
		cstate.add_color(state, name, rgb)

	def add_color_named(self, colloc, colname):
		calloc_val = triplestr.from_str(colloc)
		ctrlcat = calloc_val.category
		state = calloc_val.type
		name = calloc_val.subtype

		cstate = self.add_state(ctrlcat)
		cstate.add_color_named(state, name, colname)

	def add_font(self, colloc):
		calloc_val = triplestr.from_str(colloc)
		ctrlcat = calloc_val.category
		state = calloc_val.type

		cstate = self.add_state(ctrlcat)
		cprop = cstate.add_prop(state)
		return cprop.font

	def to_xml(self, part, name):
		cpart = ET.SubElement(part, name)
		if self.colfrom: cpart.set('color_from', '|'.join(self.colfrom))
		for k, v in self.states.items(): 
			if v:
				v.to_xml(cpart, k)

	def get_color(self, colloc):
		calloc_val = triplestr.from_str(colloc)
		ctrlcat = calloc_val.category
		state = calloc_val.type
		name = calloc_val.subtype

		if ctrlcat in self.states:
			return self.states[ctrlcat].get_color(state, name)

	def simple_add_col(self, colloc, nameval):
		calloc_val = triplestr.from_str(colloc)
		ctrlcat = calloc_val.category
		state = calloc_val.type
		name = calloc_val.subtype

		if ctrlcat not in self.states: self.states[ctrlcat] = basstyle_state()
		cstate = self.states[ctrlcat]
		if not nameval[0]: cstate.add_color(state, name, nameval[1])
		else: cstate.add_color_named(state, name, nameval[1])


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
		self.supported_types = []

	def add_global_color(self, name, rgb):
		c_obj = data_color()
		c_obj.set_manual(rgb)
		self.colors[name] = c_obj

	def add_stylecontrol(self, name):
		if name not in self.style_part:
			s_obj = basstyle_main()
			self.style_part[name] = s_obj
		s_obj = self.style_part[name]

		if name not in self.controls:
			c_obj = data_control()
			c_obj.styles.append(name)
			self.controls[name] = c_obj
		c_obj = self.controls[name]

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

	def get_color(self, controlname, colloc, alwayscol):
		styleobj = self.style_global

		c = styleobj.get_color(colloc)

		if controlname in self.controls:
			style = self.controls[controlname]
			for s in style.styles:
				stylep = self.style_part[s]
				oc = stylep.get_color(colloc)
				if oc is not None: 
					c = oc
				else:
					print('debug:', str(colloc), 'not found in', controlname)

		if c:
			isname, val = c
			if alwayscol:
				if isname: val = self.colors[val]
				return val.color.copy()
			else:
				return isname, val.copy() if not isname else val

	def complete_incomplete(self):
		globalstyle = self.style_global

		ctrl_main_bg = globalstyle.get_color('control:main:bg')
		ctrl_main_fg = globalstyle.get_color('control:main:fg')
		if (not ctrl_main_bg) or (not ctrl_main_fg):
			print('control BG or FG missing')
			exit()

		text_main_bg = globalstyle.get_color('text:main:bg')
		text_main_fg = globalstyle.get_color('text:main:fg')
		if (not text_main_bg) or (not text_main_fg):
			print('text BG or FG missing')
			exit()

		greytxt_needed = False

		# ----------------- selected -----------------
		#text
		text_sel_bg = globalstyle.get_color('text:selected:bg')
		text_sel_fg = globalstyle.get_color('text:selected:fg')
		if (not text_sel_bg) or (not text_sel_fg):
			globalstyle.simple_add_col('text:selected:fg', text_main_bg)
			globalstyle.simple_add_col('text:selected:bg', text_main_fg)

		#control
		text_sel_bg = globalstyle.get_color('control:text_selected:bg')
		text_sel_fg = globalstyle.get_color('control:text_selected:fg')
		if (not text_sel_bg) or (not text_sel_fg):
			globalstyle.simple_add_col('control:text_selected:fg', text_main_bg)
			globalstyle.simple_add_col('control:text_selected:bg', text_main_fg)

		# ----------------- disabled -----------------
		#control
		ctxt = 'control:disabled:bg'
		if not globalstyle.get_color(ctxt): globalstyle.simple_add_col(ctxt, ctrl_main_bg)
		if not globalstyle.get_color('control:disabled:fg'):
			globalstyle.add_color_named('control:disabled:fg', '_generated_greytext')
			greytxt_needed = True

		#text
		ctxt = 'text:disabled:bg'
		if not globalstyle.get_color(ctxt): globalstyle.simple_add_col(ctxt, ctrl_main_bg)
		if not globalstyle.get_color('text:disabled:fg'):
			globalstyle.add_color_named('text:disabled:fg', '_generated_greytext')
			greytxt_needed = True

		if greytxt_needed:
			greytxt1 = self.get_color(None, 'control:main:bg', True)
			greytxt2 = self.get_color(None, 'text:main:fg', True)
			greytxt1 /= 2
			greytxt2 /= 2
			greycolor = (greytxt1+greytxt2)
			self.add_global_color('_generated_greytext', greycolor.get_int() )

	def import_win32_colors(self):
		win32_colors = self.win32_colors
		if win32_colors.used == True and 'basic' not in self.supported_types:
			self.supported_types.append('basic')
			self.add_global_color('activeborder', win32_colors.activeborder.get_int() )
			self.add_global_color('activetitle', win32_colors.activetitle.get_int() )
			self.add_global_color('appworkspace', win32_colors.appworkspace.get_int() )
			self.add_global_color('background', win32_colors.background.get_int() )
			self.add_global_color('buttonalternateface', win32_colors.buttonalternateface.get_int() )
			self.add_global_color('buttondkshadow', win32_colors.buttondkshadow.get_int() )
			self.add_global_color('buttonface', win32_colors.buttonface.get_int() )
			self.add_global_color('buttonhilight', win32_colors.buttonhilight.get_int() )
			self.add_global_color('buttonlight', win32_colors.buttonlight.get_int() )
			self.add_global_color('buttonshadow', win32_colors.buttonshadow.get_int() )
			self.add_global_color('buttontext', win32_colors.buttontext.get_int() )
			self.add_global_color('gradientactivetitle', win32_colors.gradientactivetitle.get_int() )
			self.add_global_color('gradientinactivetitle', win32_colors.gradientinactivetitle.get_int() )
			self.add_global_color('graytext', win32_colors.graytext.get_int() )
			self.add_global_color('hilight', win32_colors.hilight.get_int() )
			self.add_global_color('hilighttext', win32_colors.hilighttext.get_int() )
			self.add_global_color('hottrackingcolor', win32_colors.hottrackingcolor.get_int() )
			self.add_global_color('inactiveborder', win32_colors.inactiveborder.get_int() )
			self.add_global_color('inactivetitle', win32_colors.inactivetitle.get_int() )
			self.add_global_color('inactivetitletext', win32_colors.inactivetitletext.get_int() )
			self.add_global_color('infotext', win32_colors.infotext.get_int() )
			self.add_global_color('infowindow', win32_colors.infowindow.get_int() )
			self.add_global_color('menu', win32_colors.menu.get_int() )
			self.add_global_color('menubar', win32_colors.menubar.get_int() )
			self.add_global_color('menuhilight', win32_colors.menuhilight.get_int() )
			self.add_global_color('menutext', win32_colors.menutext.get_int() )
			self.add_global_color('scrollbar', win32_colors.scrollbar.get_int() )
			self.add_global_color('titletext', win32_colors.titletext.get_int() )
			self.add_global_color('window', win32_colors.window.get_int() )
			self.add_global_color('windowframe', win32_colors.windowframe.get_int() )
			self.add_global_color('windowtext', win32_colors.windowtext.get_int() )

			globalstyle = self.style_global
			globalstyle.add_color_named('control:main:bg', 'buttonface')
			globalstyle.add_color_named('control:main:fg', 'windowtext')
			globalstyle.add_color_named('control:disabled:bg', 'buttonface')
			globalstyle.add_color_named('control:disabled:fg', 'graytext')
			globalstyle.add_color_named('text:main:bg', 'window')
			globalstyle.add_color_named('text:main:fg', 'windowtext')
			globalstyle.add_color_named('text:selected:bg', 'hilight')
			globalstyle.add_color_named('text:selected:fg', 'hilighttext')
			globalstyle.add_color_named('text:disabled:bg', 'buttonface')
			globalstyle.add_color_named('text:disabled:fg', 'graytext')

			# ------ desktop -----
			curstyle, curctrl = self.add_stylecontrol('desktop')
			curstyle.add_color_named('control:main:bg', 'Background')

			# ------ tooltip -----
			curstyle, curctrl = self.add_stylecontrol('tooltip')
			curstyle.add_color_named('control:main:bg', 'infowindow')
			curstyle.add_color_named('control:main:fg', 'infotext')

			# ------ menubar -----
			curstyle, curctrl = self.add_stylecontrol('menubar')
			curstyle.add_color_named('control:main:bg', 'menubar')
			curstyle.add_color_named('control:main:fg', 'menutext')

			# ------ menu -----
			curstyle, curctrl = self.add_stylecontrol('menu')
			curstyle.add_color_named('control:main:bg', 'menu')
			curstyle.add_color_named('control:main:fg', 'menutext')

			# ------ scrollbar -----
			curstyle, curctrl = self.add_stylecontrol('scrollbar')
			curstyle.add_color_named('scrollbar:main:bg', 'scrollbar')
			curstyle.add_color_named('scrollbar:main:fg', 'buttonface')

	def export_win32_colors(self):
		win32_colors = self.win32_colors
		if win32_colors.used == False and 'win32' not in self.supported_types:
			self.supported_types.append('win32')

			globalstyle = self.style_global
			ctrl_main_bg = self.get_color(None, 'control:main:bg', True)
			ctrl_main_fg = self.get_color(None, 'control:main:fg', True)
			text_main_bg = self.get_color(None, 'text:main:bg', True)
			text_main_fg = self.get_color(None, 'text:main:fg', True)
			text_sel_bg = self.get_color(None, 'text:selected:bg', True)
			text_sel_fg = self.get_color(None, 'text:selected:fg', True)

			threed_dark = ctrl_main_bg.copy()*0.7
			threed_light = ctrl_main_bg.copy()*1.3

			win32_colors.set('buttonface', ctrl_main_bg.get_int() )
			win32_colors.set('buttondkshadow', threed_dark.get_int() )
			win32_colors.set('buttonshadow', threed_dark.get_int() )
			win32_colors.set('buttonhilight', threed_light.get_int() )
			win32_colors.set('buttonlight', threed_light.get_int() )

			win32_colors.set('buttontext', ctrl_main_fg.get_int() )
			win32_colors.set('menutext', ctrl_main_fg.get_int() )

			win32_colors.set('window', text_main_bg.get_int() )
			win32_colors.set('windowtext', text_main_fg.get_int() )

			win32_colors.set('hilight', text_sel_bg.get_int() )
			win32_colors.set('hilighttext', text_sel_fg.get_int() )

			win32_colors.set('activeborder', ctrl_main_bg.get_int() )
			win32_colors.set('activetitle', ctrl_main_bg.get_int() )
			win32_colors.set('gradientactivetitle', ctrl_main_bg.get_int() )
			win32_colors.set('gradientinactivetitle', ctrl_main_bg.get_int() )
			win32_colors.set('inactiveborder', ctrl_main_bg.get_int() )
			win32_colors.set('inactivetitle', ctrl_main_bg.get_int() )
			win32_colors.set('windowframe', ctrl_main_bg.get_int() )

			win32_colors.set('inactivetitletext', ctrl_main_fg.get_int() )
			win32_colors.set('titletext', ctrl_main_fg.get_int() )

			# ------ desktop -----
			color_bg = self.get_color('desktop', 'control:main:bg', True)
			win32_colors.set('background', color_bg.get_int() )

			# ------ tooltip -----
			color_bg = self.get_color('tooltip', 'control:main:bg', True)
			color_fg = self.get_color('tooltip', 'text:main:fg', True)
			win32_colors.set('infowindow', color_bg.get_int() )
			win32_colors.set('infotext', color_fg.get_int() )

			# ------ menubar -----
			color_bg = self.get_color('menubar', 'control:main:bg', True)
			win32_colors.set('menubar', color_bg.get_int() )

			# ------ menu -----
			color_bg = self.get_color('menu', 'control:main:bg', True)
			color_fg = self.get_color('menu', 'text:main:fg', True)
			win32_colors.set('menu', color_bg.get_int() )
			win32_colors.set('menutext', color_fg.get_int() )

			# ------ scrollbar -----
			scrollbar = self.get_color('scrollbar', 'control:main:bg', True)
			win32_colors.set('scrollbar', scrollbar.get_int() )
