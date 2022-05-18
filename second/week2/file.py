import csv

def readfile(filename):
    arr = []
    with open(filename) as file:
        csv.register_dialect("emdialect", skipinitialspace=True, strict=True)
        reader = csv.DictReader(file, dialect="emdialect")
        for row in reader:
            arr.append(row)

    return arr

emlist = readfile("employees.csv")

def processreport(emarr):
    obj = {}
    