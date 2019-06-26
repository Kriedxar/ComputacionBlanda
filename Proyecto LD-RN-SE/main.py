import difusa as ld
import red_neuronal as rn
import sistema_experto as se

print("\n***Sistema de calculo de velocidad***\n")
dia=int(input("Ingrese el dia [1-7]: "))
dia+= -1
mes=int(input("Ingrese el mes [1-12]: "))
mes+= -1
hora=int(input("Ingrese la hora [0-23]: "))
lluvia=float(input("Ingrese el nivel de lluvia [0-10]: "))
estadocarretera=float(input("Ingrese el estado de la carretera [0-10]: "))

riesgold=ld.aplicar(dia, mes, hora, lluvia)

riesgorn=rn.calcular(estadocarretera, riesgold)

se.sugerencia(riesgorn)