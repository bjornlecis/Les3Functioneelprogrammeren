#keuze menu voor de gebruiker
def keuze_menu():
    print("1: toon de set")
    print("2: voeg element toe")
    print("3 pas element aan")
    print("4 verwijder element")

def voeg_item_toe(verzameling):
    item = input("geef je element in")
    verzameling.add(item)
    #als je het al een lijst wil omzetten
    #lijst = list(verzameling)
    #item = input("geef je item in")
    #lijst.append(item)
    #verzameling = set(lijst)
    return verzameling
#functie toon set
def toon_set(verzameling):
    for element in verzameling:
        print(element)
#functie verander een item in de set
def verander_element(verzameling):
    item_te_veranderen = input("welke item wil je vervangen")
    if item_te_veranderen in verzameling:
        lijst = list(verzameling)
        item_veranderen_in = input("geef de nieuwe waarde van het item in")
        lijst[lijst.index(item_te_veranderen)] = item_veranderen_in
        verzameling = set(lijst)
        print("wijziging doorgevoerd")
    else:
        print("naam is niet in lijst")
    return verzameling

def verwijder_element(verzamelig):
    item_te_verwijderen = input("welk item wil je verwijden")
    if item_te_verwijderen in verzamelig:
        verzamelig.remove(item_te_verwijderen)
        #indien je met een lijst wilt werken
       # lijst = list(verzamelig)
       # lijst.remove(item_te_verwijderen)
       # print("item is verwijderd")
       # verzamelig = set(lijst)
    else:
        print("item is niet in de lijst")
    return verzamelig

#aanmaken van de set
steden_set = {"Parijs","Rome","Londen","Madrid"}
keuze_menu()
#gebruiker geeft een invoer
invoer = input("maak je keuze")
while(not invoer == "stop"):
    if(invoer == "1"):
        toon_set(steden_set)
    elif(invoer == "2"):
        steden_set = voeg_item_toe(steden_set)
    elif(invoer == "3"):
        steden_set = verander_element(steden_set)
    elif(invoer == "4"):
        steden_set = verwijder_element(steden_set)
    keuze_menu()
    invoer = input("maak je keuze")
