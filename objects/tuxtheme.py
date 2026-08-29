
import xml.etree.ElementTree as ET
from objects.colors import win32 as colors_win32
from objects.colors import gtk as colors_gtk
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

class data_font():
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
			xpart = ET.SubElement(part, name)
			if self.face: xpart.set('face', self.face)
			if self.size: xpart.set('size', str(self.size))
			if self.fx: xpart.set('fx', '|'.join(self.fx))
			#if self.color.used: self.color.to_xml(part, 'color')

# =============================================== STYLE ===============================================

class basstyle_state():
	def __init__(self):
		self.prop = {}
		self.colors = {}
		self.fonts = {}
	def __bool__(self): return True in [bool(c) for c in self.colors]

	def create_color(self, name):
		if name not in self.colors: self.colors[name] = data_color()
		return self.colors[name]

	def create_font(self, name):
		if name not in self.fonts: self.fonts[name] = data_font()
		return self.fonts[name]

	def to_xml(self, part, name):
		cpart = ET.SubElement(part, name)
		if self.fonts:
			xpart = ET.SubElement(cpart, 'fonts')
			for k, v in self.fonts.items(): v.to_xml(xpart, k)
		if self.prop:
			xpart = ET.SubElement(cpart, 'prop')
			for k, v in self.prop.items(): xpart.set(k, str(v))
		if self.colors:
			xpart = ET.SubElement(cpart, 'colors')
			for k, v in self.colors.items(): v.to_xml(xpart, k)

	def add_color(self, name, rgb):
		self._internal_add_color(name, rgb, False)

	def add_color_named(self, name, val):
		self._internal_add_color(name, val, True)

	def _internal_add_color(self, name, val, isname):
		colorobj = self.create_color(name)
		if not isname: colorobj.set_manual(val)
		else: colorobj.set_named(val)

	def get_color(self, name):
		if name in self.colors: return self.colors[name].get_simp()

	def exists_color(self, name):
		return name in self.colors

