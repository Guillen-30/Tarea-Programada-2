import xml.etree.ElementTree as ET

tree = ET.parse('Datos.xml')
root = tree.getroot()

################### CONNEXION SQL ##################



################## CONEXION SQL ####################git 
puestos = [] #
tipo_evento = [] #
tipo_movimiento = [] #
empleados = [] #
movimientos = [] #
usuarios = []
error = [] #



for child in root:
    if child.tag == 'Movimientos':
        # Recorrer cada nodo 'movimiento' en el nodo 'Movimientos'
        for movimiento in child:
            # Obtener los atributos como diccionario
            atributos = movimiento.attrib
            # Guardar los atributos en la lista
            movimientos.append(atributos)
    elif child.tag == "Puestos":
        # Recorrer cada nodo 'movimiento' en el nodo 'Movimientos'
        for puesto in child:
            # Obtener los atributos como diccionario
            atributos = puesto.attrib
            # Guardar los atributos en la lista
            puestos.append(atributos)
    elif child.tag == "Empleados":
        # Recorrer cada nodo 'movimiento' en el nodo 'Movimientos'
        for empleado in child:
            # Obtener los atributos como diccionario
            atributos = empleado.attrib
            # Guardar los atributos en la lista
            empleados.append(atributos)        
    elif child.tag == "Error":
            # Recorrer cada nodo 'movimiento' en el nodo 'Movimientos'
            for errores in child:
                # Obtener los atributos como diccionario
                atributos = error.attrib
                # Guardar los atributos en la lista
                error.append(atributos)        
    elif child.tag == "Usuarios":
        # Recorrer cada nodo 'movimiento' en el nodo 'Movimientos'
        for usuario in child:
            # Obtener los atributos como diccionario
            atributos = usuario.attrib
            # Guardar los atributos en la lista
            usuarios.append(atributos)        
    elif child.tag == "TiposMovimientos":
        # Recorrer cada nodo 'movimiento' en el nodo 'Movimientos'
        for tmovimiento in child:
            # Obtener los atributos como diccionario
            atributos = tmovimiento.attrib
            # Guardar los atributos en la lista
            tipo_movimiento.append(atributos)
    elif child.tag == "TiposEvento":
        # Recorrer cada nodo 'movimiento' en el nodo 'Movimientos'
        for tevento in child:
            # Obtener los atributos como diccionario
            atributos = tevento.attrib
            # Guardar los atributos en la lista
            tipo_evento.append(atributos)