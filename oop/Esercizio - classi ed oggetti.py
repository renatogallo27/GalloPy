class Prospetti_Nba:
    def __init__(self,nome_e_cognome, altezza, ruolo, nazionalità, stelle_di_valutazione):
        self.nome_e_cognome = nome_e_cognome
        self.altezza = altezza
        self.ruolo = ruolo
        self.nazionalità = nazionalità
        self.stelle = stelle_di_valutazione

    def scheda_cestista(self):
            return f"\nScheda\n Nome e cognome: {self.nome_e_cognome}\n Altezza: {self.altezza}\n Ruolo: {self.ruolo}\n Nazionalità: {self.nazionalità}\n Stelle di valutazione: {self.stelle}"

cestista_uno= Prospetti_Nba("Paolo Banchero", "2.08 m", "ala", "italiano", 5)
cestista_due= Prospetti_Nba("Anton Watson", "2.03 m", "centro", "statunitense", 4)
cestista_tre= Prospetti_Nba("James Akinjo", "1.85 m", "playmaker", "statunitense", 4)
cestista_quattro= Prospetti_Nba("Timmy Allen", "1.98 m", "ala", "statunitense", 4)
cestista_cinque= Prospetti_Nba("Roko Prkačin", "2.06 m", "ala", "croato", 5)

print(Prospetti_Nba.scheda_cestista(cestista_uno))
print(Prospetti_Nba.scheda_cestista(cestista_due))
print(Prospetti_Nba.scheda_cestista(cestista_tre))
print(Prospetti_Nba.scheda_cestista(cestista_quattro))
print(Prospetti_Nba.scheda_cestista(cestista_cinque))
