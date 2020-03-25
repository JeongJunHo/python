def func(x):
    if x > 0:
        return x
    else:
        return None

# origin
origin_list = list(filter(func, range(-5, 10)))
print(origin_list)
# lambda expression
lambda_list = list(filter(lambda x : x > 0, range(-5,10)))
print(lambda_list)
# generator expression
gen_list = [i for i in range(-5,10) if i > 0]
print(gen_list)