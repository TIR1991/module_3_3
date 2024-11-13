def print_params(a=1, b='строка', c=True):
    print(a,b,c)

print_params()
print_params(1991,27)
print_params(9)
print_params(b=25)
print_params(c = [1,2,3])


values_list = [2017,'тир',[20]]
values_dict = {'a':1991, 'b':"Ильдар", 'c':[1,9,9,1]}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [33, 'Ильдар']
print_params(*values_list_2, 42)
