from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoksetKorissa = 0
        self.koriHinta = 0
        self.ostoksetList = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.ostoksetKorissa
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self.koriHinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self.ostoksetKorissa += 1
        self.koriHinta += lisattava.hinta()
        
        searchResult = next((o for o in self.ostoksetList if o.tuotteen_nimi() == lisattava.nimi()), None)

        if searchResult == None:
            self.ostoksetList += [Ostos(lisattava)]
        else: 
            searchResult.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        searchResult = next((o for o in self.ostoksetList if o.tuotteen_nimi() == poistettava.nimi()), None)

        if not searchResult == None:
            searchResult.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoksetList
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
