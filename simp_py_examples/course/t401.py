from m8x8 import M8X8
from font8x8 import get_font8x8
# M8X8(sck,din,css)
mx=M8X8(19,23,18,2,1)            
while 1:
    for i in range (33,128):
        data = get_font8x8(i)
        for i in range(8):
            bx, data = data[0], data[1:]
            mx.maxOne(1,i, bx)
        time.sleep(0.2)
    time.sleep(2)    
