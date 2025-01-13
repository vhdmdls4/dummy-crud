# simple division
print(9/4)
# common \n, isnt necessary using print cause it already breaks
print("\n")
# division discarding fractional part
print(9//4)
# getting the remainder of the division
print(9%4)
# multiplying float values
print(2.3233*4)
# testing multiple values in print
print(2, 3, 5, 2*2.5)
# power calculation
print(2**3)
# assign variable
foo: str = "anything"
print(foo)
# TypeError: can only concatenate str (not "int") to str
# print(foo.+3)
# NameError: name 'var' is not defined
# print(var)
# dealing with quotes inside print
print('spam\'t')
# dealing with backslashes inside strings
# wrong ->
print('C:\some\name')
# right ->
print(r"C:\some\name")
# print with multiple lines
print("""
Try this one
    -h display usage message
    -H hostname to connect to
""")
# concat with +
print("ok, é ass" + "im")
# concat automatic without symbols between strings
print("Try this " "one")
txt = "join strings with multiple ones, " 'is a good feature implemented natively ' "in Python."
print(txt)
prefix = "Try this 2"
rest_of_string = ' one'
print(prefix + rest_of_string + " " + rest_of_string)
# its possible to treat strings like vectors in python
print(prefix[2])
# print till number 2 or third item in array
print(prefix[:2])
# print starting number 2 or third item in array
print(prefix[2:])
# strings can be accessed backwards using negative index and associated with :
print("//////////////////")
print(prefix[-2])
print(prefix[-1])
print(prefix[:-1])
# trying access index invalid: IndexError:string indexoutofrange



# int float bool str dict tuple list

