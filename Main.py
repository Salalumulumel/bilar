import Bilar

looping = True

Ford_red = Bilar.Bil("Ford","Röd",5)
Volvo_svart = Bilar.Bil("Volvo", "Svart", 23)
Volvo_vit = Bilar.Bil("Volvo", "Vit", 7)

Billista = {Ford_red,Volvo_svart,Volvo_vit}



while looping:
    print("-----------------------------")
    print("BilAutomat")
    
    i = 0

    for Bil in Billista:

        print(str(i+1) + " : " + Bil.Fabrikat + "  : " + Bil)
        i +=1


    svar = input("\n vill du avsluta programmet? j/n?")
    if (svar == "j"):
        break