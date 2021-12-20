#keuze menu voor de gebruiker
def keuze_menu():
    print("1: toon de dictionary")
    print("2: voeg element toe")
    print("3 pas element aan")
    print("4 verwijder element")

def toon_dic(d):
    for x in d.values():
        print(x)

def voeg_item_toe(d):
    sleutel = input("geef de key")
    waarde = input("geef de waarde")
    d[sleutel] = waarde
    return d
def verander_waarde(d):
    print("wat wil je wijzigen?")
    print(d.keys())
    sleutel = input("geef de key die je wilt wijzigen")
    if sleutel in d.keys():
        waarde = input("welke waarde wil je geven")
        d[sleutel] = waarde
    else:
        print("wijziging niet doorgevoerd verkeerde sleutel")

    return d

def verwijder_item(d):

    print(d.keys())
    sleutel = input("welke sleutel wil je verwijderen")
    if sleutel in d.keys():
        d.pop(sleutel)
    else:
        print("Sleutel bestaat niet")
    return d

auto = {"Merk":"Ford","Model":"Focus","Bouwjaar":2020}

keuze_menu()
#gebruiker geeft een invoer
invoer = input("maak je keuze")
while(not invoer == "stop"):
    if(invoer == "1"):
        toon_dic(auto)
    elif(invoer == "2"):
       auto = voeg_item_toe(auto)
    elif(invoer == "3"):
        auto = verander_waarde(auto)
    elif(invoer == "4"):
       auto = verwijder_item(auto)
    keuze_menu()
    invoer = input("maak je keuze")


