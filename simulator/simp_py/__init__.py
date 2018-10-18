try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except:
    pass

import pygame    
from pygame.locals import *
from pygame import gfxdraw
from simp_py import tft_lib
from simp_py.tft_lib import *
from simp_py import machine

#import dbm
#import requests as urequests


LCD_X0 = 0
LCD_Y0= 55
LCD_HEIGHT = 480
LCD_WIDTH= 640

RST_X0=5
RST_Y0=5
RST_HEIGHT=40
RST_WIDTH=60
BTN_HEIGHT=50
BTN_WIDTH=60
BTN_Y0 = LCD_Y0+LCD_HEIGHT+10
BTNA_X0= 20
BTNB_X0= 220
BTNC_X0= 420
BG = (0xc0,0xd1,0xc9) #(100,149,237) # CRONFLOWER BLUE
FG = (0,0,0)

pygame.init()

class GDATA:
    def __init__(self):
        self.run=None
        

gdata=GDATA()


class Logging:
    def __init__(self):
        pass

    def debug(self,msg):
        import time
        now = time.time()
        ds = ('%.03f' % now).split('.')[1]
        YYYY,MM,DD,hh,mm,ss,_,_,_=time.localtime(now)
        print('%02d:%02d:%02d.%s %s' % (hh,mm,ss,ds,msg))

logging = Logging()

class MON:
    def __init__(self):
        pass

    def log_exc(self,e):
        print ('exc:%s' % e)

mon = MON()

class TFT:
    def __init__(self):
        self.backlit=True

    def on(self):
        self.backlit=True

    def off(self):
        self.backlit=False

tft=TFT()

