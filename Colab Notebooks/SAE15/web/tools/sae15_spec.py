# -*- coding: utf-8 -*-
"""sae15_spec

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DzgUMmGvach7vWpBGnyU2z2ALz33tdKg

#
"""



#code de :
#NOM : de Castro
#PRENOM : Kier
#GROUPE : TP1A

################################################################################################
# FONCTIONS SPECIFIQUES
# Les fonctions à coder selon l'échancier donné dans le document SAE15-Présentation.ipynb
#################################################################################################

#------------------------------------------------------------------------------------------------
# importations des modules utiles
#
# attention : geopandas et contextily doivent être installés avant l'importation
# utiliser pour cela !pip install ... dans le Notebook principal
#
import pandas as pd             # pour la mise en forme, l'analyse et la publication
import datetime as dt           # pour la détermination de la date
import geopandas as gpd         # pour la spatialisation des données
import matplotlib.pyplot as plt # pour les graphes
import contextily as ctx        # pour l'utilisation de cartes géographiques

#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des stands (en %)
def availableDocksRate(stations_df) :

    velos_valables = stations_df['numBikesAvailable']
    stands_dispo = stations_df['numDocksAvailable']
    rate=0
    rate = stands_dispo / (velos_valables + stands_dispo ) * 100

    return rate
#------------------------------------------------------------------------------------------------
# fonction qui retourne le taux de disponibilité des vélos (en %)
def availableBikesRate(stations_df) :

    velos_valables = stations_df['numBikesAvailable']
    stands_dispo = stations_df['numDocksAvailable']
    rate=0
    rate = velos_valables /(velos_valables + stands_dispo ) * 100

    return rate

#------------------------------------------------------------------------------------------------
# fonction qui retourne la date la plus récente de la mise à jour des données dynamiques
def getLatestDate(stations_df) :

    date = stations_df['last_reported']
    date = date.max()

    return date


#------------------------------------------------------------------------------------------------
# fonction qui retourne les mesures statistiques d'une clé du DataFrame de stations
def stationStatistics(stations_df_key):

    ligne = stations_df_key
    liste = [{
        'total': ligne.sum(),
        'min' : ligne.min(),
        'max' : ligne.max()}]
    stats = pd.DataFrame(liste)

    return stats

#------------------------------------------------------------------------------------------------
# fonction qui exporte au format HTML le DataFrame des mesures statistiques

def exportStatistics(stats_df, filename) :



    f=open("/content/drive/My Drive/Colab Notebooks/SAE15/tools/"+ filename ,"w") #cette ligne ne modifie pas un fichier mais cree un nouveau fichier contenant notre html
    f.write(stats_df.to_html())



    return

#------------------------------------------------------------------------------------------------
# fonction qui affiche et exporte la carte des stations Vélibs géolocalisées
def exportCityMap(geo_stations, marker_size, marker_color, title, date=None, filename=None) :

    # figure et axes
    f, axes = plt.subplots(1, figsize=(15,15))



    # conversion des coordonnées dans le système approprié
    geo_data_ = gpd.GeoDataFrame(geo_stations, crs="EPSG:4326", geometry=geom)

    # affichage en fonction des variables passées en argument
    geo_data_with_map.plot(geo_stations.num_docks_available, markersize=marker_size*geo_stations.num_docks_available, cmap=marker_color, ax=axes);

    # effacement des axes gradués
    axes.set_axis_off()


    # ajout du fond de carte correspondant aux coordonnées géographiques des stations
    ctx.add_basemap(axes)


    # affichage du titre avec la date de mise à jour
    plt.title("Carte stations disponible(MAJ) : " + date, loc = 'center')


    # sauvegarde de la carte sur le Drive
    plt.savefig('/content/drive/My Drive/Colab Notebooks/SAE15/web/data/' + filename +'.svg')
    # affichage forçé
    plt.show()

    return

#NOM : de Castro
#PRENOM : Kier
#GROUPE : TP1A

















"""NOM : de Castro
PRENOM : Kier
GROUPE : TP1A

"""