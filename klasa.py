#! /usr/bin/env python3
import sys
class klasa:
    def __init__(self,x):
        self.x = x
    def string(self, s):
        return self.x.join(s)
k=klasa('x')
print(k.string(sys.argv))

class Inna:
    def __str__(self):
        return "siema"
i = Inna()
print(i)


