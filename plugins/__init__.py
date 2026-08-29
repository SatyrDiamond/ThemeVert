import os
import traceback
import glob
import logging
from importlib import util
from external.easybinrw import easybinrw

logger_plugins = logging.getLogger('plugins')

class dv_plugin:
	def __init__(self):
		self.name = ""
		self.shortname = ""
		self.type = ""
		self.prop = {}

	#def propproc(self):
	#	if self.type in ['input','output']:
	#		propobj = info_themapp()
	#		propobj.from_dict(self.prop)
	#		self.prop_obj = propobj

class plugin_selector:
	def __init__(self, plugintype, loaded_plugins):
		self.selected_shortname = None
		self.selected_plugin = None
		self.plugintype = plugintype
		self.pluginlist = loaded_plugins

	def unset(self):
		if self.selected_plugin:
			self.selected_shortname = None
			self.selected_plugin = None
			logger_plugins.info('Unset '+self.plugintype+' plugin')

	def set(self, dvplugsn):
		if self.plugintype in self.pluginlist:
			if self.selected_shortname != dvplugsn:
				if dvplugsn in self.pluginlist[self.plugintype]:
					self.selected_shortname = dvplugsn
					self.selected_plugin = self.pluginlist[self.plugintype][dvplugsn]
					logger_plugins.info('Set '+self.plugintype+' plugin: '+self.selected_shortname+' ('+ self.selected_plugin.name+')')
					return dvplugsn
			else:
				return dvplugsn

	def set_auto(self, indata):
		outname = self.set_auto_keepset(indata)
		if not outname: self.unset()
		return outname

	def set_auto_keepset(self, inpath):
		if self.plugintype in self.pluginlist:

			d_containers = {}
			d_non_containers = []

			outd = [(shortname, dvplugin.detectdef) for shortname, dvplugin in self.pluginlist[self.plugintype].items() if dvplugin.detectdef.used]

			outname = None

			for shortname, detectdef_obj in outd:
				try:
					detectf = detectdef_obj.detect_container__file(inpath)
					if detectf: outname = shortname
					elif not detectdef_obj.container_only:
						ddd = detectdef_obj.detect_headers__file(inpath)
						if ddd: 
							outname = shortname
				except:
					pass

			if outname:
				self.selected_shortname = outname
				self.selected_plugin = self.pluginlist[self.plugintype][outname]
				logger_plugins.info('Auto-Set '+self.plugintype+' plugin from data: '+self.selected_shortname+' ('+ self.selected_plugin.name+')')
				return outname

	def get_prop_obj(self):
		return self.selected_plugin.prop_obj if self.selected_plugin else None

	def iter(self):
		plugqueue = []

		if self.plugintype in self.pluginlist:
			for shortname, dvplugin in self.pluginlist[self.plugintype].items():
				plugqueue.append((dvplugin.priority, shortname, dvplugin))

		plugqueue.sort()

		for priority, shortname, dvplugin in plugqueue: 
			yield shortname, dvplugin.plug_obj, dvplugin.prop_obj

	def iter_noorder(self):
		if self.plugintype in self.pluginlist:
			for shortname, dvplugin in self.pluginlist[self.plugintype].items():
				yield shortname, dvplugin.plug_obj, dvplugin.prop_obj

	def iter_dvp(self):
		if self.plugintype in self.pluginlist:
			for shortname, dvplugin in self.pluginlist[self.plugintype].items():
				yield shortname, dvplugin


class base:
	loaded_plugins = {}

	noname_num = 0

	def __init_subclass__(plcv_obj, **kwargs):
		super().__init_subclass__(**kwargs)
		in_object = plcv_obj()
		plugintype = in_object.is_themeconv_plugin()

		try:
			if plugintype not in base.loaded_plugins: base.loaded_plugins[plugintype] = {}
			dvplug_obj = dv_plugin()
			if 'get_shortname' in dir(in_object): 
				dvplug_obj.shortname = in_object.get_shortname()
			else: 
				dvplug_obj.shortname = 'noname_'+str(base.noname_num)
				base.noname_num += 1

			dvplug_obj.prop = in_object.get_prop()

			if dvplug_obj.shortname not in base.loaded_plugins:
				dvplug_obj.type = plugintype
				dvplug_obj.plug_obj = in_object
				if 'get_name' in dir(in_object): dvplug_obj.name = in_object.get_name()
				#dvplug_obj.propproc()
				base.loaded_plugins[plugintype][dvplug_obj.shortname] = dvplug_obj

		except: 
			traceback.print_exc()
			pass

	def create_selector(plug_type):
		selector_obj = plugin_selector(plug_type, base.loaded_plugins)
		return selector_obj

	def iter_list(plug_type):
		if plug_type in base.loaded_plugins:
			for x in base.loaded_plugins[plug_type].items():
				yield x

	def get_list(plug_type):
		return list(base.loaded_plugins[plug_type]) if plug_type in base.loaded_plugins else []

	def get_list_names(plug_type):
		return [n.name for _, n in base.loaded_plugins[plug_type].items()] if plug_type in base.loaded_plugins else []

	def get_list_prop_obj(plug_type):
		return [n.prop_obj for _, n in base.loaded_plugins[plug_type].items()] if plug_type in base.loaded_plugins else []

	def load_plugindir(plug_type, plugsetname):
		if plug_type in base.loaded_plugins: del base.loaded_plugins[plug_type]
		plugfolder = plug_type + ('_'+plugsetname if plugsetname else '')
		plugincount = 0
		for filename in glob.iglob(dirpath + '**/'+plugfolder+'/*.py', recursive=True):
			if not filename.startswith('.') and \
				not filename.endswith('__init__.py') and filename.endswith('.py'):
				try: 
					load_module(os.path.join(dirpath, filename))
					plugincount += 1
				except: 
					traceback.print_exc()
		if plug_type in base.loaded_plugins: 
			base.loaded_plugins[plug_type] = dict(sorted(base.loaded_plugins[plug_type].items()))
		logger_plugins.info('Loaded '+str(plugincount)+' '+plug_type+' Plugins.')

	def extplug_exists(pluginname, exttypes, subname):
		if 'extplugin' in base.loaded_plugins:
			if pluginname in base.loaded_plugins['extplugin']:
				plugd = base.loaded_plugins['extplugin'][pluginname]
				plugsup = plugd.plug_obj.check_exists(subname)
				for exttype in exttypes:
					if exttype in plugsup: return exttype
		return None

def load_module(path):
	name = os.path.split(path)[-1]
	spec = util.spec_from_file_location(name, path)
	module = util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module


# Get current path
path = os.path.abspath(__file__)
dirpath = os.path.dirname(path)
