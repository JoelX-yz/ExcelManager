""" 
"""

import re

def properWords(text):
    if isinstance(text,str):
        return re.sub('[^\u4e00-\u9fa5^\u3131-\ucb4c^a-z^A-Z^0-9^\^/^.^()^%^*^-^+~^$^@^#^!]','',text)
    
    return "NONAME"

def phoneNum(text):
    if text is None:
        return 'NULL'
    temp = re.sub('[^0-9]','',text)
    if len(temp) == 10:
        return re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1)\2-\3', temp)
    else:
        return re.sub(r'(\d{1})(\d{3})(\d{3})(\d{4})', r'(\2)\3-\4', temp)

def deBarcket(text):
    return re.sub('^,^()','',text)

def getDateFromFilename(text):
    return text.replace(".xlsx","").replace("LifePlus","").replace("-"," ").strip()