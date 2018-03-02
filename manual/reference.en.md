# Reference

## Python 關鍵字(keywords)

```
False None True and as assert break 
class continue def del elif else except
finally for from global if import in
is lambda nonlocal not or pass raise 
return try while with yield
```

### 有用連結
Python 关键字
  http://blog.csdn.net/liang19890820/article/details/68488392

python关键字详解
  https://www.cnblogs.com/xueweihan/p/4518022.html
  
python 学习笔记 -- Python关键字总结
  http://blog.csdn.net/jingwuge/article/details/48519689

List of Keywords in Python
  https://www.programiz.com/python-programming/keyword-list

## Python 內建函數(built-in functions)

```
abs() all()  any() bin() bool() bytearray() bytes()
callable() chr() classmethod() compile() complex()
delattr() dict() dir() divmod() enumerate() eval() exec()
filter() float() frozenset() getattr() globals()
hasattr() hash() help() hex() id() input() int()
isinstance() issubclass() iter() len() list() locals()
map() max() memoryview() min() next() object() oct()
open() ord() pow() print() property() range() repr()
reversed() round() set() setattr() slice() sorted()
staticmethod() str() sum() super() tuple() type() zip() \
__import__()

```

### 有用連結
Python 内置函数
  http://www.runoob.com/python/python-built-in-functions.html

Python内置函数详解——总结篇
  http://blog.csdn.net/oaa608868/article/details/53506188

Built-in Functions
  https://docs.python.org/2/library/functions.html
  
## MicroPython (esp32) 常用程式庫簡介

### 內建函數模組

ESP32 是繼承ESP8266 的, 由於Micopython 官方未有ESP32 的文件,這裡主要參考 ESP8266的文件.
但文件描述的函數 ESP32 不一定都已實現. 可用 dir 列出模組支援的函數.

有些函數是python 的標準函數名前加上"u"表示是Micropython 的函數庫. 在引入時可以不加"u"
例如 import utime 和 import time 都是可以的.

array - arrays of numeric data
  http://docs.micropython.org/en/latest/esp8266/library/array.html

gc - control of garbage collector
  http://docs.micropython.org/en/latest/esp8266/library/gc.html

math - mathematical functions
  http://docs.micropython.org/en/latest/esp8266/library/math.html

sys - system specific functions
  http://docs.micropython.org/en/latest/esp8266/library/sys.html

ubinascii – binary/ASCII conversions
  http://docs.micropython.org/en/latest/esp8266/library/ubinascii.html

ucollections - collections and container types
  http://docs.micropython.org/en/latest/esp8266/library/ucollections.html

uerrno – system error codes
  http://docs.micropython.org/en/latest/esp8266/library/uerrno.html

uhashlib – hashing algorithms
  http://docs.micropython.org/en/latest/esp8266/library/uhashlib.html

uheapq – heap queue algorithm
  http://docs.micropython.org/en/latest/esp8266/library/uheapq.html

uio – input/output streams
  http://docs.micropython.org/en/latest/esp8266/library/uio.html

ujson – JSON encoding and decoding
  http://docs.micropython.org/en/latest/esp8266/library/ujson.html

uos – basic “operating system” services
  http://docs.micropython.org/en/latest/esp8266/library/uos.html

ure – simple regular expressions
  http://docs.micropython.org/en/latest/esp8266/library/ure.html

uselect – wait for events on a set of streams
  http://docs.micropython.org/en/latest/esp8266/library/uselect.html

usocket – socket module
  http://docs.micropython.org/en/latest/esp8266/library/usocket.html

ussl – SSL/TLS module
  http://docs.micropython.org/en/latest/esp8266/library/ussl.html

ustruct – pack and unpack primitive data types
  http://docs.micropython.org/en/latest/esp8266/library/ustruct.html

utime – time related functions
  http://docs.micropython.org/en/latest/esp8266/library/utime.html

uzlib – zlib decompression
  http://docs.micropython.org/en/latest/esp8266/library/uzlib.html

### Micropython 特殊模組

這些模組不是Python 的標準模組.

btree – simple BTree database
  http://docs.micropython.org/en/latest/esp8266/library/btree.html

framebuf — Frame buffer manipulation
  http://docs.micropython.org/en/latest/esp8266/library/framebuf.html

machine — functions related to the hardware
  http://docs.micropython.org/en/latest/esp8266/library/machine.html

