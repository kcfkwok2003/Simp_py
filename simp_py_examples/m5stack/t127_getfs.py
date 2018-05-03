# getfs.py
def getfs():
  import os
  dt=[]
  fs = os.listdir()
  for fn in fs:
    tuplex = os.stat(fn)   # tuplex: ( .. )  
    fdict={'fn': fn,'mode':tuplex[0], 'size':tuplex[6], 'atime': tuplex[8]}
    dt.append("%(fn)s | %(size)s" % fdict)
  return dt

if __name__=='__main__':
    from simp_py import tft
    fs = getfs()
    tft.tft.text(0,50,fs[0])
