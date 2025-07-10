darkoset=input("darkoset kod ra vard koind :")
if darkoset==("circle"):
    shoa=float(input("lotfan shoa ra vard koind:"))
    masahet = 3.14 * shoa * shoa
    mohite = 2 * 3.14 * shoa
    print("masahet:", masahet)
    print("mohite:", mohite)
elif darkoset==("square"):
    zel=float(input("lotfan zelmorbeh ra vard koind:"))
    masahet=zel*zel
    mohite = 4 * zel
    print("masahet:",masahet)
    print("mohite:", mohite)
elif darkoset==("rectangle"):
    tool=float(input("tool ra vard koind:"))
    arz=float(input("arz ra vard koind:"))
    masahet=tool*arz
    print("masahet ast:",masahet)
else:
    print("shoma az bernameh kharje shodehidi:")

