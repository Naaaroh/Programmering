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

    elif

    elif

    elif

    else:

else:
    print("Nej, okej")
