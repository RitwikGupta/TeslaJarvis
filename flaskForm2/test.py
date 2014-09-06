#!venv/bin/python

a = []
def decorator(func):
	def innerfunc():
		a.append("this is first added")
		func() #does mainfunc
		a.append("this is second added")
	return innerfunc

@decorator
def mainfunc():
	a.append("this is added in main func")
	print a #prints before finishing the decorator

mainfunc()
print a