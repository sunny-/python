def countSubStringMatchRecursion(target, key):
    '''uses key string to match target string and
    return the number of times key matches the target'''
    index = str.find(target, key)
    if index == -1:
        return 0
    else:
        return 1 + countSubStringMatchRecursion(target[index+len(key):], key)


def test_countSubStringMatchRecursion():
    print(countSubStringMatchRecursion("atgacatgcacaagtatgcat","atgc"))
    print(countSubStringMatchRecursion("atgacatgcacaagtatgcat","at"))
    print(countSubStringMatchRecursion("atgacatgcacaagtatgcat","cat"))
    print(countSubStringMatchRecursion("atgacatgcacaagtatgcat","agyj"))
