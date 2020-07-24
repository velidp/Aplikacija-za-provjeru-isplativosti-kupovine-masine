# Aplikacija za provjeru isplativosti kupovine mašine

Aplikacija je implementriana korištenjem programsko jezika **Python** i modula **Tkinter**. 
Jednostvan je za korištenje i posjeduje intuitivan grafički korisnički interfejs.

Aplikacija služi za provjeru da li je mašina isplativa za kupovinu. 
Korisnik aplikacija unosi podatke o mašini i radnicima koji će raditi sa tom mašinom.
Podaci koji se unose su podijeljeni u četri kategorije:

Kategorija **_Evidnecija učinka_**:
  
  _-Broj ispravnih komada
  
  _-Broj neispravnih komada
  
  _-Cijena jednog komdaa

Kategorija **_Troškovi mašine**:

  _-Nabavna vrijednost mašine
  
  _-Broj mjeseci otplate
  
  _-Amortizovana vrijednost
  
  _-Mjesečni troškovi održavanja i servisiranja mašine
  
  _-Mjesečni troškovi alta, pribora i opreme
  
Kategorija **_Troškovi radnika**:

  _-Broj radnih sati mjesečno
  
  _-Cijena po satu
  
  _-Bonusi
  
Kategorija **_Prihodi**:
  
  _-Subvencije i poticaji
  
  _-Nusprodukti
  

Početni izgled grafičkog korisničkog interfejsa:
<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/Aplikacija-za-provjeru-isplativosti-kupovine-masine/master/Slike/GUI%201.png" width="800">
</p>
Nakon što korisnik unese gore nabrojane parametre, klikom na dugme OK u okviru Rezultat se prikazuju izračunate vrijednosti.
Vrijednosti koje aplikacija računa na osnovu unesnih parametara su:


  _-Profit iz proizvodnje
  
  _-Gubici iz proizvodnje
  
  _-Ukupan broj komada
  
  _-Troškovi radnika
  
  _-Troškovi mašine
  
  _-Ukupni trošak
  
  _-Ukupni prihodi
  
  _-Profit

Na osnovu izračunatih parametara aplikacija u okviru Zaključak nakon što korisnik aplikacija klikne na dugme prikaži zaključak ispisuje zaključak _"Mašina jeste isplativa"_ ili _"Mašina nije isplativa"_.

Ukoliko je ispunjen uslov _if ((profit * period otplate) <= (nabavna vrijednost mašine))_ aplikacija prikazuje zaključak _"Mašina nije isplativa"_.
Primjer podatak za koje ovaj uslov ispunjen i konačni izgled grafičkog korisničkog interfejsa za ovakve podatke je prikazan na sljedećoj slici:
<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/Aplikacija-za-provjeru-isplativosti-kupovine-masine/master/Slike/GUI2.png" width="800">
</p>


U suprotom, ako prethodni uslov nije ispunjen, tj. ukoliko je ispunjen uslov _if ((profit * period otplate) > (nabavna vrijednost mašine))_ aplikacija ispisuje zaključak _"Mašina jeste isplativa"_.
Izgled grafičkog korisničkog interfejsa za ovaj slučaj je prikazan na sljedećoj slici:
<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/Aplikacija-za-provjeru-isplativosti-kupovine-masine/master/Slike/GUI3.png" width="800">
</p>
