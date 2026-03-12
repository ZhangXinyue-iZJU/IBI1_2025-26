### What does this piece of code do? ###
# Answer:This code generates 11 random integers between 1 and 10 and prints their total sum.

### Import libraries ###
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
# but not used this time
from math import ceil

### Initialization ###
# Creates a variable to store the running sum of the random numbers. It starts at 0.
total_rand = 0
# Creates a counter variable to track how many times the loop has run. It starts at 0.
progress = 0

### The Loop ###
while progress<=10:
	progress+=1
	n = randint(1,10)
	total_rand+=n
# while progress <= 10:: This is a loop that continues running as long as progress is less than or equal to 10.
# Since progress starts at 0 and increases by 1 each time, the loop runs for values: 0, 1, 2, ..., 10.
# Total iterations: 10−0+1=11 times.
# progress += 1: Increments the counter by 1 immediately at the start of the loop body.
# n = randint(1, 10): Generates a random integer between 1 and 10 (inclusive) and stores it in variable n.
# total_rand += n: Adds the new random number n to the existing total_rand.

### Result ###
print(total_rand)
# 56
# 74
# 48
