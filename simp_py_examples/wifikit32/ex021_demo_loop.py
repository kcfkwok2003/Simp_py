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
    from ex022_random3 import run
    run()
    del run

def run_sin():
    from ex015_sin import SIN
    t=SIN()
    t.run()
    del t

def run_intro():
    from ex019_intro import INTRO, TEXT_FILE
    t =INTRO(TEXT_FILE)
    t.run()

def run_xled_kung_hei():
    from ex018_xled_kung_hei import XLED_CH
    x=XLED_CH()
    for i in range(6):
        x.run()
    del x

demos=[run_xled_kung_hei,]
demos2=[run_hello,run_christmas,run_kung_hei,run_random,run_sin,run_intro]

def thread_run():
    global time,demos2
    for demo in demos2:
        demo()
        gc.collect()    
        time.sleep(1)
        
def run():
    global time,demos,thread_run
    import _thread
    _thread.start_new_thread(thread_run,())
    for demo in demos:
        demo()
        gc.collect()    
        time.sleep(1)

if __name__=='__main__':
    run()
    machine.reset()
