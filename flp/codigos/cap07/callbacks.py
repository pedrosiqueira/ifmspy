import time

def call_after(delay, callback, **kwargs):
    time.sleep(delay)
    callback(**kwargs)

from datetime import datetime

def format_time(message):
    print(datetime.now(), message)

def nothing():
    format_time("I do nothing")

def sum(a, b):
    format_time(f"Sum: {a}+{b}={a+b}")

def greetings(name=None):
    format_time(f"Hello, {name if name else "world"}!" )

class Repeater:
    def __init__(self, times=3, delay=1):
        self.count = 0
        self.times = times
        self.delay = delay

    def repeat(self):
        format_time(f"repeat {self.count}")
        self.count += 1
        if self.count < self.times:
            call_after(self.delay, self.repeat)
        
call_after(3, nothing)
call_after(2, sum, a=4, b=3)
call_after(1, greetings, name="Pedro")
repeater = Repeater()
call_after(4, repeater.repeat)

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    executor.submit(call_after, 3, nothing)
    executor.submit(call_after, 2, sum, a=4, b=3)
    executor.submit(call_after, 1, greetings, name="Pedro")
    repeater = Repeater()
    executor.submit(call_after, 4, repeater.repeat)

