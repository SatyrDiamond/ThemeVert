
import fnmatch
from functions import color

# ====================================== OPENBOX ======================================

openbox_valtypes = {
	'_root': {
		"border.color": "single_color",
		"border.width": "number",
		"menu.border.color": "single_color",
		"menu.border.width": "number",
		"menu.items.active.bg>": "openbox_texture",
		"menu.items.active.disabled.text.color": "single_color",
		"menu.items.active.text.color": "single_color",
		"menu.items.bg>": "openbox_texture",
		"menu.items.disabled.text.color": "single_color",
		"menu.items.font": "openbox_font",
		"menu.items.text.color": "single_color",
		"menu.overlap": "number",
		"menu.overlap.x": "number",
		"menu.overlap.y": "number",
		"menu.separator.color": "single_color",
		"menu.separator.padding.height": "number",
		"menu.separator.padding.width": "number",
		"menu.separator.width": "number",
		"menu.title.bg>": "openbox_texture",
		"menu.title.text.color": "single_color",
		"menu.title.text.font": "openbox_font",
		"menu.title.text.justify": "align",
		"padding.height": "number",
		"padding.width": "number",
		"window.active.border.color": "single_color",
		"window.active.button.disabled.bg>": "openbox_texture",
		"window.active.button.disabled.image.color": "single_color",
		"window.active.button.hover.bg>": "openbox_texture",
		"window.active.button.hover.image.color": "single_color",
		"window.active.button.pressed.bg>": "openbox_texture",
		"window.active.button.pressed.image.color": "single_color",
		"window.active.button.toggled.hover.bg>": "openbox_texture",
		"window.active.button.toggled.hover.image.color": "single_color",
		"window.active.button.toggled.pressed.bg>": "openbox_texture",
		"window.active.button.toggled.pressed.image.color": "single_color",
		"window.active.button.toggled.unpressed.bg>": "openbox_texture",
		"window.active.button.toggled.unpressed.image.color": "single_color",
		"window.active.button.unpressed.bg>": "openbox_texture",
		"window.active.button.unpressed.image.color": "single_color",
		"window.active.client.color": "single_color",
		"window.active.grip.bg>": "openbox_texture",
		"window.active.handle.bg>": "openbox_texture",
		"window.active.label.bg>": "openbox_texture",
		"window.active.label.text.color": "single_color",
		"window.active.label.text.font": "openbox_font",
		"window.active.title.bg>": "openbox_texture",
		"window.client.padding.height": "number",
		"window.client.padding.width": "number",
		"window.handle.width": "number",
		"window.inactive.border.color": "single_color",
		"window.inactive.button.disabled.bg>": "openbox_texture",
		"window.inactive.button.disabled.image.color": "single_color",
		"window.inactive.button.hover.bg>": "openbox_texture",
		"window.inactive.button.hover.image.color": "single_color",
		"window.inactive.button.pressed.bg>": "openbox_texture",
		"window.inactive.button.pressed.image.color": "single_color",
		"window.inactive.button.pressed.toggled.image.color": "single_color",
		"window.inactive.button.toggled.bg>": "openbox_texture",
		"window.inactive.button.toggled.hover.bg>": "openbox_texture",
		"window.inactive.button.toggled.hover.image.color": "single_color",
		"window.inactive.button.toggled.image.color": "single_color",
		"window.inactive.button.toggled.pressed.bg>": "openbox_texture",
		"window.inactive.button.toggled.unpressed.bg>": "openbox_texture",
		"window.inactive.button.toggled.unpressed.image.color": "single_color",
		"window.inactive.button.unpressed.bg>": "openbox_texture",
		"window.inactive.button.unpressed.image.color": "single_color",
		"window.inactive.client.color": "single_color",
		"window.inactive.grip.bg>": "openbox_texture",
		"window.inactive.handle.bg>": "openbox_texture",
		"window.inactive.label.bg>": "openbox_texture",
		"window.inactive.label.text.color": "single_color",
		"window.inactive.label.text.font": "openbox_font",
		"window.inactive.title.bg>": "openbox_texture",
		"window.label.text.justify": "align",
	},
	'openbox_texture': {
		'_root': "string",
		'color': "single_color",
		'color.splitto': "single_color",
		'colorto': "single_color",
		'colorto.splitto': "single_color",
		'border.color': "single_color",
		'highlight': "number",
		'interlace.color': "single_color",
		'shadow': "number",
	}
}

