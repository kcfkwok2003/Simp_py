# getfs.py
def getfs():
  import os
  specials =['main.py','wifi_config.py','pass.key']
  dt =[ ]
  fs =os.listdir()
  for fn in fs:
    if fn not in specials:
      dt.append(fn)
  return dt
