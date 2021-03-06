from tkinter import *

root = Tk()
root.geometry("1140x590")
root.title("Cost effectiveness check");
root.resizable(False, False)

evidencijaUcinkaLF = LabelFrame(root, text=" 1. Performance records: ")
evidencijaUcinkaLF.grid(row=0, column=0, sticky='W', padx=5, pady=5, ipadx=87, ipady=32)

zakljucakLF = LabelFrame(root, text=" Conclusion: ")
zakljucakLF.grid(row=3, column=1, sticky='W', padx=5, pady=5, ipadx=120, ipady=80)

troskoviMasineLF = LabelFrame(root, text=" 2. Machine costs: ")
troskoviMasineLF.grid(row=0, column=1, sticky='W', padx=5, pady=5, ipadx=20, ipady=8)

troskoviRadnikaLF = LabelFrame(root, text=" 3. Worker costs: ")
troskoviRadnikaLF.grid(row=1, column=0, sticky='W', padx=5, pady=5, ipadx=103, ipady=8)

prihodiLF = LabelFrame(root, text=" 4. Income: ")
prihodiLF.grid(row=1, column=1, sticky='W', padx=5, pady=5, ipadx=115, ipady=20)

rezulatatLF = LabelFrame(root, text=" Results: ")
rezulatatLF.grid(row=3, column=0, sticky='W', padx=5, pady=5, ipadx=133, ipady=5)

ispravnihKomadaL = Label(evidencijaUcinkaLF, text="Number of correctly produced pieces: ",anchor=E)
ispravnihKomadaSB = Spinbox(evidencijaUcinkaLF, from_=0, to=1000)
ispravnihKomadaL.grid(row=8, column=0)
ispravnihKomadaL.grid(row=8, column=0, sticky='E', padx=6, pady=2)
ispravnihKomadaSB.grid(row=8, column=6)

neispravnihKomadaL = Label(evidencijaUcinkaLF, text="Number of incorrectly produced pieces: ",anchor=E)
neispravnihKomadaSB = Spinbox(evidencijaUcinkaLF, from_=0, to=1000)
neispravnihKomadaL.grid(row=10, column=0)
neispravnihKomadaL.grid(row=10, column=0, sticky='E', padx=4, pady=2)
neispravnihKomadaSB.grid(row=10, column=6)

cijenaKomadaL = Label(evidencijaUcinkaLF, text="The price of one piece: ",anchor=E)
cijenaKomadaLB = Label(evidencijaUcinkaLF, text="€/piece",anchor=E)
cijenaKomadaE = Entry(evidencijaUcinkaLF, bd =2)
cijenaKomadaL.grid(row=12, column=0)
cijenaKomadaL.grid(row=12, column=0, sticky='E', padx=6, pady=2)
cijenaKomadaE.grid(row=12, column=6)
cijenaKomadaLB.grid(row=12, column=8)

subvencijePoticajiL = Label(prihodiLF, text="Subsidies and incentives: ",anchor=E)
subvencijePoticajiLB = Label(prihodiLF, text="€",anchor=E)
subvencijePoticajiE = Entry(prihodiLF, bd =2)
subvencijePoticajiL.grid(row=8, column=0)
subvencijePoticajiL.grid(row=8, column=0, sticky='E', padx=6, pady=2)
subvencijePoticajiE.grid(row=8, column=6)
subvencijePoticajiLB.grid(row=8, column=8)

nusproduktiL = Label(prihodiLF, text="By-products: ",anchor=E)
nusproduktiLB = Label(prihodiLF, text="€",anchor=E)
nusproduktiE = Entry(prihodiLF, bd =2)
nusproduktiL.grid(row=10, column=0)
nusproduktiL.grid(row=10, column=0, sticky='E', padx=6, pady=2)
nusproduktiE.grid(row=10, column=6)
nusproduktiLB.grid(row=10, column=8)

nabavnaVrijednostL = Label(troskoviMasineLF, text="Purchase value of the machine: ",anchor=E)
nabavnaVrijednostLB = Label(troskoviMasineLF, text="€",anchor=E)
nabavnaVrijednostE = Entry(troskoviMasineLF, bd =2)
nabavnaVrijednostL.grid(row=6, column=0)
nabavnaVrijednostL.grid(row=6, column=0, sticky='E', padx=6, pady=2)
nabavnaVrijednostE.grid(row=6, column=6)
nabavnaVrijednostLB.grid(row=6, column=8)

