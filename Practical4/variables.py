### 4.1 ###
a = 5.08
b = 5.33
c = 5.55

d = b - a
e = c - b

if d<e:
    print("population growth accellerating in Scotland")
else:
    print("population growth decelerating in Scotland")

# Result: population growth decelerating in Scotland


### 4.2 ###
X = True
Y = False
W = X or Y

# X = True, Y = True then W = True
# X = True, Y = False then W = True
# X = False, Y = True then W = True
# X = False, Y = False then W = False