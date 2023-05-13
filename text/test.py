import sys
import re

pattern = r'^\d+(\.)?(\s)?.+(?:\d+[\w\s]+)?$'
text = '22. Shumin Zhang- 张淑敏 1箱'

if re.match(pattern,text): print(text)