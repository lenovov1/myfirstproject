# دریافت نمرات سه درس از کاربر
nemoresh_1 = float(input("نمره درس اول را وارد کنید: "))
nemoresh_2 = float(input("نمره درس دوم را وارد کنید: "))
nemoresh_3 = float(input("نمره درس سوم را وارد کنید: "))

# محاسبه معدل
madal = (nemoresh_1 + nemoresh_2 + nemoresh_3) / 3

# دریافت نمره انضباط
anzebat = float(input("نمره انضباط را وارد کنید: "))

# بررسی شرایط معدل و انضباط
if madal > 19 or anzebat > 19:
    print("آفرین")
else:
    if madal < 19 and anzebat < 19:
        print("بیشتر تلاش کند")
