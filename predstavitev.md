
# Motivacija
Želimo grafe, ki imajo visoko količino povezav.

Na primer imamo veliko računalnikov, ki so povezani z kabli. Želimo, da se lahko poljubna dva računalnika pogovarjata med sabo. Lahko pa se zgodi, da se tekom uporabe en (ali več) izmed kablov uniči. Zato želimo nekaj redundantnosti in, da sta poljubna dva računalnika še vedno povezana če se uniči nekaj kablov (če le ne preveč). Po drugi strani pa je polaganje kablov drago in ne želimo kar za graf povezav uporabiti polnega grafa, ki je očitno najbolj odporen proti motnjam. Želimo torej uravnotežen primer, kjer uporabimo čim manj kablov, vendar pa je naša mreža čim bolj odporna proti motnjam.

# Ekspanzivnost povezav (Cheegerjeva konstanta)
Prejšni problem bi lahko opisali bolj matematično tako:
Imamo množico vozlišč S. Če jih želimo odrezati od preostanka grafa moremo odstraniti |\partial S| = |dS| povezav. To lahko "normaliziramo" - koliko povezav smo morali odstraniti za vsako vozlišče v S v povprečju |dS|/|S|, upoštevamo pa samo S, ki so manjši od polovice grafa (sicer bi lahko gledali raje komplement). Minimum tega izraza po S predstavlja "najmanj koliko povezav moremo odstraniti v povprečju, da ločimo graf". To imenujemo Cheegerjeva konstanta c(G)

## Primeri
n-cikel ima c(G) = 4/n
Poln graf ima c(G) = n/2

# Spektralna ekspanzivnost
Obstaja še soroden pojem ekspanzivnosti: spektralna ekspanzivnost oz. spektralna luknja. Tega bomo opisali za primer d-regularnih grafov.

Grafi imajo matriko sosednjosti, ki ima lastne vrednosti. Vsi d-regularni grafi imajo največjo lastno vrednost d (v splošnem je celo največja lastna vrednost omejena z najvišjo stopnjo vozlišča v grafu). Zanima nas druga največja lastna vrednost, ki jo označimo z \lambda oziroma njena "luknja" do najvišje lastne vrednosti, d. Označimo s(G) = d-\lambda

## Primeri
TODO: Izračunaj za cikle, polne grafe etc.

# Cheegerjeva neenakost
Pojma Cheegerjeve konstante grafa in spektralne luknje sta povezana
2c >= s >= c²/(2d)
Torej če ima graf majhno spektralno luknjo ima tudi boljšo ekspanzivnost.

# Izrek Alon-Boppana
Če je graf d regularen z d vozlišči in premerom m, potem
$$
\lambda \geq 2\sqrt{d-1} - \frac{2\sqrt{d-1}-1}{\floor{m/2}}
$$

Asimptotično to pomeni da, če imamo družino d-regularnih grafov za katere |V| -> inf ko m->inf
Potem
$$
liminf_m \lambda \geq 2\sqrt{d-1}
$$


# Ramanujanov graf
Graf je Ramanujanov, če $\max_i |\lambda_i| \leq 2\sqrt{d-1}$

V nekem smislu so to grafi, za katere je Alon-Boppanova meja točna.

## Primeri

# Konstrukcije grafov
Ramanujanovi grafi so razmeroma pogosti. Enostavne konstrukcije pa potrebujejo naraščujoče stopnje vozlišč oz nelinearno stopnjevanje povezav, glede na dodajanje robov. Če fiksiramo stopnjo bo naraščanje povezav le linearno in graf bo veliko bolj učinkovit.

Problem je torej poiskati, za fiksen d, neskončno družino Ramanujanovih grafov

## Splošni grafi
### Cayleyevi grafi
Caylejev graf je način kako lahko predstavimo grupo v obliki grafa. Vsak element grupe predstavimo z enim vozliščem. Imamo še fiksno množico S. Naredimo povezave med vsemi (g, gs)
## Dvodelni grafi
