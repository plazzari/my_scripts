import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.colors as mcolors

# Filepath del file .parquet
file_path = "/g100_scratch/userexternal/vdibiagi/EMODnet_2022/NEW_int/fromSC/publication/ZenodoUpdated/MedBGCins_nut_v2.parquet"

# Leggi il file .parquet
data = pd.read_parquet(file_path)

# Sostituisci i valori mancanti (1.000000e+20) con NaN
missing_value = 1.000000e+20
data.replace(missing_value, np.nan, inplace=True)

# Filtra solo la colonna di clorofilla e le coordinate (latitudine e longitudine)
chlorophyll_col = "chlorophyll"  # Sostituisci con il nome esatto della colonna di clorofilla
latitude_col = "lat"             # Sostituisci con il nome esatto della colonna di latitudine
longitude_col = "lon"            # Sostituisci con il nome esatto della colonna di longitudine

# Assicurati che le colonne esistano
if chlorophyll_col not in data.columns or latitude_col not in data.columns or longitude_col not in data.columns:
    raise ValueError("Le colonne specificate non esistono nel file.")

# Filtra i dati validi
data = data[[latitude_col, longitude_col, chlorophyll_col]].dropna()

# Definisci il dominio della costa dell'Adriatico
adriatic_bounds = {
    "lat_min": 39.0,  # Limite inferiore della latitudine
    "lat_max": 46.5,  # Limite superiore della latitudine
    "lon_min": 12.0,  # Limite inferiore della longitudine
    "lon_max": 20.0   # Limite superiore della longitudine
}

# Filtra i dati per il dominio dell'Adriatico
adriatic_data = data[
    (data[latitude_col] >= adriatic_bounds["lat_min"]) &
    (data[latitude_col] <= adriatic_bounds["lat_max"]) &
    (data[longitude_col] >= adriatic_bounds["lon_min"]) &
    (data[longitude_col] <= adriatic_bounds["lon_max"])
]

# Plot dei punti come scatter plot
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Aggiungi la linea di costa
ax.add_feature(cfeature.COASTLINE, linewidth=0.8)
ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=0.5)
ax.set_extent([
    adriatic_bounds["lon_min"],
    adriatic_bounds["lon_max"],
    adriatic_bounds["lat_min"],
    adriatic_bounds["lat_max"]
], crs=ccrs.PlateCarree())

# Scatter plot dei punti con scala logaritmica
sc = plt.scatter(
    adriatic_data[longitude_col],
    adriatic_data[latitude_col],
    c=adriatic_data[chlorophyll_col],
    cmap="viridis",
    norm=mcolors.LogNorm(vmin=adriatic_data[chlorophyll_col].min(), vmax=adriatic_data[chlorophyll_col].max()),  # Scala logaritmica
    s=10,  # Dimensione dei punti
    transform=ccrs.PlateCarree()
)

# Aggiungi una barra dei colori
plt.colorbar(sc, label="Clorofilla (scala logaritmica)")

# Titolo e etichette degli assi
plt.title("Distribuzione della Clorofilla sulla Costa dell'Adriatico")
plt.xlabel("Longitudine")
plt.ylabel("Latitudine")

# Salva la figura in formato PNG
output_file = "/g100/home/userexternal/plazzari/my_scripts/MedBGCins/adriatic_coast_scatter.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")

# Rimuovi plt.show() per evitare di mostrare la figura
# plt.show()