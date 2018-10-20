try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except:
    pass

import pygame    
from pygame.locals import *
from pygame import gfxdraw
from simp_py import RstBtn,buttonA,buttonB,buttonC,LCD_Y0,BG,FG,lcd,tft,gdata,logging
APP_NAME='Simpy-py IOT Simulator'
TITLE_X =80
TITLE_Y = 0
TITLE_Y_C= LCD_Y0 // 2


class PGTEST:
    def __init__(self):
        global APP_NAME
        dinfo = pygame.display.Info()
        self.fpsClock=pygame.time.Clock()
        w = dinfo.current_w
        h = dinfo.current_h
        if w > 720:
            w=720
        if h > 800:
            h=800
        if w> 640:
            x0 = (w-640)//2
            lcd.refit(x0)
        APP_NAME = APP_NAME +'(%s,%s)' % (w,h)
        pygame.display.set_caption(APP_NAME)

        self.surface = pygame.display.set_mode((w,h))
        self.bg = pygame.Color(*BG)
        #self.Lcd = pygame.Rect(LCD_X0, LCD_Y0, LCD_WIDTH, LCD_HEIGHT)
        self.font = pygame.font.Font(None, 32)
        self.titleImg = self.font.render(APP_NAME, True, FG)
        lcd.set_surface(self.surface)
        #gdata.run = self.run        

    def run(self):
        self.surface.fill(self.bg)
        for event in pygame.event.get():
            #print('event type: %s' % event.type)
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos= event.pos
                if RstBtn.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                for btnx in [buttonA, buttonB,buttonC]:
                    if btnx.collidepoint(mouse_pos):
                        logging.debug('%s pressed' % btnx.name)
                        btnx.set()
                        
            if event.type==pygame.MOUSEBUTTONUP:
                print('button up')
                for btnx in [buttonA, buttonB,buttonC]:
                    btnx.clear()
                    
        self.gameTime = self.fpsClock.get_time()
        for btnx in [buttonA, buttonB, buttonC,RstBtn]:
            btnx.draw(self.surface)
        lcd.draw()
        
        #pygame.draw.rect(self.surface, [30,30,30], self.Lcd)
        self.titleRect = self.titleImg.get_rect()
        self.titleRect.centery = TITLE_Y_C
        self.titleRect.left = TITLE_X
        self.surface.blit(self.titleImg, self.titleRect) 
        #pygame.display.update()
        #self.fpsClock.tick(10)
        #testing
        pygame.display.flip()

#if __name__=='__main__':
from simp_py import machine
from simp_py import network
import sys
buttonA.set_gdata1(machine.gdata1)
buttonB.set_gdata1(machine.gdata1)
buttonC.set_gdata1(machine.gdata1)    
test = PGTEST()
from simp_py.network import mqtt
from simp_py import lcd
from simp_py.machine import Pin,unique_id
import time
mqtt_id = str(unique_id())
led = Pin(26,Pin.OUT)
led.value(0)
lcd.clear()
lcd.circle(100,100,30,lcd.RED,lcd.BLUE)

connected =False
def connected_cb(task):
    global connected
    connected=True

lights_changed=0
def data_cb(msg):
    global lights_changed
    name=msg[0]
    topic=msg[1]
    cont=msg[2]
    if cont=='on' or cont==b'on':
        lights_changed=1
    elif cont=='off' or cont==b'off':
        lights_changed=-1
    return lights_changed

#from button import Button
#buttonA = Button(39)
#buttonB = Button(38)
lcd.font(lcd.FONT_Comic, transparent=True, fixedwidth=False)
lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
lcd.text(13,155,'ON',lcd.BLACK)
lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
lcd.text(13+100,155,'OFF',lcd.BLACK)
mqttc = mqtt('lights','iot.eclipse.org',secure=False,connected_cb=connected_cb, data_cb=data_cb,clientid=mqtt_id)
while not connected:
    mqttc.run()
    time.sleep(0.1)

mqttc.subscribe('/lights')
apressed=False
bpressed=False

while True:
    if buttonA.isPressed():
        if not apressed:
            apressed=True
            mqttc.publish('/lights','on')
            lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.YELLOW)
            lcd.text(13,155,'ON',lcd.BLACK)
    else:
        if apressed:
            apressed=False
            lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
            lcd.text(13,155,'ON',lcd.BLACK)

    if buttonB.isPressed():
        if not bpressed:
            bpressed=True
            mqttc.publish('/lights','off')
            lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.YELLOW)
            lcd.text(13+100,155,'OFF',lcd.BLACK)
            time.sleep(0.1)
    else:
        if bpressed:
            bpressed=False
            lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
            lcd.text(13+100,155,'OFF',lcd.BLACK)

    if lights_changed !=0:
        if lights_changed==1:
            led.value(1)
            lcd.circle(100,100,30,lcd.RED,lcd.YELLOW)
        elif lights_changed==-1:
            led.value(0)
            lcd.circle(100,100,30,lcd.RED,lcd.BLUE)
        lights_changed=0

    test.run()
    mqttc.run()
