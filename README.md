Sistem odlučivanja o isplativnosti nabavke mašine


Grafički korisnički interfejs se satoji od sljedećih šest polja: evidencija učinka, troškovi mašine, troškovi radnika, prihodi, rezultat i zaključak. U prva četitri spomenuta polja korisnik aplikacije unosi podatke. Nakon unošenja podataka i klika na dugme OK u polju rezultat se prikazuju izračunate vrijednosti. Klikom na dugme prikaži zaključak se u polju zakljuačak prikazuje određeni zaključak koji govori o tome da li je mašina isplativa ili ne. Grafički interfejs je intuitivan i jednostavn za korištenje a prikazan je na sljedećoj slici:












Na samom početku koda pomoću from tkinter import * je omogućeno da se koriste mogućnosti iz modula tkinter.
Pomoću sljedćih linija koda je definisan glavni prozor aplikacije pod nazivom root. Definirane su njegove dimenzije, nasolv i postavljeno je da su naveden dimenzije fiksne, tj. ne postoji mogućnost izmjene dimenzija glavog prozora.

root = Tk()
root.geometry("1040x590")
root.title("Sistem odlučivanja o isplativosti nabavke nove mašine");
root.resizable(False, False)




Ranije spomenuta polja su realizirana pomoću objekata tipa labelFrame. Tako je npr. prvo polje evidencija učinka kreirano pomoću sljedeće dvije linje koda:
evidencijaUcinkaLF = LabelFrame(root, text=" 1. Evidencija učinka: ")
evidencijaUcinkaLF.grid(row=0, column=0, sticky='W', padx=5, pady=5, ipadx=87, ipady=32) 

U prvoj liniji je deklarisan objekat tipa LabelFrame pod nazivom evidencijaUcinkaLF. U zagradi se nalaze dva argumenta, prvi je root i ovaj argument definiše gdje će se nalaziti deklarisani labelFrame, dakle nalazit će se u glavnom prozoru. Drugi argument je text koji predstavlja tekst koji će se nalaziti na vrhu polja. Druga linija koda definira poziciju i dimenzije ovog polja. 

Na alogan način su realizirana i ostala polja, tj. ostali objekti tipa labelFrame. 

Kako je ranije spomenuto u prva četri polja se unose podaci. Unos podatak se ostvaruje pomoću objekata Entry i Spinbox. Objekti tipa Spinbox su namjenjeni za one podatke čija vrijednost je cijeli broj (npr. Broj ispravnih komada). Također ovaj objekat omogućava jednostavnu promjenu unesene vrijednosti pomoću strelica koje se nalaze u sklopu njega. Objekat Entry je namjenje za unos podataka čija vrijednost može biti realan broj npr. Cijena komada. 

Kao primjer navedimo polje evidencija učinka u kojem se nalaze dva objekta čiji je tip Spinbox i jedan objekat čiji je tip Entry. Pored ovih objekata u polju evidencija učinka se nalaze objekti tipa label koji služe samo za prikaz teksta. 
Opisani objekti koji se nalaze u polju evidencija učinka su realizirani pomoću sljedećeg koda:

ispravnihKomadaL = Label(evidencijaUcinkaLF, text="Ispravnih komada: ",anchor=E)
ispravnihKomadaSB = Spinbox(evidencijaUcinkaLF, from_=0, to=1000)
ispravnihKomadaL.grid(row=8, column=0)
ispravnihKomadaL.grid(row=8, column=0, sticky='E', padx=6, pady=2)
ispravnihKomadaSB.grid(row=8, column=6)

neispravnihKomadaL = Label(evidencijaUcinkaLF, text="Neispravnih komada: ",anchor=E)
neispravnihKomadaSB = Spinbox(evidencijaUcinkaLF, from_=0, to=1000)
neispravnihKomadaL.grid(row=10, column=0)
neispravnihKomadaL.grid(row=10, column=0, sticky='E', padx=6, pady=2)
neispravnihKomadaSB.grid(row=10, column=6)

