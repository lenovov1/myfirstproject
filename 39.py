for i in range (0,5):
    amliate = input("lotfan amliate ra vard koind (+، -،*،/،): ")
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
    elif amliate == "/":
      haseltagsim = aded1 / aded2
      print("حاصل تقسیم:", haseltagsim)
    else:
      print("عملیات نامعتبر است.")