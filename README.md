<div align="center">

# ThemeVert - The THEME ConVERTer
</div>

<p align="center">
    ThemeVert is a Theme/Color Scheme Converter for Themes for Unix and Windows
</p>

## How to Use

```
python3 themevert_cmd.py -i <input> -ot <output type> -o <output>

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

Short Name | Type | Name | Ext |
--- | :--- | :--- | :--- |
```blackbox``` | Unix |  blackbox | ```.cfg``` |
```fluxbox``` | Unix |  FluxBox | ```.cfg``` |
```gtk_color_scheme``` | Unix |  GTK Colors .INI | ```.ini``` |
```icewm``` | Unix |  IceWM | ```default.theme``` |
```kde_color``` | Unix |  KDE/Plasma Color Scheme | ```.colors``` |
```win32_theme``` | Win32 |  Windows .theme | ```.theme``` |
```vcl_theme``` | Win32 |  Delphi VCL | |
## Supported Outputs

| Short Name | Type | Name |
| --- | :--- | :--- |
| ```fluxbox``` | Unix |  FluxBox | ```.cfg``` |
| ```gtk_color_scheme``` | Unix | GTK Colors .INI | ```.ini``` |
| ```icewm``` | Unix | IceWM |
| ```kde_color``` | Unix | KDE/Plasma Color Scheme | ```.colors``` |
| ```win32_theme``` | Win32 | Windows .theme |