class LCD:
    def __init__(self,bg,fg=(0,255,0)):
        global LCD_X0
        self.bg=bg
        self.fg=fg
        self._fg=fg
        self._bg=bg
        self.LCD_X0= LCD_X0
        self.rect = pygame.Rect(self.LCD_X0,LCD_Y0,LCD_WIDTH, LCD_HEIGHT)
        self.pixels={}
        self.FONT_Comic = COMIC24_FONT
        self.FONT_DejaVu18 = DEJAVU18_FONT
        self.FONT_Default = DEFAULT_FONT
        tft_lib.drawPixel = self.drawPixel   #_pixel
        tft_lib.txt_drawPixel = self.txt_drawPixel
        tft_lib.TFT_pushColorRep = self.pushColorRep
        
        self.BLACK = 0x0
        self.NAVY = 0x80
        self.DARKGREEN = 0x008000
        self.DARKCYAN = 0x008080
        self.MAROON = 0x800000
        self.PURPLE = 0x800080
        self.OLIVE = 0x808000
        self.LIGHTGREY = 0xc0c0c0
        self.DARKGREY = 0x808080
        self.BLUE = 0x0000ff
        self.GREEN = 0xff00
        self.CYAN = 0Xffff
        self.RED = 0xfc0000
        self.MAGENTA = 0xfc00ff
        self.YELLOW = 0xfcfc00
        self.WHITE = 0xfcfcfc
        self.ORANGE = 0xfca400
        self.GREENYELLOW = 0xacfc2c
        self.PINK = 0xfcc0ca

    def drawPixel(self, x,y,color,sel):
        #print('**drawPixel(%s,%s,%s,%s)' % (x,y,color,sel))
        #x=x*2
        #y=y*2
        color = self.set_color(color)
        self._pixel(x,y,color,sel)
        self._pixel(x+1,y,color,sel)
        self._pixel(x,y+1,color,sel)
        self._pixel(x+1,y+1,color,sel)

    def txt_drawPixel(self, x,y,color,sel):
        #print('**txt_drawPixel(%s,%s,%s,%s)' % (x,y,color,sel))
        x=x*2
        y=y*2
        color = self.set_color(color)
        self._pixel(x,y,color,sel)
        self._pixel(x+1,y,color,sel)
        self._pixel(x,y+1,color,sel)
        self._pixel(x+1,y+1,color,sel)                
        
    def arc(self, x,y,r,thick,start,end,color=None, fillcolor=None):
        x=x*2
        y=y*2
        r=r*2
        thick=thick *2
        if color is None:
            color = self._fg
        if fillcolor is None:
            fillcolor = self._fg
        color = self.conv_color(color)
        fillcolor = self.conv_color(fillcolor)
        TFT_drawArc(x,y,r,thick,start,end,color,fillcolor)
        
    
    def refit(self,x0):
        self.LCD_X0=x0
        self.rect = pygame.Rect(self.LCD_X0,LCD_Y0,LCD_WIDTH, LCD_HEIGHT)
        
    def clear(self,color=None):
        self.pixels={}
        if color is None:
            color=self._bg
        TFT_fillScreen(color)

    def circle(self, x,y,radius,color=None,fillcolor=None):
        x=x*2
        y=y*2
        radius=radius*2
        if not color:
            color = self._fg
        if fillcolor is not None:
            TFT_fillCircle(x,y,radius, fillcolor)
            if color:
                TFT_drawCircle(x,y,radius,color)
        else:
            TFT_drawCircle(x,y,radius,color)
            
    def conv_color(self,cx):
        if type(cx)==type(1):
            r = (cx >> 16 ) & 0xff 
            g = (cx >> 8) & 0xff
            b = cx & 0xff
            return (r,g,b)
            #return '#%06x' % cx
        return cx
    
    def draw(self):
        #print('lcd.draw')
        pygame.draw.rect(self.surface,self.bg,self.rect)
        poss = self.pixels.keys()
        if tft.backlit:
            for x,y in poss:
                try:
                    gfxdraw.pixel(self.surface,x,y,self.pixels[(x,y)])
                except:
                    print('gfxdraw.pixel x:%s y:%s c:%s' % (x,y, self.pixels[(x,y)]))
                    raise


    def ellipse(self, x,y, rx,ry, opt=15,color=None, fillcolor=None):
        x=x*2
        y=y*2
        rx=rx*2
        ry=ry*2
        if color is None:
            color = self._fg
        if fillcolor:
            TFT_fillEllipse(x,y,rx,ry,fillcolor,opt)
        TFT_drawEllipse(x,y,rx,ry,color,opt)
        
    
    def font(self,fontx, rotate=None,transparent=None,fixedwidth=None,dist=None,width=None,outline=None,color=None):
        setFont(fontx,rotate,transparent,fixedwidth,dist,width,outline,color)

        
    def _pixel(self,x,y,color,sel=None):
        color = self.conv_color(color)
        #print('pixel color x:%s y:%s %s' % (x,y,str(color)))
        self.pixels[(x+self.LCD_X0,y+LCD_Y0)]=color

    def pixel(self,x,y,color):
        x=x*2
        y=y*2
        self._pixel(x,y,color)
        self._pixel(x+1,y,color)
        self._pixel(x,y+1,color)
        self._pixel(x+1,y+1,color)        

    def polygon(self,cx,cy,r,sides,thick, color=0xff00, fill=0, rot=0):
        if color is None:
            color = self._fg
        if fill is None:
            fill = self._fg
            
        color = self.conv_color(color)
        fill = self.conv_color(fill)
        diameter = r*2
        cx = cx*2
        cy= cy*2
        th=thick *2
        TFT_drawPolygon(cx,cy,sides,diameter,color,fill,rot,th)
        
    
    def pushColorRep(self,x1,y1,x2,y2,color, lenx):
        color = self.conv_color(color)
        if x1==x2:
            x=int(x1)
            y1=int(y1)
            y2 = int(y2)
            y= min(y1,y2)
            ymax = max(y1,y2)
            while y <= ymax:
                self.pixels[(x+self.LCD_X0,y+LCD_Y0)]=color
                y+=1
            return
        if y1==y2:
            y= int(y1)
            x1 = int(x1)
            x2 = int(x2)
            x = min(x1,x2)
            xmax = max(x1,x2)
            while x <= xmax:
                self.pixels[(x+self.LCD_X0,y+LCD_Y0)]=color
                x+=1
            return
        x = min(x1,x2)
        xmax = max(x1,x2)
        ymin = min(y1,y2)
        ymax = max(y1,y2)
        while x <= xmax:
            y = ymin
            while y <= ymax:
                self.pixels[(x+self.LCD_X0,y+LCD_Y0)]=color
                y+=1
            x+=1
        #print('???pushColorRep(%s,%s,%s,%s,%s,%s)' % (x1,y1,x2,y2,color, lenx))
        
    def put_char(self,dx):
        x =x1 = dx['x1']
        y = dx['y1']
        x2 =dx['x2']
        for cx in dx['colorbuf']:
            cx = self.set_color(cx)
            xx=x*2; yy=y*2
            self._pixel(xx,yy,cx)
            self._pixel(xx+1,yy,cx)
            self._pixel(xx,yy+1,cx)
            self._pixel(xx+1,yy+1,cx)
            x+=1
            if x > x2:
                x= x1
                y+=1

    def roundrect(self,x,y,w,h,r,color=None,fillcolor=None):
        x=x*2
        y=y*2
        w=w*2
        h=h*2
        
        if color is None:
            color = self._fg
        if fillcolor is not None:
            TFT_fillRoundRect(x,y,w,h,r,fillcolor)
        TFT_drawRoundRect(x,y,w,h,r,color)
        
    
    def set_color(self,cx):
        if cx:
            return self.fg
        return self.bg
    
    def set_surface(self,surface):
        self.surface = surface

    def test2(self):
        f=open('send_data.dat','rb')
        lines = f.readlines()
        f.close()
        for line in lines:
            dx = eval(line)
            print('dx:%s' % dx)
            self.put_char(dx)

    def text(self,x,y,text,color=0xff00):
        self.fg=self.conv_color(color)
        printStr(text,x,y,self.put_char)

    def textClear(self,x,y,text,color=0xff00):
        TFT_clearStringRect(x,y,text)
        
    def triangle(self,x0,y0,x1,y1,x2,y2,color=0xff00,fillcolor=None):
        x0=x0*2
        y0=y0*2
        x1=x1*2
        y1=y1*2
        x2=x2*2
        y2=y2*2
        if fillcolor:
            self.fg = self.conv_color(fillcolor)
            TFT_fillTriangle(x0,y0,x1,y1,x2,y2,fillcolor)
        self.fg = self.conv_color(color)
        TFT_drawTriangle(x0,y0,x1,y1,x2,y2, color)

            
