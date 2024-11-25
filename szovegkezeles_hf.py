# Szöveg bekérése a felhasználótól.
def beolvas_szoveg():
    szoveg = input("Kérem, adjon meg egy szöveget! ")
    return szoveg


def beolvas_szo():
    szo = input("Kérem, adjon meg egy szót! ")
    return szo


# 9.	A beolvasott mondat kisbetűit alakítsd nagybetűsre, a nagybetűs karaktereket pedig kisbetűsre!

def kilenc():
    # Beolvasás - szöveg.
    szoveg = beolvas_szoveg()

    # Kisbetű nagybetű legyen, illetve nagybetű, kisbetű legyen.
    kis_es_nagy_betu_megforditas = szoveg.swapcase()
    # Kiíratás.
    print(kis_es_nagy_betu_megforditas)


#10. Kérj be két szót, majd döntse el a program, hogy ugyanazok-e?

def tiz():
    # Két szó bekérése a felhasználótól.
    szo1 = beolvas_szo()
    szo2 = beolvas_szo()

    # Bekért szavak kiíratása.
    print(szo1)
    print(szo2)

    # Két szó egyezőségének vizsgálata.
    if szo1 == szo2 or szo2 == szo1:
        # Kiíratás.
        print("A két szó ugyanaz.")
    # Két szó nem egyezőségének vizsgálata.
    else:
        # Kiíratás.
        print("A két szó nem ugyanaz.")


# 11. A beolvasott mondatról döntsd el, hogy az visszafelé is ugyanazt jelenti-e! (Az ”Indul a görög aludni”, vagy a ”Géza kék az ég” visszafelé olvasva is ugyanazt jelenti.) Ügyelj a mondatvégi írásjelekre, mivel azok a mondat elején nem szerepelnek.

def tizenegy():
    # Beolvasás - szöveg.
    szoveg = beolvas_szoveg()

    # Pont eltávolítása a mondat végéről.
    pont_nelkuli_szoveg = szoveg.replace(".", "")

    # Szóközök eltávolítása.
    szokoz_nelkuli_szoveg = pont_nelkuli_szoveg.replace(" ", "")
    # print(szokoz_nelkuli_szoveg)
    # print(type(szokoz_nelkuli_szoveg))

    # Nagybetűk kisbetűssé tétele.
    szokoz_nelkuli_kisbetus_szoveg = szokoz_nelkuli_szoveg.lower()
    # print(szokoz_nelkuli_kisbetus_szoveg)
    # print(type(szokoz_nelkuli_kisbetus_szoveg))

    """
    # Kiíratás visszafelé.
    # len(szoveg)-1 = A szöveg utolsó elemének jelölése, plusz, hogy honnan induljon -> utolsó elemtől.
    # első -1 = Mennyivel haladjon és milyen irányban a karaktereken.
    # második -1 = Hányasával lépkedjen az adott karakteren végig.
    # end = A szöveget ne egymás alá, karakterenként írja ki. 
    for visszafele_szoveg in range(len(szokoz_nelkuli_kisbetus_szoveg)-1, -1, -1):
        print(szokoz_nelkuli_kisbetus_szoveg[visszafele_szoveg], end="")
    """

    # Visszafele szöveg létrehozása.
    visszafele_szoveg = szokoz_nelkuli_kisbetus_szoveg[::-1]

    """
    # Nulla eltávolítása.
    # Új változó eltárolás.
    visszafele_szoveg_eltarolasa = str(visszafele_szoveg).replace("0", "")
    print(visszafele_szoveg_eltarolasa)
    print(type(visszafele_szoveg_eltarolasa))
    """

    """
    visszafele_szoveg_nulla_nelkul = visszafele_szoveg_eltarolasa
    print(visszafele_szoveg_nulla_nelkul)
    """

    if szokoz_nelkuli_kisbetus_szoveg == visszafele_szoveg:
        print("A " + ",," + szoveg + "''" + " visszafelé is ugyanazt jelenti, mint " + ",," + szoveg + "''" )
    else:
        print("A " + ",," + szoveg + "''" + " visszafelé nem ugyanazt jelenti, mint " + ",," + szoveg + "''" )


# 12. Írj egy programot, ami beolvas egy nevet és megadja a monogramját (a név két szóból álljon, egy szóközzel elválasztva)

def tizenketto():
    vezeteknev = input("Kérem, adja meg a vezetéknevét! ")
    keresztnev = input("Kérem, adja meg a keresztnevét! ")

    # Első betű megjelenítése index-szel.
    monogram_vezeteknev = vezeteknev[0]
    monogram_keresztnev = keresztnev[0]

    print("Az Ön teljes nevének monogramja a következő: " + monogram_vezeteknev + monogram_keresztnev)

