# SPDX-FileCopyrightText: 2024 SatyrDiamond
# SPDX-License-Identifier: GPL-3.0-or-later

def hex_to_int(val):
	h = val.lstrip('#')
	return list(int(h[i:i+2], 16) for i in (0, 2, 4))

def writestr(c): 
	return ' '.join([str(x) for x in c.get_int()])

def mix_color(c1, c2, lvl): 
	c1 *= lvl
	c2 *= 1-lvl
	return (c1+c2)
