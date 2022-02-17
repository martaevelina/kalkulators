turpinat = True
while turpinat:
    print("""Izvelies pārveidojuma veidu:
    1 - kilogrami uz mārciņām
    2 - mārciņas uz kilogramiem
    3 - collas uz centimetriem
    4 - centimetri uz collām
    5 - jūdzes uz kilometriem
    6 - kilometri uz jūdzēm""")
    izvele = int(input(""))

    if izvele == 1:
        kgs = int(input("Ievadi kilogramus: "))
        lbs = kgs * 2.205
        print(f"{kgs} kilogrami ir {lbs} mārciņas")

        izvele = input("Vai tu vēlies turpināt? JĀ/NE: ")

        if izvele == "NĒ":
            turpinat = False
        
    if izvele == 2:
        