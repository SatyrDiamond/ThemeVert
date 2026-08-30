
from plugins import base as dv_plugins
from objects import tuxtheme
import os

pluginsets_input = {
'main': ['', 'Main'],
'apps': ['apps', 'Apps']
}

pluginsets_output = {
'main': ['', 'Main']
}

class themeverter_intent:
	def __init__(self):
		self.curdir = None

		self.input_file = ''
		self.input_folder = ''
		self.input_data = b''
		self.input_mode = 'file'
		self.input_visname = ''
		self.input_params = {}
		
		self.output_file = ''
		self.output_folder = ''
		self.output_mode = 'file'
		self.output_params = {}
		self.output_visname = ''
		self.output_samples = ''

	def copy(self):
		return copy.deepcopy(self)

	def set_file_input(self, fileloc):
		if self.curdir: self.curdir = os.getcwd()
		self.input_mode = 'file'
		self.input_file = os.path.abspath(fileloc)
		self.input_folder = os.path.dirname(self.input_file)
		self.input_visname = os.path.basename(fileloc)
		self.input_visname = os.path.splitext(self.input_visname)[0]

	def set_file_output(self, fileloc):
		if self.curdir: self.curdir = os.getcwd()
		self.output_mode = 'file'
		self.output_file = os.path.abspath(fileloc)
		self.output_folder = os.path.dirname(self.output_file)
		self.output_visname = os.path.basename(fileloc)
		self.output_visname = os.path.splitext(self.output_visname)[0]

class core:
	def __init__(self):
		self.currentplug_input = dv_plugins.create_selector('input')
		self.currentplug_output = dv_plugins.create_selector('output')
		self.cur_plugset_input = ''
		self.cur_plugset_output = ''
		self.debug = False

	def input_load_plugins(self, pluginset):
		if pluginset in pluginsets_input: 
			plugsetfolder, fullname = pluginsets_input[pluginset]
			dv_plugins.load_plugindir('input', plugsetfolder)
		else: dv_plugins.load_plugindir('input', '')

	def input_get_pluginsets(self): return list(pluginsets_input)

	def input_get_pluginsets_names(self): return [n[1] for _, n in pluginsets_input.items()]

	def input_get_pluginsets_index(self, num): return list(pluginsets_input)[num]

	def input_get_plugins(self): return dv_plugins.get_list('input')

	def input_iter_plugins(self): return dv_plugins.iter_list('input')

	def input_get_plugins_names(self): return dv_plugins.get_list_names('input')

	def input_get_plugins_props(self): return dv_plugins.get_list_prop_obj('input')

	def input_get_plugins_index(self, num): 
		pluglist = dv_plugins.get_list('input')
		if num != -1:
			if (len(pluglist)-1)>=num: return pluglist[min(num, len(pluglist)-1)]
			else: return None
		else:
			return None

	def input_get_plugins_auto(self): return dv_plugins.get_list_detect('input')

	def input_get_current(self): return self.currentplug_input.selected_shortname

	def input_get_current_name(self): return self.currentplug_input.selected_plugin.name if self.currentplug_input.selected_plugin else 'None'

	def input_set(self, pluginname): 
		return self.currentplug_input.set(pluginname)

	def input_unset(self, pluginname): 
		return self.currentplug_input.unset()

	def output_load_plugins(self, pluginset):
		if pluginset in pluginsets_output: 
			plugsetfolder, fullname = pluginsets_output[pluginset]
			dv_plugins.load_plugindir('output', plugsetfolder)
		else: dv_plugins.load_plugindir('output', '')

	def output_get_plugins(self): return dv_plugins.get_list('output')

	def output_iter_plugins(self): return dv_plugins.iter_list('output')

	def output_get_plugins_names(self): return dv_plugins.get_list_names('output')

	def output_get_plugins_props(self): return dv_plugins.get_list_prop_obj('output')

	def output_get_plugins_index(self, num):
		pluglist = dv_plugins.get_list('output')
		if num != -1:
			if (len(pluglist)-1)>=num: return pluglist[min(num, len(pluglist)-1)]
			else: return None
		else:
			return None

	def output_get_pluginsets(self): return list(pluginsets_output)

	def output_get_pluginsets_index(self, num): return list(pluginsets_output)[num]

	def output_get_pluginsets_names(self): return [n[1] for _, n in pluginsets_output.items()]

	def output_get_current(self): return self.currentplug_output.selected_shortname

	def output_get_current_name(self): return self.currentplug_output.selected_plugin.name if self.currentplug_output.selected_plugin else 'None'

	def output_set(self, pluginname): return self.currentplug_output.set(pluginname)

	def parse_input(self, themeverter_intent): 
		self.theme_obj = tuxtheme.data_theme()
		selected_plugin = self.currentplug_input.selected_plugin
		plug_obj = selected_plugin.plug_obj
		plug_obj.parse(self.theme_obj, themeverter_intent)
		if self.debug: self.theme_obj.to_xml('debug_in.xml')
		colors_win32 = self.theme_obj.colors_win32
		colors_gtk = self.theme_obj.colors_gtk
		colors_win32.import_colors(self.theme_obj)
		colors_gtk.import_colors(self.theme_obj)

		if self.debug: self.theme_obj.complete_incomplete()
		
		colors_win32.export_colors(self.theme_obj)
		colors_gtk.export_colors(self.theme_obj)
		if self.debug: self.theme_obj.to_xml('debug_mid.xml')

	def parse_output(self, themeverter_intent): 
		plug_obj = self.currentplug_output.selected_plugin.plug_obj
		plug_obj.parse(self.theme_obj, themeverter_intent)
		#logger_core.info('File outputted: '+out_file)
		if self.debug: self.theme_obj.to_xml('debug_out.xml')