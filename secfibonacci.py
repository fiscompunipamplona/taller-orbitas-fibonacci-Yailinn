#Secuencia de Fibonacci

f_1=1
f_2=1

print("Realizando un conteo desde 1 hasta mil de la secuencia de Fibonacci")
print(f_1)
while f_2<=1000:

        print(f_2)
        f_3=f_1+f_2
        f_1=f_2
        f_2=f_3