lcd = LCD((30,30,30))    


class Button:
    def __init__(self,pid, name,color,x0,y0,w,h):
        self.pid=pid
        self.name = name
        self.color=color
        self.x0=x0
        self.y0=y0
        self.w = w
        self.h = h
        self.font = pygame.font.Font(None,32)
        self.nameImg = self.font.render(name, True, FG)
        self.fontRect = self.nameImg.get_rect()
        self.rect = pygame.Rect(x0,y0,w,h)
        self.fontRect.centerx = self.rect.centerx
        self.fontRect.centery = self.rect.centery
        self.state=False
        #machine.gdata1.pins.set(self.pid, 1)

    def set_gdata1(self, gdata1):
        self.gdata1=gdata1
        
    def draw(self, surface):
        pygame.draw.rect(surface,self.color,self.rect)
        #surface.blit(self.nameImg, (self.x0,self.y0))
        surface.blit(self.nameImg, self.fontRect)

    def collidepoint(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def set(self):
        self.state=True
        if self.gdata1:
            self.gdata1.pins.set(self.pid, 0)
        
    def clear(self):
        self.state=False
        if self.gdata1:
            self.gdata1.pins.set(self.pid, 1)
        
    def isPressed(self):
        return self.state
    

RstBtn = Button(0,'Exit',(255,0,0),RST_X0,RST_Y0,RST_WIDTH,RST_HEIGHT)
buttonA = Button(39,'A', (250,250,250),BTNA_X0,BTN_Y0,BTN_WIDTH, BTN_HEIGHT)
buttonB = Button(38,'B', (250,250,250),BTNB_X0,BTN_Y0,BTN_WIDTH, BTN_HEIGHT)
buttonC = Button(37,'C', (250,250,250),BTNC_X0,BTN_Y0,BTN_WIDTH, BTN_HEIGHT)    
    

