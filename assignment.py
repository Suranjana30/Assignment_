def print_it(a,b,c,d,e):
    print(f"the items are:{a,b,c,d,e}")
lst = [10,20,30,40,50]
tuple = ('mango','orange','banana','jackfruit','grapes')
set = {1,2,3,4,5}
dict = {'name':'Ajay','roll':'06','education':'CSE(DS) Undergraduate','country':'india','State':'West Bengal'}
float = (4.5,6.7,8.9,3.4,2.3)
int = (23,45,67,89,90)
print_it(*lst)
print_it(*tuple)
print_it(*set)
print_it(*dict)
print_it(*float)
print_it(*int)
