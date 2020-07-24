# Aplikacija za provjeru isplativosti kupovine mašine

Aplikacija je implementriana korištenjem programsko jezika **Python** i modula **Tkinter**. 
Jednostvan je za korištenje i posjeduje intuitivan grafički korisnički interfejs.

Aplikacija služi za provjeru da li je mašina isplativa za kupovinu. 
Korisnik aplikacija unosi podatke o mašini i radnicima koji će raditi sa tom mašinom.
Podaci koji se unose su podijeljeni u četri kategorije:

Kategorija **Evidnecija učinka**:
  Broj ispravnih komada
  Broj neispravnih komada
  Cijena jednog komdaa
Kategorija **troškovi mašine**:
  -Nabavna vrijednost mašine
  -Broj mjeseci otplate
  -Amortizovana vrijednost
  -Mjesečni troškovi održavanja i servisiranja mašine
  -Mjesečni troškovi alta, pribora i opreme
Kategorija **Troškovi radnika**:
  -Broj radnih sati mjesečno
  -Cijena po satu
  -Bonusi
Kategorija **Prihodi**:
  
  -Subvencije i poticaji
  
  -Nusprodukti
  

Početni izgled grafičkog korisničkog interfejsa:
<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/Aplikacija-za-provjeru-isplativosti-kupovine-masine/master/Slike/GUI%201.png" width="800">
</p>
Nakon što korisnik unese gore nabrojane parametre, klikom na dugme OK u okviru Rezultat se prikazuju izračunate vrijednosti.
Vrijednosti koje aplikacija računa na osnovu unesnih parametara su:
  -Profit iz proizvodnje
  -Gubici iz proizvodnje
  -Ukupan broj komada
  -Troškovi radnika
  -Troškovi mašine
  -Ukupni trošak
  -Ukupni prihodi
  -Profit

Na osnovu izračunatih parametara aplikacija u okviru Zaključak nakon što korisnik aplikacija klikne na dugme prikaži zaključak ispisuje zaključak "Mašina jeste isplativa" ili "Mašina nije isplativa".

Ukoliko je ispunjen uslov if ((profit * period otplate) <= (nabavna vrijednost mašine)) aplikacija prikazuje zaključak "Mašina nije isplativa".
Primjer podatak za koje ovaj uslov ispunjen i konačni izgled grafičkog korisničkog interfejsa za ovakve podatke je prikazan na sljedećoj slici:
<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/Aplikacija-za-provjeru-isplativosti-kupovine-masine/master/Slike/GUI2.png" width="800">
</p>


U suprotom, ako prethodni uslov nije ispunjen, tj. ukoliko je ispunjen uslov if ((profit * period otplate) > (nabavna vrijednost mašine)) aplikacija ispisuje zaključak "Mašina jeste isplativa".
Izgled grafičkog korisničkog interfejsa za ovaj slučaj je prikazan na sljedećoj slici:
<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/Aplikacija-za-provjeru-isplativosti-kupovine-masine/master/Slike/GUI3.png" width="800">
</p>
