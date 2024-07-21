# 1.	La gasolinera Muralla, le acaban de llegar 6 bombas despachadoras de gasolina normal, el problema es que al despachar cierta cantidad de gasolina lo registra en galones, pero el precio de la gasolina está fijado en litros. Desarrollar un algoritmo y diagrama de flujo que calcule e imprima lo que hay que cobrarle al cliente, se introducirá la cantidad de galones y el precio por litro.

galones = float(input("Ingrese la cantidad de galones despachados: "))
precio_litro = float(input("Ingrese el precio por litro: "))

litros = galones * 3.785

precio_pagar = litros * precio_litro

print("El precio a pagar es de:", precio_pagar, "pesos")



# 2.	El maestro de la clase de matemáticas de la secundaria federal número 29, quiere Desarrollar un algoritmo que le permita calcular las raíces de la ecuación: Y = 3X2 + 7X – 15, con el motivo de tener una respuesta más precisa y rápida.
from math import sqrt
a = 3
b = 7
c = -15

discriminante = b**2 - 4 * a * c

raiz1 = (-b + sqrt(discriminante)) / (2 * a)
raiz2 = (-b - sqrt(discriminante)) / (2 * a)

print("La primera raíz es:", raiz1)
print("La segunda raíz es:", raiz2)

# 3.	El Zoológico la Pastora desea tener un informe estadístico de sus rinocerontes con respecto a su longevidad, tal que da como datos el nombre de un rinoceronte, su edad, su peso, y su longitud, expresados estos dos últimos en libras y pies respectivamente. Desarrollar un algoritmo que imprima el nombre del rinoceronte, su edad, su peso expresado en kilogramos y su longitud expresada en metros.

nombre = input("Ingrese el nombre del rinoceronte: ")
edad = float(input("Ingrese la edad del rinoceronte: "))
peso_libras = float(input("Ingrese el peso del rinoceronte en libras: "))
longitud_pies = float(input("Ingrese la longitud del rinoceronte en pies: "))

peso_kg = peso_libras * 0.453592

longitud_metros = longitud_pies * 0.3048

print("Informe estadístico del rinoceronte:", nombre)
print("Edad:", edad, "años")
print("Peso:", peso_kg, "kg")
print("Longitud:", longitud_metros, "m")

# 4.	El jefe del personal de operación de la industria aceitera Móvil desea calcular el sueldo neto de sus empleados bajo las siguientes normas, solicitar el nombre del empleado, número de horas trabajadas y la cuota por hora trabajada, para calcular el sueldo neto del empleado, se le otorga un incentivo del 5% si el empleado trabajó más de 40 horas. Imprimir el nombre del empleado y su sueldo. Desarrollar el algoritmo

