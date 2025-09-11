#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except (ZeroDivisionError):
        pass # This should be 'raise' according to Adrian. I didn't run it but worth considering next time
    finally:
        print("Inside result: {}".format(result))
        return result
