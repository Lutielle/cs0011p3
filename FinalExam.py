#===
#CS001X Take-Home FinalExam

# This exam is 20 questions.

# You may only use the textbook, the slides, your lecture notes, and the
# example code from lecture as references when completing this exam. You are
# allowed to use or reference any other materials or resource in completing
# this exam (e.g., you cannot use any other online resources aside from the
# textbooks/slides/lecture notes/example code, you cannot discuss the exam with
# your classmates, etc). Violating these instructions will be considered an
# academic integrity violation and penalized according to the course policy.
# Please confirm your agreement by adding your name to the honor statement
# below and indicating that you have read and agree to the honor statement.

# For each question, you should only add code between the comments

#=== START YOUR CODE HERE

# and

#--- END YOUR CODE HERE

# Remove the `pass` keyword and replace it with your code.

# You should only be adding code between these comments for each question and
# updating the values of the 7 variables below (`student_name`, `username`,
# `peoplesoft_number`, `lecture_days`, `section`, `honor_statement`, and
# `i_read_and_agree`)

# DO NOT CHANGE ANY OF THESE VARIABLE NAMES!
# Only change the assigned values

# Your full name
student_name = "Karen Chen"

# Set to your Pitt username (e.g., "nlf4")
username = "kjc90"

# Change to your peoplesoft number
peoplesoft_number = 3955245

# Change to "TH" if you have lecture on Tues/Thurs.
lecture_days = "MW"

# Change to 11 or 12, depending on your section
section = 11

# Read the following honor statement, replace your name in the statement and
# then indicate that you have read and agree to the honor statement. Do not
# change any other text in the honor statement.
honor_statement = """
By submitting this examination, I, Karen Chen, pledge on my honor, and with
acceptance of the consequences laid out in all applicable policies, that I have
neither given nor received any unauthorized assistance on this evaluation, and
that the work submitted upholds the highest standards of honesty and academic
integrity.
"""
i_read_and_agree = True
#---


### Question1
# Use the `format()` function to return the float argument as a string that
# is 10 total characters long, 3 digits after the decimal point, center
# aligned with the ! character filling in non used character spaces.
def question1(a_float=7.82593495):
	#=== START YOUR CODE HERE
	formatted = format(a_float, "!^10.3f")
	return formatted
	#--- END YOUR CODE HERE


### Question2
# Assign Boolean values to a, b, c, and d such that this function returns True
def question2():
	#=== START YOUR CODE HERE
	a = True
	b = False
	c = False
	d = True
	#--- END YOUR CODE HERE
	return (not ( not a or b) and ( not c and d) and (d or c))

### Question3
# Have this function return True if any two of the argument `a`, `b`, and `c`
# are True, but return False if all three are True or if fewer than 2 are True
def question3(a=True, b=True, c=True):
	#=== START YOUR CODE HERE
	if a and b and c == True:
		return False
	elif a or b or c == False:
		return True
	elif a or b == False:
		return False
	elif a or c == False:
		return False
	elif b or c == False:
		return False
	else:
		return True
	#--- END YOUR CODE HERE


### Question4
# Have this function return False.
# No bamboozle, its just that easy.
# You're welcome.
def question4():
	#=== START YOUR CODE HERE
	return False
	#--- END YOUR CODE HERE


### Question5
# Use a for loop to add all of the odd numbers between 10 and 30 to a list.
# Return that list.
def question5():
	#=== START YOUR CODE HERE
	odds = []
	for i in range(11, 30, 2):
		odds.append(i)

	return odds
	#--- END YOUR CODE HERE


### Question6
# Use a for loop to add all of the even numbers between 9 and 31 to a list in
# descending order. Return that list.
def question6():
	#=== START YOUR CODE HERE
	evens = []
	for i in range(30, 9, -2):
		evens.append(i)

	return evens
	#--- END YOUR CODE HERE


### Question7
# Use a for loop to find and to return the largest integer in a list argument
# You cannot use the builtin function `max()` to solve this question.
def question7(a_list=[10, 5, 95, 8, 2, 29, 97, 18]):
	#=== START YOUR CODE HERE
	pass
	#--- END YOUR CODE HERE


