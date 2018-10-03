# for realization
#def filter_list(l):
#    l1 = list();
#    for item in l:
#        if isinstance(item,int):
#            l1.append(item);
#    print(l1);
#    return l1;

# list comprehension
#def filter_list(l):
#    res = [res for res in l if isinstance(res, int)]
#    print(res);
#    return res;

# filter + lambda
def filter_list(l):
    res = list(filter(lambda x: isinstance(x, int), l))
    print(res);
    return res;


filter_list([1,2,'a','b']);
filter_list([1,'a','b',0,15]);
filter_list([1,2,'aasf','1',123,'123']);