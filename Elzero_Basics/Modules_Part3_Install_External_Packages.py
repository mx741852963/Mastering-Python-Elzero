# ---------------------------------------
# -- Modules Install External Packages --
# ---------------------------------------
# [1] Module Vs Package
# [2] External Packages Download From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install The Package And Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages And Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/"
# --------------------------------------------------------------
import termcolor
import pyfiglet
from colorama import init

init()
# print(dir(termcolor))
# print(dir(pyfiglet))
# print(pyfiglet.figlet_format("Ahmad"))
print(termcolor.colored(pyfiglet.figlet_format("Ahmad"), color="red", on_color="on_yellow"))
