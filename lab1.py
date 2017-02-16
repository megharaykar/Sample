#!/usr/bin/env python
  
  
import psutil
import operator
from collections import OrderedDict


  
#Dictionary to store the pid with the number of times it made the tcp connection
d = {}

#to store the final list containing the output data 
finallist=[]

# iterate over the attributes of the psutil.net_connection function
for c in psutil.net_connections(kind='tcp'):
        #to store each tcp connection made by the pids
    	listelement={}
        # to check if the laddr and raddr exists and also if pid is not none
	if c.laddr and c.raddr and c.pid is not None:
                # If else loop to store the count, number of times pid made a tcp connection
                if c.pid in d:
			counter=d[c.pid]+1
			d[c.pid]=counter
		else:
			d[c.pid]=1
                
                #Format the laddr and raddr in a proper string format
        	laddr = "%s@%s" % (c.laddr)
        	raddr = "%s@%s" % (c.raddr)
                # add the output of psutil function to the list
                listelement['pid']=c.pid
                listelement['laddr']=laddr
                listelement['raddr']=raddr
                listelement['status']=c.status
                # add the output the final list
                finallist.append(listelement)

# sort the dictionary containing pid and count(number of tcp connections made) in descending order
sorted_x = OrderedDict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
# convert the dictionary into a list to retrieve the keys (pid) in an descending order 
sortedlist=list(sorted_x.keys())
#assign an index to each list element created in anew lsit
order_dict = {index: pid for index, pid in enumerate(sortedlist)}
#sort the final output based on the ordering in the newly created list
finallist.sort(key=lambda x: sortedlist.index(x['pid']))
#print the output in CSV format and format each value to be a string
print('"{}"'.format("pid")+","+'"{}"'.format("laddr")+","+'"{}"'.format("raddr")+","+'"{}"'.format( "status"))
for l in finallist:
 	print('"{}"'.format(l['pid'])+","+'"{}"'.format(l['laddr'])+","+'"{}"'.format(l['raddr'])+","+'"{}"'.format(l['status']))
    
    