cijenaKomadaL = Label(evidencijaUcinkaLF, text="Cijena komada: ",anchor=E)
cijenaKomadaLB = Label(evidencijaUcinkaLF, text="€/komad",anchor=E)
cijenaKomadaE = Entry(evidencijaUcinkaLF, bd =2)
cijenaKomadaL.grid(row=12, column=0)
cijenaKomadaL.grid(row=12, column=0, sticky='E', padx=6, pady=2)
cijenaKomadaE.grid(row=12, column=6)
cijenaKomadaLB.grid(row=12, column=8)


Vidimo da se pozicija svakog objekta postavlja pozivom metode grid nad tim objektom. Linijom koda ispravnihKomadaL = Label(evidencijaUcinkaLF, text="Ispravnih komada: ",anchor=E) je deklarisan objekat tipa Label pod nazivom ispravnihKomadaL. Prvi parametar u zagradi određuje da će se ovaj objekat nalaziti u polju evidencija učinka, drugi parametar oderđuje sam tekst ovog objekta.
Pozicija ovog teksta unutar polja evidinecija učinka je definisana linijom koda ispravnihKomadaL.grid(row=8, column=0).

Na anlogan način su deklarisani svi ostali objekti tipa Label.

Pomoću linije koda ispravnihKomadaSB = Spinbox(evidencijaUcinkaLF, from_=0, to=1000) je deklarisan objekat tipa Spinbox i njegova minimalna i maksimalna vrijednost, kao i to da će se nalaziti u polju evidencija učinka. Minimalna vrijednost koja se može unijeti u ovo polje je 0 a maksimalna je 1000. Pomoću linije koda neispravnihKomadaSB.grid(row=10, column=6) je definisana pozicija ovog objekta unutar polja evidencija učinka. 

Na analogan način su definisani svi osttali objekti tipa Spinbox.

Time je opisano kako su realizirani objekti unutar polja evidencija učinka, kako možemo primjetiti da se ni ostala polja u suštini ne razlikuju od opisanog polja, iz izloženog je jasno kako su ostala polja realizirana. 

Pri pokretanju aplikacije u sva polja je unesena vrijednost 0, i to je ostvareno pomoću sljedećeg programskog koda:

profitE.insert(0,0)
nabavnaVrijednostE.insert(0,0)
periodOtplateE.insert(0,0)
cijenaPoSatuE.insert(0,0)
bonusiE.insert(0,0)
cijenaKomadaE.insert(0,0)
amortizovanaVrijednostE.insert(0,0)
alatIpriborE.insert(0,0)
subvencijePoticajiE.insert(0,0)
odrzavanjeIservisiranjeE.insert(0,0)
nusproduktiE.insert(0,0)
troskoviRadnikaE.insert(0,0)
gubiciProizvodnjeE.insert(0,0)
brojKomadaE.insert(0,0)
troskoviMasineE.insert(0,0)
ukupniTrosakE.insert(0,0)
prihodiE.insert(0,0)
profitIzProizvodnjeE.insert(0,0)

Dakle korištenjem metode insert u sva polja je unesena vrijednost 0.

Objekti koji se nalaze u polju rezultati služe za prikaz izračunatih podataka i nisu namjenjeni za unos podataka, pa je zbog to onemogućeno korisniku da unosi podatke u ovom polju. Ova zabrana je realizirana pomoću sljedećeg koda:

profitIzProizvodnjeE.configure(state=DISABLED)
gubiciProizvodnjeE.configure(state=DISABLED)
brojKomadaE.configure(state=DISABLED)
troskoviRadnikaE.configure(state=DISABLED)
troskoviMasineE.configure(state=DISABLED)
ukupniTrosakE.configure(state=DISABLED)
prihodiE.configure(state=DISABLED)
profitE.configure(state=DISABLED)


U programu se također nalaze dva dugmeta: Ok i Prikaži zaključak. Ova dva dugmenta su realizirana pomoću sljedećih linija koda:
dugmeOk = Button(root, text="OK", command=genersi)
dugmeZakljucak = Button(root, text="Prikaži zaključak", command=genersi1)

