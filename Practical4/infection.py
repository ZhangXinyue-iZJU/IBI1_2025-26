# Pseudocode for Infection Simulation
# 1. Set total_students to 91
# 2. Set infected to 5 (initial case)
# 3. Set rate to 0.4 (40% growth per day)
# 4. Set days to 1
# 5. WHILE infected is less than total_students: 
#    a. Increase days by 1
#    b. Calculate new infected count: infected = infected * (1 + rate)
#    c. Print the current day and the number of infected people
# 6. End WHILE loop when infected >= 91
# 7. Print the final total number of days taken


# total students number
total_students = 91
# infected studennts number initially
infected = 5
# growth rate over 24hrs
rate = 0.4
# days initially
days = 1

# use while sync to analyse
while infected < total_students:
    days += 1
    infected = infected * (1 + rate)
    print(str(days) + " " + str(infected))
print(days)


# Results：
# 2 7.0
# 3 9.799999999999999
# 4 13.719999999999997
# 5 19.207999999999995
# 6 26.89119999999999
# 7 37.64767999999999
# 8 52.70675199999998
# 9 73.78945279999996
# 10 103.30523391999995
# 10