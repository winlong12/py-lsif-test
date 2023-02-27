from .scr1 import src1_fun
from .scr1 import src1_fun2 as alias_fun
from .inner.inner_scr1 import INNER_SRC_Class
from .inner.inner_scr1 import INNER_SRC1 as Alia

def fun(a, b):
    c = a + b
    return c

d = fun(1,2)
e = INNER_SRC_Class()
e.inner_fun(d)

f = INNER_SRC_Class().inner_fun(e)

g = alias_fun(d)

class A:
    def a_fun(self):
        a = 1 + d
        aa: INNER_SRC_Class = INNER_SRC_Class()
        return a

class B(A):
    def b_fun(self, b: A):
        b = A()
        return [b, e]

Bb = B()

list = [src1_fun(d), Alia]

map = {'d': d, 'func': fun}

export = [A, fun]