micropython – access and control MicroPython internals
  http://docs.micropython.org/en/latest/esp8266/library/micropython.html

network — network configuration
  http://docs.micropython.org/en/latest/esp8266/library/network.html

uctypes – access binary data in a structured way
  http://docs.micropython.org/en/latest/esp8266/library/uctypes.html

### 與 ESP 有關的模組
esp — functions related to the ESP8266
  http://docs.micropython.org/en/latest/esp8266/library/esp.html


## Simp_py 模組簡介

Simp_py 模組是專為 Simp-py 固件應用在特定硬體上而度身定制的.
它主要兩個功能

### mon 用於監測功能

* mon 支持以下功能

  mon.chk_ureq()     # 檢查有無遙控指示
  mon.get_ureq()     # 讀取遙控指示
  mon.put_uresp(msg) # 以msg 回應遙控指示
  
  mon.set_hist_len(n) # 設定history 緩衝區長度
  mon.clean_hist()    # 清除history 緩衝區
  mon.hist(msg)       # 加 msg 到緩衝區
  
  mon.log_exc(exc)    # 配合try except 取得的錯誤 exc 存到日誌中. 
  mon.data            # 監測字典, 存到監測字典中的數據能在監察頁讀取.

### 板上顯示器驅動

這和硬體有關
oled 物件, 適用於 Wifi Kit 32
tft  物件, 適用於 M5Stack

* oled 支持以下功能
  oled.contrast(contrast)
  oled.fill(color)
  oled.invert(invert)
  oled.pixel(x,y, color)
  oled.poweroff()
  oled.scroll(dx,dy)
  oled.show()
  oled.text(string, x, y, color=1)

* tft 支持以下功能
  tft.on()
  tft.off()
  tft.tft.pixel(x,y,color)
  tft.tft.readPixel(x,y)
  tft.tft.line(x,y,x1,y1,color)
  tft.tft.lineByAngle(x,y,start,length,angle[,color])
  tft.tft.triangle(x,y,x1,y1,x2,y2,[,color,fillcolor])
  tft.tft.circle(x,y,r,[,color,fillcolor])
  tft.tft.ellipse(x,y,rx,ry[,opt,color,fillcolor])
  tft.tft.arc(x,y,r,thick,start,end[,color,fillcolor])
  tft.tft.poly(x,y,r,sides,thick[,color,fillcolor,rotate])
  tft.tft.rect(x,y,width,height[,color,fillcolor])
  tft.tft.roundrect(x,y,width,height,r[,color,fillcolor])
  tft.tft.clear([color])
  tft.tft.clearWin([color])
  tft.tft.font(font[,rotate,transparent,fixedwidth,dist,width,outline,color])
  tft.tft.attrib7seg(dist,width,outline,color)
  tft.tft.fontSize()
  tft.tft.print(text[,x,y,color,rotate,transparent,fixedwidth,wrap])
  tft.tft.text(x,y,text[,color])
  tft.tft.textWidth(text)
  tft.tft.textClear(x,y,text[,color])
  tft.tft.image(x,y,file[,scale,type])
  tft.tft.setwin(x,y,x1,y1)
  tft.tft.resetwin()
  tft.tft.savewin()
  tft.tft.restorewin()
  tft.tft.screensize()
  tft.tft.winsize()
  tft.hsb2rgb(hue,saturation,brightness)
  tft.tft.compileFont(file_name[,debug])
  詳情參考 : https://github.com/m5stack/M5Cloud
  

## 其他有用連結
MicroPython tutorial for ESP8266
  (ESP32 是繼承ESP8266 的, 由於Micopython 官方未有ESP32 的文件,請參考 ESP8266的文件)
  http://docs.micropython.org/en/latest/esp8266/
  http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/index.html

MicroPython libraries
  http://docs.micropython.org/en/latest/esp8266/library/index.html

ESP8266 and ESP32 Differences in One Single Table
  https://www.cnx-software.com/2016/03/25/esp8266-and-esp32-differences-in-one-single-table/

micropython/ports/esp32 源碼 (用於建立 wifi kit 32 固件)
  https://github.com/micropython/micropython/tree/master/ports/esp32

MicroPython_ESP32_psRAM_LoBo 源碼 (用於建立 M5Stack 固件)
  https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo

Differences to CPython
  https://github.com/micropython/micropython/wiki/Differences


