import inspect
from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj)
    attributes = dir(obj)

    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    module = inspect.getmodule(obj)
    module_name = module.__name__ if module else "Unknown"

    additional_info = {}

    if inspect.isclass(obj):
        additional_info['bases'] = obj.__bases__
        additional_info['mro'] = obj.__mro__
    elif inspect.ismodule(obj):
        additional_info['file'] = inspect.getfile(obj)
    elif isinstance(obj, (list, tuple, set, dict)):
        additional_info['length'] = len(obj)
    elif isinstance(obj, (int, float, str)):
        additional_info['repr'] = repr(obj)

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name,
        'additional_info': additional_info
    }

    return info


number_info = introspection_info(42)
pprint(number_info)
