# import csv
#
# file = "C:/Users/amukherj080816/Documents/Python Scripts/ML/Data/Cost_price_sell_price.txt"
#
# with open(file) as f:
#     reader = csv.reader(f,delimiter="\t")
#     d = list(reader)

import numpy
import matplotlib.pyplot as plt

file = "C:/Users/amukherj080816/Documents/Python Scripts/ML/Data/Cost_price_sell_price_no_head.txt"

val = numpy.loadtxt(file,delimiter="\t")

sum_x = 0
sum_y = 0

for i in range(0,len(val)):
    sum_x = sum_x + val[i][0]
    sum_y = sum_y + val[i][1]

mean_x = sum_x/len(val)
mean_y = sum_y/len(val)

num_b1 = 0
dec_b1 = 0

for i in range(0,len(val)):
    x = val[i][0]
    y = val[i][1]
    num_b1 = num_b1 + (x - mean_x)*(y - mean_y)
    dec_b1 = dec_b1 + (x - mean_x)*(x - mean_x)

b1 = num_b1/dec_b1
b0 = mean_y - b1*mean_x

exp_val = []

for i in range(0,len(val)):
    x = val[i][0]
    y = b0 + b1*(val[i][1])
    exp_val.append([x,y])

#print (b0 , "+" , b1 , "x")

# for i in range(0,len(val)):
#     print ( val[i][0] , " " , b0 + b1*val[i][0])

# plt.plot(val[:][0] , val[:][1] , 'ro')
# plt.plot(exp_val[:][0],exp_val[:][1])
# plt.show()

print (val)

print (exp_val)

