import re

data ="""
cho 770813-1551029
kim 800905-1049118
"""


min=re.compile("(\d{6})[-]\d{7}")
print(min.sub("\g<1>-*******",data))
