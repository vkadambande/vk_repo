a='''CustomerName=Viraj Arun Kadambande,CustomerEmail=viraj.bande@gmail.com\nCustomerName=Ravi Kumar,CustomerEmail=ravi@gmail.com\nCustomerName=Vivek Tripathi,CustomerEmail=vivek.t@yahoo.co.in'''
print("All Customer Details ",a)

print(input("Do you want to split the lines (Y/N)? "))

splitLines = a.splitlines()

print('Splited lines are ',splitLines)

print(input('Do you want to split the customer name and email (Yes/No)'))

firstCustInfo=splitLines[0].split(',')

print("First Customer Data -  ",firstCustInfo)


secCustInfo=splitLines[1].split(',')

print("Second Customer Data -  ",secCustInfo)

thirdCustInfo=splitLines[2].split(',')

print("Third Customer Data -  ",thirdCustInfo)


print("First Cust Name - ", firstCustInfo[0])

print("Second Cust Name - ", secCustInfo[0])

print("Third Cust Name - ", thirdCustInfo[0])



