# sync_modules.py
# author: C.F. Kwok
# date: 2018-1-3
# run this in vagrant

import shutil
sync_files=['app','passcode','passcodelib','server','simp_py','start','input','m5stack','max7219','m8x8','simp_py_sec']
sync_dir='/home/vagrant/MicroPython_ESP32_psRAM_LoBo-master/MicroPython_BUILD/components/micropython/esp32/modules'
#sync_dir='/home/vagrant/micropython-esp32/ports/esp32/modules'
def sync():
    for fn in sync_files:
        fn = fn +'.py'
        print 'copy %s to %s' % (fn, sync_dir)
        shutil.copy2(fn, sync_dir)

def clean():
    for fn in sync_files:
        fn = fn +'.py'
        try:
            print 'remove %s' % fn
            os.remove(sync_dir +'/' + fn)
        except:
            print 'exc'
            
if __name__=='__main__':
    import sys,os
    
    if len(sys.argv) >1:
        print '%s' % `sys.argv` 
        if sys.argv[1]=='clean':
            clean()
        sys.exit()
    sync()
