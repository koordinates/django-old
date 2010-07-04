from ctypes import c_uint, byref
from django.contrib.gis.geos.geometry import GEOSGeometry
from django.contrib.gis.geos.libgeos import get_pointer_arr
from django.contrib.gis.geos.prototypes import geom

def polygonize(*args, **kwargs):
    if not args:
        raise TypeError('Must provide at least one geometry to polygonize.')
    
    for a in args:
        if not isinstance(a, GEOSGeometry):
            raise ValueError, "Arguments to polygonize must be geometries."
    
    n_geoms = len(args)
    geoms = get_pointer_arr(n_geoms)
    for i in xrange(n_geoms): geoms[i] = args[i].ptr
    
    return GEOSGeometry(geom.polygonize(byref(geoms), c_uint(n_geoms)), **kwargs)
