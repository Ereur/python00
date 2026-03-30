import math


def NULL_not_found(object: any) -> int:
    """Identifies and prints the type of all forms of 'Null' in Python."""
    obj_type = type(object)
    if object is None:
        print(f"Nothing : {obj_type}")
    elif obj_type is float and math.isnan(object):
        print(f"Cheese : {obj_type}")
    elif obj_type is int and object == 0:
        print(f"Zero : {obj_type}")
    elif obj_type is str and object == '':
        print(f"Empty : {obj_type}")
    elif obj_type is bool and object is False:
        print(f"Fake : {obj_type}")
    else:
        print("Type not Found")
        return 1
    return 0
