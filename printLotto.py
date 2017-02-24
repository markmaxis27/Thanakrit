from random import randint

lottorec = input("Enter your Lotto : ")

lottorec+=randint(0,9)
print("\nFisrt lottorecieve is %d" %lottorecieve)

print("\nLast three number lottorecieve is... ")
for i in range(4):
    temp = randint(0,999)
    if(temp<100):
        print("0%d" %temp)
    elif(temp<10):
        print("00%d" %temp)
    else:
        print temp

print("\nLast two number lottorecieve is... ")
print randint(0,99)
