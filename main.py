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
	userAge = [21, 22, 23, 24]
	print 'list is',len(userAge), 'units long'
	print 'first element is',userAge[0]
	print 'last element is',userAge[3]
	print 'last element is',userAge[-1]






def main():
   print ("hello world")


main()
#str_example()
list_example()
