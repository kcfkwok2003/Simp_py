from simp_py import oled
def hello():
    global oled
    oled.fill(0)
    oled.text('hello',0,0)
    oled.text('world',0,10)
    oled.show()

if __name__=='__main__':
    hello()
