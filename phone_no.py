def extractAreacode(no, d):
    return int(no//pow(10, d-1))%10

def funSort(list,numberofphones, digitpos,maxdigits):

    if digitpos > maxdigits:
        return
    #@start-editable@

    bucket = [[] for _ in range(10)]
    for i in list:
        index = extractAreacode(i, digitpos)
        bucket[index].append(i)
    arr = []
    for i in bucket:
        for j in i:
            arr.append(j)
    print(arr)

    funSort(list,numberofphones,digitpos+1,maxdigits)
    #@end-editable@
    
    

def getPhoneNumbers():
    phone = []
    noOfElements = int(input())
    while noOfElements > 0:
        element=int(input())
        phone.append(element)
        noOfElements-=1
    funSort(phone,len(phone), 6,7)

def main():
    getPhoneNumbers()
    
if __name__ == '__main__':
    main()