import ProcessRawExcel as pe
import Stats as st



result = pe.formatExcel(saveFile=True)
pe.addDeliverySheet(result)
print(st.grossRevenue(result[1]))