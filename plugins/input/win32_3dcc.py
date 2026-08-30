
import plugins
import struct

class input_plug(plugins.base):
	def is_themeconv_plugin(self):
		return 'input'
	
	def get_shortname(self):
		return '3dcc'
	
	def get_name(self):
		return '[Win32] 3DCC'
	
	def get_prop(self):
		prop = {}
		prop['supported_types'] = ['win32']
		return prop
	
	def parse(self, theme_obj, themeverter_intent):
		theme_obj.supported_types.append('win32')
		win32_colors = theme_obj.colors_win32

		f = open(themeverter_intent.input_file, 'r')

		for n in range(31):
			num = int(f.readline().strip())

			col = struct.pack('I', num)
			col = struct.unpack('BBBB', col)[0:3]

			if n==0: win32_colors.set('Scrollbar', col)
			if n==1: win32_colors.set('Background', col)
			if n==2: win32_colors.set('ActiveTitle', col)
			if n==3: win32_colors.set('InactiveTitle', col)
			if n==4: win32_colors.set('Menu', col)
			if n==5: win32_colors.set('Window', col)
			if n==6: win32_colors.set('WindowFrame', col)
			if n==7: win32_colors.set('MenuText', col)
			if n==8: win32_colors.set('WindowText', col)
			if n==9: win32_colors.set('TitleText', col)
			if n==10: win32_colors.set('ActiveBorder', col)
			if n==11: win32_colors.set('InactiveBorder', col)
			if n==12: win32_colors.set('AppWorkspace', col)
			if n==13: win32_colors.set('Hilight', col)
			if n==14: win32_colors.set('HilightText', col)
			if n==15: win32_colors.set('ButtonFace', col)
			if n==16: win32_colors.set('ButtonShadow', col)
			if n==17: win32_colors.set('GrayText', col)
			if n==18: win32_colors.set('ButtonText', col)
			if n==19: win32_colors.set('InactiveTitleText', col)
			if n==20: win32_colors.set('ButtonHilight', col)
			if n==21: win32_colors.set('ButtonDkShadow', col)
			if n==22: win32_colors.set('ButtonLight', col)
			if n==23: win32_colors.set('InfoText', col)
			if n==24: win32_colors.set('InfoWindow', col)
			if n==25: win32_colors.set('ButtonAlternateFace', col)
			if n==26: win32_colors.set('HotTrackingColor', col)
			if n==27: win32_colors.set('GradientActiveTitle', col)
			if n==28: win32_colors.set('GradientInactiveTitle', col)
			if n==29: win32_colors.set('MenuHilight', col)
			if n==30: win32_colors.set('MenuBar', col)