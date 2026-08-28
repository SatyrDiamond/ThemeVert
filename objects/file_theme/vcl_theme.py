from external.easybinrw import easybinrw
import xml.etree.ElementTree as ET
from PIL import Image
from objects.file_theme import vcl_colors

def read_string(ebrw_readstr):
	size = ebrw_readstr.int_u32()
	return ebrw_readstr.string16(size)

def read_var(ebrw_readstr):
	vard = []
	vard.append(read_string(ebrw_readstr))
	vard.append(read_string(ebrw_readstr))
	vard.append(read_string(ebrw_readstr))
	return vard

def read_vars(ebrw_readstr, count):
	out = {}
	for x in range(count):
		data = read_var(ebrw_readstr)
		out[data[0]] = data[2]
	return out

def tpf_string(ebrw_readstr):
	size = ebrw_readstr.int_u8()
	return ebrw_readstr.string(size)

class tpf_attrib:
	def __repr__(self):
		return str(self.value)

	def __init__(self, ebrw_readstr):
		self.name = ''
		self.valtype = 0
		self.value = None

		self.name = tpf_string(ebrw_readstr)
		if self.name:
			self.valtype = ebrw_readstr.int_u8()
			self.value = None
			if self.valtype==2: self.value = int(ebrw_readstr.int_u8())
			elif self.valtype==3: self.value = int(ebrw_readstr.int_u16())
			elif self.valtype==4: self.value = int(ebrw_readstr.int_u32())
			elif self.valtype==6: self.value = tpf_string(ebrw_readstr)
			elif self.valtype==7: self.value = tpf_string(ebrw_readstr)
			elif self.valtype==8: self.value = False
			elif self.valtype==9: self.value = True
			elif self.valtype==11: self.value = int(ebrw_readstr.int_u8())
			elif self.valtype==10: 
				self.value = ebrw_readstr.raw( ebrw_readstr.int_u32() )

				part_ebrw_readstr = easybinrw.binread()
				part_ebrw_readstr.load_data(self.value)
				count = part_ebrw_readstr.int_u16()
				unkv = part_ebrw_readstr.int_u16()
				outval = {}
				for _ in range(count):
					object_type = read_string(part_ebrw_readstr)
					data = part_ebrw_readstr.raw(part_ebrw_readstr.int_u32())
					data = tpf_data(data)
					outval[data.object_name] = data
				self.value = outval

			else: 
				#print('ATTRIB --', self.name, '| unknown valtype', self.valtype, ebrw_readstr.raw(64))
				exit()
			#print('ATTRIB --', self.name, self.value if not self.valtype==10 else 'DATA')

class tpf_data:
	def __repr__(self):
		return '<TPF %s Obj: %s>' % (self.object_type, self.object_name)
 
	def __getitem__(self, data):
		return self.attribs[data]

	def __contains__(self, data):
		return self.attribs.__contains__(data)

	def items(self):
		return self.attribs.items()

	def __init__(self, data):
		ebrw_readstr = easybinrw.binread()
		ebrw_readstr.load_data(data)
		assert ebrw_readstr.raw(4)==b'TPF0'
		self.object_type = tpf_string(ebrw_readstr)
		self.object_name = tpf_string(ebrw_readstr)
		self.attribs = {}
		while ebrw_readstr.remaining():
			attrib = tpf_attrib(ebrw_readstr)
			if not attrib.name: break
			self.attribs[attrib.name] = attrib.value

	def to_xml(self, part):
		part = ET.SubElement(part, self.object_type)
		part.set('name', self.object_name)
		od = {}
		for k, v in self.attribs.items():
			if k in ['Left', 'Top', 'Height', 'Width']:
				if 'Size' not in od: od['Size'] = ET.SubElement(part, 'Size')
				od['Size'].set(k, str(v))
			elif k.startswith('Margin'):
				if 'Margin' not in od: od['Margin'] = ET.SubElement(part, 'Margin')
				od['Margin'].set(k.split('Margin')[1], str(v))
			elif k.startswith('TextMargin'):
				if 'Text' not in od: od['Text'] = ET.SubElement(part, 'Text')
				if 'TextMargin' not in od: od['TextMargin'] = ET.SubElement(od['Text'], 'Margin')
				od['TextMargin'].set(k.split('TextMargin')[1], str(v))
			elif k.startswith('Text'):
				if 'Text' not in od: od['Text'] = ET.SubElement(part, 'Text')
				od['Text'].set(k.split('Text')[1], str(v))
			elif '.' in k:
				sk = k.split('.')
				if sk[0] not in od: od[sk[0]] = ET.SubElement(part, sk[0])
				od[sk[0]].set(sk[1], str(v))
			else:
				if not isinstance(v, dict):
					ET.SubElement(part, k).text = str(v)
				else:
					inpart = ET.SubElement(part, k)
					for n, x in v.items():
						x.to_xml(inpart)

