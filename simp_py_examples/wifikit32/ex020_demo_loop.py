from simp_py import mon
import time
import gc
import machine

def run_hello():
    from ex012_hello import hello
    hello()
    del hello

def run_christmas():
    from ex011_christmas_mix3a import Christmas
    test=Christmas()
    test.run()
    del test

def run_kung_hei():
    from ex013_kung_hei import draw
    draw()
    del draw

def run_random():
    from ex014_random2 import run
    run()
    del run

def run_sin():
    from ex015_sin import SIN
    t=SIN()
    t.run()
    del t

def run_intro():
    from ex016_intro import INTRO, TEXT_FILE
    t =INTRO(TEXT_FILE)
    t.run()
    
demos=[run_hello,run_christmas,run_kung_hei,run_random,run_sin,run_intro]

def run():
    global time,demos
    for demo in demos:
        demo()
        gc.collect()    
        time.sleep(1)

if __name__=='__main__':
    while 1:
        run()
        machine.reset()
