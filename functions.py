def func_name():
	print("Hello")

func_name()

def add_two_numbers(num1, num2):
	answer = num1 + num2 + 8.90
	# print(answer)
	return answer

# add_two_numbers(100, 200)

total = add_two_numbers(150, 200)
print(total)


def add_two_numbers(num1, num2):
	answer = num1 + num2 + 8.90
	# print(answer)
	return answer

total = add_two_numbers(150, 200)
print(total)


def greeting(name):
	return f"Hello, {name}"

result = greeting("Jason")
print(result)
print(result.count('a'))
print(result.upper())

# can drink
def check_age(age):
	if age >= 21:
		return True
	else:
		return False

user_drink = check_age(20)
print(user_drink)

# default function params
def greeting(name="User"):
	print(f"Hello {name}")
greeting()


def create_person(name, age, role='Developer', required_books=5):
	person = {
		'person_name' : name,
		'person_age' : age,
		'person_role' : role,
		'total_books' : required_books
	}
	return person

new_user = create_person('Jason', 28, 'Application Developer')
print(new_user)


# Lambda Function
square = lambda num: num**2
print(square(5))

add = lambda num1, num2: num1 +num2

print(add(10,8))

# Python Scope
# LEGB 
# Local, Enclosed Function Locals,  Global, Built in Python Library
language = "Python"

def change_language():
	language = "Javascript"
	return language

print(language) # Python
func_lang = change_language() # Javascript
print(func_lang)

name = "Jason" #global
def greeting():
	name = 'Savvy' #Enclosing

	def say_hello():
		name = "Bryndle" #Local
		print(f"Name is {name}")

	say_hello()

print(greeting())