### Question8
# Return a count of the number of characters in the file named `fname`. Return
# None if the file named `fname` does not exist, or you are unable to open it
# for any reason.
def question8(fname="question8.txt"):
	#=== START YOUR CODE HERE
	try:
		curfile = open(fname)
		characters = 0
		for line in curfile:
			characters = characters + len(line)
	except:
		None
	#--- END YOUR CODE HERE


### Question9
# Attempt to convert the arugment `a_string` to an integer and return that
# integer. Return None if `a_string` cannot be converted to an integer.
def question9(a_string="7"):
	#=== START YOUR CODE HERE
	try:
		return int(a_string)
	except:
		return None
	#--- END YOUR CODE HERE


### Question10
# Return the contents of `a_list` stored as a tuple
def question10(a_list=[1, 5, 8, 2, 10]):
	#=== START YOUR CODE HERE
	return tuple(a_list)
	#--- END YOUR CODE HERE


### Question11
# Return a list that contains all of the unique items in both `tupleA` and
# `tupleB`. There should be no duplicates in the returned list
def question11(tupleA=(5, 7, 2, 3, 3), tupleB=(3, 7, 4, 8, 10)):
	#=== START YOUR CODE HERE
	setA = set(tupleA)
	setB = set(tupleB)
	l = list(setA | setB)

	return l
	#--- END YOUR CODE HERE


### Question12
# Return a dictionary that uses all of the items in `listA` as keys tied to
# items from `listB` at the same index as values (e.g., key 5 mapping to
# value 10 because 5 appears at index 0 of `listA` and 10 appears at index 0
# of `listB`). If listA and listB are not the same size, return None.
def question12(listA=[5, 2, 3, 8, 15], listB=[10, 15, 20, 2, 8]):
	#=== START YOUR CODE HERE
	if len(listA) != len(listB):
		return None

	d = {}
	for i in range(len(listA)):
		d[listA[i]] = listB[i]

	return d
	#--- END YOUR CODE HERE


### Question13
# Return a list of the items that are in either `listA` or `listB`, but not
# in both.
def question13(listA=[1, 2, 5, 7, 9], listB=[2, 3, 7, 10, 8, 9]):
	#=== START YOUR CODE HERE
	setA = set(listA)
	setB = set(listB)
	l = list(setA ^ setB)

	return l
	#--- END YOUR CODE HERE


### Question14
# Return a dictionary that, for each repeated item in the argument `a_list`,
# contains a key/value pair mapping that item as a key to a value that is a
# count of the number of times it appears in `a_list` (e.g., the key 6 would
# map to the value 2 for the default `a_list`, because 6 appears twice). Items
# that appear only once in `a_list` should not appear as keys in the
# dictionary.
def question14(a_list=[1, 1, 13, 2, 3, 3, 4, 4, 10, 12, 4, 4, 4, 5, 6, 6, 13]):
	#=== START YOUR CODE HERE
	set_list = list(set(a_list))

	count_list = []
	for num in set_list:
		count_list.append(a_list.count(num))

	dict_list = []

	for i in range(len(set_list)):
		if count_list[i] != 1:
			t = (set_list[i], count_list[i])
			dict_list.append(t)

	return dict(dict_list)
	#--- END YOUR CODE HERE


### Question15
# Write an class named Animal that has the following:
# * An initializer method that takes a `name` argument, and uses that to set
#   an attribute named `name`. You do not need to use private attributes.
# * A method named `speak` that takes no arguments and returns the string:
#   "NOISE"
# * A `__str__` method that returns the animal's name

#=== START YOUR CODE HERE
class Animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		return "NOISE"

	def __str__(self):
		return self.name
#--- END YOUR CODE HERE
def question15():
	a = Animal("Phil")
	return str(a), a.speak()


### Question16
# Write a class named Cat that Inherits from Animal has the following:
# * An initializer method that takes a `name` argument, and uses Animal's
#   initializer method to set an attribute named `name`.
# * A method named `speak` that takes no arguments and returns the string:
#   "meow"
# * Uses Animals's __str__ method.

#=== START YOUR CODE HERE
class Cat(Animal):
	def __init__(self, name):
		Animal.__init__(self, name)

	def speak(self):
		return "meow"

	def __str__(self):
		return Animal.__str__(self)
