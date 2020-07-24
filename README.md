# Aplikacija za provjeru isplativosti kupovine mašine

Aplikacija je implementriana korištenjem programsko jezika **Python** i modula **Tkinter**. Jednostvan je za korištenje i posjeduje intuitivan grafički korisnički interfejs. Aplikacija služi za provjeru da li je mašina isplativa za kupovinu. 

Korisnik aplikacija unosi podatke o mašini i radnicima koji će raditi sa tom mašinom. Podaci koji se unose su podijeljeni u četiri kategorije.  

U kategoriji **_Evidnecija učinka_** korisnik unosi sljedeće parametre:  
  _-Broj ispravnih komada_  
  _-Broj neispravnih komada_  
  _-Cijena jednog komdaa_  

U kategorija **_Troškovi mašine_** unose se sljedeći parametri:  
  _-Nabavna vrijednost mašine_  
  _-Broj mjeseci otplate_  
  _-Amortizovana vrijednost_  
  _-Mjesečni troškovi održavanja i servisiranja mašine_  
  _-Mjesečni troškovi alta, pribora i opreme_  
  
U kategoriji **_Troškovi radnika_** potrebno je unijeti sljedeće parametre:

  _-Broj radnih sati mjesečno_
  
  _-Cijena po satu_
  
  _-Bonusi_
  
U kategoriji **_Prihodi_** se unose sljedeća dva parametra:
  
  _-Subvencije i poticaji_
  
  _-Nusprodukti_
  

Početni izgled grafičkog korisničkog interfejsa:
<p align="left">
  <img src="https://raw.githubusercontent.com/velidp/Aplikacija-za-provjeru-isplativosti-kupovine-masine/master/Slike/GUI%201.png" width="800">
</p>
Nakon što korisnik unese gore nabrojane parametre, klikom na dugme OK u okviru **_Rezultat_** se prikazuju izračunate vrijednosti.
Vrijednosti koje aplikacija računa na osnovu unesnih parametara su:





  _-Profit iz proizvodnje_
  
  _-Gubici iz proizvodnje_
  
  _-Ukupan broj komada_
  
  _-Troškovi radnika_
  
  _-Troškovi mašine_
  
  _-Ukupni trošak_
  
  _-Ukupni prihodi_
  
  _-Profit_

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
