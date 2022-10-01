# 格式：
# 人名：商品，数量：商品2，数量 
# 不填数量默认为 1

import sys

def sort(docname):
    f = open(docname,'r',encoding="utf-8")
    new = open("RES_" + docname,"w",encoding="utf-8")

    customer = []
    for line in f:
        customer = line.split(" ")
        customer = [x.strip() for x in customer]
        for i in range(1,len(customer)):
            if ',' not in customer[i]:
                new.write("{}.{},1\n".format(customer[0],customer[i]))
            else:
                new.write("{}.{}\n".format(customer[0],customer[i]))

    f.close()
    new.close()
    return "RES_"+docname

def count(docname):
    doc = open(docname,'r',encoding="utf-8")
    products = {}
    temp = []
    order = []
    for line in doc:
        try:
            order = line.split(".")
            temp = order[2::]
        except IndexError:
            print(docname + " : " + line)

        if (temp[0] in products):
            products[temp[0]] += int(temp[1])
        else:
            products[temp[0]] = int(temp[1])
    for key,val in products.items():
        print(key,":",val)
    print("---------------")
    for key,val in products.items():
        print(key)
    print("================")

def sumOutput(number):
    new = open("sum.txt","w",encoding = "utf-8")
    for i in range(1,number+1):
        currDoc = open("RES_" + str(i) + ".txt","r",encoding="utf-8")
        for line in currDoc:
            new.write(line.replace(",","."))
        currDoc.close()
    new.close()

def multiRun(number):
    for i in range(1,number + 1):
        sort(str(i) + ".txt")

    sumOutput(number)
    count("sum.txt")

def main(arg):
    multiRun(arg)

if __name__ == "__main__":
    main(int(sys.argv[1]))