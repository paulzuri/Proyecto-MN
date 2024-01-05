from sympy import *

x, y, z, t = symbols('x y z t')

print("Solucionador de raíces para la ecuación de la montaña rusa")

error = 1.0
toler = 0.05
i = 0

# Introducir aquí 0.3*x**3 - 5*x**2 + 21*x
print("Introduzca una funcion f(x) y un punto inicial x0:")
funcion = sympify(input("f(x): "))
x0 = sympify(input("x0: "))
toler_b=input("¿Desea ajustar la tolerancia? (Tolerancia defecto = 0.05) y/n: ")

if toler_b == "y":
    toler = float(input("Introduzca un nuevo valor de e: "))
        
# cambiar la letra a diferenciar
funcion_d = diff(funcion, x)

print("Inicio de las iteraciones...")
print(f"Para {funcion} en {x0:.3f} con e = {toler}:")

print("i || x0 || x1 || funcion(x0)/funcion_d(x0) || error")
while error > toler:
    i+=1

    x1 = x0 - funcion.subs(x, x0)/funcion_d.subs(x, x0)
    error = abs((x1-x0)/x1)
    x0 = x1

    print(f"{i} || {x0:.3f} || {x1:.3f} || {(funcion.subs(x,x0)/funcion_d.subs(x,x0)):.3f} || {error:.3f}")
            
    if(i > 30):
        print("No se encontró ninguna raíz")
        break

print(f"Se encontró una raíz en el punto: {x0:.3f}")
print(f"{funcion} en {x0} = {funcion.subs(x, x0)}")

print("Gráfico: ")
plot(funcion, (x, -10, 10))