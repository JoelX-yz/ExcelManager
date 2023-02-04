import pandas as pd
import matplotlib.pyplot as plt

def priceDstribution(products):
    prices = []
    count = []
    for v in products.values():
        if v.price is not None:
            prices.append(int(v.price))
            count.append(v.count)
    
    priceAndCount = pd.DataFrame({"Price":prices,"Count":count})
    priceAndCount.plot.scatter(x="Price", y="Count", alpha=0.5)
    plt.savefig("stats.jpg")


def getStats(products):
    prices = []
    count = []
    for v in products.values():
        if v.price is not None:
            prices.append(int(v.price))
            count.append(v.count)
    return [prices,count]