import math
#DATOS INICIALES
numero_de_datos=int(input("introduca el numero de datos "))
Dato_menor=float(input("asigne dato menor "))
Dato_mayor=float(input("asigne dato mayor "))
Rango=Dato_mayor-Dato_menor
intervalos=1+3.3*(math.log(numero_de_datos))
round(intervalos)
Ampl_Clase=Rango/intervalos
round(Ampl_Clase)
Datos=[]
#FORMULA PAR GENERACION DE DATOS VARIABLES AUTOMATICAS
for i in range(numero_de_datos):
    Datos.append(float(input("introdusca el valor{}: ".format(i+1))))
for j in range(numero_de_datos):
    print(Datos[j])
print("El intervalo es ",intervalos)
print("El rango es ",Rango)
print("La Amplitud de clase es ",Ampl_Clase)

print("|limite inf|limite sup|")
print("-----------------------")
print("|",Dato_menor,"|",Dato_menor+Ampl_Clase-1,"|")