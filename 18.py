nomrehdars_1 = float(input("نمره درس اول را وارد کنید: "))
nomrehdars_2 = float(input("نمره درس دوم را وارد کنید: "))
nemrehdars_3 = float(input("نمره درس سوم را وارد کنید: "))
enzebat=float(input("lotfan enzbat ar vard koind"))
moadel=(nomrehdars_1+nomrehdars_2+nemrehdars_3)/3
if moadel > 19 or enzebat > 19:
    print("آفرین")
elif moadel < 19 and enzebat < 19:
    print("بیشتر تلاش کند",moadel)