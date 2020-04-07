# GenomicIT

Repository for the master course Genomic IT at the School of Electrical Engineering

## Zadatak 5
Implementirati na programskom jeziku Python algoritam za indeksirano pretraživanje stringova u zatadom tekstu koristeći Burrows-Wheeler transformaciju i FM index. Inicijalna verzija algoritma treba da bude realizovana na tradicionalan način opisan na predavanju, bez optimizicije memorije i vremena izvršavanja (10 poena).

Za svaku od funkcija u kodu, kao i za sam finalni algoritam napisati testove (5 poena).

Izvršiti optimizaciju koda iz aspekta zauzeća memorije i vremena izvršavanja. Pokrenuti prethodno definisane testove i proveriti da li i dalje svi prolaze (regresiono testiranje). Izmeriti unapređenje zauzeća memorije i vremena izvršavanja koristeći kao test podatke 3 seta (10 poena):
* Tekst: Coffea arabica, Chromosome 1c i paterni: ATGCATG, TCTCTCTA, TTCACTACTCTCA
* Tekst: Mus pahari chromosome X, i paterni: ATGATG, CTCTCTA, TCACTACTCTCA
* Genom po slobodnom izboru iz NIH baze i proizvoljna 3 paterna različite dužine.

Pripremiti prezentaciju (Google slides ili power point) inicijalnog i optimizovanog algoritma, kao i samih rezultata (5 poena).

Pripremiti video prezentaciju projekta (3 - 5 minuta trajanja) koja će biti dostupna na YouTube ili drugom on-line video servisu (10 poena).

## Komande za pokretanje analize i pertraživanje

`python main.py -s/-ss/-o file_full_path niz_stringova_koji_se_pretražuje`

Treba navesti samo jednu od opcija -s -ss -c
* -s - jednostavan algoritam sa naivnom implementacijom konstrukcije sufiksnog niza
* -ss - jednostavan algoritam koji za konustrukciu sufiksnog niza koristi SAIS implementaciju u C-u
* -o - optimizovan algoritam koji za konustrukciu sufiksnog niza koristi SAIS implementaciju u C-u

Potrebno je imati izvršni fajl SAIS imlementacije za konstrukciju sufiksnog niza pod nazivom `sais` u istom folderu gde se nalazi skripta `main.py`

Primer pretraživanja stringova `ACACAC`, `ATGCATGC`, `ATTTTATAT` u okviru fajla `Coffea arabica chromosome 1c.fasta` pomoću optimizovanog algoritma

`python main.py -o "puna\putanja\do\fajla\Coffea arabica chromosome 1c.fasta"` `ACACAC`, `ATGCATGC`, `ATTTTATAT`

Skripta sa testovima se naziva `bwt_fm_test.py`. Ona zahteva fajlove koji sadrže sufiksni niz za svaki od tekstova koji se testira ("", "ABAABA", "MAMA", "BANANA", "ABRACADABRA") i jedan fajl koji sadrži BWT teksta "ABRACADABRA". Svi fajlovi treba da imaju naziv kao tekst na koji se odnose zapisan malim slovima osmi za prazan tekst gde se fajl zove "empty". Ektstenzije fajlova treba da budu .suffix ili .bwt. Fajlovi se očekuju u folderu test.

Video: https://youtu.be/YDkezNHV2Uw 
