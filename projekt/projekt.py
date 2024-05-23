import random

alternativ = ["sten", "sax", "påse"]
dator_val = random.choice(alternativ)

def a():
    if spela.lower() == ("ja") or spela.lower() == ("yes"):

        ditt_val = input("Välj sten, sax eller påse ")

        print("Du valde",ditt_val)
        print("Jag valde",dator_val)

        if dator_val == ditt_val.lower(): 
            print("Det blev lika")

        elif ditt_val.lower() == "påse" and dator_val == "sten":
            print("Du vann")

        elif ditt_val.lower() == "sax" and dator_val == "påse":
            print("Du vann")

        elif ditt_val.lower() == "sten" and dator_val == "sax":
            print("Du vann")

        else:
            print("Jag vann")

    else:
        print("Nej, okej")

spela = input("Vill du spela sten sax påse? Ja eller nej ")
    
a()

spela_igen = input("Vill du spela igen? ")

while spela_igen.lower() == ("ja"):
    dator_val = random.choice(alternativ)

    a()
    spela_igen = input("Vill du spela igen? ")
else: 
    print("Nej okej")