class basstyle_main():
	def __init__(self):
		self.mainstate = basstyle_state()
		self.states = {}
		self.colfrom = []

	def add_state(self, state):
		if state=='main':
			return self.mainstate
		else:
			if state not in self.states: self.states[state] = basstyle_state()
			return self.states[state]

	def add_color(self, colloc, rgb):
		calloc_val = triplestr.from_str(colloc)
		state = calloc_val.category
		name = calloc_val.type

		cstate = self.add_state(state)
		cstate.add_color(name, rgb)

	def add_color_named(self, colloc, colname):
		calloc_val = triplestr.from_str(colloc)
		state = calloc_val.category
		name = calloc_val.type

		cstate = self.add_state(state)
		cstate.add_color_named(name, colname)

	def add_font(self, colloc):
		calloc_val = triplestr.from_str(colloc)
		state = calloc_val.category
		name = calloc_val.type

		cstate = self.add_state(state)
		return cstate.create_font(name)

	def to_xml(self, cpart):
		if self.colfrom: cpart.set('color_from', '|'.join(self.colfrom))
		self.mainstate.to_xml(cpart, 'main')
		if self.states:
			spart = ET.SubElement(cpart, 'states')
			for k, v in self.states.items(): 
				if v:
					v.to_xml(spart, k)

	def get_color(self, colloc):
		calloc_val = triplestr.from_str(colloc)
		state = calloc_val.category
		name = calloc_val.type

		if state in self.states: 
			c = self.states[state].get_color(name)
			if c: return c
		return self.mainstate.get_color(name)

	def exists_color(self, colloc):
		calloc_val = triplestr.from_str(colloc)
		state = calloc_val.category
		name = calloc_val.type

		if state=='main': return self.mainstate.exists_color(name)
		elif state in self.states: return self.states[state].exists_color(name)
		else: return False

	def simple_add_col(self, colloc, nameval):
		calloc_val = triplestr.from_str(colloc)
		state = calloc_val.category
		name = calloc_val.type

		cstate = self.add_state(state)
		if not nameval[0]: cstate.add_color(name, nameval[1])
		else: cstate.add_color_named(name, nameval[1])


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
		self.colors_win32 = colors_win32.colors_win32()
		self.colors_gtk = colors_gtk.colors_gtk()
		self.supported_types = []

	def add_global_color(self, name, rgb):
		c_obj = data_color()
		c_obj.set_manual(rgb)
		self.colors[name] = c_obj

	def add_stylecontrol(self, name):
		s_obj = self.add_style(name)
		c_obj = self.add_control(name)
		return s_obj, c_obj

	def add_style(self, name):
		if name not in self.style_part:
			s_obj = basstyle_main()
			self.style_part[name] = s_obj
		return self.style_part[name]

	def add_control(self, name):
		if name not in self.controls:
			c_obj = data_control()
			c_obj.styles.append(name)
			self.controls[name] = c_obj
		return self.controls[name]

	def to_xml(self, out_file):
		outx = ET.Element("theme")

		part = ET.SubElement(outx, 'colors')
		for k, v in self.colors.items(): v.to_xml(part, k)

		self.colors_win32.to_xml(outx, 'colors_win32')

		self.colors_gtk.to_xml(outx, 'colors_gtk')

		part = ET.SubElement(outx, 'style_global')
		self.style_global.to_xml(part)

		part = ET.SubElement(outx, 'style_part')
		for k, v in self.style_part.items():
			cpart = ET.SubElement(part, k)
			v.to_xml(cpart)

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

		ctrl_main_bg = globalstyle.get_color('main:control_bg')
		ctrl_main_fg = globalstyle.get_color('main:control_fg')

		if (not ctrl_main_bg) or (not ctrl_main_fg):
			print('control BG or FG missing')
			exit()

		text_main_bg = globalstyle.get_color('main:edit_bg')
		text_main_fg = globalstyle.get_color('main:edit_fg')
		if (not text_main_bg) or (not text_main_fg):
			print('text BG or FG missing')
			exit()

		greytxt_needed = False

		# ----------------- selected -----------------
		#text
		color1 = globalstyle.exists_color('selected:edit_bg')
		color2 = globalstyle.exists_color('selected:edit_fg')
		if (not color1) or (not color2):
			globalstyle.simple_add_col('selected:edit_fg', text_main_bg)
			globalstyle.simple_add_col('selected:edit_bg', text_main_fg)

		#control
		color1 = globalstyle.exists_color('main:control_text_selected_bg')
		color2 = globalstyle.exists_color('main:control_text_selected')
		if (not color1) or (not color2):
			globalstyle.simple_add_col('main:control_text_selected_bg', ctrl_main_fg)
			globalstyle.simple_add_col('main:control_text_selected', ctrl_main_bg)

		# ----------------- disabled -----------------
		#control
		ctxt = 'disabled:control_bg'
		if not globalstyle.exists_color(ctxt): globalstyle.simple_add_col(ctxt, ctrl_main_bg)
		if not globalstyle.exists_color('disabled:control_fg'):
			globalstyle.add_color_named('disabled:control_fg', 'generated__greytext')
			greytxt_needed = True

		#text
		ctxt = 'disabled:edit_bg'
		if not globalstyle.exists_color(ctxt): globalstyle.simple_add_col(ctxt, ctrl_main_bg)
		if not globalstyle.exists_color('disabled:edit_fg'):
			globalstyle.add_color_named('disabled:edit_fg', 'generated__greytext')
			greytxt_needed = True

		if greytxt_needed:
			greytxt1 = self.get_color(None, 'main:control_bg', True)
			greytxt2 = self.get_color(None, 'main:edit_fg', True)
			greytxt1 /= 2
			greytxt2 /= 2
			greycolor = (greytxt1+greytxt2)
			self.add_global_color('generated__greytext', greycolor.get_int() )
