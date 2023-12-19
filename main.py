import process_excel as pe
import Modules.Stats as st



currentSession = pe.format_excel(saveFile=True)
print(currentSession.calc_gross_revenue())

pe.gen_delivery_sheet(currentSession)
#pe.similarityCheck(result)