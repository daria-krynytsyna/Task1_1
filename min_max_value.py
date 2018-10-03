def min_max(l):
    res = [int(res) for res in l if isint(res)]
    print(res);
    print("min value: {0}; max value: {1}".format(min(res), max(res)))



def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
min_max(numbers);
