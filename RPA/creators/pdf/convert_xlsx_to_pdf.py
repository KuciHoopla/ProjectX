
from RPA.creators.variables.variables import excel_path, pdfs_folder
import pythoncom
import win32com.client as client


def convert_xlsx_to_pdf(pdf_path):
    pythoncom.CoInitialize()
    xl_App = client.Dispatch("Excel.Application")
    books = xl_App.Workbooks.Open(excel_path)
    ws = books.Worksheets[0]
    ws.Visible = 1
    ws.ExportAsFixedFormat(0, pdf_path)
    books.Close(True)
    xl_App.Quit()






