# Solution au démonstrations

import pandas as pd
donnees = pd.read_excel("estimation-emissions-directes-ges.xlsx")

# A
donnees.sort_values("date", inplace=True)
donnees_17_mars = donnees.iloc[0:24,]
print(donnees_17_mars)

# B
indice_max_eolien = donnees.idxmax()["quebec_consommation_sources_eolien"]
print(donnees.iloc[indice_max_eolien, 0])

# C
indice_min_ges = donnees.idxmin()["quebec_estimation_consommation_ges_total"]
ligne_min_ges = donnees.iloc[indice_min_ges, ]
taux_production_hydro = ligne_min_ges["quebec_consommation_sources_hydraulique"]/ligne_min_ges["quebec_consommation_sources_total"]
taux_production_hydro = taux_production_hydro * 100
print(f"{taux_production_hydro:.2f}%")

# D
consommation_par_source = {}
moyennes = donnees.mean(numeric_only=True)
print(moyennes)

sources = {"hydraulique", "eolien", "autres", "solaire", "thermique", "nucleaire", "geothermique", "biomasse"}

for source in sources:
    consommation_par_source[source] = moyennes["quebec_consommation_sources_" + source]
    
print(consommation_par_source)