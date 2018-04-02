# getfs.py
def getfs():
  import os
  specials =['main.py','wifi_config.py','pass.key']
  fs = os.listdir()
  for i in range(len(fs)-1, -1, -1):
    if fs[i] in specials:
      del fs[i]
  return fs

if __name__=='__main__':
  from simp_py import tft
  fs = getfs()
  tft.tft.text(0,50,fs[0])
