# A list comnprehension combine the for loops and the creation of new element into one line and autamatically append each new element
from math import factorial


cube=[value**3 for value in range(1,11)]
print(cube)

odd_number=[value+2 for value in range(1,11,2)]
print(odd_number)

factoral=[value]