openbox_defaults = {
	'_root': {
		"border.color": [False, "black"],
		"border.width": [False, "1"],
		"menu.border.color": [True, "window.active.border.color"],
		"menu.border.width": [True, "border.width"],
#		"menu.items.active.bg": [False, "none"],
		"menu.items.active.disabled.text.color": [True, "menu.items.disabled.text.color"],
		"menu.items.active.text.color": [False, "black"],
#		"menu.items.bg": [False, "none"],
		"menu.items.disabled.text.color": [False, "black"],
#		"menu.items.font": [False, "no shadow"],
		"menu.items.text.color": [False, "white"],
		"menu.overlap": [False, "0"],
		"menu.overlap.x": [True, "menu.overlap"],
		"menu.overlap.y": [True, "menu.overlap"],
		"menu.separator.color": [True, "menu.items.text.color"],
		"menu.separator.padding.height": [False, "3"],
		"menu.separator.padding.width": [False, "6"],
		"menu.separator.width": [False, "1"],
#		"menu.title.bg": [False, "none"],
		"menu.title.text.color": [False, "black"],
#		"menu.title.text.font": [False, "no shadow"],
		"menu.title.text.justify": [False, "left"],
		"osd.bg": [True, "window.active.title.bg"],
		"osd.border.color": [True, "window.active.border.color"],
		"osd.border.width": [True, "border.width"],
		"osd.hilight.bg": [True, "window.active.label.bg"],
		"osd.hilight.bg.color": [False, "black"],
		"osd.label.bg": [True, "window.active.label.bg"],
		"osd.label.text.color": [False, "black"],
#		"osd.label.text.font": [False, "no shadow"],
		"osd.unhilight.bg": [True, "window.inactive.label.bg"],
		"osd.unhilight.bg.color": [False, "black"],
		"padding.height": [True, "padding.width"],
		"padding.width": [False, "3"],
		"window.active.border.color": [True, "border.color"],
#		"window.active.button.disabled.bg": [False, "none"],
		"window.active.button.disabled.image.color": [False, "white"],
		"window.active.button.hover.bg": [True, "window.active.button.unpressed.bg"],
		"window.active.button.hover.image.color": [True, "window.active.button.unpressed.image.color"],
#		"window.active.button.pressed.bg": [False, "none"],
		"window.active.button.pressed.image.color": [True, "window.active.button.unpressed.image.color"],
		"window.active.button.toggled.bg": [True, "window.active.button.pressed.bg"],
		"window.active.button.toggled.hover.bg": [True, "window.active.button.toggled.unpressed.bg"],
		"window.active.button.toggled.hover.image.color": [True, "window.active.button.toggled.unpressed.image.color"],
		"window.active.button.toggled.image.color": [True, "window.active.button.pressed.image.color"],
		"window.active.button.toggled.pressed.bg": [True, "window.active.button.pressed.bg"],
		"window.active.button.toggled.pressed.image.color": [True, "window.active.button.pressed.image.color"],
		"window.active.button.toggled.unpressed.bg": [True, "window.active.button.toggled.bg"],
		"window.active.button.toggled.unpressed.image.color": [True, "window.active.button.toggled.image.color"],
#		"window.active.button.unpressed.bg": [False, "none"],
		"window.active.button.unpressed.image.color": [False, "black"],
		"window.active.client.color": [False, "white"],
#		"window.active.grip.bg": [False, "none"],
#		"window.active.handle.bg": [False, "none"],
#		"window.active.label.bg": [False, "none"],
		"window.active.label.text.color": [False, "black"],
#		"window.active.label.text.font": [False, "no shadow"],
#		"window.active.title.bg": [False, "none"],
		"window.active.title.separator.color": [True, "window.active.border.color"],
		"window.client.padding.height": [True, "window.client.padding.width"],
		"window.client.padding.width": [True, "padding.width"],
		"window.handle.width": [False, "6"],
		"window.inactive.border.color": [True, "window.active.border.color"],
#		"window.inactive.button.disabled.bg": [False, "none"],
		"window.inactive.button.disabled.image.color": [False, "black"],
		"window.inactive.button.hover.bg": [True, "window.inactive.button.unpressed.bg"],
		"window.inactive.button.hover.image.color": [True, "window.inactive.button.unpressed.image.color"],
#		"window.inactive.button.pressed.bg": [False, "none"],
		"window.inactive.button.pressed.image.color": [True, "window.inactive.button.unpressed.image.color"],
		"window.inactive.button.toggled.bg": [True, "window.inactive.button.pressed.bg"],
		"window.inactive.button.toggled.hover.bg": [True, "window.inactive.button.toggled.unpressed.bg"],
		"window.inactive.button.toggled.hover.image.color": [True, "window.inactive.button.toggled.unpressed.image.color"],
		"window.inactive.button.toggled.image.color": [True, "window.active.button.pressed.image.color"],
		"window.inactive.button.toggled.pressed.bg": [True, "window.inactive.button.pressed.bg"],
		"window.inactive.button.toggled.pressed.image.color": [True, "window.inactive.button.pressed.image.color"],
		"window.inactive.button.toggled.unpressed.bg": [True, "window.inactive.button.toggled.bg"],
		"window.inactive.button.toggled.unpressed.image.color": [True, "window.inactive.button.toggled.image.color"],
#		"window.inactive.button.unpressed.bg": [False, "none"],
		"window.inactive.button.unpressed.image.color": [False, "white"],
		"window.inactive.client.color": [False, "white"],
#		"window.inactive.grip.bg": [False, "none"],
#		"window.inactive.handle.bg": [False, "none"],
#		"window.inactive.label.bg": [False, "none"],
		"window.inactive.label.text.color": [False, "white"],
#		"window.inactive.label.text.font": [False, "no shadow"],
#		"window.inactive.title.bg": [False, "none"],
		"window.inactive.title.separator.color": [True, "window.inactive.border.color"],
		"window.label.text.justify": [False, "left"]
	}
}

