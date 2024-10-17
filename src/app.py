import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
#Esto funciona para poder usar los valores del archivo .env
load_dotenv()

#Agregar las Keys a variables dentro del codigo
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#Conectar con la API de spotify usando SpotifyClientCredentials
con = spotipy.Spotify(auth_manager= SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
print('🟢 Conexion exitosa con Spotify API')

#Almacenar spotipy.Spotiify() en una varible, para resumir codigo

#ID del artista - Ricardo Arjona
artist_id = "0h1zs4CTlU9D2QtgPxptUD"

#Obtener informacion del Artista
artist_info = con.artist_top_tracks(artist_id)

#Agregar esa informacion a un Data Frame
df = pd.DataFrame.from_records(artist_info['tracks'])
df.sort_values(['popularity'])
print(df[['name','popularity','duration_ms']].head(3))

#Hacer Scatter Plot con seaborn
scatter_plot = sns.scatterplot(data = df, x='popularity', y='duration_ms')
fig = scatter_plot.get_figure()
scatter_plot.figure.savefig("scatter_plot.png")
scatter_plot.figure.show()

print('Como podemor ver no hay relacion directa entre lo largo de la cancion y su popularidad')

del con