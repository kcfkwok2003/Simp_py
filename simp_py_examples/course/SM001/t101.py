"""
This is M5Stack micropython example
"""
import simp_py      # keyword “import”
# clear screen
simp_py.tft.tft.clear()     # module -> module -> object -> method()
# show message on screen
simp_py.tft.tft.text(0,0,"hello")

