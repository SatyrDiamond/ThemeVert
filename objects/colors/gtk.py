
import xml.etree.ElementTree as ET
from objects import visual
from functions import color as colorfunc

class colors_gtk():
	__slots__ = ['used', 'base_color', 'text_color', 'bg_color', 'fg_color', 'error_bg_color', 'error_color', 'error_fg_color', 'inactive_fg_color', 'inactive_text_color', 'info_bg_color', 'info_fg_color', 'other_bg_color', 'other_fg_color', 'question_bg_color', 'question_fg_color', 'selected_base_color', 'selected_bg_color', 'selected_fg_color', 'selected_text_color', 'tooltip_color', 'url_color', 'visited_url_color', 'warning_bg_color', 'warning_fg_color']

	def __init__(self):
		self.used = False

		self.base_color = visual.visual_color()
		self.text_color = visual.visual_color()
		self.bg_color = visual.visual_color()
		self.fg_color = visual.visual_color()
		self.error_bg_color = visual.visual_color()
		self.error_color = visual.visual_color()
		self.error_fg_color = visual.visual_color()
		self.inactive_fg_color = visual.visual_color()
		self.inactive_text_color = visual.visual_color()
		self.info_bg_color = visual.visual_color()
		self.info_fg_color = visual.visual_color()
		self.other_bg_color = visual.visual_color()
		self.other_fg_color = visual.visual_color()
		self.question_bg_color = visual.visual_color()
		self.question_fg_color = visual.visual_color()
		self.selected_base_color = visual.visual_color()
		self.selected_bg_color = visual.visual_color()
		self.selected_fg_color = visual.visual_color()
		self.selected_text_color = visual.visual_color()
		self.tooltip_color = visual.visual_color()
		self.url_color = visual.visual_color()
		self.visited_url_color = visual.visual_color()
		self.warning_bg_color = visual.visual_color()
		self.warning_fg_color = visual.visual_color()

	def set(self, c, v):
		if v:
			self.used = True
			match c.lower():
				case 'base_color': self.base_color.set_int(v)
				case 'text_color': self.text_color.set_int(v)
				case 'bg_color': self.bg_color.set_int(v)
				case 'fg_color': self.fg_color.set_int(v)
				case 'error_bg_color': self.error_bg_color.set_int(v)
				case 'error_color': self.error_color.set_int(v)
				case 'error_fg_color': self.error_fg_color.set_int(v)
				case 'inactive_fg_color': self.inactive_fg_color.set_int(v)
				case 'inactive_text_color': self.inactive_text_color.set_int(v)
				case 'info_bg_color': self.info_bg_color.set_int(v)
				case 'info_fg_color': self.info_fg_color.set_int(v)
				case 'other_bg_color': self.other_bg_color.set_int(v)
				case 'other_fg_color': self.other_fg_color.set_int(v)
				case 'question_bg_color': self.question_bg_color.set_int(v)
				case 'question_fg_color': self.question_fg_color.set_int(v)
				case 'selected_base_color': self.selected_base_color.set_int(v)
				case 'selected_bg_color': self.selected_bg_color.set_int(v)
				case 'selected_fg_color': self.selected_fg_color.set_int(v)
				case 'selected_text_color': self.selected_text_color.set_int(v)
				case 'tooltip_color': self.tooltip_color.set_int(v)
				case 'url_color': self.url_color.set_int(v)
				case 'visited_url_color': self.visited_url_color.set_int(v)
				case 'warning_bg_color': self.warning_bg_color.set_int(v)
				case 'warning_fg_color': self.warning_fg_color.set_int(v)
				case _: print('unknown color type', c)

	def to_xml(self, part, name):

		def xml_write(part, name, color):
			if color:
				part.set(name, colorfunc.writestr(color) )

		if self.used:
			part = ET.SubElement(part, name)
			xml_write(part, 'base_color', self.base_color)
			xml_write(part, 'text_color', self.text_color)
			xml_write(part, 'bg_color', self.bg_color)
			xml_write(part, 'fg_color', self.fg_color)
			xml_write(part, 'error_bg_color', self.error_bg_color)
			xml_write(part, 'error_color', self.error_color)
			xml_write(part, 'error_fg_color', self.error_fg_color)
			xml_write(part, 'inactive_fg_color', self.inactive_fg_color)
			xml_write(part, 'inactive_text_color', self.inactive_text_color)
			xml_write(part, 'info_bg_color', self.info_bg_color)
			xml_write(part, 'info_fg_color', self.info_fg_color)
			xml_write(part, 'other_bg_color', self.other_bg_color)
			xml_write(part, 'other_fg_color', self.other_fg_color)
			xml_write(part, 'question_bg_color', self.question_bg_color)
			xml_write(part, 'question_fg_color', self.question_fg_color)
			xml_write(part, 'selected_base_color', self.selected_base_color)
			xml_write(part, 'selected_bg_color', self.selected_bg_color)
			xml_write(part, 'selected_fg_color', self.selected_fg_color)
			xml_write(part, 'selected_text_color', self.selected_text_color)
			xml_write(part, 'tooltip_color', self.tooltip_color)
			xml_write(part, 'url_color', self.url_color)
			xml_write(part, 'visited_url_color', self.visited_url_color)
			xml_write(part, 'warning_bg_color', self.warning_bg_color)
			xml_write(part, 'warning_fg_color', self.warning_fg_color)

	def import_colors(self, theme_obj):

		def globalcolor_add(name, color):
			if color:
				theme_obj.add_global_color('gtk__'+name, color.get_int() )
				return True
			return False

		if self.used == True and 'basic' not in theme_obj.supported_types:
			theme_obj.supported_types.append('basic')

			curstyle = theme_obj.style_global

			theme_obj.add_stylecontrol('tooltip')
			theme_obj.add_stylecontrol('infobar_error')
			theme_obj.add_stylecontrol('infobar_warning')
			theme_obj.add_stylecontrol('infobar_info')
			theme_obj.add_stylecontrol('infobar_question')
			theme_obj.add_stylecontrol('infobar_other')

			if globalcolor_add('base_color', self.base_color): 
				theme_obj.add_color_named(None, 'main:edit_bg', 'gtk__base_color')
			if globalcolor_add('text_color', self.text_color): 
				theme_obj.add_color_named(None, 'main:edit_fg', 'gtk__text_color')
				theme_obj.add_color_named(None, 'main:edit_font_fg', 'gtk__text_color')

			if globalcolor_add('bg_color', self.bg_color): 
				theme_obj.add_color_named(None, 'main:control_bg', 'gtk__bg_color')
			if globalcolor_add('fg_color', self.fg_color): 
				theme_obj.add_color_named(None, 'main:control_fg', 'gtk__fg_color')
				theme_obj.add_color_named(None, 'main:control_font_fg', 'gtk__fg_color')

			if globalcolor_add('selected_bg_color', self.selected_bg_color): 
				theme_obj.add_color_named(None, 'selected:control_bg', 'gtk__selected_bg_color')
			if globalcolor_add('selected_fg_color', self.selected_fg_color): 
				theme_obj.add_color_named(None, 'selected:control_fg', 'gtk__selected_fg_color')
				theme_obj.add_color_named(None, 'selected:control_font_fg', 'gtk__selected_fg_color')

			if globalcolor_add('selected_base_color', self.selected_base_color): 
				theme_obj.add_color_named(None, 'main:edit_bg_selected', 'gtk__selected_base_color')
			if globalcolor_add('selected_text_color', self.selected_text_color): 
				theme_obj.add_color_named(None, 'main:edit_fg_selected', 'gtk__selected_text_color')
				theme_obj.add_color_named(None, 'main:edit_font_fg_selected', 'gtk__selected_text_color')

			if globalcolor_add('inactive_fg_color', self.inactive_fg_color): 
				theme_obj.add_color_named(None, 'inactive:control_fg', 'gtk__inactive_fg_color')
			if globalcolor_add('inactive_text_color', self.inactive_text_color): 
				theme_obj.add_color_named(None, 'inactive:edit_fg', 'gtk__inactive_text_color')
				theme_obj.add_color_named(None, 'inactive:edit_font_fg', 'gtk__inactive_text_color')

			if globalcolor_add('url_color', self.url_color): 
				theme_obj.add_color_named(None, 'main:edit_fg_url', 'gtk__url_color')
				theme_obj.add_color_named(None, 'main:edit_font_fg_url', 'gtk__url_color')
			if globalcolor_add('visited_url_color', self.visited_url_color): 
				theme_obj.add_color_named(None, 'main:edit_fg_url_visited', 'gtk__visited_url_color')
				theme_obj.add_color_named(None, 'main:edit_font_fg_url_visited', 'gtk__visited_url_color')

			if globalcolor_add('tooltip_color', self.tooltip_color): 
				theme_obj.add_color_named('tooltip', 'main:control_bg', 'gtk__tooltip_color')

			if globalcolor_add('error_bg_color', self.error_bg_color): 
				theme_obj.add_color_named('infobar_error', 'main:control_bg', 'gtk__error_bg_color')
			if globalcolor_add('error_fg_color', self.error_fg_color): 
				theme_obj.add_color_named('infobar_error', 'main:control_fg', 'gtk__error_fg_color')
				theme_obj.add_color_named('infobar_error', 'main:control_font_fg', 'gtk__error_fg_color')

			if globalcolor_add('warning_bg_color', self.warning_bg_color): 
				theme_obj.add_color_named('infobar_warning', 'main:control_bg', 'gtk__warning_bg_color')
			if globalcolor_add('warning_fg_color', self.warning_fg_color): 
				theme_obj.add_color_named('infobar_warning', 'main:control_fg', 'gtk__warning_fg_color')
				theme_obj.add_color_named('infobar_warning', 'main:control_font_fg', 'gtk__warning_fg_color')

			if globalcolor_add('info_bg_color', self.info_bg_color): 
				theme_obj.add_color_named('infobar_info', 'main:control_bg', 'gtk__info_bg_color')
			if globalcolor_add('info_fg_color', self.info_fg_color): 
				theme_obj.add_color_named('infobar_info', 'main:control_fg', 'gtk__info_fg_color')
				theme_obj.add_color_named('infobar_info', 'main:control_font_fg', 'gtk__info_fg_color')

			if globalcolor_add('question_bg_color', self.question_bg_color): 
				theme_obj.add_color_named('infobar_question', 'main:control_bg', 'gtk__question_fg_color')
			if globalcolor_add('question_fg_color', self.question_fg_color): 
				theme_obj.add_color_named('infobar_question', 'main:control_fg', 'gtk__question_fg_color')
				theme_obj.add_color_named('infobar_question', 'main:control_font_fg', 'gtk__question_fg_color')

			if globalcolor_add('other_bg_color', self.other_bg_color): 
				theme_obj.add_color_named('infobar_other', 'main:control_bg', 'gtk__other_bg_color')
			if globalcolor_add('other_fg_color', self.other_fg_color): 
				theme_obj.add_color_named('infobar_other', 'main:control_fg', 'gtk__other_fg_color')
				theme_obj.add_color_named('infobar_other', 'main:control_font_fg', 'gtk__other_fg_color')
			
			globalcolor_add('error_color', self.error_color)

	def export_colors(self, theme_obj):

		if self.used == False and 'gtk' not in theme_obj.supported_types:
			theme_obj.supported_types.append('gtk')

			globalstyle = theme_obj.style_global
			
			ctrl_main_bg = theme_obj.get_color_rgb(None, 'main:control_bg')
			ctrl_main_fg = theme_obj.get_color_rgb(None, 'main:control_fg')
			self.set('base_color', ctrl_main_bg.get_int() )
			self.set('text_color', ctrl_main_fg.get_int() )

			text_main_bg = theme_obj.get_color_rgb(None, 'main:edit_bg')
			text_main_fg = theme_obj.get_color_rgb(None, 'main:edit_fg')
			self.set('bg_color', ctrl_main_bg.get_int() )
			self.set('fg_color', ctrl_main_fg.get_int() )

			text_sel_bg = theme_obj.get_color_rgb(None, 'main:edit_bg_selected')
			text_sel_fg = theme_obj.get_color_rgb(None, 'main:edit_fg_selected')
			self.set('selected_bg_color', text_sel_bg.get_int() )
			self.set('selected_fg_color', text_sel_fg.get_int() )