periodOtplateL = Label(troskoviMasineLF, text="Repayment period: ",justify=LEFT)
periodOtplateLB = Label(troskoviMasineLF, text="months",justify=LEFT)
periodOtplateE = Entry(troskoviMasineLF, bd = 2)
periodOtplateL.grid(row=8, column=0)
periodOtplateL.grid(row=8, column=0, sticky='E', padx=6, pady=2)
periodOtplateE.grid(row=8, column=6)
periodOtplateLB.grid(row=8, column=8)

amortizovanaVrijednostL = Label(troskoviMasineLF, text="Depreciated value: ",justify=LEFT)
amortizovanaVrijednostLB = Label(troskoviMasineLF, text="€",justify=LEFT)
amortizovanaVrijednostE = Entry(troskoviMasineLF, bd = 2)
amortizovanaVrijednostL.grid(row=10, column=0)
amortizovanaVrijednostL.grid(row=10, column=0, sticky='E', padx=6, pady=2)
amortizovanaVrijednostE.grid(row=10, column=6)
amortizovanaVrijednostLB.grid(row=10, column=8)

odrzavanjeIservisiranjeL = Label(troskoviMasineLF, text="Monthly costs of machine maintenance and servicing: ",justify=LEFT)
odrzavanjeIservisiranjeLB = Label(troskoviMasineLF, text="€",anchor=E)
odrzavanjeIservisiranjeE = Entry(troskoviMasineLF, bd =2)
odrzavanjeIservisiranjeL.grid(row=12, column=0)
odrzavanjeIservisiranjeL.grid(row=12, column=0, sticky='E', padx=6, pady=2)
odrzavanjeIservisiranjeE.grid(row=12, column=6)
odrzavanjeIservisiranjeLB.grid(row=12, column=8)

alatIpribor = Label(troskoviMasineLF, text="Monthly costs of tools, accessories and equipment: ",justify=LEFT)
alatiIpriborL = Label(troskoviMasineLF, text="€",anchor=E)
alatIpriborE = Entry(troskoviMasineLF, bd =2)
alatIpribor.grid(row=14, column=0)
alatIpribor.grid(row=14, column=0, sticky='E', padx=6, pady=2)
alatIpriborE.grid(row=14, column=6)
alatiIpriborL.grid(row=14, column=8)

brojRadnihSatiLabel = Label(troskoviRadnikaLF, text="Number of working hours per month: ",anchor=E)
brojRadnihSatiLB = Label(troskoviRadnikaLF, text=" ",anchor=E)
brojRadnihSatiSB = Spinbox(troskoviRadnikaLF, from_=0, to=1000)
brojRadnihSatiLabel.grid(row=6, column=0)
brojRadnihSatiLabel.grid(row=6, column=0, sticky='E', padx=6, pady=2)
brojRadnihSatiSB.grid(row=6, column=6)
brojRadnihSatiLB.grid(row=6, column=8)

cijenaPoSatuLB = Label(troskoviRadnikaLF, text="The price of one working hour: ",anchor=E)
cijenaPoSatuL = Label(troskoviRadnikaLF, text="€/h",anchor=E)
cijenaPoSatuE = Entry(troskoviRadnikaLF, bd =2)
cijenaPoSatuLB.grid(row=8, column=0)
cijenaPoSatuLB.grid(row=8, column=0, sticky='E', padx=6, pady=2)
cijenaPoSatuE.grid(row=8, column=6)
cijenaPoSatuL.grid(row=8, column=8)

bonusiL = Label(troskoviRadnikaLF, text="Bonuses: ",anchor=E)
bonusiLB = Label(troskoviRadnikaLF, text="€",anchor=E)
bonusiE = Entry(troskoviRadnikaLF, bd =2)
bonusiL.grid(row=10, column=0)
bonusiL.grid(row=10, column=0, sticky='E', padx=6, pady=2)
bonusiE.grid(row=10, column=6)
bonusiLB.grid(row=10, column=8)

