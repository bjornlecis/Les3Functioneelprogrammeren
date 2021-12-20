#keuze menu voor de gebruiker
def keuze_menu():
    print("1: toon de tupple")
    print("2: voeg element toe")
    print("3 pas element aan")
    print("4 verwijder element")

def voeg_item_toe(tuppel):
    lijst = list(tuppel)
    item = input("geef je item in")
    lijst.append(item)
    tuppel = tuple(lijst)
    return tuppel
#functie toon tuppel
def toon_tupple(tuppel):
    for element in tuppel:
        print(element)
#functie verander een item in de tuppel
def verander_element(tuppel):
    item_te_veranderen = input("welke item wil je vervangen")
    if item_te_veranderen in tuppel:
        lijst = list(tuppel)
        item_veranderen_in = input("geef de nieuwe waarde van het item in")
        lijst[lijst.index(item_te_veranderen)] = item_veranderen_in
        tuppel = tuple(lijst)
        print("wijziging doorgevoerd")
    else:
        print("naam is niet in lijst")
    return tuppel

def verwijder_element(tuppel):
    item_te_verwijderen = input("welk item wil je verwijden")
    if item_te_verwijderen in tuppel:
        lijst = list(tuppel)
        lijst.remove(item_te_verwijderen)
        print("item is verwijderd")
        tuppel = tuple(lijst)
    else:
        print("item is niet in de lijst")
    return tuppel

#aanmaken van de tupple
steden_tupple = ("Parijs","Rome","Londen","Madrid")
keuze_menu()
#gebruiker geeft een invoer
invoer = input("maak je keuze")
while(not invoer == "stop"):
    if(invoer == "1"):
        toon_tupple(steden_tupple)
    elif(invoer == "2"):
        steden_tupple = voeg_item_toe(steden_tupple)
    elif(invoer == "3"):
        steden_tupple = verander_element(steden_tupple)
    elif(invoer == "4"):
        steden_tupple = verwijder_element(steden_tupple)
    keuze_menu()
    invoer = input("maak je keuze")

