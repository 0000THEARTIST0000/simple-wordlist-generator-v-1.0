import sys
print "####################################"
print "#                                  #"
print "# SIMPLE WORDLIST GENERATOR V 0.1  #"
print "# ARTIST_00                        #"
print "#                                  #"
print "####################################"
global file1, richiesta

var1 = raw_input("Inserisci il nome: ")
var2 = raw_input("Inserisci il cognome: ")
var3 = raw_input("Inserisci l'anno di nascita: ")
var4 = raw_input("Inserisci il giorno (es 01) di nascita: ")
var5 = raw_input("Inserisci il mese di nascita: ")
special = raw_input("Inserisci le ultime 2 cifre dell'anno di nascita: ")

def crea():
    var6 = var1.title() + var2.title()
    var7 = var2.title() + var1.title()
    var8 = var1 + var2
    var9 = var2 + var1
    var10 = var1.title() + var2.title() + var3
    var11 = var1.title() + var3
    var12 = var1 + var3
    var13= var1 + var2 + var3
    var14= var4 + var5 + var3
    var15= var3 + var5 + var4
    var16 = var4 + var5 + special
    var17 = var1.title()+"_"+ var3
    var18 = var1 +"_"+ var3
    var19= var1 + "_" + var2 + var3
    var20 = var1.title()+"_"+ special
    var21 = var1.title() + var2 + var3
    var22 = var1 + " " + var2
    var23 = var1 + var2 + var4 + var5 + var3
    var24 = var1 + var4 + var5 + var3
    var25= var1.title() + var4 + var5 + var3
    var26 = var1.title() + "_" + var4 + var5 + var3
    var27 = var1 + var4 +  var5 + special
    var28 = var1.title() + var4 + var5 + special
    var29 = var1.title()+ var2 + var4 + var5 + var3
    var30= var1.title()+ var2 + var4 + var5 + special
    var31 = var1.upper() + var3
    var32 = var1.upper() + "_" + var3
    var33 = var1.upper() + var2.upper()
    var34= var1.upper() + var2.upper() + var3
    var35 = var1.upper() + var2.upper() + "_"+ var3
    var36 = var1.upper() + "_" + var2.upper() + "_" + var3
    file1 = open("wordlist.lst", "w")
    file1.write(var6+"\n")
    file1.write(var7+"\n")
    file1.write(var8+"\n")
    file1.write(var9+"\n")
    file1.write(var10+"\n")
    file1.write(var11+"\n")
    file1.write(var12+"\n")
    file1.write(var13+"\n")
    file1.write(var14+"\n")
    file1.write(var15+"\n")
    file1.write(var16+"\n")
    file1.write(var17+"\n")
    file1.write(var18+"\n")
    file1.write(var19+"\n")
    file1.write(var20+"\n")
    file1.write(var21+"\n")
    file1.write(var22+"\n")
    file1.write(var23+"\n")
    file1.write(var24+"\n")
    file1.write(var25+"\n")
    file1.write(var26+"\n")
    file1.write(var27+"\n")
    file1.write(var28+"\n")
    file1.write(var29+"\n")
    file1.write(var30+"\n")
    file1.write(var31+"\n")
    file1.write(var32+"\n")
    file1.write(var33+"\n")
    file1.write(var34+"\n")
    file1.write(var35+"\n")
    file1.write(var36+"\n")
    file1.close()

def aggiungi():
    parola = raw_input(" Parola da aggiungere: ")
    file1.append(parola)
    file1.close()

crea()
print "La wordlist è stata creata e nominata wordlist.lst"
while (1 == 1):
    richiesta = raw_input("Vuoi aggiungere altre parole? [s\n]")
    if richiesta=="s":
        aggiungi()
        continue
    if richiesta=="n":
        print "Ok esco..."
        break

sys.exit()


    




    

