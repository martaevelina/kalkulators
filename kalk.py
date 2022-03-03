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
    9 - eiro uz ASV dolāriem
    10 -ASV dolāri uz eiro""")
    izvele = int(input(""))

    if izvele == 1:
        kgs = int(input("Ievadi kilogramus: "))
        lbs = kgs * 2.205
        print(f"{kgs} kilogrami ir {lbs} mārciņas")

        izvele = input("Vai tu vēlies turpināt? JĀ/NE: ")

        if izvele == "NĒ":
            turpinat = False

    if izvele == 2:
        lbs = int(input("Ievadi mārciņas: "))
        kgs = lbs * 0.4536
        print(f"{lbs} mārciņas ir {kgs} kilogrami")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    
    if izvele == 3:
        inch = int(input("Ievadi collas: "))
        cm = inch * 2.54
        print(f"{inch} collas ir {cm} centimetri")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False

    if izvele == 4:
        cm = int(input("Ievadi centimetrus: "))
        inch = cm * 0.3937
        print(f"{cm} centimetri ir {inch} collas")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    
    if izvele == 5:
        mi = int(input("Ievadi jūdzes: "))
        km = mi * 1.60934
        print(f"{mi} jūdzes ir {km} kilometri")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    
    if izvele == 6:
        km =  int(input("Ievadi kilometrus: "))
        mi = km * 0.621371
        print(f"{km} kilometri ir {mi} jūdzes")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    

    if izvele == 7:
        cm3 =  int(input("Ievadi kubikcentimetrus: "))
        l = cm3 * 0.001
        print(f"{cm3} kubikcentimetri ir {l} litri")

        izvele = input("Vai tu vēlies turpināt? JĀ/NĒ: ")

        if izvele.lower() == "nē" or izvele.lower() == "ne":
            turpinat = False
    