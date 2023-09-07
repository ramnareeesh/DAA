# You have two numbers number1 and number2, your job is to check the number of borrow operations needed for
# subtraction of number1 from number2. If the subtraction is not possible then return the string not possible.

n1 = int(input())
n2 = int(input())
count = 0
if n1 < n2:
    print("Not Possible")
else:
    while (n1 != 0 and n2 != 0):
        units_n1 = n1 % 10
        units_n2 = n2 % 10
        n1 = n1 // 10
        n2 = n2 // 10
        if units_n1 < units_n2:
            n1 -= 1
            count += 1
    print(count)

# number1=int(input("n1: "))
# number2=int(input("n2: "))
# count=0
# if(number1< number2):
#     print("Not possible")
# else:
#     flag=0
#     while(number1!=0 and number2!=0):
#         temp1=0
#         temp2=number2%10
#         if(flag):
#             temp1=number1%10-1
#         else:
#             temp1=number1%10
#         if(temp1< temp2):
#             count+=1
#             flag=1
#         else:
#             flag=0
#         number1=number1//10
#         number2=number2//10
#     print(count)