openbox_casereplace = [
	['colorto', 'colorTo'],
]

# ====================================== FLUXBOX ======================================

fluxbox_valtypes = {
	'_root': {
		"background.modX": "number",
		"background.modY": "number",
		"background.pixmap": "filename",
		"background>": "fluxbox_texture",
		"menu.bevelWidth": "number",
		"menu.borderColor": "single_color",
		"menu.borderWidth": "number",
		"menu.bullet": "string",
		"menu.bullet.position": "string",
		"menu.frame.disableColor": "single_color",
		"menu.frame.font": "font",
		"menu.frame.justify": "align",
		"menu.frame.pixmap": "filename",
		"menu.frame.textColor": "single_color",
		"menu.frame>": "fluxbox_texture",
		"menu.hilite.font": "font",
		"menu.hilite.justify": "align",
		"menu.hilite.pixmap": "filename",
		"menu.hilite.textColor": "single_color",
		"menu.hilite>": "fluxbox_texture",
		"menu.itemHeight": "number",
		"menu.roundCorners": "string",
		"menu.selected.pixmap": "filename",
		"menu.submenu.pixmap": "filename",
		"menu.title.font": "font",
		"menu.title.justify": "align",
		"menu.title.pixmap": "filename",
		"menu.title.textColor": "single_color",
		"menu.title>": "fluxbox_texture",
		"menu.titleHeight": "number",
		"menu.unselected.pixmap": "filename",
		"slit.bevelWidth": "number",
		"slit.borderColor": "single_color",
		"slit.borderWidth": "number",
		"slit.pixmap": "filename",
		"slit>": "fluxbox_texture",
		"toolbar.bevelWidth": "number",
		"toolbar.borderColor": "single_color",
		"toolbar.borderWidth": "number",
		"toolbar.button.pressed>": "fluxbox_texture",
		"toolbar.button.scale": "number",
		"toolbar.button>": "fluxbox_texture",
		"toolbar.clock.borderColor": "single_color",
		"toolbar.clock.borderWidth": "number",
		"toolbar.clock.font": "font",
		"toolbar.clock.justify": "align",
		"toolbar.clock.pixmap": "filename",
		"toolbar.clock.textColor": "single_color",
		"toolbar.clock>": "fluxbox_texture",
		"toolbar.height": "number",
		"toolbar.iconbar.borderColor": "single_color",
		"toolbar.iconbar.borderWidth": "number",
		"toolbar.iconbar.empty.pixmap": "filename",
		"toolbar.iconbar.empty>": "fluxbox_texture",
		"toolbar.iconbar.focused.borderColor": "single_color",
		"toolbar.iconbar.focused.borderWidth": "number",
		"toolbar.iconbar.focused.font": "font",
		"toolbar.iconbar.focused.justify": "align",
		"toolbar.iconbar.focused.pixmap": "filename",
		"toolbar.iconbar.focused.textColor": "single_color",
		"toolbar.iconbar.focused>": "fluxbox_texture",
		"toolbar.iconbar.unfocused.borderColor": "single_color",
		"toolbar.iconbar.unfocused.borderWidth": "number",
		"toolbar.iconbar.unfocused.font": "font",
		"toolbar.iconbar.unfocused.justify": "align",
		"toolbar.iconbar.unfocused.pixmap": "filename",
		"toolbar.iconbar.unfocused.textColor": "single_color",
		"toolbar.iconbar.unfocused>": "fluxbox_texture",
		"toolbar.label>": "fluxbox_texture",
		"toolbar.pixmap": "filename",
		"toolbar.shaped": "string",
		"toolbar.windowlabel>": "fluxbox_texture",
		"toolbar.workspace.borderColor": "single_color",
		"toolbar.workspace.borderWidth": "number",
		"toolbar.workspace.font": "font",
		"toolbar.workspace.justify": "align",
		"toolbar.workspace.pixmap": "filename",
		"toolbar.workspace.textColor": "single_color",
		"toolbar.workspace>": "fluxbox_texture",
		"toolbar>": "fluxbox_texture",
		"window.bevelWidth": "number",
		"window.borderColor": "single_color",
		"window.borderWidth": "number",
		"window.button.focus.picColor": "single_color",
		"window.button.focus.pixmap": "filename",
		"window.button.focus>": "fluxbox_texture",
		"window.button.pressed.pixmap": "filename",
		"window.button.pressed>": "fluxbox_texture",
		"window.button.unfocus.picColor": "single_color",
		"window.button.unfocus.pixmap": "filename",
		"window.button.unfocus>": "fluxbox_texture",
		"window.close.pixmap": "filename",
		"window.close.pressed.pixmap": "filename",
		"window.close.unfocus.pixmap": "filename",
		"window.frame.focusColor": "single_color",
		"window.frame.unfocusColor": "single_color",
		"window.grip.focus.pixmap": "filename",
		"window.grip.focus>": "fluxbox_texture",
		"window.grip.unfocus.pixmap": "filename",
		"window.grip.unfocus>": "fluxbox_texture",
		"window.handle.focus.pixmap": "filename",
		"window.handle.focus>": "fluxbox_texture",
		"window.handle.unfocus.pixmap": "filename",
		"window.handle.unfocus>": "fluxbox_texture",
		"window.handleWidth": "number",
		"window.iconify.pixmap": "filename",
		"window.iconify.pressed.pixmap": "filename",
		"window.iconify.unfocus.pixmap": "filename",
		"window.justify": "align",
		"window.label.active.textColor": "single_color",
		"window.label.active>": "fluxbox_texture",
		"window.label.focus.font": "font",
		"window.label.focus.pixmap": "filename",
		"window.label.focus.textColor": "single_color",
		"window.label.focus>": "fluxbox_texture",
		"window.label.unfocus.font": "font",
		"window.label.unfocus.pixmap": "filename",
		"window.label.unfocus.textColor": "single_color",
		"window.label.unfocus>": "fluxbox_texture",
		"window.lhalf.pixmap": "filename",
		"window.lhalf.unfocus.pixmap": "filename",
		"window.maximize.pixmap": "filename",
		"window.maximize.pressed.pixmap": "filename",
		"window.maximize.unfocus.pixmap": "filename",
		"window.rhalf.pixmap": "filename",
		"window.rhalf.unfocus.pixmap": "filename",
		"window.roundCorners": "string",
		"window.shade.pixmap": "filename",
		"window.shade.pressed.pixmap": "filename",
		"window.shade.unfocus.pixmap": "filename",
		"window.stick.pixmap": "filename",
		"window.stick.pressed.pixmap": "filename",
		"window.stick.unfocus.pixmap": "filename",
		"window.stuck.pixmap": "filename",
		"window.stuck.unfocus.pixmap": "filename",
		"window.title.focus.pixmap": "filename",
		"window.title.focus>": "fluxbox_texture",
		"window.title.height": "number",
		"window.title.unfocus.pixmap": "filename",
		"window.title.unfocus>": "fluxbox_texture",
		"borderwidth": "number",
		"bevelwidth": "number",
		"handlewidth": "number",
		"bordercolor": "number",
		"framewidth": "number",
		"window.frame.focuscolor": "single_color",
		"window.frame.unfocuscolor": "single_color",
		"window.font": "string",
	},
	'fluxbox_texture': {
		'_root': "string",
		'color': "single_color",
		'colorto': "single_color",
	}
}

