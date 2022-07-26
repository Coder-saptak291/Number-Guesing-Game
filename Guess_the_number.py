import random
n = random.randint(1,100)
# print(n)
g= 0
gc=0
while n != g:
    g= int(input("Enter Your guess = "))
    gc=gc+1
    if g == n:
        print("You have done in ",gc,"Guesses")
    elif g>n:
        print("Please enter a smaller number")
    elif g<n:
        print("Please enter a greater number")


