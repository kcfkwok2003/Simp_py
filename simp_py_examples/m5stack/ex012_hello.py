from simp_py import tft
def hello():
    global tft
    tft.tft.clear()
    tft.tft.text(0,0,'hello')
    tft.tft.text(0,20,'world')

if __name__=='__main__':
    hello()
