def not_null(array):
    if (array == None):
        return "nullarray"
    else:
        for i in array:
            if (i == None):
                return "nullitem"
            else:
                pass

    return 0
