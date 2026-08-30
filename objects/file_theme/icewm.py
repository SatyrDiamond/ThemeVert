
from external.easybinrw import easybinrw

class icewm_theme():
	def __init__(self):
		self.data = {}

	def read(self, filename):
		f = open(filename, 'r')
		c = None
		for x in f.readlines():
			x = x.strip().rstrip()
			if x:
				if x[0]!='#':
					name, val = x.split('=', 1)
					name = name.strip().rstrip()
					val = val.strip().rstrip()
					if val:
						valtype = None
						if val[0]=='"' and val[-1]=='"':
							valtype = 'string'
							val = val[1:-1]
						elif val.lstrip('-').isdigit(): valtype = 'number'
						else: valtype = 'type'
						self.data[name] = [valtype, val]

	def write(self, filename):
		f = open(filename, 'w')
		for k, v in self.data.items():
			valtype, val = v
			if valtype=='string': f.write(k+'="'+str(val)+'"'+'\n')
			else: f.write(k+'='+str(val)+'\n')
