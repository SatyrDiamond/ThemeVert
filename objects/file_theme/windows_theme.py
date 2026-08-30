
from external.easybinrw import easybinrw
import numpy as np


class tagLOGFONTA():
	def __init__(self, ebrw_readstr):
		self.lfHeight = ebrw_readstr.int_s32()
		self.lfWidth = ebrw_readstr.int_s32()
		self.lfEscapement = ebrw_readstr.int_s32()
		self.lfOrientation = ebrw_readstr.int_s32()
		self.lfWeight = ebrw_readstr.int_s32()
		self.lfItalic = ebrw_readstr.int_u8()
		self.lfUnderline = ebrw_readstr.int_u8()
		self.lfStrikeOut = ebrw_readstr.int_u8()
		self.lfCharSet = ebrw_readstr.int_u8()
		self.lfOutPrecision = ebrw_readstr.int_u8()
		self.lfClipPrecision = ebrw_readstr.int_u8()
		self.lfQuality = ebrw_readstr.int_u8()
		self.lfPitchAndFamily = ebrw_readstr.int_u8()

		#print(	self.lfHeight,
		#		self.lfWidth,
		#		self.lfEscapement,
		#		self.lfOrientation,
		#		self.lfWeight,
		#		self.lfItalic,
		#		self.lfUnderline,
		#		self.lfStrikeOut,
		#		self.lfCharSet,
		#		self.lfOutPrecision,
		#		self.lfClipPrecision,
		#		self.lfQuality,
		#		self.lfPitchAndFamily
		#		)
		self.lfFaceName = ebrw_readstr.string_t()
		ebrw_readstr.raw(25)
		#print(self.lfFaceName)

class tagNONCLIENTMETRICS():
	def __init__(self, ebrw_readstr):
		self.cbSize = ebrw_readstr.int_s32()
		self.iBorderWidth = ebrw_readstr.int_s32()
		self.iScrollWidth = ebrw_readstr.int_s32()
		self.iScrollHeight = ebrw_readstr.int_s32()
		self.iCaptionWidth = ebrw_readstr.int_s32()
		self.iCaptionHeight = ebrw_readstr.int_s32()
		self.lfCaptionFont = tagLOGFONTA(ebrw_readstr)
		self.iSmCaptionWidth = ebrw_readstr.int_s32()
		self.iSmCaptionHeight = ebrw_readstr.int_s32()
		self.lfSmCaptionFont = tagLOGFONTA(ebrw_readstr)
		self.iMenuWidth = ebrw_readstr.int_s32()
		self.iMenuHeight = ebrw_readstr.int_s32()
		self.lfMenuFont = tagLOGFONTA(ebrw_readstr)
		self.lfStatusFont = tagLOGFONTA(ebrw_readstr)
		self.lfMessageFont = tagLOGFONTA(ebrw_readstr)

class wintheme():
	def __init__(self):
		self.data = {}
		self.colors = {}

	def read(self, filename):
		f = open(filename, 'rb')
		c = None
		for x in f.readlines():
			x = x.decode('latin1').rstrip().lstrip().split(';')[0]
			if x:
				if x[0]=='[':
					c = x[1:-1]
					d = self.data[c] = {}
				else:
					k, v = x.split('=')
					d[k] = v

		self.NonclientMetrics = None
		if 'Metrics' in self.data:
			if 'NonclientMetrics' in self.data['Metrics']:
				NonclientMetrics = self.data['Metrics']['NonclientMetrics'].split(' ')
				NonclientMetrics = np.array([int(x) for x in NonclientMetrics], np.uint8)

				ebrw_readstr = easybinrw.binread()
				ebrw_readstr.load_data(NonclientMetrics)
		
				self.NonclientMetrics = tagNONCLIENTMETRICS(ebrw_readstr)

		if 'Control Panel\\Colors' in self.data:
			for k, v in self.data['Control Panel\\Colors'].items():
				color = [int(x) for x in v.split(' ')]
				self.colors[k] = color

	def write(self, filename):
		import configparser
		f = open(filename, 'rb')

		config = configparser.ConfigParser()
		config['Control Panel\\Colors'] = self.colors

		with open(filename, 'w') as configfile:
		    config.write(configfile)