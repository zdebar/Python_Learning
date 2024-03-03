import numpy as np
import re

pattern = re.compile("^[A-Z]+$")  #Control str for big letter, + at least one character
print(pattern.search("Hello World"))
print(pattern.search("HELLOWORLD"))
print("OK")