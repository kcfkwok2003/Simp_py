from song import *

NOTES=  [e,e,e,e,e,e,e,g,c,d,e,f,f,f,f,f,e,e,e,e,d,d,e,d,g]
DURATIONS=[400,400,800,400,400,800,400,400,400,400,1600,400,400,400,400,400,400,400,400,400,400,400,400,800,800]
song=SONG(25)
song.set_notes(NOTES,DURATIONS)

if __name__=='__main__':
    song.play()
