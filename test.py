# TODO: turn these into unit tests
from PyInputGuard import *

if __name__ == "__main__":
    print(enforceInt("Int pass: "))
    print(enforceInt("Int fail: "))
    print(enforceFloat("Float pass: "))
    print(enforceFloat("Float fail: "))
    print(enforceStringFormat("String pass (hello1): "))
    print(enforceStringFormat("String fail: ", "hello[0-9]+"))
    print(enforceBool("bool pass: "))
    print(enforceBool("bool fail: "))