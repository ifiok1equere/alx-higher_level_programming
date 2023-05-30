#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except ZeroDivisionError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    except IndexError as t:
        print("Exception: ".format(t), file=sys.stderr)
    except Exception as p:
        print("Exception: {}".format(p), file=sys.stderr)
        return None
