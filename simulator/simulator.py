try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except:
    pass

import pygame    
from pygame.locals import *
from pygame import gfxdraw

import os, sys
import time

from simp_py import RstBtn,buttonA,buttonB,buttonC,LCD_Y0,BG,FG,lcd,tft,gdata,logging
APP_NAME='Simpy-py IOT Simulator'

network=None
t_sleep= time.sleep
def _sleep(t):
    now = time.time()
    #print('sleep @%s' % now)
    tout = time.time() + t
    while True:
        if gdata is not None:
            if gdata.run is not None:
                gdata.run()
        if network:
            if network.gdata2.run is not None:
                network.gdata2.run()
                #print ('gdata2:%s' % network.gdata2.run)
        if time.time() > tout:
            #print('wake @%s' % time.time())
            break
time.sleep = _sleep


TITLE_X =80
TITLE_Y = 0
TITLE_Y_C= LCD_Y0 // 2

import os.path

from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_file_location

class MyMetaFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        #print('+++find_spec:fullname:%s path:%s target:%s' % (fullname,path,target))
        if path is None or path == "":
            path = [os.getcwd()] # top level import -- 
        if "." in fullname:
            *parents, name = fullname.split(".")
        else:
            name = fullname
        #print('path:%s' % path)
        path.append('simp_py')
        for entry in path:
            #print('entry:%s' % entry)
            if os.path.isdir(os.path.join(entry, name)):
                # this module has child modules
                filename = os.path.join(entry, name, "__init__.py")
                submodule_locations = [os.path.join(entry, name)]
            else:
                filename = os.path.join(entry, name + ".py")
                submodule_locations = None
            #print('filename:%s' % filename)
            if not os.path.exists(filename):
                continue
            if 'simp_py' not in filename:
                #print('---find spec return None1')
                return None
            v= spec_from_file_location(fullname, filename, loader=MyLoader(filename), submodule_search_locations=submodule_locations)
            print('find spec return :%s' % v)
            return v
        #print('---find spec return None')
        return None # we don't know how to import this

class MyLoader(Loader):
    def __init__(self, filename):
        #print('MyLoader.__init__')
        self.filename = filename

    def create_module(self, spec):
        #print('MyLoader.create_module')
        return None # use default module creation semantics

    def exec_module(self, module):
        #print('MyLoader.exec_module %s' % module)
        with open(self.filename) as f:
            data = f.read()

        # manipulate data some way...
        #print('exec(%s , %s)' % (data, vars(module)))
        exec(data, vars(module))

def install():
    """Inserts the finder into the import machinery"""
    sys.meta_path.insert(0, MyMetaFinder())
    
install()

class SIMULATOR:
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
        gdata.run = self.run
        
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


if __name__=='__main__':
    import machine
    import network
    import sys
    buttonA.set_gdata1(machine.gdata1)
    buttonB.set_gdata1(machine.gdata1)
    buttonC.set_gdata1(machine.gdata1)
    simulator = SIMULATOR()
    x=0
    y=0
    while True:
        simulator.run()
        #lcd.test2()
        try:
            f=open('test.py')
            cont=f.read()
            exec(cont, {'gdata1':machine.gdata1, '__name__':'__main__'})
            s ="test.py end"
            lcd.text(2,200,s)
            break
        except FileNotFoundError:
            s="No test.py"
            lcd.text(2,120,s)
        except:
            s ="test.py has exc"
            lcd.text(2,200,s)
            simulator.run()
            raise
    while True:
        simulator.run()
        
    
    
