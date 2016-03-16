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

	# replace
	print "Hello World".replace("World","Krunk")

	print "inserts a new line"
	print "does not",
	print " insert a new line",
	print "okay there it is"

	# big old string.  these will all be left justified
	bos = """the first
the second
the third
"""
	print bos

	# strings are never number
	x = "42"
	y = "36"

	print x+y # print 4236
	# eval first
	print int (x) + int (y)
	print eval (x) + eval (y) # this is 78



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


	# the pass operator
	a = 2
	if a == 2:
		pass # this is a no op
	else:
		print "inside the else"
	print "done"

	# using the in operator in an if statment
	s = "long ass string"
	if "ass" in s:
		print "yep, it's an ass"

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

def sum (x):
	s = 0
	for i in range (len(x)):
		s += x[i];

	s = 0
	for i in x:
		s += i

	return s

def function_example ():
	x = [1,2,3,4,5,6,7,8]
	print sum (x) # should be 4*7+8 = 1+7*5 = 36

def scope_example ():
	print 'scope_example'
	x = 5;
	print x # clearly 5
	if True:
		x = 6
		print x # clearly 6
	print x # supplies! it's six!

	def anon():
		x = 7
		print x # clearly 7
	anon () # calling the function
	print x # back to six because that used local function scope

def main():
   print ("hello world")

def module_example ():
	import random
	print random.randrange(6,7)

	import random as r
	print r.randrange(7,8)

	from random import randrange
	print randrange(8,9)

	from random import randrange, randint
	print randint(8,9)

	# add a dir to your path so you can import
	import sys
	path = '/path/doesn/exit'
	if path not in sys.path:
		sys.path.insert(0, path)

def file_example ():
	print "file_example"
	file = 'tempfile.txt'
	f = open (file,'w') #write only and wipe the file first
	f.write ('first line: d00d')
	f.write ('\t same line brah')
	f.write ('\n')
	f.write ('second line')
	f.write ('\nlast line\n')
	f.close()

    # Or with open "context"
	with open(file, 'w') as f:
	    f.write ('first line: d00d')
	    f.write ('\t same line brah')
	    f.write ('\n')
	    f.write ('second line')
	    f.write ('\nlast line\n')


	f = open (file, 'r') # read only
	# first line. note that this line has a \n on the end of it
	firstline = f.readline()
	# strip that last character off
	firstline2 =  firstline[0:-1]
	print firstline2

	print f.readline() # second line which doesn't have a \n on the end of it
	f.close() # close it up

	# can also do super fast in this two liner
	for l in open (file):
		print l,

	# or use the readlines
	lines = open(file).readlines()
	for line in lines:
		print line,

	# open the file and copy it line by line
	f = open (file, 'r') # read only
	outputfile = "outputfile.txt"
	o = open (outputfile, "w")
	msg = f.read(5) # read five bytes
	while len(msg):
		o.write (msg)
		msg = f.read(5)
	o.close()
	f.close()

	#rename a file
	import os
	new_name = "funk.txt"
	os.rename (outputfile,new_name)

	# clean up the files
	import os
	os.remove (new_name)
	os.remove (file)

def eval_example ():
	print "eval_example"
	expression =  "1 + 2 + 7"
	print expression
	print eval (expression)

def dictionary_deep_dive ():
	print "dictionary_deep_dive"
	dict1 = {}
	print dict1
	dict1 ["Jan"] = "January"
	dict1.clear() # clear it out
	print dict1

	# fill it back up
	dict1 ["Jan"] = "January"
	dict1 ["Feb"] = "February"
	dict1 ["Mar"] = "March"
	dict1 ["Dummy"] = "shouldn't see this"
	del dict1 ["Dummy"]
	print dict1

	print dict1["Jan"]
	print dict1.get("Jan")
	try:
		print dict1["this key Doesnt exist"]
	except Exception as e:
		print "That don't work man.  I can't seem to find this key: ",e

	# looking for a key
	if "Doesn't exist" in dict1:
		out = dict1["doesn't exist"]
	else:
		out = "nope"
	print out

	# or we can do the same thing using get
	out = dict1.get("doesn't exist", "nope")
	print out

	# use the in keywork
	if "Jan" in dict1:
		print "yeah, it's here"

	# each keyword value pair as a tuple
	print dict1.items()

	# all of the keys
	for k in dict1.keys():
		print k
	for index, key in enumerate (dict1.keys()):
		print index, key

	# try the update
	dict2 = {}
	for index, key in enumerate (dict2.keys()):
		print "you shoulnd't see this",index, key
	dict2.update(dict1)
	for index, key in enumerate (dict2.keys()):
		print "you should see this:",index, key

	dict3 = {}
	dict3["Jan"] = "this will be overwritten aften an update"
	for index, key in enumerate (dict3.keys()):
		print index, "the key [", key, "] refers to [",dict3[key],"]"
	dict3.update(dict1)

	for index, key in enumerate (dict3.keys()):
		print index, "the key [", key, "] refers to [",dict3[key],"]"

	for index, value in enumerate (dict3.values()):
		print index, value

