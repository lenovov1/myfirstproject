vazen=float(input("lotfan avazen kod ra vard koind:"))
gad=float(input("lotfan gad kod ra vard koin:"))
if vazen>0 and gad >0:
      bmi=vazen/(gad**2)
      if bmi >15 and bmi<25:
          print("normal:")
      elif bmi>35 and bmi<35:
          print("ezafeh vazen dared")
      elif bmi>35:
          print("chegi mofraed:")


