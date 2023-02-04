import ProcessRawExcel as pe
import Modules.Stats as st



currentSession = pe.formatExcel(saveFile=True)
print(currentSession.getGrossSale())
pe.addDeliverySheet(currentSession)
#pe.similarityCheck(result)
