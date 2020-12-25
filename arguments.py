# args kwargs
def func_name(*args):
	print(args)
	print(type(args))
# type = tuple
func_name(2, 4, 6, "ColdFusion")

def print_args(*args):
	for arg in args:
		print(arg)

print_args('book', 'paint', 'case', 'hammer')

# kwargs
def kwarg_func(**kwargs):
	print(kwargs)
	print(type(kwargs))

kwarg_func(name='Jason', drink='rum', hobby='coding')


def kwarg_func(**kwargs):
	for key, value in kwargs.items():
		print(f"Key: {key}  Value: {value}")
	
kwarg_func(name='Jason', drink='rum', hobby='coding')

# ordering function
def order(name, *args, **kwargs):
	print(f"Hello {name}")
	for arg in args:
		print(f"You ordered: {arg}\n")

	if kwargs.get("address"):
		address = kwargs.get("address")
		print(f"Delivering to {address}\n")

your_order = order("Jason", "Hamburgers", "Fries", "Shake", address="104 Beach Way")
print(your_order)