fluxbox_defaults = {
	'_root': {}
}

fluxbox_casereplace = [
	['colorto', 'colorTo'],
	['textcolor', 'textColor'],
	['piccolor', 'picColor'],
	['borderwidth', 'borderWidth'],
	['bevelwidth', 'bevelWidth'],
	['handlewidth', 'handleWidth'],
	['framewidth', 'frameWidth'],
	['bordercolor', 'borderColor'],
	['windowlabel', 'windowLabel'],
]

# ====================================== blackbox ======================================

blackbox_valtypes = {
	'_root': {
		"menu.active.appearance": "string",
		"menu.active.backgroundcolor": "single_color",
		"menu.active.color1": "single_color",
		"menu.active.color2": "single_color",
		"menu.active.foregroundcolor": "single_color",
		"menu.active.textcolor": "single_color",
		"menu.frame.alignment": "align",
		"menu.frame.appearance": "string",
		"menu.frame.backgroundcolor": "single_color",
		"menu.frame.color1": "single_color",
		"menu.frame.color2": "single_color",
		"menu.frame.disabledcolor": "single_color",
		"menu.frame.foregroundcolor": "single_color",
		"menu.frame.marginwidth": "number",
		"menu.frame.textcolor": "single_color",
		"menu.title.alignment": "align",
		"menu.title.appearance": "string",
		"menu.title.backgroundcolor": "single_color",
		"menu.title.color1": "single_color",
		"menu.title.color2": "single_color",
		"menu.title.font": "font",
		"menu.title.foregroundcolor": "single_color",
		"menu.title.marginwidth": "number",
		"menu.title.textcolor": "single_color",
		"rootcommand": "unknown",
		"slit.appearance": "string",
		"slit.backgroundcolor": "single_color",
		"slit.color1": "single_color",
		"slit.color2": "single_color",
		"slit.marginwidth": "number",
		"toolbar.alignment": "align",
		"toolbar.appearance": "string",
		"toolbar.backgroundcolor": "single_color",
		"toolbar.clock.appearance": "string",
		"toolbar.clock.backgroundcolor": "single_color",
		"toolbar.clock.color1": "single_color",
		"toolbar.clock.color2": "single_color",
		"toolbar.color1": "single_color",
		"toolbar.color2": "single_color",
		"toolbar.label.appearance": "string",
		"toolbar.label.backgroundcolor": "single_color",
		"toolbar.label.color1": "single_color",
		"toolbar.label.color2": "single_color",
		"toolbar.windowlabel.appearance": "string",
		"toolbar.windowlabel.backgroundcolor": "single_color",
		"toolbar.windowlabel.color1": "single_color",
		"toolbar.windowlabel.color2": "single_color",
		"window.button.pressed.appearance": "string",
		"window.button.pressed.backgroundcolor": "single_color",
		"window.button.pressed.color1": "single_color",
		"window.button.pressed.color2": "single_color",
		"window.button.pressed.foregroundcolor": "single_color",
		"window.button.focus.appearance": "string",
		"window.button.focus.backgroundcolor": "single_color",
		"window.button.focus.color1": "single_color",
		"window.button.focus.color2": "single_color",
		"window.button.focus.foregroundcolor": "single_color",
		"window.button.unfocus.appearance": "string",
		"window.button.unfocus.backgroundcolor": "single_color",
		"window.button.unfocus.color1": "single_color",
		"window.button.unfocus.color2": "single_color",
		"window.button.unfocus.foregroundcolor": "single_color",
		"window.font": "font",
		"window.grip.focus.appearance": "string",
		"window.grip.focus.backgroundcolor": "single_color",
		"window.grip.focus.color1": "single_color",
		"window.grip.focus.color2": "single_color",
		"window.grip.unfocus.appearance": "string",
		"window.grip.unfocus.backgroundcolor": "single_color",
		"window.grip.unfocus.color1": "single_color",
		"window.grip.unfocus.color2": "single_color",
		"window.handle.focus.appearance": "string",
		"window.handle.focus.backgroundcolor": "single_color",
		"window.handle.focus.color1": "single_color",
		"window.handle.focus.color2": "single_color",
		"window.handle.unfocus.appearance": "string",
		"window.handle.unfocus.backgroundcolor": "single_color",
		"window.handle.unfocus.color1": "single_color",
		"window.handle.unfocus.color2": "single_color",
		"window.handleheight": "number",
		"window.label.focus.appearance": "string",
		"window.label.focus.backgroundcolor": "single_color",
		"window.label.focus.color1": "single_color",
		"window.label.focus.color2": "single_color",
		"window.label.focus.justify": "single_color",
		"window.label.focus.textcolor": "single_color",
		"window.label.marginwidth": "number",
		"window.label.unfocus.appearance": "string",
		"window.label.unfocus.backgroundcolor": "single_color",
		"window.label.unfocus.color1": "single_color",
		"window.label.unfocus.color2": "single_color",
		"window.label.unfocus.justify": "single_color",
		"window.label.unfocus.textcolor": "single_color",
		"window.title.focus.appearance": "string",
		"window.title.focus.backgroundcolor": "single_color",
		"window.title.focus.color1": "single_color",
		"window.title.focus.color2": "single_color",
		"window.title.unfocus.appearance": "string",
		"window.title.unfocus.backgroundcolor": "single_color",
		"window.title.unfocus.color1": "single_color",
		"window.title.unfocus.color2": "single_color",
		"toolbar.marginwidth": "number",
		"toolbar.font": "font",
		"toolbar.label.textcolor": "single_color",
		"toolbar.label.marginwidth": "number",
		"toolbar.windowlabel.textcolor": "single_color",
		"toolbar.clock.textcolor": "single_color",
		"toolbar.button.color1": "single_color",
		"toolbar.button.color2": "single_color",
		"toolbar.button.appearance": "string",
		"toolbar.button.backgroundcolor": "single_color",
		"toolbar.button.pressed.color1": "single_color",
		"toolbar.button.pressed.color2": "single_color",
		"toolbar.button.pressed.appearance": "string",
		"toolbar.button.pressed.backgroundcolor": "single_color",
		"toolbar.button.foregroundcolor": "single_color",
		"toolbar.button.marginwidth": "number",
		"window.title.marginwidth": "number",
		"window.button.pressed.color1": "single_color",
		"window.button.pressed.color2": "single_color",
		"window.button.pressed.appearance": "string",
		"window.button.marginwidth": "number",
		"window.frame.borderwidth": "number",
		"window.frame.focus.bordercolor": "single_color",
		"window.frame.unfocus.bordercolor": "single_color",
		"window.alignment": "align",
		"bordercolor": "number",
	}
}

