import sys
import os
import inspect

def module_path(local_function):
    return os.path.dirname(inspect.getsourcefile(local_function))
