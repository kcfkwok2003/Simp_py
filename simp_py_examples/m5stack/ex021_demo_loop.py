from simp_py import mon
import time
import gc
import machine

def thread_run():
    global mon,time,demos2
    try:
        from ex018_xled_kung_hei import XLED_CH
        x=XLED_CH()
        for i in range(6):
            x.run()
    except Exception as e:
        mon.log_exc(e)


if __name__=='__main__':
    _thread.start_new_thread('xled',thread_run,())
    from ex012_hello import hello
    hello()
    del hello
    
    from ex013_kung_hei import draw
    draw()
    del draw
    
    from ex011_christmas_mix2 import Christmas
    test=Christmas()
    test.run()
    del test
    
    from ex014_random2 import run
    run()
    del run

    from ex015_sin import SIN
    t=SIN()
    t.run()
    del t

    from ex019_intro import INTRO, TEXT_FILE
    t =INTRO(TEXT_FILE)
    t.run()    
    
    machine.reset()    
