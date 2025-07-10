amliate = input("lotfan amliate ra vard koind (+، -،*،): ")
aded1 = float(input("lotfan aded ra vard koind: "))
aded2 = float(input("lotfan aded ra vard koind: "))
if amliate == "+":
    haseljam = aded1 + aded2
    print("حاصل جمع:", haseljam)
elif amliate == "-":
    haseltafrig = aded1 - aded2
    print("حاصل تفریق:", haseltafrig)
elif amliate == "*":
    haselzarbe = aded1 * aded2
    print("حاصل ضرب:", haselzarbe)
else:
    print("عملیات نامعتبر است.")