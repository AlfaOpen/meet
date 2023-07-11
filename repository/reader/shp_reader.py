import geopandas as gpd
import re



class SHPReader:

    def __init__(self):
        self.geom = None

    def shp_reader(self, path):
        shapefile = gpd.read_file(path)
        print(shapefile.head())
        nomi_colonne = list(shapefile)
        info_geom = []
        print(nomi_colonne)
        domanda = input("Se si desidera caricare solo una parte dei dati relativi alla geometria digitare 'si', altrimenti premere invio\n")
        matchshp1 = re.search("^\s*s\s*i\s*$", domanda, re.IGNORECASE)
        if matchshp1:
            domanda2= input("Digitare '1' se i dati sono relativi all'unità geologica; \nDigitare '2' se sono relativi alle faglie\n")
            match2 = re.search("^\s*1\s*$", domanda2)
            match3 = re.search("^\s*2\s*$", domanda2)
            if match2:
                for i in range(0, len(shapefile.Name)):
                    nomi_geo = shapefile.Name
                    if nomi_geo[i] == "TE_u_west":
                        info_geom.append(shapefile.geometry[i])
                self.geom = info_geom
            if match3:
                for i in range(0, 1065):
                    info_geom.append(shapefile.geometry[i])
                self.geom = info_geom
        else:
            self.geom = shapefile.geometry
        print("lunghezza file: " + str(len(self.geom)))
        return self.geom

# for i in range(0,len(id)):
#     query_ins= """ INSERT INTO "Geometry"  (
#                     "id",
#                     "x",
#                     "y",
#                     "depth",
#                     "the_geom") VALUES (%s, %s, %s, %s, %s)"""
#     values_ins = (str(id[i]), str(x[i]), str(y[i]), str(depth[i]), str(geom[i]))
#     cursor = opened_connection.connection.cursor()
#     cursor.execute(query_ins, values_ins)
#     opened_connection.connection.commit()
# print ('INSERT riuscite')
