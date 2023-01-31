#   ----------------------------------Sorting & Ranking--------------------------------
orderedList: dict [float, Customer] = {}
#   map a unique number to a customer for ranking
for customer in session.customerDict.values():
    hashCode: float = 0.0
    #   generate a unique hashcode that represent
    for char in customer.name:
        hashCode += ord(char)
    #   make the magnitude hashCode less significant to avoid anomalies
    #   Basically converting the code to a decimal number
    hashCode /= 10 ** (math.ceil(math.log(hashCode, 10)) + 1)

    #   Load the list with value plus the hash code
    orderedList[round(hashCode + customer.shopList.total,3)] = customer

#   Now we have the sorted key as a list
rank = list(orderedList)
rank.sort(reverse=True)