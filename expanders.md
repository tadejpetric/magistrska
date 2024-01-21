
# Cheegerjeva konstanta
V grafu imamo množico vozlišč $V(G)$. Gledamo njene podmnožice \(A\subseteq V(G)\) in kako se povezujejo s komplementom \(\overline A\). Množico povezav do komplementa označimo z \(\partial A\).
Definiramo Cheegerjevo konstanto kot [^1]

\[h(g) = \min\left(\frac{\partial A}{A} \mid 0 < |A| \leq |V(G)|/2\right)\]

Konstanta je 0 natanko takrat, ko je graf nepovezan (vzamemo \(A\) kot povezano komponento). Visoka konstanta pomeni visoko povezljivost glede na število vozlišč. 

# Spektralne lastnosti
Grafom lahko pripišemo matriko sosednosti (polje je 1 na koordinati \(ij\) v matriki, če sta vozlišči povezani). Matrika je vedno simetrična (torej ima realne lastne vrednosti).

Če je graf d-regularen so lastne vrednosti v \([-d, d]\) (najmanjša je \(-d\) natanko ko je graf dvodelen). Največja lastna vrednost je \(\lambda_1=d\)

Najmanjšo lastno vrednost označimo z \(\lambda_n\), največjo z \(\lambda_1\).

Pri regularnih grafih je stacionarna distribucija (\(Au=du\)) vektor \(1/n\). Spektralno luknjo definiramo kot \(d-\lambda_2\).

Spectral expansion definiramo kot mejo lastnih vrednosti: \(\lambda = \max_{i\neq 1}|\lambda_i|\) otiroma \(\lambda = \max(|\lambda_2|, |\lambda_n|)\)

# Alon-Boppanov izrek [^2]
Za vse dovolj velike d-regularne grafe velja

\[\lambda_2 \geq 2\sqrt{d-1} -o(1)\]

oziroma (kjer je m premer - največja razdalja med dvema vozliščema v grafu)

\[\lambda_2 \geq 2\sqrt{d-1} - \frac{2\sqrt{d-1}-1}{\lfloor m/2 \rfloor}\]

Torej tudi \(\lambda \geq 2\sqrt{d-1} -o(1)\) za dovolj velike grafe. Obratno, \(\lambda < 2\sqrt{d-1}\) samo za končno mnogo grafov (s parametri \(n, d, \lambda\))

# Ramanujanovi grafi
Za Ramanujanove grafe je ta meja točna.

Konstrukcija [^3]


[^1]: [Exapander graph](https://en.wikipedia.org/wiki/Expander_graph)
[^2]: [Alon boppana meja](https://en.wikipedia.org/wiki/Alon%E2%80%93Boppana_bound)
[^3]: [5.12 (51) konstrukcija ramanujan](https://www.cs.huji.ac.il/~nati/PAPERS/expander_survey.pdf)