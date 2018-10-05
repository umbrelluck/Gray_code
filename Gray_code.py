def makeCode(item):
    """
    item - iterable or positive integer
     returns iterable or positive integer or string if input not valid
    """
    if type(item) == list:
        codded_list = []
        for elem in item:
            codded_list.append(elem ^ (elem >> 1))
        return codded_list
    elif type(item) == int:
        return item ^ (item >> 1)
    else:
        return 'Not valid input'


def deCode(item):
    """
    item - iterable or positive integer
     returns iterable or positive integer or string if input not valid
    """
    if type(item) == list:
        decodded_list = []
        for elem in item:
            res, elem_copy = elem, elem >> 1
            while elem_copy != 0:
                res ^= elem_copy
                elem_copy >>= 1
            decodded_list.append(res)
        return decodded_list
    elif type(item) == int:
        res, elem_copy = item, item >> 1
        while elem_copy != 0:
            res ^= elem_copy
            elem_copy >>= 1
        return res
    else:
        return 'Not valid input'
