# navigate to dir: py run.py
name = "Jason" #global
def greeting():
	name = 'Savvy' #Enclosinh

	def say_hello():
		name = "Bryndle" #Local
		print(f"Name is {name}")

	say_hello()

print(greeting())