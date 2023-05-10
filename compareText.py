import sys
from vector import Vector
from sketch import Sketch

filenames = ["texts/1.txt", "texts/2.txt", "texts/3.txt"]
k = 5
d = 100000
sketches = [0 for i in filenames]
for i in range(len(filenames)):
    with open(filenames[i], 'r') as f:
        text = f.read()
        sketches[i] = Sketch(text, k, d)

print(' ' * 15, end="")
for filename in filenames:
    print('{:>22}'.format(filename), end="")
print()

for i in range(len(filenames)):
    print('{:15}'.format(filenames[i]), end="")
    for j in range(len(filenames)):
        print(('{:22}'.format(sketches[i].similarTo(sketches[j]))),end="")
    print()
