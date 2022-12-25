''' Q. In this project you have to enter a positive integer range[A,B] and system will find out the status(prime or composite) of each no.
        available in the given range. At the end print the count also.'''




print("\n  WELCOME TO MY PYTHON PROJECT")
print("  ----------------------------\n")

''' a,b are the lower limit and upper limit of the range '''

a,b=input("  Enter lower limit and upper limit : ").split(",")
a=int(a)
b=int(b)

''' here initially prime and composite variables are assigned with zero in order to count total no. of 
prime and composite no. are present in the given range '''

prime=0
composite=0
print("\n  The status of each number in the range is : \n")

for i in range(a,b+1):
    count=0

    '''The below for loop checks the condition of composite no.'''

    for j in range(2,i):
        if i%j==0:
            count+=1

            '''The loop assign 0 in count variable if the specific no. is prime, otherwise 1 if the no. is composite'''
            
    if count>0:
        print(" ",i,"is composite")
        composite+=1
    else:
        print(" ",i,"is prime")
        prime+=1

print("\n  Total count ->")
print("\n ",prime," prime and ",composite," composite numbers in the range.")
print("\n  ------------------------------------------------\n")
print("\n THANK YOU\n HOPE YOU GOT YOUR ANSWER \n Made By - ABDUL AZIZ KHAN\n SECTION - KOC37\n REG. NO.- 12200012\n ROLL NO.- B65\n")
