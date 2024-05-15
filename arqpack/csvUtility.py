import csv
from tkinter import filedialog

def saveDataToCSV(data: list[tuple]):
    """Saves data to a CSV file

    Args:
        data (list[tuple]): Data to save - single tuple should be in this format: (<bit count>, <encoding>, <data block size>, <bit error rate>, <redundant bits count>)
    """
    file = filedialog.asksaveasfile(mode='w', initialfile="data", defaultextension=".csv", filetypes=[("All Files","*.*"),("CSV","*.csv")])
    if file is None:
        return
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(["Bit count", "Encoding", "Data block size", "Bit error rate", "Redundant bits count"])
    writer.writerows(data)
    file.close()
    
saveDataToCSV([(1, "Hamming", 4, 0.1, 3), (2, "Parity", 8, 0.2, 1), (3, "CRC", 16, 0.3, 5)])