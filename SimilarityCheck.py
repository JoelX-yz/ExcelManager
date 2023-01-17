from difflib import SequenceMatcher

def check(a,b):
    return SequenceMatcher(None,a,b).ratio()

def similarityCheck(result):
    customers = result[0][0]
    prev = ""

    for i in range(len(customers) + 1):
        for j in range(1, len(customers) + 1):
            sim = check(customers[i].name, customers[j].name)
            if sim != 1:
                print("Potential overlap: %s <==> %s -----> %f\n",customers[i].name, customers[j].name,sim)
                

        

        