profitIzProizvodnjeL = Label(rezulatatLF, text="Profit from production: ",anchor=E)
profitIzProizvodnjeLB = Label(rezulatatLF, text="€",anchor=E)
profitIzProizvodnjeE = Entry(rezulatatLF, bd =2)
profitIzProizvodnjeL.grid(row=8, column=0)
profitIzProizvodnjeL.grid(row=8, column=0, sticky='E', padx=6, pady=2)
profitIzProizvodnjeE.grid(row=8, column=6)
profitIzProizvodnjeLB.grid(row=8, column=8)

gubiciProizvodnjeL = Label(rezulatatLF, text="Production losses: ",anchor=E)
gubiciProizvodnjeLB = Label(rezulatatLF, text="€/piece",anchor=E)
gubiciProizvodnjeE = Entry(rezulatatLF, bd =2)
gubiciProizvodnjeL.grid(row=10, column=0)
gubiciProizvodnjeL.grid(row=10, column=0, sticky='E', padx=6, pady=2)
gubiciProizvodnjeE.grid(row=10, column=6)
gubiciProizvodnjeLB.grid(row=10, column=8)

brojKomadaL = Label(rezulatatLF, text="Total number of pieces: ",anchor=E)
brojKomadaE = Entry(rezulatatLF, bd =2)
brojKomadaL.grid(row=12, column=0)
brojKomadaL.grid(row=12, column=0, sticky='E', padx=6, pady=2)
brojKomadaE.grid(row=12, column=6)

troskoviRadnikaL = Label(rezulatatLF, text="Worker costs: ",anchor=E)
troskoviRadnikaLB = Label(rezulatatLF, text="€",anchor=E)
troskoviRadnikaE = Entry(rezulatatLF, bd =2)
troskoviRadnikaL.grid(row=14, column=0)
troskoviRadnikaL.grid(row=14, column=0, sticky='E', padx=6, pady=2)
troskoviRadnikaE.grid(row=14, column=6)
troskoviRadnikaLB.grid(row=14, column=8)


troskoviMasineL = Label(rezulatatLF, text="Machine costs: ",anchor=E)
troskoviMasineLB = Label(rezulatatLF, text="€",anchor=E)
troskoviMasineE = Entry(rezulatatLF, bd =2)
troskoviMasineL.grid(row=16, column=0)
troskoviMasineL.grid(row=16, column=0, sticky='E', padx=6, pady=2)
troskoviMasineE.grid(row=16, column=6)
troskoviMasineLB.grid(row=16, column=8)


ukupniTrosak = Label(rezulatatLF, text="Total cost: ",anchor=E)
ukupniTrosakL = Label(rezulatatLF, text="€",anchor=E)
ukupniTrosakE = Entry(rezulatatLF, bd =2)
ukupniTrosak.grid(row=18, column=0)
ukupniTrosak.grid(row=18, column=0, sticky='E', padx=6, pady=2)
ukupniTrosakE.grid(row=18, column=6)
ukupniTrosakL.grid(row=18, column=8)

prihodiL = Label(rezulatatLF, text="Total revenue: ",anchor=E)
prihodiLB = Label(rezulatatLF, text="€",anchor=E)
prihodiE = Entry(rezulatatLF, bd =2)
prihodiL.grid(row=20, column=0)
prihodiL.grid(row=20, column=0, sticky='E', padx=6, pady=2)
prihodiE.grid(row=20, column=6)
prihodiLB.grid(row=20, column=8)

profitL = Label(rezulatatLF, text="Profit: ",anchor=E)
troskoviMasineLB = Label(rezulatatLF, text="€",anchor=E)
profitE = Entry(rezulatatLF, bd =2)
profitL.grid(row=22, column=0)
profitL.grid(row=22, column=0, sticky='E', padx=6, pady=2)
profitE.grid(row=22, column=6)
troskoviMasineLB.grid(row=22, column=8)


zakljucakL = Label(zakljucakLF, text=" The following conclusion applies to the entered parameters:",justify=LEFT)
zakljucakL.grid(row=0, column=0)

prazanZakljucakL = Label(zakljucakLF, text="       ",justify=LEFT, font=("Helvetica", 15))
prazanZakljucakL.grid(row=1, column=0)

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

