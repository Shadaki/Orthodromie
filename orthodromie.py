from math import *
def orthodromie(lat_a,lon_a,lat_b,lon_b):
    lat_a,lon_a,lat_b,lon_b=lat_a*pi/180,lon_a*pi/180,lat_b*pi/180,lon_b*pi/180
    rayon=6378137
    formule_brute=acos(sin(lat_a)*sin(lat_b)+cos(lat_a)*cos(lat_b)*cos(lon_b-lon_a))
    print(str(round(formule_brute*rayon,3))+" m")
