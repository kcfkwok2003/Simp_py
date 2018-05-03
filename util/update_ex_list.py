import os
import string

EX_PATH='../simp_py_examples'
def work_on_path(path):
    print 'work_on_path(%s)' % path
    flist=[]
    files = os.listdir(EX_PATH+'/'+path)
    files.sort()
    for fn in files:
        if fn=='file.list':
            continue
        print fn
        flist.append(fn)
    flist_path= '%s/%s/file.list' % (EX_PATH,path)   
    f=open(flist_path,'w')
    f.write(string.join(flist,'\n'))
    f.close()
    print('%s updated' % flist_path)
        
def update_list():
    subpaths= os.listdir(EX_PATH)
    print 'subpaths:', subpaths
    for path in subpaths:
        if os.path.isdir(EX_PATH+'/'+path):
            print path, '-----------'
            work_on_path(path)

update_list()
