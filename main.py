'''
a big comment
'''



# some string crap
def str_example ():
	a = 30
	name = 'peter'

	# the comma operator this puts spaces in
	print 'my name is', name, 'and i am', a, 'years old'
	# if we use str cat, we need to put spaces back in
	print 'my name is '+ name +' and i am', a, 'years old'

	#this fails because you can't concat an int
	#print 'my name is '+ name +' and i am' + a +'years old'

	# convert the int to a string.  remember the spaces!
	#print 'my name is '+ name +' and i am ' + str(a) +' years old'

	# print it with formatting
	print 'my name is %s and i am %d years old' % (name, a)

	# formatting works where you dump it into a str
	message = 'my name is %s and i am %d years old' % (name, a)
	print message

def list_example ():
	userAge = [21, 22, 23, 24, 25]
	print 'list is',len(userAge), 'units long'
	print 'first element is',userAge[0]
	print 'last element is',userAge[4]
	print 'last element is',userAge[-1]

	# slice it!
	print userAge
	slice = userAge [1:2]
	print slice

	#slice defaults
	print 'slice defaults'
	slice_def = userAge [0:5] # for a slice, give the number _after_ the end
	print slice_def
	slice_def = userAge [:5] #defailt beginning is zero
	print slice_def
	slice_def = userAge [0:] # default end is the one past the last element
	print slice_def

	# now a slice with a stepper
	slice_with_step = userAge [0:3:2]
	print slice_with_step

	print 'append a item at the end'
	print userAge
	userAge.append(99)
	print userAge

	print 'delete an element item at the end'
	print userAge
	del userAge[-1]
	print userAge

def tuple_example ():
	months_of_the_year = ("jan", "feb", "dec")
	print months_of_the_year
	print 'first month', months_of_the_year[0]
	print 'last month', months_of_the_year[-1]

def dictionary_example ():
	print 'dictionary_example'
	
	#define using the dict function
	dic = dict (Jan=01,Feb=2,Dec=12)
	print dic		

	#define using curly braces
	dic = {"Jan":01,
			"Feb":02,"Dec":12}
	print dic

	# loop up using keyword
	print "January is month",dic["Jan"]
	
	#edit
	dic["Jan"]=-1
	print "January is month",dic["Jan"]

	#append
	dic["Nov"]=11
	print "November is month",dic["Nov"]

	# delete a KVP
	del dic["Nov"]
	print dic

def control_loops ():
	print "control_loops"
	a = 5
	if 5 == a:
		print "yes"
	elif 4 == b:
		print "funk"
	else: 
		print "no"

	# inline if then else
	print "yes" if 5 == a else "no"
	print "yes" if 4 == a else "no"

	#for loops
	dic = dict (Jan=01,Feb=2,Mar=3,Apr=4,May=5,Dec=12)
	for d in dic:
		print d ,"is number", dic[d]

	for i, d in enumerate(dic):
		print "[",i,"]",d ,"is number", dic[d]

	# looping over numbers with range
	for i in range (0,5):
		print i
	#same as this
	for i in range (5):
		print i
	for i in range (1,26,5): # count by fives
		print i

	# while loopage 
	count=5
	while count>0:
		print count
		count -= 1;

	# the break and continue
	for i in range (0,100):
		if 2==i:
			continue # skip the two
		if 4==i:
			break # break at four
		print i
	print "done"

def try_example ():
	print "try_example"
	try:
		a = 12/0
		print a
	except:
		print "can't divide by zero"

	try:
		a = 12/0
		print a
	except ZeroDivisionError:
		print "caught a zero division error"


	try:
		a = 12/0
		print a
	except Exception as e:
		print "generic error:",e



def main():
   print ("hello world")


main()
#str_example()
#list_example()
#tuple_example()
#dictionary_example ()
#control_loops ()
try_example ()