nombre_empleado = input("Ingrese el nombre del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
cuota_hora = float(input("Ingrese la cuota por hora trabajada: "))

sueldo_bruto = horas_trabajadas * cuota_hora

if horas_trabajadas > 40:
    incentivo = sueldo_bruto * 0.05
else:
    incentivo = 0

sueldo_neto = sueldo_bruto + incentivo

print("Nombre del empleado:", nombre_empleado)
print("Sueldo neto:", sueldo_neto)

# 5.	La compañía de seguros de vida atlas se va a cambiar de domicilio y por lo tanto pone en venta su terreno, pero no tiene una idea del valor del terreno, entonces solicita al departamento de sistemas que le desarrolle un algoritmo con la finalidad de que calcule e imprima el precio del terreno del cual se tiene los siguientes datos: largo, ancho y precio por metro cuadrado, si el terreno tiene más de 400 metros cuadrados se hace un descuento del 10%. 

largo = float(input("Ingrese el largo del terreno (en metros): "))
ancho = float(input("Ingrese el ancho del terreno (en metros): "))
precio_metro_cuadrado = float(input("Ingrese el precio por metro cuadrado: "))

area = largo * ancho

precio_total_sin_descuento = area * precio_metro_cuadrado

if area > 400:
    descuento = precio_total_sin_descuento * 0.1
    precio_total = precio_total_sin_descuento - descuento
else:
    precio_total = precio_total_sin_descuento

print("Precio final del terreno:", precio_total)


# 6.	El jefe del almacén de ropa almacenes del mayo pone una promoción en sus trajes por un período de tres días para sus clientes, de tal manera que si un cliente ordena un traje se captura el modelo del traje y el precio unitario. Si el cliente ordena tres o más trajes se le hace un descuento del 17%, si no se le cobra al precio normal. Desarrollar el algoritmo.

modelo_traje = input("Ingrese el modelo del traje: ")
precio_unitario = float(input("Ingrese el precio unitario del traje: "))
cantidad_trajes = int(input("Ingrese la cantidad de trajes: "))

precio_total_sin_descuento = cantidad_trajes * precio_unitario

if cantidad_trajes >= 3:
    descuento = precio_total_sin_descuento * 0.17
    precio_total = precio_total_sin_descuento - descuento
else:
    precio_total = precio_total_sin_descuento

print("Modelo del traje:", modelo_traje)
print("Cantidad de trajes:", cantidad_trajes)
print("Precio total:", precio_total)

# 7.	Un cliente ordena cierta cantidad de brochas de cerda, rodillos y sellador; las brochas de cerda tienen un 20% de descuento y los rodillos un 15% de descuento. Los datos que se tienen por cada tipo de artículo son: la cantidad pedida y el precio unitario. Además, si se paga de contado todo tiene un descuento del 7%. Desarrollar un algoritmo que calcule y muestre el costo total de la orden, tanto para el pago de contado como para el caso de pago de crédito.  

# Se definen las variables
cantidad_brochas = int(input("Ingrese la cantidad de brochas de cerda: "))
precio_brocha = float(input("Ingrese el precio unitario de la brocha de cerda: "))

cantidad_rodillos = int(input("Ingrese la cantidad de rodillos: "))
precio_rodillo = float(input("Ingrese el precio unitario del rodillo: "))

cantidad_sellador = int(input("Ingrese la cantidad de sellador: "))
precio_sellador = float(input("Ingrese el precio unitario del sellador: "))

precio_total_brochas = cantidad_brochas * precio_brocha

descuento_brochas = precio_total_brochas * 0.2

precio_final_brochas = precio_total_brochas - descuento_brochas

precio_total_rodillos = cantidad_rodillos * precio_rodillo

descuento_rodillos = precio_total_rodillos * 0.15

precio_final_rodillos = precio_total_rodillos - descuento_rodillos

precio_total_sellador = cantidad_sellador * precio_sellador

subtotal = precio_final_brochas + precio_final_rodillos + precio_total_sellador

descuento_contado = 0
if input("¿El pago es de contado? (si/no): ") == "si":
    descuento_contado = subtotal * 0.07

total_contado = subtotal - descuento_contado

total_credito = subtotal

print("--------------------------------------------")
print("Detalle de la orden:")
print("Brochas de cerda:", cantidad_brochas, "unidades", "Precio unitario:", precio_brocha, "Costo total:", precio_final_brochas)
print("Rodillos:", cantidad_rodillos, "unidades", "Precio unitario:", precio_rodillo, "Costo total:", precio_final_rodillos)
print("Sellador:", cantidad_sellador, "unidades", "Precio unitario:", precio_sellador, "Costo total:", precio_total_sellador)
print("Subtotal:", subtotal)
print("--------------------------------------------")
print("Total para pago de contado:", total_contado)
print("Total para pago de crédito:", total_credito)
print("--------------------------------------------")

# 8.	En la tienda de mayoreo San Juanita el impuesto que se debe pagar por los artículos adquiridos se calcula de la siguiente manera: los primeros $30 no causan impuesto, los siguientes $30 tienen un 30% de impuesto y el resto el 40% de impuesto, pero si el costo del producto es mayor a $400, entonces se cobra el 50%. Desarrollar un algoritmo que lea el costo básico de un artículo y calcule el costo total. Muestre el artículo y su costo total.

def calcular_impuesto(costo):
    if costo <= 30:
        return 0
    elif costo <= 60:
        return costo * 0.3
    elif costo <= 400:
        return costo * 0.4
    else:
        return costo * 0.5

costo = float(input("Ingrese el costo del artículo: "))
impuesto = calcular_impuesto(costo)
costo_total = costo + impuesto

print("Costo total del artículo:", costo_total)
