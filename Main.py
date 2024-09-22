import xml.etree.ElementTree as ET

tree = ET.parse('Datos.xml')
root = tree.getroot()

puestos = [] #
tipo_evento = [] #
tipo_movimiento = [] #
empleados = [] #
movimientos = [] #
usuarios = []
error = [] #

################### CONNEXION SQL ##################
import pandas as pd
from sqlalchemy import create_engine, text
from flask import Flask, jsonify, request
from flask_cors import CORS

def conexion_sql_server():
    connection_string = 'mssql+pyodbc://sa:BasesTec@25.8.143.41/Tarea Programada 2?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes'
    engine = create_engine(connection_string)
    return engine
################## CONEXION SQL ####################git 


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
                atributos = errores.attrib
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
            


from sqlalchemy import create_engine, text

def insertar_puesto(engine):

    for elemento in puestos:
        name = elemento['Nombre']
        salary = elemento['SalarioxHora']

        try:
            # Define the query to call the stored procedure with output parameter using bind parameters
            sql_query = text("""
                DECLARE @OutResulTCode INT;
                EXEC InsertarPuesto 
                    @Nombre = :name, 
                    @Salario = :salary, 
                    @OutResulTCode = @OutResulTCode OUTPUT;
                SELECT @OutResulTCode;
            """)

            # Begin a transaction explicitly
            with engine.begin() as connection:
                result = connection.execute(sql_query, {'name': name, 'salary': salary})

                # Fetch the result code from the output parameter
                out_result_code = result.fetchone()[0]

                # Log the output result code
                print(f"Stored Procedure executed. Output Result Code: {out_result_code}")
                if out_result_code == 0:
                    print(f"Record for '{name}' inserted successfully with salary '{salary}'.")
                else:
                    print(f"Error inserting record for '{name}' with salary '{salary}'. Error Code: {out_result_code} Error Message: {error[out_result_code]}")

        except Exception as e:
            print(f"\n\n\nError: {e}\n\n\n")
def buscar_puesto(nombre,engine):
    try:
        sql_query = text("""
                    DECLARE @OutResulTCode INT;
                    DECLARE @OutPuestoSalario MONEY;
                    EXEC BuscarPuesto 
                        @Nombre = :name,
                        @OutPuestoSalario = @OutPuestoSalario OUTPUT,
                        @OutResulTCode = @OutResulTCode OUTPUT;
                    SELECT @OutResulTCode;
                    SELECT @OutPuestoSalario;
                """)
        with engine.begin() as connection:
                result = connection.execute(sql_query, {'name': nombre})
                print(result.fetchall())
                # Fetch the result code from the output parameter
                out_result_code = result.fetchone()[0]
                for i in result:
                    print(i)
                #REVISAR DESPUES


    except Exception as e:
            print(f"\n\n\nError: {e}\n\n\n")

def insertar_error(engine):
        for elemento in error:
            codigo = elemento['Codigo']
            descripcion = elemento['Descripcion']
    
            try:
                # Define the query to call the stored procedure with output parameter using bind parameters
                sql_query = text("""
                    DECLARE @OutResulTCode INT;
                    EXEC InsertarError 
                        @Codigo = :codigo, 
                        @Descripcion = :descripcion,
                        @OutResulTCode = @OutResulTCode OUTPUT;
                    SELECT @OutResulTCode;
                """)
    
                # Begin a transaction explicitly
                with engine.begin() as connection:
                    result = connection.execute(sql_query, {'codigo': codigo, 'descripcion': descripcion})
    
                    # Fetch the result code from the output parameter
                    out_result_code = result.fetchone()[0]
    
                    # Log the output result code
                    print(f"Stored Procedure executed. Output Result Code: {out_result_code}")
                    if out_result_code == 0:
                        print(f"Record for '{codigo}' inserted successfully with descripcion '{descripcion}'.")
                    else:
                        print(f"Error inserting record for '{codigo}' with descripcion '{descripcion}'. Error Code: {out_result_code} Error Message: {error[out_result_code]}")
    
            except Exception as e:
                print(f"\n\n\nError: {e}\n\n\n")

buscar_puesto("Camarero",conexion_sql_server())

def get_error_by_code(engine, codigo):
    pass
    #HACER Y SUSTITUIR EN LINEA 144