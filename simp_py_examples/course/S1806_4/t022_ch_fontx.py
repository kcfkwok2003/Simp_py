# t022.py
from ch_fontx import CH_FONTS
BITM={0: 0x80, 1: 0x40, 2:0x20, 3:0x10, 4:0x8,5:0x4,6:0x2,7:0x1}
def pr_ch(x,y,fntdat,color):
  global BITM
  while fntdat:
    fnt0,fnt1, fntdat = fntdat[0],fntdat[1], fntdat[2:]
    ix=0
    for i in range(8):
      if fnt0 & BITM[i]:
        tft.tft.pixel(x+ix, y, color)
      else:
        tft.tft.pixel(x+ix, y, 0x000000)
      ix+=1
    for i in range(8):
      if fnt1 & BITM[i]:
        tft.tft.pixel(x+ix, y, color)
      else:
        tft.tft.pixel(x+ix, y, 0x000000)
      ix+=1
    y+=1
if __name__=='__main__':
  x=0; y=0; color = 0xff0000
  for chx in CH_FONTS.keys():
    fntdat = CH_FONTS[chx]
    pr_ch(x,y,fntdat,color)
    x+=16