def get_color_int(val):
	if val[0]=='$': 
		h = val.lstrip('$')
		return list(int(h[i:i+2], 16) for i in (2, 4, 6))
	elif val[0]=='#': 
		h = val.lstrip('#')
		return list(int(h[i:i+2], 16) for i in (0, 2, 4))
	else:
		return val

class masterstyle_data:

	def __init__(self, filename):
		ebrw_readstr = easybinrw.binread()
		ebrw_readstr.load_file(filename)

		self.text1 = read_string(ebrw_readstr)
		self.text2 = read_string(ebrw_readstr)
		self.text3 = read_string(ebrw_readstr)
		self.text4 = read_string(ebrw_readstr)
		self.text5 = read_string(ebrw_readstr)
		self.text6 = read_string(ebrw_readstr)

		self.unk1 = ebrw_readstr.int_u16()
		size = ebrw_readstr.int_u32()
		self.unk2 = ebrw_readstr.int_u32()
		self.unk3 = ebrw_readstr.raw(size)

		size = ebrw_readstr.int_u32()
		self.images = {}
		for x in range(size):
			style_name = read_string(ebrw_readstr)
			style_size_x = ebrw_readstr.int_u32()
			style_size_y = ebrw_readstr.int_u32()
			style_data = ebrw_readstr.raw(style_size_x*style_size_y*4)
			image = Image.frombytes('RGBA', (style_size_x,style_size_y), style_data, 'raw')

			b, g, r, a = image.split()
			image = Image.merge("RGBA", (r, g, b, a))
			image = image.transpose(Image.FLIP_TOP_BOTTOM)

			unkd = ebrw_readstr.int_u16()
			self.images[style_name] = [image, style_size_x, style_size_y, unkd]

		size = ebrw_readstr.int_u32()
		self.objects = {}
		for x in range(size):
			object_type = read_string(ebrw_readstr)
			data = ebrw_readstr.raw(ebrw_readstr.int_u32())
			data = tpf_data(data)
			self.objects[data.object_name] = data

		size = ebrw_readstr.int_u8()
		self.color = read_vars(ebrw_readstr, size+1)

		size = ebrw_readstr.int_u32()
		self.color_win32 = read_vars(ebrw_readstr, size)

		size = ebrw_readstr.int_u8()
		self.fonts = read_vars(ebrw_readstr, size+1)

	def image_crop(self, filename, left, upper, right, lower, outname):
		if filename in self.images:
			imgcropped = self.images[filename][0].crop([left, upper, right, lower])
			imgcropped.save(outname)

	def get_color_w32(self, name):
		ov = None
		if name in self.color_win32: ov = self.color_win32[name]
		elif name in vcl_colors.colors_win32: ov = vcl_colors.colors_win32[name]
		while (ov in vcl_colors.colors_win32) or (ov in vcl_colors.colors):
			if ov in vcl_colors.colors_win32: ov = vcl_colors.colors_win32[ov]
			if ov in vcl_colors.colors: ov = vcl_colors.colors[ov]
		if ov in vcl_colors.colors: ov = vcl_colors.colors[ov]
		return ov

	def to_xml(self, out_file):
		outx = ET.Element("masterstyle")

		part = ET.SubElement(outx, 'objects')
		for k, v in self.objects.items(): 
			if v.object_name == 'Form':
				v.to_xml(part)

		part = ET.SubElement(outx, 'color')
		for k, v in self.color.items(): part.set(k, v)

		part = ET.SubElement(outx, 'color_win32')
		for k, v in self.color_win32.items(): part.set(k, v)

		part = ET.SubElement(outx, 'fonts')
		for k, v in self.fonts.items(): 
			ipart = ET.SubElement(part, k)
			ipart.set('data', v)

		outfile = ET.ElementTree(outx)
		ET.indent(outfile, space="\t", level=0)
		outfile.write(out_file, xml_declaration = True)
