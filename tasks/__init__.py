from os import listdir, getcwd
from os.path import isfile, join, splitext

if (__name__ == '__main__'):
    cd = getcwd()
else:
    cd =  './tasks/'

tasks_for_test = [splitext(f)[0] for f in listdir(cd) if isfile(join(cd,f)) and splitext(join(cd,f))[1] == '.py']
tasks_for_test.remove('__init__')

__all__ = tasks_for_test
