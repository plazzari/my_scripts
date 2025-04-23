import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

# Filepath del file .parquet
file_path = "/g100_scratch/userexternal/vdibiagi/EMODnet_2022/NEW_int/fromSC/publication/ZenodoUpdated/MedBGCins_nut_v2.parquet"

# Leggi il file .parquet
data = pd.read_parquet(file_path)

# Sostituisci i valori mancanti (1.000000e+20) con NaN
missing_value = 1.000000e+20
data.replace(missing_value, np.nan, inplace=True)

# Filtra solo la colonna di clorofilla e le coordinate (latitudine e longitudine)
chlorophyll_col = "chlorophyll"  # Sostituisci con il nome esatto della colonna di clorofilla
latitude_col = "lat"        # Sostituisci con il nome esatto della colonna di latitudine
longitude_col = "lon"      # Sostituisci con il nome esatto della colonna di longitudine

# Assicurati che le colonne esistano
if chlorophyll_col not in data.columns or latitude_col not in data.columns or longitude_col not in data.columns:
    raise ValueError("Le colonne specificate non esistono nel file.")

# Filtra i dati validi
data = data[[latitude_col, longitude_col, chlorophyll_col]].dropna()

# Definisci il dominio del Mediterraneo (incluso il Mar di Alborán)
mediterranean_bounds = {
    "lat_min": 30.0,  # Limite inferiore della latitudine
    "lat_max": 46.0,  # Limite superiore della latitudine
    "lon_min": -10.0, # Limite inferiore della longitudine (esteso per includere il Mar di Alborán)
    "lon_max": 36.0   # Limite superiore della longitudine
}

# Filtra i dati per il dominio del Mediterraneo
data = data[
    (data[latitude_col] >= mediterranean_bounds["lat_min"]) &
    (data[latitude_col] <= mediterranean_bounds["lat_max"]) &
    (data[longitude_col] >= mediterranean_bounds["lon_min"]) &
    (data[longitude_col] <= mediterranean_bounds["lon_max"])
]

# Crea i bin di 0.5° per latitudine e longitudine
data["lat_bin"] = (data[latitude_col] // 0.5) * 0.5
data["lon_bin"] = (data[longitude_col] // 0.5) * 0.5

# Calcola la climatologia (media per ogni bin)
climatology = data.groupby(["lat_bin", "lon_bin"])[chlorophyll_col].mean().reset_index()

# Converte in un formato pivot per il plotting
climatology_pivot = climatology.pivot(index="lat_bin", columns="lon_bin", values=chlorophyll_col)

# Plot della climatologia
plt.figure(figsize=(12, 8))
plt.imshow(
    climatology_pivot,
    extent=[
        mediterranean_bounds["lon_min"],
        mediterranean_bounds["lon_max"],
        mediterranean_bounds["lat_min"],
        mediterranean_bounds["lat_max"]
    ],
    origin="lower",
    aspect="equal",  # Mantieni le proporzioni corrette
    cmap="viridis"
)

# Aggiungi una barra dei colori
plt.colorbar(label="Clorofilla (media)")

# Imposta i tick di longitudine e latitudine
plt.xticks(np.arange(mediterranean_bounds["lon_min"], mediterranean_bounds["lon_max"] + 2, 2))
plt.yticks(np.arange(mediterranean_bounds["lat_min"], mediterranean_bounds["lat_max"] + 2, 2))

# Titolo e etichette degli assi
plt.title("Climatologia della Clorofilla nel Mediterraneo (bin 0.5°)")
plt.xlabel("Longitudine")
plt.ylabel("Latitudine")

# Mostra il grafico
plt.show()