import time
gen_start_time = time.time()
print(sum(n for n in range(1000000)))
gen_stop = time.time() - gen_start_time

list_start_time = time.time()
print (sum([n for n in range(1000000)])
list_time = time.time() - list_start_time

print(f'sum(n for n in range(1000000)) took: {gen_time}')
print(f'sum([n for n in range(1000000)]) took: {list_time}')


#Allows you to compare speed of each method, generator v. list
#Notice that generator is 4 seconds faster