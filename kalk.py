turpinat = True
while turpinat == True:
    print("""Izvelies pārveidojuma veidu:
    1 - kilogrami uz mārciņām
    2 - mārciņas uz kilogramiem
    3 - collas uz centimetriem
    4 - centimetri uz collām
    5 - jūdzes uz kilometriem
    6 - kilometri uz jūdzēm
    7 - kubikcentimetri  uz litriem
    8 - litri uz kubikcentimetriem
    9 - kg/m3 uz g/ml
    10 - g/ml uz kg/m3
    11- eiro uz ASV dolāriem
    12 -ASV dolāri uz eiro""")
    izvele = float(input(""))

    if izvele == 1:
        kgs = float(input("Ievadi kilogramus: "))
        lbs = kgs * 2.205
        lbs = round(lbs, 2)
        print(f"{kgs} kilogrami ir {lbs} mārciņas")

        izvele = input("Vai tu vēlies turpināt? JĀ/NE: ")

        if izvele == "NĒ":
            turpinat = False

    if izvele == 2:
        lbs = float(input("Ievadi mārciņas: "))
        kgs = lbs * 0.4536
        kgs = round(kgs, 3)
        print(f"{lbs} mārciņas ir {kgs} kilogrami")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    
    if izvele == 3:
        inch = float(input("Ievadi collas: "))
        cm = inch * 2.54
        cm = round(cm, 2)
        print(f"{inch} collas ir {cm} centimetri")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False

    if izvele == 4:
        cm = float(input("Ievadi centimetrus: "))
        inch = cm * 0.3937
        inch = round(inch, 2)
        print(f"{cm} centimetri ir {inch} collas")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    
    if izvele == 5:
        mi = float(input("Ievadi jūdzes: "))
        km = mi * 1.60934
        km = round(km, 2)
        print(f"{mi} jūdzes ir {km} kilometri")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    
    if izvele == 6:
        km =  float(input("Ievadi kilometrus: "))
        mi = km * 0.621371
        mi = round(mi, 2)
        print(f"{km} kilometri ir {mi} jūdzes")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    

    if izvele == 7:
        cm3 =  float(input("Ievadi kubikcentimetrus: "))
        l = cm3 * 0.001
        l = round(l, 2)
        print(f"{cm3} kubikcentimetri ir {l} litri")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    
    if izvele == 8:
        l = float(input("Ievadi litrus: "))
        cm3 = l * 1000
        cm3 = round(cm3, 2)
        print(f"{l} litri ir {cm3} kubikcentimetri")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False

    if izvele == 9:
        kg_m3 = float(input("Ievadi kg/m3: "))
        g_ml = kg_m3 * 0.001
        cm3 = round(cm3, 2)
        print(f"{l} litri ir {cm3} kubikcentimetri")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False

    if izvele == 11:
        eiro = float(input("Ievadi Eiro: "))
        usd = eiro * 1.1043
        usd = round(usd, 2)
        print(f"{eiro} Eiro ir {usd} dolāri.")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False

    if izvele == 12:
        usd = float(input("Ievadi dolārus: "))
        eiro = usd * 0.9055
        eiro = round(eiro, 2)
        print(f"{usd} Dolāri ir {eiro} eiro.")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
        


