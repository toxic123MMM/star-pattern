print("half pyramid pattern made up of * symbols")
n=int(input("enter a number of rows: "))
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()