import uuid
from datetime import datetime


class _TProperty:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)
    def __set__(self, instance, value):
        # if not readonly:
        instance.__dict__[self.name] = value

class _TPropertyTyped(_TProperty):
    expected_type = type(None)
    def __set__(self, instance, value):
        if not isinstance(value, (self.expected_type,type(None))):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)

class _TPropertyUnsigned(_TProperty):
    def __set__(self, instance, value):
        if value is not None:
            if value < 0:
                raise ValueError('Expected >= 0')
        super().__set__(instance, value)

class _TPropertyReadOnly(_TProperty):
    def __init__(self, name=None, **opts):
        setattr(self,'readonly', False)
        # if 'readonly' not in opts:
        #     raise TypeError('missing readonly option')
        super().__init__(name, **opts)
    def __set__(self, instance, value):
        if not self.readonly:
            if value is not None:
                if value < 0:
                    raise ValueError('Expected >= 0')
            super().__set__(instance, value)
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # self.readonly=True
        else:
            raise ValueError('ReadOnly')


class _TPropertySized(_TProperty):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)

#  Simple Type
class TPropertyStrSized(_TPropertyTyped, _TPropertySized):
    expected_type = str

class TPropertyInt(_TPropertyTyped):
    expected_type = int

class TPropertyUnInt(TPropertyInt, _TPropertyUnsigned):
    pass

class TPropertyUnROInt(_TPropertyReadOnly, TPropertyInt, _TPropertyUnsigned ):
    readonly = True
    pass


class TPropertyFloat(_TPropertyTyped):
    expected_type = float

class TPropertyUnFloat(TPropertyFloat, _TPropertyUnsigned):
    pass

class TPropertyDate(_TPropertyTyped):
    expected_type = datetime

class TPropertyUUID(_TPropertyTyped):
    expected_type = uuid.UUID

class TPropertyObject(_TPropertyTyped):
    expected_type = object


class TAddress:
    region_id = TPropertyUnInt('region_id')
    region =    TPropertyStrSized('region', size=255)
    distr_id =  TPropertyUnInt('distr_id')
    distr =     TPropertyStrSized('distr', size=255)
    def __init__(self, **kwargs):
        pass



class TPropertyAddress(_TPropertyTyped):
    expected_type = TAddress


def main():
    pass


if __name__ == '__main__':
    main()
