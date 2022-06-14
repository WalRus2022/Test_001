from collections import defaultdict

from Objects.TProperty import TPropertyStrSized


class TParam:
    _prm_name = TPropertyStrSized('_prm_name', size=50)
    _prm_type = type(None)
    _prm_value = None

    @classmethod
    def addparam(cls, prm_name, prm_type, prm_value):
        prm = cls.__new__(cls)
        prm._prm_type = prm_type
        prm._prm_name = prm_name
        prm._prm_value = prm_value
        return prm


class TParams(defaultdict):
    pass


def main():
    pass

if __name__ == '__main__':
    main()
