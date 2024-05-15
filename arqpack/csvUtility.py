import csv
from tkinter import filedialog

def saveDataToCSV(data: list[tuple]):
    file = filedialog.asksaveasfile(mode='w', initialfile="data", defaultextension=".csv", filetypes=[("All Files","*.*"),("CSV","*.csv")])
    if file is None:
        return
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()