profitIzProizvodnjeE.configure(state=DISABLED)
gubiciProizvodnjeE.configure(state=DISABLED)
brojKomadaE.configure(state=DISABLED)
troskoviRadnikaE.configure(state=DISABLED)
troskoviMasineE.configure(state=DISABLED)
ukupniTrosakE.configure(state=DISABLED)
prihodiE.configure(state=DISABLED)
profitE.configure(state=DISABLED)

def genersi() : (prazanZakljucakL.config(text=" "),prazanZakljucakL.config(fg="RED"),
profitIzProizvodnjeE.configure(state=NORMAL),
profitIzProizvodnjeE.delete(0,END), 
profitIzProizvodnjeE.insert(0,int(ispravnihKomadaSB.get()) * float(cijenaKomadaE.get())), 
profitIzProizvodnjeE.configure(state=DISABLED),

gubiciProizvodnjeE.configure(state=NORMAL),
gubiciProizvodnjeE.delete(0,END), 
gubiciProizvodnjeE.insert(0,int(neispravnihKomadaSB.get()) * float(cijenaKomadaE.get())), 
gubiciProizvodnjeE.configure(state=DISABLED),

troskoviMasineE.configure(state=NORMAL),
troskoviMasineE.delete(0,END), 
troskoviMasineE.insert(0,float(amortizovanaVrijednostE.get()) + float(alatIpriborE.get()) + float(odrzavanjeIservisiranjeE.get())), 
troskoviMasineE.configure(state=DISABLED),

brojKomadaE.configure(state=NORMAL),
brojKomadaE.delete(0,END), 
brojKomadaE.insert(0,int(ispravnihKomadaSB.get()) + int(neispravnihKomadaSB.get())), 
brojKomadaE.configure(state=DISABLED),

troskoviRadnikaE.configure(state=NORMAL),
troskoviRadnikaE.delete(0,END), 
troskoviRadnikaE.insert(0,(int(brojRadnihSatiSB.get()) * float(cijenaPoSatuE.get())) + float(bonusiE.get())), 
troskoviRadnikaE.configure(state=DISABLED),

ukupniTrosakE.configure(state=NORMAL),
ukupniTrosakE.delete(0,END), 
ukupniTrosakE.insert(0,float(amortizovanaVrijednostE.get()) + float(alatIpriborE.get()) + float(odrzavanjeIservisiranjeE.get()) + int(brojRadnihSatiSB.get()) * float(cijenaPoSatuE.get()) + float(bonusiE.get())+int(neispravnihKomadaSB.get()) * float(cijenaKomadaE.get())),  
ukupniTrosakE.configure(state=DISABLED),

prihodiE.configure(state=NORMAL),
prihodiE.delete(0,END), 
prihodiE.insert(0, int(ispravnihKomadaSB.get()) * float(cijenaKomadaE.get()) + float(subvencijePoticajiE.get()) + float(nusproduktiE.get())),  
prihodiE.configure(state=DISABLED),


profitE.configure(state=NORMAL),
profitE.delete(0,END), 
profitE.insert(0, (int(ispravnihKomadaSB.get()) * float(cijenaKomadaE.get()) + float(subvencijePoticajiE.get()) + float(nusproduktiE.get())) - (float(amortizovanaVrijednostE.get()) + float(alatIpriborE.get()) + float(odrzavanjeIservisiranjeE.get()) + int(brojRadnihSatiSB.get()) * float(cijenaPoSatuE.get()) + float(bonusiE.get())+int(neispravnihKomadaSB.get()) * float(cijenaKomadaE.get()))),  
profitE.configure(state=DISABLED),

)

def genersi1():
    if float(profitE.get()) * int(periodOtplateE.get()) <= float(nabavnaVrijednostE.get()):
        prazanZakljucakL.config(text="The machine is not cost effective!")
        prazanZakljucakL.config(fg="RED")
    elif float(profitE.get()) * int(periodOtplateE.get())>float(nabavnaVrijednostE.get()):
        prazanZakljucakL.config(text="The machine is cost effective!")
        prazanZakljucakL.config(fg="GREEN")
    

dugmeOk = Button(root, text="OK", command=genersi)
    
dugmeZakljucak = Button(root, text="Show conclusion", command=genersi1)

dugmeOk.grid(row=2, column=0);
dugmeZakljucak.grid(row=2, column=1);


root.mainloop()