#!/usr/bin/env python

import os
import datetime


myPath = os.getcwd()
files = os.listdir(myPath)

#def myGraph():
    ##Create a networkx graph object
    #my_graph = nx.Graph()

    ## Add Edges to the Graph object
    ## Each tupple represents an edge between two nodes
    #my_graph.add_edges_from([
                        #(1,2),
                        #(1,3),
                        #(3,4),
                        #(1,5),
                        #(3,5),
                        #(4,2),
                        #(2,3),
                        #(3,0)])

    ## Draw the resulting Graph
    #nx.draw(my_graph, with_labels=True, font_weight='bold')

for f in files:
    if f.endswith("xyz") :
        print(f)
        fx=open(f)
        lines=fx.readlines()
        # print(lines)
        fx.close()
        data = ((lines[0]).split(","))
        # print(data)
        # print(data[0])
        # print(data[1])
        mytype=data[0]
        myname=data[1]

        print(mytype + "--" + myname)
        mynewfilename = (mytype + "-" + str(datetime.date.today()) + "-" + myname + "-" + (f.replace("'","-")).replace(".xyz",".csv") )
        new_file = open(mynewfilename, "w")
        i=0
        for line in lines:
            if i==0:
                print(line)
            else:
                new_file.write(line)
                print(i, line)
            i = i+1
        new_file.close()
        os.remove(f)
        print(" ")
