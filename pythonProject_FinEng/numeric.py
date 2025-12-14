def is_valid_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def is_valid_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False