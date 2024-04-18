import random

alternativ = ["sten", "sax", "påse"]
spela = input("Vill du spela sten sax påse? Ja eller nej ")

if spela.lower() == ("ja"):
    val = input("Välj sten, sax eller påse ")

else:
    print("Nej, okej")
