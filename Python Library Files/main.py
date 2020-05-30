from imports import *

#Math
def sqrt(val):
    if val > 0:
        return math.sqrt(val)
    elif val < 0:
        return complex(0 + sqrt(-1 * val))

def root(x, root):
    return pow(x, 1 / root)

def rand(valmin, valmax):
    return random.randint(valmin, valmax)

def map(value, valmin, valmax, mapmin, mapmax):
    valmax = (valmax - valmin)
    mapmax = (mapmax - mapmin)
    return (value - valmin) * (mapmax / valmax) + mapmin

def exp(x):
    return sum([
        x**n /factorial(n)
        for n in range(100)
    ])

def factorial(val):
    return math.factorial(val)

def pow(x, val):
    return x**val


#Pynput
keyboard = Controller()

def key_type(text):
    sleep(0.1)
    keyboard.type(text)

def key_press(ch):
    keyboard.press(ch)
    keyboard.release(ch)

def sleep(sec):
    return time.sleep(sec)
