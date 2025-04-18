# Konstrukcija Ramanujanivih grafov
## Ramanujanova domneva


# Konstrukcija dvodelnih ramanujanovih grafov

Članek [Interlacing Families I: Bipartite Ramanujan Graphs of All Degrees](https://arxiv.org/pdf/1304.4132.pdf)

## Intro
Vsi d-regularni grafi imajo lastno vrednost matrike sosednosti \(d\). Natanko dvodelni imajo tudi \(-d\).
Graf je Ramanujanov, če so vse ostale lastne vrednosti v \([-2\sqrt{d-1}, 2\sqrt{d-1}]\).

Enostavno je najti Ramanujanove grafe (npr. \(K_n\)). Težava je poiskati neskončno družino Ramanujanovih grafov za fiksni \(d\) (kjer je \(d\) stopnja regularnosti) (pri polnih grafih ta narašča)

## 2-dvig

Imamo graf G=(V, E). Vsako vozlišče podvojimo (par vozlišč je vlakno).
Če smo imeli prej povezavo \((u, v)\) in je \(\{u_0, u_1\}\) vlakno \(u\) in \(\{v_0, v_1\}\) vlakno \(v\), potem dvig lahko vsebuje povezave tipa
- \((u_0, v_0) \land (u_1, v_1)\)
- \((u_0, v_1) \land (u_1, v_0)\)

Zaradi nekega razloga ne dovolimo obeh povezav med istima vozliščema hkrati.

Če ima samo prvega, dobimo dve kopiji G.

![Kopiji G](images/image.png)
Če vsebuje samo povezave drugega tipa dobimo dobimo "dvojni krov" G.

![Dvojni krov](images/image-2.png)

Matriko sosednosti dviga se lahko definira kot matriko sosednosti G, le da so vrednosti -1, če je povezava drugega tipa (in +1, če prvega tipa). Lastne vrednosti dvignjenega grafa so unija prejšnjih lastnih vrednosti, in lastnih vrednosti nove matrike sosednosti.

Pokazali so, da ima vsak graf (z kvečjemu \(d\) sosedov) izbiro povezav, da so lastne vrednosti dviga \(O(\sqrt{d\log^3(d)})\). Potem delajo expander grafe, da delajo 2-dvige d-regularnega grafa. Sumili so, da obstaja izbira dviga, da so absolutne lastne vrednosti kvečjemu \(2\sqrt{d-1}\). Če delamo z dvodelnimi grafi vemo, da so lastne vrednosti simetrične. Torej lahko dokažemo le, da so manjše od \(2\sqrt{d-1}\) in absolutnost sledi (in iz tega Ramanujanost).


## Irregularni ramanujanovi grafi
Graf je \((c,d)\)-biregularen, če je dvodelen in ena particija stopnje \(c\), druga stopnje \(d\). Vedno ima trivialne lastne vrednosti \(\pm\sqrt{cd}\) Je Ramanujanov, če so netrivialne lastne vrednosti po absolutni vrednosti manjše od \(\sqrt{c-1} + \sqrt{d-1}\). Dokažejo obstoj neskončnih družin Ramanujanovih grafov za vse \(c, d\geq 3\)

## Univerzalni krov
Univerzalni krov grafa G je neskončno drevo T, za katerega so vsi povezani dvigi Gja kvocienti Tja.

### Konstrukcija univerzalnega krova
Pot na grafu je povratna, če naredi korak nazaj, t.j., \(v_{i+1} = v_{i-1}\).

Izberemo si začetno vozlišče \(v_0\). Potem v T dodamo vozlišča, za vsako nepovratno pot v G, ki se začne v \(v_0\). Med sprehodi je povezava, če lahko dobimo drugega kot en dodatni korak prvega \((v_0,\ldots, v_j)\sim(v_0,\ldots,v_{j+1})\). Dobimo neke vrste Trie.

Pravi, da je rezultat izomorfen ne glede na izbiro \(v_0\) ampak mislim, da more biti za to graf povezan

### Lastnosti
Sosednostna matrika je neskončno dimenzionalna in simetrična. Zanima nas spektralni radij matrike

\(\rho(T) = \sup_{\lVert x \rVert = 1}\lVert A_T x \rVert_2\)

(Norme so standardne, ko vrste konvergirajo.)

Če imamo neskončno družino grafov, ki imajo isti univerzalni krov T, potem imajo vsi dovolj veliki grafi netrivialno vrednost večjo od \(\rho(T)-\varepsilon\). Definiramo, da je graf ramanujanov, če so vse njegove netrivialne vrednosti manjše od \(\rho(T)\) po absolutni vrednosti.

Univerzalni krov d-regularnega grafa je d-arno drevo. (c,d)-biregularno drevo ima stopnje, ki alternirajo med c in d.

# Reading list
[New and Explicit Constructions of Unbalanced Ramanujan Bipartite Graphs](https://arxiv.org/pdf/1910.03937.pdf)