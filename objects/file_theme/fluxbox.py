
import fnmatch
from functions import color

def doubv(r):
	if len(r)==1: return r+r
	else: return r

def get_color(incolor):
	if incolor.startswith('rgb:'):
		r, g, b = incolor.strip('rgb:').split('/')
		r = int(doubv(r), 16)
		g = int(doubv(g), 16)
		b = int(doubv(b), 16)
		return [r,g,b]
	elif incolor.startswith('#'):
		if len(incolor)!=7: return None
		else: return color.hex_to_int(incolor)
	elif incolor=='white':
		return [255,255,255]
	elif incolor=='grey':
		return [196,196,196]
	elif incolor=='darkgrey':
		return [64,64,64]
	elif incolor=='black':
		return [0,0,0]
	elif incolor.startswith('grey'):
		greyc = (int(incolor.strip('grey'))/100)*255
		return [greyc,greyc,greyc]
	else:
		print('unknown value', incolor)

class fluxbox_theme():
	def __init__(self):
		self.data = {}
		self.data_wildcard = {}

	def read(self, filename):
		f = open(filename, 'r')
		c = None
		for x in f.readlines():
			x = x.strip().rstrip()
			if x:
				if x[0]=='!': continue
				elif x[0]=='#': continue
				else:
					name, val = x.split(':', 1)
					name = name.lower()
					name = name.strip().rstrip()
					val = val.strip().rstrip()

					if '*' not in name:
						self.data[name] = val
					else:
						self.data_wildcard[name] = val

	def get_data(self, name):
		name = name.lower()
		if name in self.data: return self.data[name]
		else:
			out = None
			outs = 0
			for k in self.data_wildcard:
				res = fnmatch.fnmatch(name, k)
				if res: 
					s = len(k)
					if s>outs: out = self.data_wildcard[k]
			return out