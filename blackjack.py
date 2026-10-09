#random importálása
import random

#létre kell hoznom egy színek, es kártyak részt, amiben tárolomn az értékeket
szinek = ["Káró", "Kör", "Treff", "Pikk"]
ertekek = {
            "2": 2,
            '3': 3,
            "4": 4,
            "5": 5,
            "6": 6,
            '7': 7,
            "8": 8,
            "9": 9,
            "10": 10,

            "J": 10,    #bubi
            "Q": 10,    #dáma
            "K": 10,    #király
            "A": 11     #ász
        }
    
def pakli_letrehozasa():
    pakli = []
    for szin in szinek:
        for ertek in ertekek.keys(): #végigmegyünk a szótár kulcsain, és hozzáfűzzük
            pakli.append((szin, ertek)) 
    random.shuffle(pakli) #gemini
    return pakli #gemini
    
def kezerteke(kez):
    ertek = 0 #a kéz érteke 0
    aszok_szama = 0 #gemini


    for lap in kez:
        szam = lap[1]
        ertek = ertek + ertekek[szam]

        if szam == "A":
            aszok_szama += 1

    #ászok értéke, abban az esetben ha túllépnénk a 21-et
    while ertek > 21 and aszok_szama > 0:
        ertek -= 10
        aszok_szama -= 1

    return ertek

def lapok_megjelenitese(kez): #gemini kezdete
    szoveg = ""
    for lap in kez:
        szoveg = szoveg + lap[0] + " " + lap[1] + ", "
    return szoveg

def jatek():
    print("--- Üdvözöllek a Blackjack játékában 🎰 ---")
    pakli = pakli_letrehozasa() 

    jatekote_kez = []
    osztokez = [] #gemini vége

    #lapok kiosztása, 2-2 lap ezért van egy darab kétszer
    jatekote_kez.append(pakli.pop())
    jatekote_kez.append(pakli.pop())
    
    osztokez.append(pakli.pop())
    osztokez.append(pakli.pop())

    #a játékos köre
    #gemini kezdete
    while True: 
        print("\nA te lapjaid: " + lapok_megjelenitese(jatekote_kez) + "(Érték: " +str(kezerteke(jatekote_kez)) + ")")
        print("Az osztó látható lapja: " + osztokez[0][0] + " " + osztokez[0][1]) #gemini vége

        if kezerteke(jatekote_kez) == 21:
            print("Gratulálunk, blackjack! Nyertél!")
            return
    
        if kezerteke(jatekote_kez) > 21:
            print("Ennyi volt, vesztettél haver!")
            return
        
        valasz = input("Kérsz még egy lapot? (k / m - kér / megáll): ")
        if valasz == "k":
            
            jatekote_kez.append(pakli.pop())
        elif valasz == 'm':
            break

        else:
            print("Érvénytelen válasz!")

    #az osztó köre
    print("\nAz osztó felfedi lapjait: " +lapok_megjelenitese(osztokez) + "(Érték: " + str(kezerteke(osztokez)) + ")")
    while kezerteke(osztokez) < 17:
        print("Az osztó most éppen lapot húz...")
        osztokez.append(pakli.pop())
        print("Az osztó lapjai: " + lapok_megjelenitese(osztokez) + "(Érték: " + str(kezerteke(osztokez)) + ")")
    #gemini vége   

    #végeredmény, és annak kiírása
    jatekos_pontszama = kezerteke(jatekote_kez)     #gemini
    osztopont = kezerteke(osztokez)                 #gemini

    if osztopont > 21:
        print("Gratulálunk! Te nyertél! 💵")

    elif jatekos_pontszama > osztopont:
        print("Gratulálunk! Nyertél az osztó ellen! 💵")

    elif jatekos_pontszama < osztopont:
        print("Sajnálom, de az osztó nyert!")

    else:
        print("Dötletlen! A tét pedig visszajár!")

if __name__ == "__main__":          #gemini
    jatek()                         #gemini

while True:     #Herndái Gábor ötlete, ennek a kezdete                   
    jatek()
    if input("\nÚj szeretne játszani? (i/n): ") != "i":
        break   #Herndái Gábor ötlete, ennek a vége