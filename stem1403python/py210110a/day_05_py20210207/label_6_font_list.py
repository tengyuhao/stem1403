"""

"""

from tkinter import *
from tkinter import font

root = Tk()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()


# setting

# set a title
root.title('Python GUI - Font list')

#  ====== Extra requirements =====

# specify dimension at 16:9
ww = 1600
wh = 900

# init posx, posy
x = ws / 2 - ww / 2
y = hs / 2 - wh / 2

x = int(x)
y = int(y)

# Make it at center point on your screen
root.geometry(f'{ww}x{wh}+{x}+{y}')

# Set a background color
root.configure(background="black")

# make it topmost
root.attributes('-topmost', True)

# Set max size and min size
root.maxsize(1600, 900)
root.minsize(300, 300)

# Make it resizable
root.resizable(True, True)


res = font.families()
print(res)

for i in res:
    print(i)
root.mainloop()


"""
Font
Baoli TC
Baoli SC
BiauKai
Hiragino Sans GB
Heiti TC
Heiti SC
STFangsong
STHeiti
STKaiti
STSong
SimSong
Kaiti TC
Kaiti SC
Lantinghei TC
Lantinghei SC
Libian TC
Libian SC
LiHei Pro
LiSong Pro
LingWai TC
LingWai SC
HanziPen TC
HanziPen SC
PingFang TC
PingFang HK
PingFang SC
Apple LiSung
Apple LiGothic
Hannotate TC
Hannotate SC
Songti TC
Songti SC
Wawati TC
Wawati SC
Weibei TC
Weibei SC
Xingkai TC
Xingkai SC
Yuppy TC
Yuppy SC
Yuanti TC
Yuanti SC
Academy Engraved LET
Al Bayan
Al Nile
Al Tarikh
American Typewriter
Andale Mono
Apple Braille
Apple Chancery
Apple Color Emoji
Apple SD Gothic Neo
Apple Symbols
AppleGothic
AppleMyungjo
Arial
Arial Black
Arial Hebrew
Arial Hebrew Scholar
Arial Narrow
Arial Rounded MT Bold
Arial Unicode MS
Avenir
Avenir Next
Avenir Next Condensed
Ayuthaya
Baghdad
Baloo
Baloo Bhai
Baloo Bhaijaan
Baloo Bhaina
Baloo Chettan
Baloo Da
Baloo Paaji
Baloo Tamma
Baloo Tammudu
Baloo Thambi
Bangla MN
Bangla Sangam MN
Baskerville
Beirut
Big Caslon
Bodoni 72
Bodoni 72 Oldstyle
Bodoni 72 Smallcaps
Bodoni Ornaments
Bradley Hand
Brush Script MT
Cambay Devanagari
Century Gothic
Chalkboard
Chalkboard SE
Chalkduster
Charter
Cochin
Comic Sans MS
Copperplate
Corsiva Hebrew
Courier
Courier New
Damascus
DecoType Naskh
Devanagari MT
Devanagari Sangam MN
Didot
DIN Alternate
DIN Condensed
Diwan Kufi
Diwan Thuluth
Euphemia UCAS
Farah
Farisi
Futura
Galvji
GB18030 Bitmap
Geeza Pro
Geneva
Georgia
Gill Sans
Gotu
Grantha Sangam MN
Gujarati MT
Gujarati Sangam MN
GungSeo
Gurmukhi MN
Gurmukhi MT
Gurmukhi Sangam MN
HeadLineA
Hei
Helvetica
Helvetica Neue
Herculanum
Hiragino Maru Gothic ProN
Hiragino Mincho ProN
Hiragino Sans
Hiragino Sans CNS
Hoefler Text
Impact
InaiMathi
ITF Devanagari
ITF Devanagari Marathi
Jaini
Jaini Purva
Kai
Kailasa
Kannada MN
Kannada Sangam MN
Kefa
Khmer MN
Khmer Sangam MN
Klee
Kohinoor Bangla
Kohinoor Devanagari
Kohinoor Gujarati
Kohinoor Telugu
Kokonor
Krungthep
KufiStandardGK
Lahore Gurmukhi
Lao MN
Lao Sangam MN
Lucida Grande
Luminari
Maku
Malayalam MN
Malayalam Sangam MN
Marker Felt
Menlo
Microsoft Sans Serif
Mishafi
Mishafi Gold
Modak
Monaco
Mshtakan
Mukta Mahee
Mukta Malar
Mukta Vaani
Muna
Myanmar MN
Myanmar Sangam MN
Nadeem
Nanum Brush Script
Nanum Gothic
Nanum Myeongjo
Nanum Pen Script
New Peninim MT
Noteworthy
Noto Nastaliq Urdu
Noto Sans Kannada
Noto Sans Myanmar
Noto Sans Oriya
Noto Serif Kannada
Noto Serif Myanmar
Optima
Oriya MN
Oriya Sangam MN
Osaka
Palatino
Papyrus
Party LET
PCMyungjo
Phosphate
PilGi
Plantagenet Cherokee
PSL Ornanong Pro
PT Mono
PT Sans
PT Sans Caption
PT Sans Narrow
PT Serif
PT Serif Caption
Raanana
Rockwell
Sana
Sathu
Savoye LET
SF Pro
SF Pro Display
SF Pro Rounded
SF Pro Text
Shobhika
Shree Devanagari 714
SignPainter
Silom
Sinhala MN
Sinhala Sangam MN
Skia
Snell Roundhand
STIXGeneral
STIXIntegralsD
STIXIntegralsSm
STIXIntegralsUp
STIXIntegralsUpD
STIXIntegralsUpSm
STIXNonUnicode
STIXSizeFiveSym
STIXSizeFourSym
STIXSizeOneSym
STIXSizeThreeSym
STIXSizeTwoSym
STIXVariants
Sukhumvit Set
Symbol
Tahoma
Tamil MN
Tamil Sangam MN
Telugu MN
Telugu Sangam MN
Thonburi
Times
Times New Roman
Tiro Bangla
Tiro Gurmukhi
Tiro Hindi
Tiro Kannada
Tiro Marathi
Tiro Sanskrit
Tiro Tamil
Tiro Telugu
Toppan Bunkyu Gothic
Toppan Bunkyu Midashi Gothic
Toppan Bunkyu Midashi Mincho
Toppan Bunkyu Mincho
Trattatello
Trebuchet MS
Tsukushi A Round Gothic
Tsukushi B Round Gothic
Verdana
Waseem
Webdings
Wingdings
Wingdings 2
Wingdings 3
YuGothic
YuKyokasho
YuKyokasho Yoko
YuMincho
YuMincho +36p Kana
Zapf Dingbats
Zapfino
"""