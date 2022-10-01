import pandas as pd
import matplotlib.pyplot as plt
import os
import Stats as st
from ProcessRawExcel import formatExcel
from StringMethod import getDateFromFilename
import datetime as dt

path = "./historical/"

priceList = []
countList = []
dates = []
revenue = []
for file in os.listdir(path):
    filename = os.fsdecode(file)
    if filename.endswith(".xlsx"):
        result = formatExcel(path+filename)[1]
        priceList.extend(st.getStats(result)[0])
        countList.extend(st.getStats(result)[1])

        dates.append(getDateFromFilename(filename))
        revenue.append(st.grossRevenue(result))

priceAndCount = pd.DataFrame({"Price":priceList,"Count":countList})
norm = pd.DataFrame(priceAndCount[(priceAndCount["Price"] < 98) & (priceAndCount["Count"] < 18)])
norm.plot.scatter(x="Price", y="Count", alpha = 0.2,yticks=[x for x in range(0,19,5)])
plt.savefig("scatter.jpg")


revenueDate = pd.DataFrame({"Revenue":revenue,"Date":dates})
revenueDate["Date"] = pd.to_datetime(revenueDate["Date"],format='%Y %m %d').dt.date
revenueDate = revenueDate.sort_values(by="Date")
revenueDate.plot.bar(x = 'Date', y = 'Revenue',fontsize=10,figsize=(15,10))
plt.savefig("HistoryRevenue")