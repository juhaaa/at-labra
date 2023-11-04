# Aiheen määrittely

## Polunetsintä, Dijkstra vs JPS

Työn aiheista mielenkiintoisimmaksi koin verkot ja polunetsinnän. Tarkoituksenani on toteuttaa ja vertailla vähintään kahta reitinhakualgoritmia, alustavasti Dijkstra ja Jump Point Search. Jos työ sujuu ja etenee, olisi algoritmeja mielenkiintoista toteuttaa kolmaskin. Työ on tarkoitus toteuttaa käyttäen Python- ohjelmointikieltä.

---

## Algoritmit ja tietorakenteet

* Dijkstran- algoritmi
> BFS/Dijkstra on jollain tapaa tuttu aikaisemmilta tietorakenteiden kursseilta. Toteutukseen löytyy hyvä apu aikaisemmasta kurssimonisteesta.
* Jump Point Search
> JPS tulee olemaan uuteen tutustumista tämän kurssin myötä.
* Verkko ja sen muodostaminen
> Verkkona täytynee käyttää JPS- algoritmin myötä ruudukkotyyppistä verkkoa. Liikkumisen kustannus on joka suuntaan sama ja solmulla voi olla maksimissaan 8 naapuria ja kulku maksimissaan yhtä moneen suuntaan. Verkkoon pitää voida merkitä solmut, joissa kulkeminen ei ole sallittua.

## Ohjelma syöte ja toiminta

Ajatuksena on käyttää ohjelman syötteenä kurssin moodle- sivuilta löytyvän [linkin](https://www.movingai.com/benchmarks/street/index.html) karttoja png muotoisina. Ohjelmaan voi graafisen käyttöliittymän kautta tuoda kuvatiedoston. Vaatimuksena kartoille on (lähinnä linkin kuvien formaatin vuoksi), että ne ovat kaksivärisiä(0,0,0 ja 229,229,229) ja png- muodossa. Musta väri kuvaa aluetta jolla ei voi liikkua ja harmaa alue kuvaa vapaata kulkua. Png- muotoisesta kuvasta muodostetaan verkko niin, että 1 pikseli kuvaa yhtä solmua. Karttoja voi myös piirtää itse.

Käyttöliittymän kautta käyttäjä valitsee lähtö- ja maalikoordinaatit, sekä käytettävän algoritmin. Ohjelma suorittaa reittihaun, kun käyttäjä valitsee "Start". Haun suorittamisen jälkeen ohjelma raportoi tulokset ja palauttaa uuden kuvan, johon on lisätty vieraillut solmut ja löydetty reitti.

## Koulutusohjelma ja kieli

Koulutusohjelmani on tietojenkäsittelytieteen kandidaatti ja dokumentaatiossa ja koodin kommentoinnissa käytetty kieli on suomi.


## Lähteet

[Tirakirja](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)
[Dijkstra wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
[JPS](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf)
[JPS, medium](https://dibyendu-biswas.medium.com/understanding-jump-point-search-jps-algorithm-554c99aab178)
