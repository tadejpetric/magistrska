# Cheegerjeva konstanta
V grafu imamo množico vozlišč $V(G)$. Gledamo njene podmnožice \(A\subseteq V(G)\) in kako se povezujejo s komplementom \(\overline A\). Množico povezav do komplementa označimo z \(\partial A\).
Definiramo Cheegerjevo konstanto kot

\[h(g) = \min\left(\frac{\partial A}{A} \mid 0 < |A| \leq |V(G)|/2\right)\]

Konstanta je 0 natanko takrat, ko je graf nepovezan (vzamemo \(A\) kot povezano komponento). Visoka konstanta pomeni visoko povezljivost glede na število vozlišč. 

# Spektralne lastnosti
Grafom lahko pripišemo matriko sosednosti (polje je 1 na koordinati \(ij\) v matriki, če sta vozlišči povezani). Matrika je vedno simetrična (torej ima realne lastne vrednosti).

Če je graf d-regularen so lastne vrednosti v \([-d, d]\) (najmanjša je \(-d\) natanko ko je graf dvodelen). Največja lastna vrednost je \(\lambda_1=d\)

Najmanjšo lastno vrednost označimo z \(\lambda_n\), največjo z \(\lambda_1\).

Pri regularnih grafih je stacionarna distribucija (\(Au=du\)) vektor \(1/n\). Spektralno luknjo definiramo kot \(d-\lambda_2\)