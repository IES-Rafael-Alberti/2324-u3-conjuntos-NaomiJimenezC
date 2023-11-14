"""
Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, 
la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:

[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente 
y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede haber hecho más de una compra en el mes, 
por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez.
"""

#Entrada
#Procesado
def sacar_direccion_factura(nombre_cliente:str,dia_del_mes:int,monto:float,domicilio_cliente:str)->str:
    """Saca la direccion del cliente dentro de una serie de datos

    Parameters
    ----------
    nombre_cliente : str
        Nombre del cliente
    dia_del_mes : int
        Mes de cuando se hizo la factura
    monto : float
        Monto a pagar
    domicilio_cliente : str
        Donde vive el cliente

    Returns
    -------
    str
        Devuelve la dirección del cliente
    """

    direccion = domicilio_cliente

    return direccion

#Salida

def mostrar_direcciones(direcciones:set)->str:
    """Crea el mensaje de las direcciones donde se enviarán facturas

    Parameters
    ----------
    direcciones : set
        El conjunto que contiene las direcciones

    Returns
    -------
    str
        Devuelve el mensaje creado
    """

    mensaje_direcciones = ""
    for direccion in direcciones:
        mensaje_direcciones += direccion +"\n"
    return mensaje_direcciones

if __name__ == "__main__":
    #Entrada
    detalles_compra = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
    #Procesado
    direcciones = set()
    for detalle_compra in detalles_compra:
        direccion = sacar_direccion_factura(detalle_compra[0],detalle_compra[1],detalle_compra[2],detalle_compra[3])
        direcciones.add(direccion)
    #Salida
    direcciones_sacadas = mostrar_direcciones(direcciones)

    print(direcciones_sacadas)