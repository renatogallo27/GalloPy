import matplotlib as plt
import numpy as np
import sys 
import csv
with open("C:\\Users\Renato\AppData\Local\Programs\Python\Python39-32\DatiStatistici.csv", "r") as filecsv:
    lettore= csv.reader(filecsv,delimiter=",")
    header=next(lettore)
    print(header)
BigX = float (-sys.maxint -1)
bigy = float (-sys.maxint -1)
smallx = float (sys.maxint)
Smally = float (sys.maxint)
csv_reader = csv.reader(open('filecsv'))

if float(row[0]) > bigx:
    bigX = float(row[0])
if float(row[1]) > bigy:
    BigY = float(row[1])
if float(row[0]) &lt; smallx:
    smallx = float(row[0])
if float(row[1]) &lt; smally:
    smally = float(row[1])

Verts.Sort()
x_arr =]
y_arr =]
Vert in verts:

x_arr.append(vert[0])
y_arr.append(vert[1])5