def create_dummy_file (filename, n):
	f = open (filename,"w")
	for i in range (n):
		line = "Line " + str(i) + "\n"
		f.write (line)
	f.close()

def read_this_line_by_line (filename):
	print "this only happens once"
	for line in open (filename):
		yield (line) # the yield makes this a generator
	print "all done"

def generator ():
	print "generator"
	filename = "dummy file"
	size = 5
	create_dummy_file (filename, size)

	# define the variable
	a_line_from_this_file = read_this_line_by_line(filename)
	print "nothing has happened yet!"

	# now call next.  should see just one line
	print a_line_from_this_file.next(),

	# call to next and one more line
	for l in range (size):
		try:
			print a_line_from_this_file.next(),
		except:
			print "can't call next when the file is empty!"

	# let's try this again with feeling
	for l in read_this_line_by_line(filename):
		print l,

def logging ():
    # USE LOGGING!!!!  It's so good it's now a built in to the language!!
    # Instead of using print to communicate with the user, use logging.  All
    # you have to do is import logging in all your modules, and use it instead
    # of print, that's it!!
    import os
    import time
    import logging

    # Log some messages
    logging.warn('warn message')
    logging.debug('debug message')
    logging.info('info message')
    logging.fatal('fatal message')

    # Then in the entry point of your program, usually in the 'if __name__ ==
    # "__main__"' block, you define your sinks for logging messages (screen,
    # file, etc) Here is my boilerplate to log to file and to screen.  There
    # are a million and one options on logging sinks, so see the python
    # documentation for more info.

    # Make log directory if it does not exist
    if not os.path.isdir('log'):
        os.makedirs('log')

    # File Sink
    logfile = time.strftime("RepoSync-%Y%m%d-%H%M%S.log")
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%Y%m%d %H:%M:%S',
        filename=os.path.join('log', logfile),
        filemode='w')

    # Screen Sink
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def argparse_example():
	print "testing argparse_example"
	import argparse

	# set up the arg parser
	parser = argparse.ArgumentParser(description="Run example functions")

	# don't know what this does
	group = parser.add_mutually_exclusive_group()
	
	# register the verbosity flag and store results as a bool
	group.add_argument("-v", "--verbose", action="store_true")

	# register the quiet flag and store results as a bool
	group.add_argument("-q", "--quiet", action="store_true")

	# this is a required file and you are going to store the string in 
	# the variable EXAMPLE.  if you don't get this string, it is going to 
	# raise an error
	#parser.add_argument("EXAMPLE", type=str, help="the example to execute")

	# now go parse the command line
	# note that by leaving it blank, the argumentparser 
	# will automatically determine the command-line arguments from sys-argv
	args = parser.parse_args()

	# now we are actually going to do something with the args
	if args.quiet:
	    print("Quiet mode set")
	elif args.verbose:
	    print("Verbose mode set")
	else:
	    print("Quiet/Verbose mode not set")
	
	# if example isn't already in globals(), put it there or else toss a raise
	# if args.EXAMPLE in globals():
	#    globals()[args.EXAMPLE]()
	# else:
    #	raise NotImplementedError("Example %s not implemented" % args.EXAMPLE)

# This block makes the file both a library and an executable.  The following
# code is only executed if the file is executed.
if __name__ == "__main__":

	#str_example()
	#list_example()
	#tuple_example()
	#dictionary_example ()
	#control_loops ()
	#try_example ()
	#function_example ()
	#scope_example()
	#module_example ()
	#file_example()
	#eval_example()
	#dictionary_deep_dive ()
	#generator()
	argparse_example ()



# import sys
# print sys.path[0]

# import os
# dirlist = os.listdir (sys.path[0])
#for p in dirlist:
#	print p


# import refresh_file_list


# pwd = sys.path[0]
# paths = [pwd]
# paths.append ("/etc/") # fully qualified
# paths.append ("../") #relative

# wildcards = ["*.py"]
# new_file_generator = refresh_file_list.file_list_generator (paths, wildcards)

# refresh_file_list.camp_on_file_change (new_file_generator)