blackbox_defaults = {
	'_root': {},
}

blackbox_casereplace = [
	['windowlabel', 'windowLabel'],
	['bordercolor', 'borderColor'],
	['backgroundcolor', 'backgroundColor'],
	['foregroundcolor', 'foregroundColor'],
	['disabledcolor', 'disabledColor'],
	['textcolor', 'textColor'],
	['bordercolor', 'borderColor'],
	['borderwidth', 'borderWidth'],
	['marginwidth', 'marginWidth'],
	['handleheight', 'handleHeight'],
]

# ====================================== MAIN ======================================

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

def splitgrp(inval):
	partg_element = [k for k in inval if not k.endswith('>')]
	partg_group = [k[0:-1] for k in inval if k.endswith('>')]
	partg_group.sort(key=len,reverse=True)
	return partg_element, partg_group

class manybox_theme():
	def __init__(self):
		self.data = {}
		self.def_valtypes = {}
		self.def_defaults = {}
		self.def_casereplace = []

	def set_openbox(self):
		self.def_valtypes = openbox_valtypes
		self.def_defaults = openbox_defaults
		self.def_valtypes_splt = dict([[k,splitgrp(v)] for k,v in self.def_valtypes.items()])
		self.def_casereplace = openbox_casereplace

	def set_fluxbox(self):
		self.def_valtypes = fluxbox_valtypes
		self.def_defaults = fluxbox_defaults
		self.def_valtypes_splt = dict([[k,splitgrp(v)] for k,v in self.def_valtypes.items()])
		self.def_casereplace = fluxbox_casereplace

	def set_blackbox(self):
		self.def_valtypes = blackbox_valtypes
		self.def_defaults = blackbox_defaults
		self.def_valtypes_splt = dict([[k,splitgrp(v)] for k,v in self.def_valtypes.items()])
		self.def_casereplace = blackbox_casereplace

	def parse_part(self, inname, val, ingroupname, outdict, display_error):
		partg = self.def_valtypes[ingroupname]

		partg_element, partg_group = self.def_valtypes_splt[ingroupname]

		if inname in partg_element:
			outdict[inname] = val
			return True
		elif inname=='': 
			outdict['_root'] = val
			return True
		else:
			for groupname in partg_group:
				if inname.startswith(groupname):
					exgrpname = self.def_valtypes[ingroupname][groupname+'>']

					innerparam = inname[len(groupname):]
					if innerparam: innerparam = innerparam[1:]

					if groupname not in outdict: outdict[groupname] = {}
					groupdata = outdict[groupname]

					res = self.parse_part(innerparam, val, exgrpname, groupdata, False)
					if (not res): outdict[inname] = val
					return True

			if display_error: print('value not defined:', inname)
		return False

	def iter_valid(self, groupname):
		partg = self.def_valtypes[groupname]
		out = []
		for valname, valtype in partg.items():
			if valname=='_root': valname = ''
			if valname.endswith('>'): 
				extd = valname[0:-1]
				if valtype in self.def_valtypes:
					g_v = self.iter_valid(valtype)
					g_v = [((extd+'.'+x) if x else extd) for x in g_v]
					out += g_v
			else:
				out.append(valname)
		return out

	def __setitem__(self, name, val):
		self.parse_part(name.lower(), val, '_root', self.data, True)

	def add_data(self, name, val):
		self.parse_part(name.lower(), val, '_root', self.data, True)

	def add_data_wild(self, name, val):
		valid_all = self.iter_valid('_root')
		for valid_name in valid_all:
			res = fnmatch.fnmatch(valid_name, name)
			if res: self.add_data(valid_name, val)

	def read(self, filename):
		f = open(filename, 'r')
		predata = {}
		predata_wild = {}

		for x in f.readlines():
			x = x.strip().rstrip()
			if x:
				if x[0]=='!': continue
				elif x[0]=='#': continue
				else:
					splval = x.split(':', 1)
					if len(splval)==2:
						name, val = splval
						name = name.lower().strip().rstrip()
						val = val.strip().rstrip()

						if '*' not in name: predata[name] = val
						else: predata_wild[name] = val

		valid_all = self.iter_valid('_root')
		for k, v in predata_wild.items():
			self.add_data_wild(k, v)

		for k, v in predata.items():
			self.add_data(k, v)

	def get_data(self, name):
		def_root = self.def_defaults['_root']
		name = name.lower()
		if name in self.data: return self.data[name]

		while name in def_root:
			defgrp, name = def_root[name]
			if name in self.data: return self.data[name]

	def write_group(self, jdata, outtab, starttxt):
		for k, v in jdata.items():
			for to, tt in self.def_casereplace:
				if to in k: 
					k = k.replace(to, tt)

			tabname = k.split('.')
			if '_root' in tabname: tabname.remove('_root')
			if isinstance(v, dict): 
				self.write_group(v, outtab, tabname)
			else: 
				outtab.append([starttxt+tabname, v])

	def write(self, filename):
		outtab = []
		f = open(filename, 'w')
		self.write_group(self.data, outtab, [])

		for k, v in outtab:
			f.write(('.'.join(k))+': '+str(v)+'\n')