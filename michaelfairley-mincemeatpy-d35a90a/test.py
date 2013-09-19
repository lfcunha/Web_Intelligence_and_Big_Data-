#!/usr/bin/env python
import mincemeat
import glob
import re, string; pattern = re.compile('[\W_]+')
text_files = glob.glob('../hw3data/*')

"""data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great fall",
        "All the King's horses and all the King's men",
        "Couldn't put Humpty together again",
        ]

"""

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()





# The data source can be any dictionary-like object

"""datasource = dict(enumerate(data))
"""

datasource = dict((file_name, file_contents(file_name))
              for file_name in text_files)


#setup map and reduce functions
def mapfn(k, v):
	print v
	for lines in v.splitlines():
		#content=sanitize(line[2])
		#for x in lines:
			#print x
		a= [(x+"-"+pattern.sub('', y), 1) for x in lines.split(":::")[1].split("::") for y in lines.split(":::")[2].split()]
		return [a for a in a]

#or w in v.split():
#        yield w, 1'''

def reducefn(k, vs):
    result = sum(vs)
    return result

a= [(a,b) for (a,b) in datasource.items()]
print mapfn(a[1][0], a[1][1])