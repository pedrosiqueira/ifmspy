from datetime import datetime
import time


def call_after(delay, callback, **kwargs):
    time.sleep(delay)
    callback(**kwargs)


def format_time(message):
    print(datetime.now(), message)


def nothing():
    format_time("I do nothing")


def sum(a, b):
    format_time(f"Sum: {a}+{b}={a+b}")


def greetings(name=None):
    format_time(f"Hello, {name if name else 'world'}!")


format_time("Valendo!")
call_after(3, nothing)
call_after(2, sum, a=4, b=3)
call_after(1, greetings, name="Pedro")
