import geopandas as gpd

shapefile = gpd.read_file(r"C:\Users\giuli\Documents\prova_shp_daPLuxlsx.shp")
print(shapefile.head())
shapefile2 = shapefile.head()
nomi_colonne = list(shapefile)
geom = shapefile2.geometry
id = shapefile2.Id
x = shapefile2.x
y = shapefile2.y
depth = shapefile2.depth

for i in range(0,len(id)):
    query_ins= """ INSERT INTO "Geometry"  (
                    "id",
                    "x",
                    "y",
                    "depth",
                    "the_geom") VALUES (%s, %s, %s, %s, %s)"""
    values_ins = (str(id[i]), str(x[i]), str(y[i]), str(depth[i]), str(geom[i]))
    cursor = opened_connection.connection.cursor()
    cursor.execute(query_ins, values_ins)
    opened_connection.connection.commit()
print ('INSERT riuscite')