
import ctypes

lib = ctypes.CDLL("libfunction.so")

lib.triplo.argtypes = [ctypes.c_double]
lib.triplo.restype = ctypes.c_double

valor = lib.triplo(1)

print(valor) #Teste