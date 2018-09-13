try:
    from simp_py.Ubuntu16 import tft_Ubuntu16
    from simp_py.DefaultFont import tft_DefaultFont
    from simp_py.comic24 import tft_Comic24
    from simp_py.def_small import tft_def_small
    from simp_py.DejaVuSans18 import tft_Dejavu18
    from simp_py.DejaVuSans24 import tft_Dejavu24
    from simp_py.minya24 import tft_minya24
    from simp_py.SmallFont import tft_SmallFont
    from simp_py.tooney32 import tft_tooney32
except:
    from Ubuntu16 import tft_Ubuntu16
    from DefaultFont import tft_DefaultFont
    from comic24 import tft_Comic24
    from def_small import tft_def_small
    from DejaVuSans18 import tft_Dejavu18
    from DejaVuSans24 import tft_Dejavu24
    from minya24 import tft_minya24
    from SmallFont import tft_SmallFont
    from tooney32 import tft_tooney32    
# === Embedded fonts constants ===
DEFAULT_FONT =   0
DEJAVU18_FONT=   1
DEJAVU24_FONT=   2
UBUNTU16_FONT=   3
COMIC24_FONT =   4
MINYA24_FONT =   5
TOONEY32_FONT=   6
SMALL_FONT   =           7
DEF_SMALL_FONT=  8
FONT_7SEG     =          9
USER_FONT     =          10  
font_forceFixed=0
font_rotate=0
_fg = 1
_bg = 0
LASTX= 7000
LASTY = 8000
CENTER = -9003
RIGHT = -9004
BOTTOM = -9004
DEFAULT_TFT_DISPLAY_WIDTH = 640
DEFAULT_TFT_DISPLAY_HEIGHT=480

class DispWin:
    def __init__(self):
        self.x1=0
        self.y1=0
        self.x2= DEFAULT_TFT_DISPLAY_WIDTH
        self.y2 = DEFAULT_TFT_DISPLAY_HEIGHT

dispWin = DispWin()

class PropFont:
    def __init__(self):
        self.charCode=None
        self.adjYOffset=None
        self.width=None
        self.height=None
        self.xOffset=None
        self.xDelta=None
        self.dataPtr=None

    def print_info(self):
        print('PropFont.print: charCode:%s adjYOffset:%s width:%s height:%s xOffset:%s xDelta:%s dataPtr:%s' % \
              (self.charCode, self.adjYOffset, self.width, self.height, self.xOffset, self.xDelta, self.dataPtr))
        
fontChar = PropFont()
        
class FONT:
    def __init__(self,font,x_size,y_size,offset,numchars,bitmap):
        self.font=font
        self.x_size=x_size
        self.y_size=y_size
        self.offset=offset
        self.numchars=numchars
        self.bitmap=bitmap

    def print_info(self):
        print('font.print x_size:%s y_size:%s offset:%s numchars:%s bitmap:%s fonts:%s' % (self.x_size,self.y_size,self.offset, self.numchars, self.bitmap, len(self.font)))

cfont =FONT(tft_DefaultFont, 0, 0x0B, 0, 95,1)
font_buffered_char=1
font_transparent=0

def send_data(x1,y1,x2, y2, lenx, colorbuf,callback=None):
    #print('send_data x1:%s y1:%s x2:%s y2:%s len:%s colorbuf:%s' % (x1,y1,x2, y2, lenx, len(colorbuf)))
    data={'x1':x1,'y1':y1,'x2':x2,'y2':y2,'len':lenx,'colorbuf':colorbuf}
    if callback:
        callback(data)
    else:
        f=open('send_data.dat','a')
        f.write(str(data))
        f.write('\n')
        f.close()
        j=0
        txt=''
        for i in range(len(colorbuf)):
            txt +='%s, ' % colorbuf[i]
            j+=1
            if (j % 9)==0:
                print (txt)
                txt=''
    

