try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except:
    pass

import pygame    
from pygame.locals import *
from pygame import gfxdraw
from simp_py.tft_lib import *
#import requests as urequests


LCD_X0 = 0
LCD_Y0= 55
LCD_HEIGHT = 480
LCD_WIDTH= 640

RST_X0=5
RST_Y0=5
RST_HEIGHT=40
RST_WIDTH=60
BTN_HEIGHT=40
BTN_WIDTH=60
BTN_Y0 = LCD_Y0+LCD_HEIGHT+10
BTNA_X0= 20
BTNB_X0= 120
BTNC_X0= 220
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
        YYYY,MM,DD,hh,mm,ss,_,_,_=time.localtime(now)
        print('%02d:%02d:%02d %s' % (hh,mm,ss,msg))

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
    def __init__(self,bg, fg=(0,255,0)):
        self.bg=bg
        self.fg=fg
        self.rect = pygame.Rect(LCD_X0,LCD_Y0,LCD_WIDTH, LCD_HEIGHT)
        self.pixels={}
        
    def set_surface(self,surface):
        self.surface = surface
        
    def draw(self):
        #print('lcd.draw')
        pygame.draw.rect(self.surface,self.bg,self.rect)
        poss = self.pixels.keys()
        if tft.backlit:
            for x,y in poss:
                #print('gfxdraw.pixel x:%s y:%s c:%s' % (x,y, self.pixels[(x,y)]))
                gfxdraw.pixel(self.surface,x,y,self.pixels[(x,y)])
            
    def clear(self):
        self.pixels={}
        
    def pixel(self,x,y,color):
        self.pixels[(x+LCD_X0,y+LCD_Y0)]=color

    def conv_color(self,cx):
        if type(cx)==type(1):
            r = (cx >> 16 ) & 0xff 
            g = (cx >> 8) & 0xff
            b = cx & 0xff
            return (r,g,b)
            #return '#%06x' % cx
        return cx

    def text(self,x,y,text,color=0xff00):
        self.fg=self.conv_color(color)
        printStr(text,x,y,self.put_char)

    def put_char(self,dx):
        x =x1 = dx['x1']
        y = dx['y1']
        x2 =dx['x2']
        for cx in dx['colorbuf']:
            cx = self.set_color(cx)
            xx=x*2; yy=y*2
            self.pixel(xx,yy,cx)
            self.pixel(xx+1,yy,cx)
            self.pixel(xx,yy+1,cx)
            self.pixel(xx+1,yy+1,cx)
            x+=1
            if x > x2:
                x= x1
                y+=1

    def set_color(self,cx):
        if cx:
            return self.fg
        return self.bg
    
    def test2(self):
        f=open('send_data.dat','rb')
        lines = f.readlines()
        f.close()
        for line in lines:
            dx = eval(line)
            print('dx:%s' % dx)
            self.put_char(dx)
            
lcd = LCD((30,30,30))    


class Button:
    def __init__(self,name,color,x0,y0,w,h):
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
        
    def draw(self, surface):
        pygame.draw.rect(surface,self.color,self.rect)
        #surface.blit(self.nameImg, (self.x0,self.y0))
        surface.blit(self.nameImg, self.fontRect)

    def collidepoint(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def set(self):
        self.state=True

    def clear(self):
        self.state=False

    def isPressed(self):
        return self.state
    

RstBtn = Button('Exit',(255,0,0),RST_X0,RST_Y0,RST_WIDTH,RST_HEIGHT)
buttonA = Button('A', (250,250,250),BTNA_X0,BTN_Y0,BTN_WIDTH, BTN_HEIGHT)
buttonB = Button('B', (250,250,250),BTNB_X0,BTN_Y0,BTN_WIDTH, BTN_HEIGHT)
buttonC = Button('C', (250,250,250),BTNC_X0,BTN_Y0,BTN_WIDTH, BTN_HEIGHT)    
    