dugmeOk.grid(row=2, column=0);
dugmeZakljucak.grid(row=2, column=1);

Dakle, linijom koda – je deklarisan objekat tipa Button, prvi parametar u zagradi je root i ovime je određeno da će se dugme nalaziti direktno u glavnom prozoru, a ne u nekom od polja. Drugi parametar je tekst koji se nalazi na dugmetu, dok je treći parametar naziv funkcije koja će se pozvati kada korisnik klikne na dugme. Vidimo da je naziv ove funkcije generisi. Funkcija generiši će biti opisana u nastavku. Na analogan način je realizirano i drugo dugme.

U tijelu funkcije generisi se izračunavaj sve potrebne vrijednosti. Tako pomoću koda 

profitIzProizvodnjeE.configure(state=NORMAL),
profitIzProizvodnjeE.delete(0,END), 
profitIzProizvodnjeE.insert(0,int(ispravnihKomadaSB.get()) * float(cijenaKomadaE.get())), 
profitIzProizvodnjeE.configure(state=DISABLED),

se u prvoj liniji omogućava unos u ovo polje, u drugoj linije se briše sve iz ovog polja, u trećoj liniji se unosi podatak koji je umnožak vrijednosti koja je unesena u polje broj ispravnih komada i vrijednosti unesene u polje cijena komada. Na kraju u posljednjoj liniji se ponovo onemogućava unos u ovo polje. 

Dakle korištenjem metode delete je izbrisan sadržaj polja, a metodom insert je unesena izračunata vrijednost. Metodom get je očitana vrijednost iz ostalih polja, dok metoda configure služu za postavljanje stanja polja tj. hoće li se ono moći mjenjati ili ne. 

Na analogan način su izračunate i ostale vrijednosti koje se nalaze u polju rezultati.

Pomoću linija koda 

prazanZakljucakL = Label(zakljucakLF, text="       ",justify=LEFT, font=("Helvetica", 15))
prazanZakljucakL.grid(row=1, column=0) 

se deklariše objekat tipa Label pod nazivom prazanZakljucak, za razliku od ostalih objekata tipa Label, kod ovog objekta je pri deklaraciji zadan font i veličina fonta. Ovaj objekat je će služiti za ispis zaključka kojeg aplikacija generiše, što će biti opisano na kraju. Dakle tekst ovog objekta je podložan promjenama. 

U funkciji generisi1 se nalazi if – else konstrukcija:

if float(profitE.get()) * int(periodOtplateE.get()) <= float(nabavnaVrijednostE.get()):
        prazanZakljucakL.config(text="Mašina nije isplativa!")
        prazanZakljucakL.config(fg="RED")
    elif float(profitE.get()) * int(periodOtplateE.get())>float(nabavnaVrijednostE.get()):
        prazanZakljucakL.config(text="Mašina jeste isplativa!")
        prazanZakljucakL.config(fg="GREEN") 

Vidim da ukoliko je vrijednost iz polja profit pomnožena sa vrijednošću iz polja period otplate manja ili jednaka od vrijednosti iz polja nabavna vrijedost tekst objekta prazanZakljucak će pomoću metode config biti postavljen na "Mašina nije isplativa". Također boja ovog teksta je crvena. Ovo je ostvareno linijama koda :

prazanZakljucakL.config(text="Mašina nije isplativa!")
prazanZakljucakL.config(fg="RED"),

dakle korištenjem metode config.

Ukoliko pak spomenuti uslov nije zadovoljen pozivaju se sljedeće dvije linije koda:

prazanZakljucakL.config(text="Mašina jeste isplativa!")
prazanZakljucakL.config(fg="GREEN")

koje rezultiraju time da će tekst objekta prazanZaključak biti postavljen na "Mašina jeste isplativa" i to u zelenoj boji. 

Time je opisan način na koji je ova jednostavna ali korisna aplikacija isporogramiran, koji objekti iz moula tkinter su korišteni, na koji način je rukovano unesenim podacima, kao i logika same aplikacije. 

