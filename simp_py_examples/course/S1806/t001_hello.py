"""
t001.py
This is M5Stack micropython example
"""
import simp_py      # keyword    
# clear screen
simp_py.lcd.clear()     # module -> object -> method()
# show message on screen
simp_py.lcd.text(0,0,'hello')
