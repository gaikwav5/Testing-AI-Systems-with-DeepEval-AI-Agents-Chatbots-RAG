# If Else Loop
from traceback import print_tb

Greetings = "Good Morning"

if Greetings == "Good":
    print("Greeting is partially printed")
    print("Second Line")
elif Greetings == "Good Morning":
    print(Greetings + " Message Delivered")
else:
    print("No greeting found")

print("if else code execution has been done")



# For Loop

a = [1,2,3,"abc","dfz",5.4]
for i in a:
    print(i)

# Summation of natural numbers from 1 to 5

summation = 0

for j in range(1,6):
    summation = summation + j
print(summation)


print("****************************************************")

# Range with indexing

for m in range(1,10,2):
    print(m)

print("*******************Skipping Indexing*********************")

for k in range (10):
    print(k) # Staring from 0 as we skip the starting index and also interval



# While Loop

num = 10
while num > 1:
    print(num)
    num = num - 1

# Break and Continue use case in loop statement

it = 13
while it > 1:
    if it == 11:
        it = it - 1  # Decrement before continue to avoid an infinite loop!
        continue     # Skip printing 11 and jump to the next loop check
    print(it)
    it = it - 1

dec = 12
while dec > 1:
    if dec == 11:
        break
    print(dec)
    dec = dec -1



