# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:26:13 2024

@author: Aamir Ali
"""

import re

#Check if "ain" is present at the end of a WORD:
txt = "The rain in Spain"

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

