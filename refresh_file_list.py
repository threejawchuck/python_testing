# a list of paths
# a list of wild cards

import os
import glob
import fnmatch
def refresh_file_list (paths, globs):
		master_files_list = []
		print "searching these paths: "
		for path in paths:
			
			# make sure its fully qualified
			path = os.path.abspath(path)

			for file in os.listdir (path):

				for g in globs:
					if fnmatch.fnmatch(file,g):
						print "Found one!:",file





import time
def file_list_generator (paths, globs):

		master_files_set = set()
		
		# loop forever
		count =0
		while True:
			print "a loop", count
			# loop over all paths you are camping on
			for path in paths:
				
				# make sure its fully qualified
				path = os.path.abspath(path)

				# loop over every file in this path
				for file in os.listdir (path):
					for g in globs:
						if fnmatch.fnmatch(file,g):
							fully_qualified_file = path+"/"+file # not windows friendly!
							if fully_qualified_file not in master_files_set:
								master_files_set.add (fully_qualified_file)
								print "Found one!:",file
								yield (fully_qualified_file)
			# take a break and look some more
			time.sleep(1)
			count += 1
			if count > 10:
				break

def camp_on_file_change (new_file_generator):
	print "inside the file change camper"

	# this loop never ends
	master_file_list = []

	# loop on the generator
	for new_file in new_file_generator:
		print "loop gave me this", new_file
		#master_file_list.append(new_file)



	# do something smart in here
	time.sleep(.1) 