def getStringWidth(str):
    strWidth=0
    if cfont.bitmap ==2:
        strWidth = ((_7seg_width() +2) * len(str)) -2
    elif cfont.x_size !=0:
        strWidth = len(str) * cfont.x_size
    else:
        # calculate the width of the string of proportional chars
        for cc in str:
            if getCharPtr(cc):
                if fontChar.width > fontChar.xDelta:
                    strWidth += fontChar.width +1
                else:
                    strWidth += fontChar.xDelta +1
        strWidth -=1
    return strWidth

                    
def getMaxWidthHeight():
    global cfont
    tp=4
    cfont.numchars=0
    cfont.max_x_size=0
    cc = cfont.font[tp]
    tp+=1
    while cc !=0xff:
        cfont.numchars+=1
        cy =cfont.font[tp]; tp+=1
        cw =cfont.font[tp]; tp+=1
        ch =cfont.font[tp]; tp+=1
        tp+=1
        cd = cfont.font[tp]; tp+=1
        cy+= ch
        if cw > cfont.max_x_size:
            cfont.max_x_size=cw
        if cd > cfont.max_x_size:
            cfont.max_x_size=cd
        if ch > cfont.y_size:
            cfont.y_size=ch
        if cy > cfont.y_size:
            cfont.y_size=cy
        if cw !=0:
            # packed bits
            tp += (((cw * ch) -1) //8) + 1
        cc = cfont.font[tp]
        tp+=1
    cfont.size = tp
    
def getCharPtr(c):
    c = ord(c)
    #print('** getCharPtr:%s' % c)
    if 1:
        tp=4
        while True:
            v=cfont.font[tp]; tp+=1
            fontChar.charCode=v
            #print('v:%s' % v)
            if fontChar.charCode==0xff:
                #print('getCharStr, *1 return 0')
                return 0
            fontChar.adjYOffset= cfont.font[tp] ; tp+=1
            fontChar.width = cfont.font[tp]; tp+=1
            fontChar.height = cfont.font[tp]; tp+=1
            fontChar.xOffset = cfont.font[tp]; tp+=1
            if fontChar.xOffset >= 0x80:
                fontChar.xOffset = -(0xff - fontChar.xOffset)
            fontChar.xDelta = cfont.font[tp]; tp+=1
            if c!=fontChar.charCode and fontChar.charCode !=0xff:
                if fontChar.width !=0:
                    #packed bits
                    tp += ((( fontChar.width * fontChar.height)-1) // 8) +1
            if c != fontChar.charCode and fontChar.charCode !=0xff:
                continue
            else:
                break
        fontChar.dataPtr = tp
        #print("getCharPtr c:%s, charCode:%s" % (c, fontChar.charCode))
        if c==fontChar.charCode:
            if font_forceFixed >0:
                #fix width & offset for forced fixed width
                fontChar.xDelta = cfont.max_x_size
                fontChar.xOffset = (fontChar.xDelta - fontChar.width) //2
        else:
            #print('getCharStr, *2 return 0')
            return 0
        return 1        


def printProportionalChar(x,y,callback=None):
    ch=0
    char_width=fontChar.xDelta
    if fontChar.width > fontChar.xDelta:
        char_width = fontChar.width
    if font_buffered_char and not font_transparent:
        # buffer Glyph data for faster sending
        lenx = char_width * cfont.y_size
        color_line =[]
        # fill with bg color
        #print('lenx:%s' % lenx)
        for n in range(lenx):
            color_line.append(_bg)
        # set char pixels to foreground color
        mask = 0x80
        for j in range(fontChar.height):
            for i in range(fontChar.width):
                if ((i+ (j* fontChar.width)) % 8) ==0:
                    mask=0x80
                    ch = cfont.font[fontChar.dataPtr]
                    fontChar.dataPtr+=1
                if (ch & mask) !=0:
                    # visible pixel
                    bufPos = ((j+fontChar.adjYOffset)* char_width) + (fontChar.xOffset +i) # bufY+bufX
                    #print('bufPos:%s' % bufPos)
                    try:
                        color_line[bufPos]= _fg
                    except:
                        while len(color_line) < bufPos:
                            color_line.append( _bg)
                        color_line.append(_fg)
                        
                            
                mask >>=1
        # send to display in one transaction
        # disp_select()
        #print('printProportionalChar: send_data callback:%s' % callback)
        send_data(x,y,x+char_width-1, y+cfont.y_size-1, lenx, color_line,callback)
        # disp_deselect()
        return char_width
    if not font_transparent:
        _fillRect(x,y,char_width+1, cfont.y_size,_bg)
    # draw Glyph
    mask = 0x80
    #disp_select()
    for j in range(fonChar.height):
        for i in range(fontChar.width):
            if ((i+(j* fontChar.width)) % 8)==0:
                mask=0x80
                ch = cfont.font[fontChar.dataPtr]
                fontChar.dataPtr+=1
            if (ch & mask) !=0:
                cx = x+fontChar.xOffset +i
                cy = y + j +fontChar.adjYOffset
                _drawPixel(cx,cy,_fg,0)
            mask >>=1
    #disp_deselect()
    return char_width

def setFont(font):
    if 1:
        #print('setFont %s' % str(font))
        cfont.font=None
        if font==FONT_7SEG:
            cfont.bitmap=2
            cfont.x_size=24
            cfont.y_size=6
            cfont.offset=0
            cfont.color=_fg
        else:
            if font==UBUNTU16_FONT:
                cfont.font=tft_Ubuntu16
                #print('cfont.font:%s' % `cfont.font`)
            elif font==COMIC24_FONT:
                cfont.font=tft_Comic24
            elif font==DEF_SMALL_FONT:
                cfont.font=tft_def_small
            elif font==DEJAVU18_FONT:
                cfont.font=tft_Dejavu18
            elif font==DEJAVU24_FONT:
                cfont.font=tft_Dejavu24
            elif font==MINYA24_FONT:
                cfont.font=tft_minya24
            elif font==SMALL_FONT:
                cfont.font=tft_SmallFont
            elif font==TOONEY32_FONT:
                cfont.font=tft_tooney32
            else:
                cfont.font= tft_DefaultFont
            cfont.bitmap=1
            cfont.x_size = cfont.font[0]
            cfont.y_size = cfont.font[1]
            #cfont.print_info()
            if cfont.x_size>0:
                cfont.offset=cfont.font[2]
                cfont.numchars = cfont.font[3]
                cfont.size = cfont.x_size * cfont.y_size * cfont.numchars
            else:
                cfont.offset=4
                getMaxWidthHeight()

def printChar(c, x, y,callback=None):
    #print('printChar: callback:%s' % callback)
    if 1:
        #print('printChar c:%s x:%s y:%s' % (c,x,y))
        # fz = bytes per char row
        fz = cfont.x_size//8
        if cfont.x_size % 8:
            fz+=1
        #print('fz:%s' % fz)
        # get char position in buffer
        temp = (c-cfont.offset) * (fz * cfont.y_size) + 4
        #print('temp:%s' % temp)
        if font_buffered_char and (not font_transparent):
            # buffer Glyph data for faster sending
            len = cfont.x_size * cfont.y_size
            color_line=[]
            # fill with background color
            for n in range(len):
                color_line.append(_bg)
            # set character pixels to fg color
            for j in range(cfont.y_size):
                for k in range(fz):
                    ch = cfont.font[temp+k]
                    mask=0x80
                    for i in range(8):
                        if (ch & mask) !=0:
                            color_line[j*cfont.x_size + (i + (k*8))] = _fg
                        mask >>=1
                temp += fz
            # send to display in one transaction
            #disp_select()
            #print('printChar send_data callback:%s' % callback)
            send_data(x,y,x+cfont.x_size-1, y+cfont.y_size-1, len, color_line,callback)
            #disp_deselect()
            return
        if not font_transparent:
            _fillRect(x,y, cfont.x_size, cfont.y_size, _bg)
            disp_select()
            for j in range(cfont.y_size):
                for k in range(fz):
                    ch = cfont.font[temp+k]
                    mask=0x80
                    for i in range(8):
                        if (ch & mask) !=0:
                            cx = x+j + k*8
                            cy = y+j
                            _drawPixel(cx,cy, _fg,0)
                        mask >>=1
                temp+=fz
            disp_deselect()
            
def printStr(st, x,y,callback=None):
    #print('printStr: callback:%s' % callback)
    if 1:
        #print('printStr: %s' % st)
        if cfont.bitmap==0:
            return # wrong font selected
        # rotated string cannot be aligned
        if font_rotate !=0 and (x <= CENTER or y <= CENTER):
            return
        if x < LASTX or font_rotate==0 :
            TFT_OFFSET=0
        if x >= LASTX and x < LASTY:
            x= TFT_X + (x - LASTX)
        elif x > CENTER:
            x += dispWin.x1
        if y >= LASTY:
            y = TFT_Y + (y-LASTY)
        elif y > CENTER:
            y += dispWin.y1

        # get number of chars in string to print
        stl = len(st)
        #print('stl:%s' % stl)
        
        # calculate CENTER, RIGHT or BOTTOM position
        tmpw = getStringWidth(st)  # string width in pixels
        fh = cfont.y_size  # font height
        if cfont.x_size !=0 and cfont.bitmap==2:
            # 7-segment font
            fh = (3* (2 * cfont.y_size +1)) + (2 * cfont.x_size) # 7-segment char height
        if x == RIGHT :
            x = dispWin.x2 - tmpw + dispWin.x1
        elif x==CENTER:
            x = (((dispWin.x2 - dispWin.x1 +1) - tmpw) //2) + dispWin.x1
        if y==BOTTOM :
            y=dispWin.y2 -fh + dispWin.y1
        elif y==CENTER:
            y= (((dispWin.y2 - dispWin.y1 +1) - (fh//2)) //2) +dispWin.y1
        if x < dispWin.x1:
            x = dispWin.x1
        if y < dispWin.y1:
            y = dispWin.y1
        if x > dispWin.x2 or y> dispWin.y2:
            return
        TFT_X= x
        TFT_Y = y
        #print('x:%s y:%s' % (x,y))
        # Adjust y position
        tmph = cfont.y_size # font height
        #for non-proportional fonts, char width is the same for all chars
        tmpw = cfont.x_size
        if cfont.x_size !=0:
            if cfont.bitmap ==2:
                # 7 seg-font
                tmpw = _7seg_width()
                tmph = _7seg_height()
        else:
            TFT_OFFSET = 0 # fixed font, offset not needed
        if (TFT_Y + tmph -1) > dispWin.y2:
            return
        offset = TFT_OFFSET
        for i in range(stl):
            ch = st[i]  # get string char
            #print('ch:%s' % ch)
            if ch == 0x0D:  # \r, erase to eol
                if not font_transparent and font_rotate==0:
                    _fillRect(TFT_X, TFT_Y, dispWin.x2 + 1 - TFT_X, tmph, _bg)
            elif ch==0x0A:  # \n, new line
                if cfont.bitmap==1:
                    TFT_Y += tmph + font_line_space
                    if TFT_Y > dispWin.y2 - tmph:
                        break
                    TFT_X = dispWin.x1
            else: # other chars
                #print('other chars x_size:%s' % cfont.x_size)
                if cfont.x_size ==0:
                    # for proportional font get char data to fontChar
                    if getCharPtr(ch):
                        tmpw = fontChar.xDelta
                    else:
                        continue
                # check if char can be displayed in the current line
                if (TFT_X + tmpw) > (dispWin.x2):
                    if text_wrap ==0:
                        break
                    TFT_Y += tmph + font_line_space
                    if TFT_Y > (dispWin.y2-tmph):
                        break
                    TFT_X = dispWin.x1

                # Let's print the char
                if cfont.x_size ==0:
                    # proportional font
                    if font_rotate==0 :
                        TFT_X += printProportionalChar(TFT_X, TFT_Y,callback) + 1
                    else:
                        # rotated proportional font
                        offset += rotatePropChar(x,y,offset)
                        TFT_OFFSET = offset
                else:
                    if cfont.bitmap==1:
                        # fixed font
                        if ch < cfont.offset or ((ch- cfont.offset) > cfont.numchars):
                            ch = cfont.offset
                        if font_rotate ==0:
                            printChar(ch, TFT_X, TFT_Y,callback)
                            TFT_X += tmpw
                        else:
                            rotatChar(ch, x,y,i)
                    elif cfont.bitmap==2:
                        # 7seg
                        _draw7seg(TFT_X, TFT_Y,ch, cfont.y_size, cfont.x_size, _fg)
                        TFT_X += tmpw+2

# ================================================================
# === Main function to send data to display ======================
# If  rep==true:  repeat sending color data to display 'len' times
# If rep==false:  send 'len' color data from color buffer to display
# ** Device must already be selected and address window set **
# ================================================================
#----------------------------------------------------------------------------------------------
def _TFT_pushColorRep(color,  lenx, rep, wait):
    print('_TFT_pushColorRep(%s, %s, %s, %s)' % (color,lenx,rep,wait))
    if (len == 0):
        return;

# override this
# Write 'len' color data to TFT 'window' (x1,y2),(x2,y2)
#-----------------------------------------------------------------------------------------------
def TFT_pushColorRep( x1,  y1,  x2, y2, color,  lenx):
    print('TFT_pushColorRep(%s,%s,%s,%s,%s,%s)' % ( x1,  y1,  x2, y2, color,  lenx))

    
# override this 
def drawPixel(x, y, color, sel):
    print('drawPixel(%s,%s,%s,%s)' % (x,y,color,sel))

    
# draw color pixel on screen
#------------------------------------------------------------------------
def  _drawPixel( x, y,  color, sel):
    if ((x < dispWin.x1) or (y < dispWin.y1) or (x > dispWin.x2) or (y > dispWin.y2)):
        return
    drawPixel(x, y, color, sel)

#====================================================================
def TFT_drawPixel(x,  y,  color,  sel):
    _drawPixel(x+dispWin.x1, y+dispWin.y1, color, sel);


#===========================================
def TFT_readPixel( x, y) :
    if ((x < dispWin.x1) or (y < dispWin.y1) or (x > dispWin.x2) or (y > dispWin.y2)):
        return TFT_BLACK;
    return readPixel(x, y);

#--------------------------------------------------------------------------
def _drawFastVLine( x,  y,  h, color) :
    # clipping
    if ((x < dispWin.x1) or (x > dispWin.x2) or (y > dispWin.y2)):
        return;
    if (y < dispWin.y1):
        h -= (dispWin.y1 - y);
        y = dispWin.y1;
        
    if (h < 0):
        h = 0;
    if ((y + h) > (dispWin.y2+1)):
        h = dispWin.y2 - y + 1;
    if (h == 0):
        h = 1;
    TFT_pushColorRep(x, y, x, y+h-1, color, h);

#---------------------------------------------------------------------------
def _drawFastVLine_( x,  y, h, color):
    # clipping
    if ((x < dispWin.x1) or (x > dispWin.x2) or (y > dispWin.y2)):
        return;
    if (y < dispWin.y1):
        h -= (dispWin.y1 - y);
        y = dispWin.y1;
        
    if (h < 0):
        h = 0;
    if ((y + h) > (dispWin.y2+1)):
        h = dispWin.y2 - y + 1;
    if (h == 0):
        h = 1;
    TFT_pushColorRep_nocs(x, y, x, y+h-1, color, h);

#--------------------------------------------------------------------------
def _drawFastHLine( x,  y,  w, color):
    # clipping
    if ((y < dispWin.y1) or (x > dispWin.x2) or (y > dispWin.y2)):
        return;
    if (x < dispWin.x1):
        w -= (dispWin.x1 - x);
        x = dispWin.x1;
        
    if (w < 0):
        w = 0;
    if ((x + w) > (dispWin.x2+1)):
        w = dispWin.x2 - x + 1;
    if (w == 0):
        w = 1;

    TFT_pushColorRep(x, y, x+w-1, y, color, w);


#======================================================================
def TFT_drawFastVLine( x, y,  h, color):
    _drawFastVLine(x+dispWin.x1, y+dispWin.y1, h, color);


#======================================================================
def TFT_drawFastHLine( x,  y,  w,  color) :
    _drawFastHLine(x+dispWin.x1, y+dispWin.y1, w, color);

# Bresenham's algorithm - thx wikipedia - speed enhanced by Bodmer this uses
# the eficient FastH/V Line draw routine for segments of 2 pixels or more
#----------------------------------------------------------------------------------
def _drawLine(x0, y0, x1, y1, color):
    #print('_drawLine(%s,%s,%s,%s,%s)' % (x0, y0, x1, y1, color))
    if (x0 == x1):
        if (y0 <= y1):
            _drawFastVLine(x0, y0, y1-y0, color);
        else:
            _drawFastVLine(x0, y1, y0-y1, color);
        return;
  
    if (y0 == y1):
        if (x0 <= x1):
            _drawFastHLine(x0, y0, x1-x0, color);
        else:
            _drawFastHLine(x1, y0, x0-x1, color);
        return;
    steep = 0;
    if (abs(y1 - y0) > abs(x1 - x0)):
        steep = 1;
    if (steep):
        x0,y0 = y0,x0 #swap(x0, y0);
        x1,y1 = y1,x1  #swap(x1, y1);
  
    if (x0 > x1):
        x0,x1 = x1,x0 #swap(x0, x1);
        y0,y1 = y1,y0 #swap(y0, y1);

    dx = x1 - x0
    dy = abs(y1 - y0);
    err = dx >> 1
    ystep = -1
    xs = x0
    dlen = 0;

    if (y0 < y1):
        ystep = 1;

    # Split into steep and not steep for FastH/V separation
    if (steep):
        while x0<=x1:
            dlen+=1;
            err -= dy;
            if (err < 0):
                err += dx;
                if (dlen == 1):
                    _drawPixel(y0, xs, color, 1);
                else:
                    _drawFastVLine(y0, xs, dlen, color);
                dlen = 0; y0 += ystep; xs = x0 + 1;
      
            x0+=1
            
        if (dlen):
            _drawFastVLine(y0, xs, dlen, color);
    else:
        while x0 <=x1: 
            dlen+=1;
            err -= dy;
            if (err < 0):
                err += dx;
                if (dlen == 1):
                    _drawPixel(xs, y0, color, 1);
                else:
                    _drawFastHLine(xs, y0, dlen, color);
                dlen = 0; y0 += ystep; xs = x0 + 1;
            x0+=1
        if (dlen):
            _drawFastHLine(xs, y0, dlen, color);


#==============================================================================
def TFT_drawLine( x0, y0, x1, y1, color):
    _drawLine(x0+dispWin.x1, y0+dispWin.y1, x1+dispWin.x1, y1+dispWin.y1, color);


                        
# Draw a triangle
#--------------------------------------------------------------------------------------------------------------------
def _drawTriangle(x0, y0, x1, y1, x2, y2,color):
    _drawLine(x0, y0, x1, y1, color)
    _drawLine(x1, y1, x2, y2, color)
    _drawLine(x2, y2, x0, y0, color)


#================================================================================================================
def TFT_drawTriangle( x0,  y0,  x1,  y1,  x2,  y2,  color):
    x0 += dispWin.x1;
    y0 += dispWin.y1;
    x1 += dispWin.x1;
    y1 += dispWin.y1;
    x2 += dispWin.x1;
    y2 += dispWin.y1;
    
    _drawLine(x0, y0, x1, y1, color);
    _drawLine(x1, y1, x2, y2, color);
    _drawLine(x2, y2, x0, y0, color);
    

# Fill a triangle
#--------------------------------------------------------------------------------------------------------------------
def _fillTriangle( x0,  y0,  x1,  y1,  x2,  y2,  color):
  # Sort coordinates by Y order (y2 >= y1 >= y0)
    if (y0 > y1):
        y0,y1 = y1,y0 #swap(y0, y1);
        x0,x1 = x1,x0 #swap(x0, x1);
  
    if (y1 > y2):
        y2,y1 = y1,y2 #swap(y2, y1);
        x2,x1 = x1,x2 #swap(x2, x1);
  
    if (y0 > y1):
        y0,y1 = y1,y0 #swap(y0, y1);
        x0,x1 = x1,x0 #swap(x0, x1);
  

    if(y0 == y2) : # Handle awkward all-on-same-line case as its own thing
        a = b = x0;
        if(x1 < a):
            a = x1
        elif (x1 > b):
            b = x1
        if (x2 < a):
            a = x2;
        elif (x2 > b):
            b = x2;
        #print('_drawFastHLine(a, y0, b-a+1, color)')
        _drawFastHLine(a, y0, b-a+1, color);
        return
    
    dx01 = x1 - x0
    dy01 = y1 - y0
    dx02 = x2 - x0
    dy02 = y2 - y0
    dx12 = x2 - x1
    dy12 = y2 - y1

    sa   = 0
    sb   = 0

    # For upper part of triangle, find scanline crossings for segments
    # 0-1 and 0-2.  If y1=y2 (flat-bottomed triangle), the scanline y1
    # is included here (and second loop will be skipped, avoiding a /0
    # error there), otherwise scanline y1 is skipped here and handled
    # in the second loop...which also avoids a /0 error here if y0=y1
    # (flat-topped triangle).
    if(y1 == y2):
        last = y1;   # Include y1 scanline
    else:
        last = y1-1; # Skip it

    y=y0
    while y <= last:
        a   = x0 + sa / dy01;
        b   = x0 + sb / dy02;
        sa += dx01;
        sb += dx02;
        skip=''' longhand:
        a = x0 + (x1 - x0) * (y - y0) / (y1 - y0);
        b = x0 + (x2 - x0) * (y - y0) / (y2 - y0);
        '''
        if(a > b):
            a,b = b,a #swap(a,b);
        #print('bbb _drawFastHLine(%s,  %s,  %s,  %s)' % (a, y, b-a+1, color))
        _drawFastHLine(a, y, b-a+1, color);
        y+=1

    # For lower part of triangle, find scanline crossings for segments
    # 0-2 and 1-2.  This loop is skipped if y1=y2.
    #print('y:%s y1:%s y0:%s dx12:%s dx02:%s sa:%s sb:%s' % (y,y1,y0,dx12,dx02,sa,sb))
    sa = dx12 * (y - y1);
    sb = dx02 * (y - y0);
    while y <=y2:
        a   = x1 + sa / dy12;
        b   = x0 + sb / dy02;
        #print('x0:%s x1:%s sa:%s sb:%s dy12:%s dy02:%d a:%s  b:%s' % (x0,x1,sa,sb,dy12,dy02,a,b))
        sa += dx12;
        sb += dx02;
        skip=''' longhand:
        a = x1 + (x2 - x1) * (y - y1) / (y2 - y1);
        b = x0 + (x2 - x0) * (y - y0) / (y2 - y0);
        '''
        if (a > b):
            a,b = b,a #swap(a,b);
        #print('ccc _drawFastHLine(%s,  %s,  %s,  %s)' % (a, y, b-a+1, color))
        _drawFastHLine(a, y, b-a+1, color);
        y+=1


#================================================================================================================
def  TFT_fillTriangle(x0, y0, x1, y1, x2, y2, color):
    _fillTriangle(
	x0 + dispWin.x1, y0 + dispWin.y1,
	x1 + dispWin.x1, y1 + dispWin.y1,
	x2 + dispWin.x1, y2 + dispWin.y1,
	color);


if __name__=='__main__':
    setFont(UBUNTU16_FONT)
    printStr('hello',5,20)
    TFT_drawLine(0,0,10,10,(0,255,0))
    TFT_drawTriangle(0,0,10,10,20,20,(0,255,0))
