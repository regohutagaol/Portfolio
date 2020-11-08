import random

p4=0 #pity counter for 4 stars item
p5=0 #pity counter for 5 stars item
n4=0 #amount of 4 stars item obtained
n5=0 #amount of 5 stars obtained
i=0

n = 1000000 #number of simulations run

while i<n:
    rng=random.random()
    if rng<0.006 or p5==89: #6% chance to get 5 stars or guaranteed 5 stars at 90th roll
        p5=0
        p4=0
        n5+=1
        i+=1
    elif rng<(0.006+ 0.051) or p4==9: #5.1% chance to get 4 stars or guaranteed 4 stars at 10th roll
        p4=0
        p5+=1
        n4+=1
        i+=1
    else:
        p4+=1
        p5+=1
        i+=1

# Probability of getting 4 or 5 stars = number of 4 or 5 stars * 100 /number of simulations run
print("The consolidated probability to get 4 star is : {:.2f}% \n"
      "The consolidated probability to get 5 star is : {:.2f}%".format(n4*100/n, n5*100/n))

#The consolidated probability to get 4 star is : 11.83%
#The consolidated probability to get 5 star is : 1.43%"