# SPDX-FileCopyrightText: 2024 SatyrDiamond
# SPDX-License-Identifier: GPL-3.0-or-later

# -------------------------------------------- values --------------------------------------------

def clamp(n, minn, maxn): return max(min(maxn, n), minn)

def between_from_one(minputv, maxval, value): return (minputv*(1-value))+(maxval*value)

def between_to_one(minputv, maxval, value): return 0 if minputv == maxval else (value-minputv)/(maxval-minputv)

def is_between(i_min, i_max, i_value): return min(i_min, i_max) <= i_value <= max(i_min, i_max)