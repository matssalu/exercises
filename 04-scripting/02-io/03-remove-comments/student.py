import sys
import re

with open(sys.argv[1], 'r') as file:
    contents = file.read()
    contents = re.sub('#.*$', '', contents, flags=re.MULTILINE)
    
    with open(sys.argv[1], "w") as file2:
        file2.write(contents)