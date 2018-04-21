import os
import string

EX_PATH='../simp_py_examples'
def work_on_path(path):
    flist=[]
    files = os.listdir(EX_PATH+'/'+path)
    files.sort()
    for fn in files:
        if fn=='file.list':
            continue
        flist.append(fn)
    flist_path= '%s/%s/file.list' % (EX_PATH,path)   
    f=open(flist_path,'w')
    f.write(string.join(flist,'\n'))
    f.close()
    print('%s updated' % flist_path)
        
def update_list():
    subpaths= os.listdir(EX_PATH)
    for path in subpaths:
        if os.path.isdir(path):
            print path, '-----------'
            work_on_path(path)

update_list()
