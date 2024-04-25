import random

alternativ = ["sten", "sax", "påse"]

dator_val = random.choice(alternativ)

spela = input("Vill du spela sten sax påse? Ja eller nej ")

if spela.lower() == ("ja"):

    ditt_val = input("Välj sten, sax eller påse ")

    print("Du valde",ditt_val)
    print("Jag valde",dator_val)

    if dator_val == ditt_val: 
        print("Det blev lika")

    elif ditt_val == "påse" and dator_val == "sten":
        print("Du vann")

    elif ditt_val == "sax" and dator_val == "påse":
        print("Du vann")

    elif ditt_val == "sten" and dator_val == "sax":
        print("Du vann")

    else:
        print("Jag vann")

else:
    print("Nej, okej")
