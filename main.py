import ProcessRawExcel as pe
import Modules.Stats as st



currentSession = pe.format_excel(saveFile=True)
print(currentSession.getGrossSale())

pe.addDeliverySheet(currentSession)
#pe.similarityCheck(result)

for n in currentSession.customerDict.keys():
    print(n)