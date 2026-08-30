# SPDX-FileCopyrightText: 2024 SatyrDiamond
# SPDX-License-Identifier: GPL-3.0-or-later

from dataclasses import dataclass
from dataclasses import field
from functions import xtramath
import copy

def hsv_to_rgb(h, s, v) -> tuple:
	h -= h.__ceil__()-1
	if s:
		if h == 1.0: h = 0.0
		i = int(h*6.0); f = h*6.0 - i
		w = v * (1.0 - s)
		q = v * (1.0 - s * f)
		t = v * (1.0 - s * (1.0 - f))
		if i==0: return (v, t, w)
		if i==1: return (q, v, w)
		if i==2: return (w, v, t)
		if i==3: return (w, q, v)
		if i==4: return (t, w, v)
		if i==5: return (v, w, q)
	else: return (v, v, v)

@dataclass
class visual_color:
	r_i: int = 0
	g_i: int = 0
	b_i: int = 0
	r_f: float = 0
	g_f: float = 0
	b_f: float = 0
	used: bool = False
	fx_allowed: list = field(default_factory=list)
	priority: int = 0

	def json__make(self):
		outjson = {}
		if used: outjson['color'] = [self.r_i, self.g_i, self.b_i]
		outjson['fx_allowed'] = self.fx_allowed
		outjson['priority'] = self.priority
		return outjson

	@classmethod
	def json__parse(cls, injson):
		cls = cls()
		if 'color' in injson: 
			self.r_i, self.g_i, self.b_i = injson['color']
			self.internal_tofloat()
		if 'fx_allowed' in injson: cls.fx_allowed = injson['fx_allowed']
		if 'priority' in injson: cls.priority = injson['priority']
		return cls

	@classmethod
	def from_float(self, indata):
		color_obj = visual_color()
		color_obj.set_float(indata)
		return color_obj

	@classmethod
	def from_int(self, indata):
		color_obj = visual_color()
		color_obj.set_int(indata)
		return color_obj

	@classmethod
	def from_hex(self, indata):
		color_obj = visual_color()
		color_obj.set_hex(indata)
		return color_obj

	@classmethod
	def from_hsv(self, h, s, v):
		color_obj = visual_color()
		color_obj.set_hsv(h, s, v)
		return color_obj

	def __add__(self, valuein):
		obj_copy = copy.copy(self)
		if obj_copy.used:
			if isinstance(valuein, visual_color):
				obj_copy.r_f += valuein.r_f
				obj_copy.g_f += valuein.g_f
				obj_copy.b_f += valuein.b_f
			else:
				obj_copy.r_f += valuein
				obj_copy.g_f += valuein
				obj_copy.b_f += valuein
			obj_copy.internal_clamp()
			obj_copy.internal_toint()
		return obj_copy

	def __iadd__(self, valuein):
		if self.used:
			if isinstance(valuein, visual_color):
				self.r_f += valuein.r_f
				self.g_f += valuein.g_f
				self.b_f += valuein.b_f
			else:
				self.r_f += valuein
				self.g_f += valuein
				self.b_f += valuein
			self.internal_clamp()
			self.internal_toint()
		return self

	def __sub__(self, valuein):
		obj_copy = copy.copy(self)
		if obj_copy.used:
			if isinstance(valuein, visual_color):
				obj_copy.r_f -= valuein.r_f
				obj_copy.g_f -= valuein.g_f
				obj_copy.b_f -= valuein.b_f
			else:
				obj_copy.r_f -= valuein
				obj_copy.g_f -= valuein
				obj_copy.b_f -= valuein
			obj_copy.internal_clamp()
			obj_copy.internal_toint()
		return obj_copy

	def __isub__(self, valuein):
		if self.used:
			if isinstance(valuein, visual_color):
				self.r_f -= valuein.r_f
				self.g_f -= valuein.g_f
				self.b_f -= valuein.b_f
			else:
				self.r_f -= valuein
				self.g_f -= valuein
				self.b_f -= valuein
			self.internal_clamp()
			self.internal_toint()
		return self

	def __mul__(self, valuein):
		obj_copy = copy.copy(self)
		if obj_copy.used:
			if isinstance(valuein, visual_color):
				obj_copy.r_f *= valuein.r_f
				obj_copy.g_f *= valuein.g_f
				obj_copy.b_f *= valuein.b_f
			else:
				obj_copy.r_f *= valuein
				obj_copy.g_f *= valuein
				obj_copy.b_f *= valuein
			obj_copy.internal_clamp()
			obj_copy.internal_toint()
		return obj_copy

	def __imul__(self, valuein):
		if self.used:
			if isinstance(valuein, visual_color):
				self.r_f *= valuein.r_f
				self.g_f *= valuein.g_f
				self.b_f *= valuein.b_f
			else:
				self.r_f *= valuein
				self.g_f *= valuein
				self.b_f *= valuein
			self.internal_clamp()
			self.internal_toint()
		return self

	def __rtruediv__(self, valuein):
		obj_copy = copy.copy(self)
		if obj_copy.used:
			if isinstance(valuein, visual_color):
				obj_copy.r_f /= valuein.r_f
				obj_copy.g_f /= valuein.g_f
				obj_copy.b_f /= valuein.b_f
			else:
				obj_copy.r_f /= valuein
				obj_copy.g_f /= valuein
				obj_copy.b_f /= valuein
			obj_copy.internal_clamp()
			obj_copy.internal_toint()
		return obj_copy

	def __itruediv__(self, valuein):
		if self.used:
			if isinstance(valuein, visual_color):
				self.r_f /= valuein.r_f
				self.g_f /= valuein.g_f
				self.b_f /= valuein.b_f
			else:
				self.r_f /= valuein
				self.g_f /= valuein
				self.b_f /= valuein
			self.internal_clamp()
			self.internal_toint()
		return self

	def __bool__(self):
		return self.used

	def remove(self):
		self.used = False

	def copy(self):
		return copy.copy(self)

	def get_int(self):
		return [self.r_i, self.g_i, self.b_i] if self.used else None

	def get_float(self):
		return [self.r_f, self.g_f, self.b_f] if self.used else None

	def get_hex(self): 
		return ('#%02x%02x%02x' % (self.r_i, self.g_i, self.b_i)) if self.used else None

	def getbgr_int(self):
		return [self.b_i, self.g_i, self.r_i] if self.used else None

	def getbgr_float(self):
		return [self.b_f, self.g_f, self.r_f] if self.used else None

	def getbgr_hex(self): 
		return ('#%02x%02x%02x' % [self.b_i, self.g_i, self.r_i]) if self.used else None

	def get_hex_fb(self, r, g, b): 
		outcolor = [self.r_i, self.g_i, self.b_i] if self.used else [r, g, b]
		return ('#%02x%02x%02x' % (outcolor[0],outcolor[1],outcolor[2]))

	def internal_clamp(self):
		self.r_f = xtramath.clamp(self.r_f, 0, 1)
		self.g_f = xtramath.clamp(self.g_f, 0, 1)
		self.b_f = xtramath.clamp(self.b_f, 0, 1)

	def internal_tofloat(self):
		self.r_f = self.r_i/255
		self.g_f = self.g_i/255
		self.b_f = self.b_i/255

	def internal_toint(self):
		self.r_i = int(self.r_f*255)
		self.g_i = int(self.g_f*255)
		self.b_i = int(self.b_f*255)

	def set_int(self, indata):
		if indata:
			self.r_i = int(indata[0])
			self.g_i = int(indata[1])
			self.b_i = int(indata[2])
			self.used = True
			self.internal_tofloat()

	def set_float(self, indata):
		if indata:
			self.r_f = indata[0]
			self.g_f = indata[1]
			self.b_f = indata[2]
			self.used = True
			self.internal_toint()

	def set_hex(self, hexcode):
		if hexcode:
			nonumsign = hexcode.lstrip('#')
			self.r_i, self.g_i, self.b_i = tuple(int(nonumsign[i:i+2], 16) for i in (0, 2, 4))
			self.used = True
			self.internal_tofloat()

	def set_hsv(self, h, s, v):
		self.r_f, self.g_f, self.b_f = hsv_to_rgb(h, s, v)
		self.used = True
		self.internal_toint()

	def copy_to_self(self, other_color):
		self.r_i = other_color.r_i
		self.g_i = other_color.g_i
		self.b_i = other_color.b_i
		self.r_f = other_color.r_f
		self.g_f = other_color.g_f
		self.b_f = other_color.b_f
		self.used = other_color.used
		self.fx_allowed = other_color.fx_allowed
		self.priority = other_color.priority

	def merge(self, other_color):
		if other_color: 
			if not self: self.copy_to_self(other_color)
			elif other_color.priority > self.priority and other_color: self.copy_to_self(other_color)

	def fx_saturate(self, amount):
		self *= 1-amount
		self += amount/2

	def fx_pow(self, amount):
		if self.used:
			self.r_f **= amount
			self.g_f **= amount
			self.b_f **= amount
			self.internal_clamp()
			self.internal_toint()