#--- END YOUR CODE HERE
def question16():
	c = Cat("Mittens")
	return str(c), c.speak()


### Question17
# Write a class named Dog that Inherits from Animal has the following:
# * An initializer method that takes a `name` argument, and uses Animal's
#   initializer method to set an attribute named `name`. Further it should
#   set an attribute named `tricks` to be an empty list.
# * A method named `learn` that takes an argument and adds that argument to
#   the `tricks` list.
# * A method named `getTricks` that returns the list referenced by the
#   attribute `tricks`
# * A method named `speak` that takes no arguments and returns the string:
#   "BARK"
# * Uses Animals's __str__ method.

#=== START YOUR CODE HERE
class Dog(Animal):
	def __init__(self, name):
		Animal.__init__(self, name)
		self.tricks = []

	def learn(self, trick):
		self.tricks.append(trick)

	def getTricks(self):
		return self.tricks

	def speak(self):
		return "BARK"

	def __str__(self):
		return Animal.__str__(self)
#--- END YOUR CODE HERE
def question17():
	d = Dog("Buddy")
	d.learn("sit")
	d.learn("stay")
	d.learn("fetch")
	return str(d), d.speak(), d.getTricks()


### Question18
# Write a recursive function to determine if the character `a_char` is in the
# string `a_string`. You cannot use the string methods `.find()`, `.rfind()`,
# `.index()`, or `.rindex`. You cannot use the `in` operator. You can index
# the string with `[]`, and you may slice the string.
def question18(a_string="This is a test string", a_char="e"):
	#=== START YOUR CODE HERE
	if len(a_string) == 0:
		return False
	elif a_string[0] == a_char:
		return True
	else:
		return question18(a_string[1:], a_char)
	#--- END YOUR CODE HERE


### Question19
# Write a recursive function to determine if the string argument `a_string`
# is a palindrome (i.e., it reads the same backwards and forwards). You cannot
# use any loops to solve this question.
def question19(a_string="racecar"):
	#=== START YOUR CODE HERE
	if len(a_string) <= 0:
		return "Please input a valid string!"
	elif len(a_string) == 1:
		return True
	elif a_string[0] != a_string[-1]:
		return False
	else:
		return question19(a_string[1:-1])
	#--- END YOUR CODE HERE


### Question20
# Write a recursive function to return the largest integer in a list argument
# You cannot use any loops or the builtin function `max()` to solve this
# question. Return None if `a_list` is empty.
def question20(a_list=[10, 5, 95, 8, 2, 29, 97, 18]):
	#=== START YOUR CODE HERE
	if len(a_list) == 0:
		return None

	elif len(a_list) == 1:
		return a_list[0]
	elif a_list[0] < a_list[1]:
		return question20(a_list[1:])
	else:
		a_list.append(a_list[0])
		return question20(a_list[1:])
	#--- END YOUR CODE HERE


# IGNORE AND DO NOT MODIFY ANY FOLLOWING CODE
# This will run all of your code for each question when executing this file
def main():
	hs = "\nBy submitting this examination, I"
	he = """pledge on my honor, and with
acceptance of the consequences laid out in all applicable policies, that I have
neither given nor received any unauthorized assistance on this evaluation, and
that the work submitted upholds the highest standards of honesty and academic
integrity.
"""
	if not honor_statement.startswith(hs) or not honor_statement.endswith(he):
		print("Modified text of honor statement!")
		return
	if student_name not in honor_statement or not i_read_and_agree:
		print("Did not agree to honor statement!")
		return
	print("FinalExam submission")
	print(f"CS00{section} ({lecture_days} lecture)")
	print(f"by: {student_name} ({username})")
	print(f"PS#: {peoplesoft_number}")
	print()
	print()
	for i in range(1, 21):
		print(f"===RUNNING_Q{i}_CODE:")
		try:
			rv = eval("question" + str(i) + "()")
		except Exception as e:
			print(f"ERROR: {e}")
		else:
			print(f"RETURNED: {rv}")
		print(f"---Q{i}_DONE")
		print()

if __name__ == "__main__":
	main()
