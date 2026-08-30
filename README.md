<div align="center">

# ThemeVert - The THEME ConVERTer
</div>

<p align="center">
    ThemeVert is a Theme/Color Scheme Converter for Themes for Unix and Windows
</p>

## How to Use

```
python3 dawvert_cmd.py -i <input> -ot <output type> -o <output>

input type: -it 
input file: -i 
output type: -ot 
output file: -o

e.g: 
    python3 themevert_cmd.py -it 'kde_color' -i 'CarbonSlateNeutral.colors' -ot 'win32_theme' -o out.theme

```

## Required Libraries
```
varint
numpy
```

## Supported Inputs

Short Name | Name | Ext |
--- | :--- | :--- |
```gtk_color_scheme``` | Gtk Colors .INI | ```.ini``` |
```icewm``` | IceWM | ```default.theme``` |
```kde_color``` | KDE/Plasma Color Scheme | ```.colors``` |
```win32_theme``` | Windows .theme | ```.theme``` |
```vcl_theme``` | Delphi VCL | |
## Supported Outputs

| Short Name | Name |
| --- | :--- |
| ```icewm``` | IceWM |
| ```win32_theme``` | Windows .theme |
