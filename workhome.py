import sys


def introspection_info(obj):
    obj_info = {}


    obj_info['type'] = type(obj).__name__


    obj_info['attributes'] = dir(obj)


    obj_info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]


    obj_info['module'] = obj.__mod__


    if obj_info['type'] == 'int':
        obj_info['min_value'] = -sys.maxsize - 1
        obj_info['max_value'] = sys.maxsize
    elif obj_info['type'] == 'float':
        obj_info['min_value'] = -sys.float_info.max
        obj_info['max_value'] = sys.float_info.max
    elif obj_info['type'] == 'str':
        obj_info['length'] = len(obj)

    return obj_info

number_info = introspection_info(42)
print(number_info)