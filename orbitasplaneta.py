#Orbitas planetarias. A partir de la segunda ley de Kepler escriba un programa
#que calcule la posiciòn y velocidad en el afelio dada la posiciòn y velocidad
#en al perihelio

G=6.67e-11
M_e=1.989e30

R_p=float(input("Ingrese un valor para el radio del perihelio Rp: "))
V_p=float(input("Ingrese la velocidad para perihelio Vp: "))

from math import pi
V_a=(((2*G*M_e)/(V_p*R_p))+((((2*G*M_e)/(V_p*R_p))**(2))+4*((V_p**2-2*G*M_e)/R_p))**1/2)/2
print("La velocidad del afelio es Va: " ,V_a)
R_a=(R_p*V_p)/V_a
print("El radio del afelio es Ra: " ,R_a)
a=(R_p+R_a)/2
print("La distancia al semieje mayor es a: " ,a)
b=(R_p*R_a)**(1/2)
print("La distancia al semieje menor es b: " ,b)
T=(2*pi*a*b)/(R_p*V_p)
print("El periodo orbital es T: ", T)
e=(R_a-R_p)/(R_a+R_p)
print("La excentricidad Orbital es e: " ,e)
