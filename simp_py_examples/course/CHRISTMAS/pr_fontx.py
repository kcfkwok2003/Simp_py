from simp_py import lcd
BITM={0: 0x80, 1: 0x40, 2:0x20, 3:0x10, 4:0x8,5:0x4,6:0x2,7:0x1}
sp=bytearray([
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,    
])
def pixel(x,y,color,scale):
  global lcd
  if scale==2:
    x=x*2; y=y*2
    lcd.pixel(x,y,color)
    lcd.pixel(x+1,y,color)
    lcd.pixel(x,y+1,color)
    lcd.pixel(x+1,y+1,color)
  else:
    lcd.pixel(x,y,color)
    
def read_texts(fn):
  f=open(fn,'rb')
  lines=f.readlines()
  txts=[]
  for line in lines:
    txts.append(line.decode('utf-8'))
  return txts

def pr_ch(x,y,fntdat,color=0xffffff,transparent=True,scale=2):
  global BITM,lcd
  while fntdat:
    #print('fntdata:%s' % fntdat)
    fnt0,fnt1, fntdat = fntdat[0],fntdat[1], fntdat[2:]
    ix=0
    for i in range(8):
      if fnt0 & BITM[i]:
        pixel(x+ix, y, color,scale)
      else:
        if not transparent:
          pixel(x+ix, y, 0x000000,scale)
      ix+=1
    for i in range(8):
      if fnt1 & BITM[i]:
        pixel(x+ix, y, color,scale)
      else:
        if not transparent:
          pixel(x+ix, y, 0x000000,scale)
      ix+=1
    y+=1
  return x+ix

def pr_texts(x,y,texts,CH_FONTS):
  for text in texts:
    for chx in text:
      fntdat =CH_FONTS.get(chx,sp)
      x= pr_ch(x,y,fntdat)
      
if __name__=='__main__':
  from text1_fontx import CH_FONTS
  lines = read_texts('text1.txt')
  pr_texts(0,0,lines,CH_FONTS)

