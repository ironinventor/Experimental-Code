#Fixed rate mortgages @author Aaron
#Admin N is number of years
#c is annual rate
#P0 is inital loan
#t is time as norm

import numpy as Npy
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
def Mortgage(APR, N, P0):
    #######################
    ##integer N convert  ##
    #######################
    M = int(Npy.ceil(N * 12))
    r = APR/(100*12)
    c = r*P0/(1-(1+r)**(-N*12))
    t = [0.0] * (M+1)
    P = [0.0] * (M+1)
    Q = [0.0] * (M+ 1)



    #####################
    ##Value computation##
    #####################
    for n in range (0, len(t)):
        t[n] = n/12
        P[n] = P0 * (1+r)**n - c * ( (1+r)**n -1 )/r
        Q [n] = c*n
        C = 1000*c
    return c, P, t,Q
fsize = 12
N = 20000
#########################
##get user info        ##
#########################

N = input("How long is your mortgage N = ")
if N == "":
    N = 30
    print ("Why did you take out this loan if you don't know how long it is N = 30")
else:
    N = float(N)
APR = input ("Annual percentage rate APR = ")
if APR == "":
    APR = 5
    print ("Why did you take out this loan if you don't know how long it is againnn APR = 15%")
else:
    APR = float(APR)
P0 = input("How much did you steal from the bank? How many thousands? P0 = ")
if P0 == "":
    P0 = 250
    print (""""OK WHATS IS WRONG WITH YOU HOW DO YOU NOT KNOW HOW MUCH YOU STOLEEE
     default = 5""")
else:
    P0 = float(P0)
c, P, t, Q = Mortgage(APR, N, P0)
print(" randoms = " + str(Npy.around(c, 2)*100))

fig = plt.figure(figsize = (10, 8))
plt.plot( t,P, '-',label = "Mortgage value P", color = [1, 0, 0])
plt.plot( t,Q, '-',label = " payment Q", color = [0, 0, 1])
plt.xlabel ("Number of months", size =fsize)
plt.ylabel ("value of pounds", size =fsize)
plt.title ("Fixed rate mortgage N =" +str(N) + " APR = " + str(APR) +"%, P0 = $" + str(P0)+ "k",size=fsize)
plt.legend( fontsize = fsize,loc = "upper right")
plt.grid(True)
fig.savefig('mortgage.png', dpi =300)
input("Press any key to continue......")
