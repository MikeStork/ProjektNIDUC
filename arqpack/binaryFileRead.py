def binaryFileRead(fileName):
    try:
        with open(fileName, 'rb') as binaryFile:
            binaryData = binaryFile.read()
        return binaryData
    except FileNotFoundError:
        print("Nie znaleziono pliku o podanej nazwie!!!\n")
        return None
    except Exception as e:
        print("Wystapil blad podczas odczytu pliku: ", e)
        return None
