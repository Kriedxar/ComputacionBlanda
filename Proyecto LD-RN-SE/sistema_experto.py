from pyDatalog import pyDatalog

pyDatalog.create_terms('Velocidad, V, Riesgo, Velocidad_Sugerida')

+Velocidad(0, "90 km/h")
+Velocidad(1, "70 km/h")
+Velocidad(2, "50 km/h")
+Velocidad(3, "30 km/h")
+Velocidad(4, "15 km/h")

V(Riesgo, Velocidad_Sugerida) <= Velocidad(Riesgo, Velocidad_Sugerida)


def sugerencia(riesgorn):
	print("\n")
	print (V(riesgorn, Velocidad_Sugerida))