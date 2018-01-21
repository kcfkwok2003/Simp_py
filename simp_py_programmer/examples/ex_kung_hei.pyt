from simp_py import oled, mon
mc_width= 120
mc_height= 29
mc_bits = bytearray([
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x80, 0x01, 0x00, 0x00, 0x38, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x30,
   0x00, 0x00, 0x00, 0xc0, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x07, 0x07,
   0x00, 0x00, 0x30, 0x1f, 0x00, 0x00, 0xe0, 0x00, 0x00, 0x00, 0x00, 0x06,
   0x00, 0x06, 0x03, 0x00, 0xe0, 0xff, 0x07, 0x00, 0xf8, 0x3f, 0x0c, 0x00,
   0x40, 0x00, 0x0e, 0x00, 0x87, 0x17, 0x00, 0xc0, 0x75, 0x00, 0x00, 0xd0,
   0x33, 0x0e, 0x00, 0xff, 0x01, 0x0e, 0x00, 0xe6, 0x1f, 0x00, 0x00, 0x30,
   0x00, 0x00, 0xc0, 0x61, 0x07, 0x00, 0xc7, 0x01, 0x06, 0x80, 0xff, 0x03,
   0x00, 0x00, 0xfc, 0x07, 0x00, 0xc0, 0xc0, 0x00, 0x00, 0xc1, 0x01, 0x06,
   0x80, 0x86, 0x03, 0x00, 0x00, 0x5f, 0x01, 0x00, 0x66, 0x80, 0x01, 0x00,
   0xc3, 0x01, 0x06, 0x00, 0x86, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x6e,
   0x80, 0x03, 0x00, 0xf3, 0x01, 0x7e, 0x00, 0x86, 0xfd, 0x00, 0x00, 0xff,
   0x07, 0x00, 0x3c, 0xe0, 0x07, 0x00, 0xcf, 0xf9, 0x3f, 0x00, 0xff, 0xff,
   0x01, 0x00, 0x0b, 0x07, 0x00, 0xf8, 0xf9, 0x3e, 0x00, 0xc1, 0xf9, 0x0f,
   0xf8, 0x3f, 0x03, 0x00, 0x00, 0x02, 0x03, 0x00, 0xbc, 0xdb, 0x7c, 0x00,
   0xc3, 0x01, 0x07, 0x60, 0x0f, 0x04, 0x00, 0x00, 0xfe, 0x03, 0x00, 0x8e,
   0xc8, 0xf8, 0x03, 0xff, 0x81, 0x07, 0x00, 0x07, 0x1c, 0x00, 0x00, 0xdf,
   0x03, 0x00, 0xc7, 0xc9, 0xf0, 0x00, 0xeb, 0x81, 0x07, 0x00, 0x33, 0x18,
   0x00, 0x00, 0x83, 0x07, 0x80, 0xf1, 0xc8, 0x04, 0x00, 0xc3, 0xc1, 0x07,
   0x80, 0x61, 0x70, 0x00, 0x00, 0x06, 0x03, 0x40, 0x18, 0x8c, 0x07, 0x00,
   0xc1, 0xe1, 0x06, 0xc0, 0x60, 0xe0, 0x00, 0x00, 0x86, 0xfb, 0x03, 0x18,
   0x04, 0x02, 0x00, 0xff, 0x70, 0x06, 0x60, 0x60, 0xe0, 0x03, 0x00, 0xff,
   0xff, 0x03, 0xfc, 0xe1, 0x03, 0x00, 0x87, 0x38, 0x06, 0x30, 0x66, 0xd8,
   0x1f, 0xfe, 0x01, 0x00, 0x00, 0x8c, 0x9d, 0x03, 0x00, 0x2e, 0x0e, 0x06,
   0x18, 0x67, 0xb3, 0x0f, 0x2c, 0x80, 0x06, 0x00, 0x8c, 0xb9, 0x01, 0x00,
   0xe6, 0x04, 0x06, 0x04, 0x63, 0x76, 0x00, 0x80, 0xfd, 0x0f, 0x00, 0x80,
   0xf0, 0x00, 0x00, 0xc3, 0x01, 0x06, 0x80, 0x61, 0x66, 0x00, 0x80, 0x07,
   0x1e, 0x00, 0xc0, 0xe0, 0x01, 0x80, 0x81, 0x01, 0x06, 0xc0, 0x60, 0x6e,
   0x00, 0x00, 0x01, 0x0e, 0x00, 0xc0, 0xe0, 0x03, 0xc0, 0x80, 0x41, 0x07,
   0x00, 0x60, 0x04, 0x00, 0x00, 0x03, 0x06, 0x00, 0xe0, 0x70, 0x07, 0x40,
   0x00, 0x80, 0x07, 0x00, 0x78, 0x00, 0x00, 0x00, 0xff, 0x07, 0x00, 0x70,
   0x1c, 0x06, 0x00, 0x00, 0x00, 0x07, 0x00, 0x78, 0x00, 0x00, 0x00, 0xbf,
   0x03, 0x00, 0x70, 0x04, 0x0e, 0x00, 0x00, 0x00, 0x06, 0x00, 0x30, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00
])
BITM={0: 1, 1: 2, 2:4, 3:8, 4:0x10,5:0x20,6:0x40,7:0x80}
def draw():
    global mc_bits,BITM,mc_width,oled,mon
    import time
    frm = oled.framebuf
    x=0
    y=30
    mon.set_hist_len(30)
    mon.clean_hist()
    for bx in mc_bits:
        for j in range(8):
            b = bx & BITM[j]
            if b:
                frm.pixel(x,y,1)
            else:
                frm.pixel(x,y,0)
            x+=1
        if x>= mc_width:
            x=0
            y+=1
            mon.hist('%s x:%d y:%d\n' % (time.ticks_ms(),x,y))
    oled.show()
        
try:
    draw()
except Exception as e:
    mon.log_exc(e)

