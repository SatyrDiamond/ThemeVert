
import fnmatch

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