'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

y = 3
x = 6
d = 12
i  = 40
p  = 380123456
print(p + i + x - d)
#but now i need to add seconds to per day