"""
[Homework]
Date: 2021-03-14
Project.  Full Color Charts
Description:
Save all color names into an external text file
Read the data (of color names) files
Display a full color chart
Calculate the execution time
Hints:
You may set MAX_ROWS or MAX_COLUMNS as you wish
All cells must be of equal width
Exception handling
Data file:
evaluate_3_project/full_color_chart/colors.txt
"""

from tkinter import *
import time
import sys

# You can put one number for your computer
MAX_ROWS = 45

# start time
start_time = time.time()

# READ FILE
try:
    print("Start opening file...")

    filepath = "colors.txt"

    file = open(filepath, 'r', encoding="utf-8")

    # print("==================")
    content = file.readlines()
    # print(content)
    # print("==================")
    # print()

    file.close()
    print("Done.")
except FileNotFoundError as fe:
    print(fe)
    sys.exit()
except IOError as ioe:
    print(ioe)
    sys.exit()
except UnicodeDecodeError as ude:
    print(ude)
    sys.exit()
except Exception as e:
    print(e)
    sys.exit()

# create one list for after
COLORS = []

# replace list is to be separate between every color
replace_list = ["[", "]", "'", ",", "\n"]

for i in content:
    colors = i.split(", ")

    for i2 in colors:
        for i3 in replace_list:
            i2 = i2.replace(i3, "")
        """
        Traceback (most recent call last):
        File "/Users/tengyuhao/PycharmProjects/stem1403/stem1403python/py210110a/day_10_py20210314/project_demo_20210314.py", line 114, in <module>
        label = Label(root, text=color, bg=color, font=('SF Pro Text', FONT_SIZE, 'bold'), padx=5, pady=5)
        File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 3144, in __init__
        Widget.__init__(self, master, 'label', cnf, kw)
        File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/tkinter/__init__.py", line 2568, in __init__
        self.tk.call(
        _tkinter.TclError: unknown color name " blue"
        """

        if i2 == " blue":
            i2 = "blue"

        COLORS.append(i2)

"""
Before, when we just use split tom make a list.
["'snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',\n", "    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',\n", "    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',\n", "    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',\n", "    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',\n", "    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',\n", "    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',\n", "    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',\n", "    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',\n", "    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',\n", "    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',\n", "    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',\n", "    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',\n", "    'indian red', 'saddle brown', 'sandy brown',\n", "    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',\n", "    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',\n", "    'pale violet red', 'maroon', 'medium violet red', 'violet red',\n", "    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',\n", "    'thistle', 'snow2', 'snow3',\n", "    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',\n", "    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',\n", "    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',\n", "    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',\n", "    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',\n", "    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',\n", "    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',\n", "    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',\n", "    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',\n", "    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',\n", "    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',\n", "    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',\n", "    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',\n", "    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',\n", "    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',\n", "    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',\n", "    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',\n", "    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',\n", "    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',\n", "    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',\n", "    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',\n", "    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',\n", "    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',\n", "    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',\n", "    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',\n", "    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',\n", "    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',\n", "    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',\n", "    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',\n", "    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',\n", "    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',\n", "    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',\n", "    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',\n", "    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',\n", "    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',\n", "    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',\n", "    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',\n", "    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',\n", "    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',\n", "    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',\n", "    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',\n", "    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',\n", "    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',\n", "    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',\n", "    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',\n", "    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',\n", "    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',\n", "    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',\n", "    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',\n", "    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',\n", "    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',\n", "    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',\n", "    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',\n", "    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',\n", "    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',\n", "    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',\n", "    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99'\n"]

....
we need delete : 
    [
    ]
    '
    ,
    \n
"""
# # test
# print(COLORS)

# main program for GUI
root = Tk()
root.geometry('+400+300')
root.config(bg='#ddddff')
root.title('Python GUI - Color Chart Full - YUHAO TENG')

row = 0
col = 0

MAX_COLUMNS = len(COLORS) // MAX_ROWS + 1
FONT_SIZE = 10

for color in COLORS:
    # create color label
    label = Label(root, text=color, bg=color, font=('SF Pro Text', FONT_SIZE, 'bold'), padx=5, pady=5)
    label.grid(row=row, column=col, sticky=E+W)
    row += 1

    if row > MAX_ROWS:
        row = 0
        col += 1

for col in range(MAX_COLUMNS):
    root.columnconfigure(col, minsize=120)

root.mainloop()

print("Execution time : {}s seconds ~~~".format(time.time() - start_time))



