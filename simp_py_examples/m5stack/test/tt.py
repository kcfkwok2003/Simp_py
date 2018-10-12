import os.path,sys

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

prog='''
import machine
gg =globals()
ggk = gg.keys()
print ('ggk:%s' % ggk)
print ('gdata1:%s' % id(gdata1))
print( 'machine: %s' % dir(machine))
'''

import machine
gdata1 = machine.gdata1
print('*gdata1:%s' % id(gdata1))
exec(prog, {'gdata1':gdata1})



