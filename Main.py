import xml.etree.ElementTree as ET
from datetime import datetime

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


#llenado de diccionarios de xml
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

def buscar_puesto(nombre, engine):
    try:
        sql_query = text("""
            DECLARE @OutResultCode INT;
            DECLARE @OutPuestoSalario MONEY;
            DECLARE @OutPuestoId INT;
            
            EXEC BuscarPuesto
                @Nombre = :name,
                @OutResultCode = @OutResultCode OUTPUT,
                @OutPuestoSalario = @OutPuestoSalario OUTPUT,
                @OutPuestoId = @OutPuestoId OUTPUT;
            
            SELECT @OutResultCode AS OutResultCode, @OutPuestoSalario AS OutPuestoSalario, @OutPuestoId AS OutPuestoId;
        """)
        with engine.begin() as connection:
            result = connection.execute(sql_query, {'name': nombre})
            output = result.fetchone()
            
            # Check if the query returned a valid result
            if output is None:
                print(f"Error: No result found for job {nombre}.")
                return None

            salario = output.OutPuestoSalario
            id = output.OutPuestoId
            
            print(f"Found Puesto '{nombre}' with Id '{id}' and Salario '{salario}'.")
            salida = {'salario': salario, 'id': id}
            return salida

    except Exception as e:
        print(f"\n\n\nError in buscar_puesto: {e}\n\n\n")
        return None


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

def insertar_usurario(engine):
    for elemento in usuarios:
        print (elemento)
        Id = elemento['Id']
        Username = elemento['Nombre']
        Password = elemento['Pass']
        
        try:
            sql_query = text("""
                DECLARE @OutResulTCode INT;
                EXEC dbo.InsertarUsuario 
                    @Username = :Username, 
                    @Id = :Id,
                    @Password = :Password, 
                    @OutResulTCode = @OutResulTCode OUTPUT;
                SELECT @OutResulTCode;
            """)
            with engine.begin() as connection:
                result = connection.execute(sql_query, {'Id': Id, 'Username': Username, 'Password': Password})
    
                    # Fetch the result code from the output parameter
                out_result_code = result.fetchone()[0]
    
                # Log the output result code
                print(f"Stored Procedure executed. Output Result Code: {out_result_code}")
                if out_result_code == 0:
                    print(f"Record for '{Username}' inserted successfully with Id '{Id}'.")
                else:
                    print(f"Error inserting record for '{Username}' with Id '{Id}'. Error Code: {out_result_code} Error Message: {error[out_result_code]}")
        except Exception as e:
            print(f"\n\n\nError: {e}\n\n\n")             

def insertar_tipo_movimiento(engine):
    for elemento in tipo_movimiento:
        print (elemento)
        Id = elemento['Id']
        Nombre = elemento['Nombre']
        TipoAccion = elemento['TipoAccion']
        
        try:
            sql_query = text("""
                DECLARE @OutResulTCode INT;
                EXEC dbo.InsertarTipoMovimiento 
                    @Id = :Id, 
                    @Nombre = :Nombre,
                    @TipoAccion = :TipoAccion,
                    @OutResulTCode = @OutResulTCode OUTPUT;
                SELECT @OutResulTCode;
            """)
            with engine.begin() as connection:
                result = connection.execute(sql_query, {'Id': Id, 'Nombre': Nombre, 'TipoAccion': TipoAccion})
    
                    # Fetch the result code from the output parameter
                out_result_code = result.fetchone()[0]
    
                # Log the output result code
                print(f"Stored Procedure executed. Output Result Code: {out_result_code}")
                if out_result_code == 0:
                    print(f"Record for '{Nombre}' inserted successfully with Id '{Id}'.")
                else:
                    print(f"Error inserting record for '{Nombre}' with Id '{Id}'. Error Code: {out_result_code} Error Message: {error[out_result_code]}")
        except Exception as e:
            print(f"\n\n\nError: {e}\n\n\n")
            
def insertar_tipo_evento(engine):
    for elemento in tipo_evento:
        print (elemento)
        Id = elemento['Id']
        Nombre = elemento['Nombre']
        
        try:
            sql_query = text("""
                DECLARE @OutResulTCode INT;
                EXEC dbo.InsertarTipoEvento 
                    @Id = :Id, 
                    @Nombre = :Nombre,
                    @OutResulTCode = @OutResulTCode OUTPUT;
                SELECT @OutResulTCode;
            """)
            with engine.begin() as connection:
                result = connection.execute(sql_query, {'Id': Id, 'Nombre': Nombre})
    
                    # Fetch the result code from the output parameter
                out_result_code = result.fetchone()[0]
    
                # Log the output result code
                print(f"Stored Procedure executed. Output Result Code: {out_result_code}")
                if out_result_code == 0:
                    print(f"Record for '{Nombre}' inserted successfully with Id '{Id}'.")
                else:
                    print(f"Error inserting record for '{Nombre}' with Id '{Id}'. Error Code: {out_result_code} Error Message: {error[out_result_code]}")
        except Exception as e:
            print(f"\n\n\nError: {e}\n\n\n")

def insertar_empleado(engine):
    for elemento in empleados:
        print(elemento)
        IdPuesto = buscar_puesto(elemento['Puesto'], engine)
        
        # Check if IdPuesto is None (indicating a failure to find the job)
        if IdPuesto is None or 'id' not in IdPuesto:
            print(f"Skipping employee '{elemento['Nombre']}' because Puesto '{elemento['Puesto']}' was not found.")
            continue  # Skip to the next employee if no IdPuesto is found
        
        ValorDocumentoIdentidad = elemento['ValorDocumentoIdentidad']
        Nombre = elemento['Nombre']
        FechaContratacion = elemento['FechaContratacion']
        
        try:
            # Convert the FechaContratacion to the correct format
            FechaContratacion_date = datetime.strptime(FechaContratacion, '%Y-%m-%d').date()
            
            sql_query = text("""
                DECLARE @OutResulTCode INT;
                EXEC dbo.InsertarEmpleado 
                    @IdPuesto = :IdPuesto, 
                    @ValorDocumentoIdentidad = :ValorDocumentoIdentidad,
                    @Nombre = :Nombre,
                    @FechaContratacion = :FechaContratacion,
                    @SaldoVacaciones = 0,
                    @EsActivo = 1,
                    @OutResulTCode = @OutResulTCode OUTPUT;
                SELECT @OutResulTCode;
            """)
            
            with engine.begin() as connection:
                print(IdPuesto['id'], ValorDocumentoIdentidad, Nombre, FechaContratacion)
                result = connection.execute(sql_query, {
                    'IdPuesto': IdPuesto['id'],
                    'ValorDocumentoIdentidad': ValorDocumentoIdentidad,
                    'Nombre': Nombre,
                    'FechaContratacion': FechaContratacion_date
                })

                # Fetch the result code from the output parameter
                out_result_code = result.fetchone()[0]
    
                # Log the output result code
                print(f"Stored Procedure executed. Output Result Code: {out_result_code}")
                if out_result_code == 0:
                    print(f"Record for '{Nombre}' inserted successfully with IdPuesto '{IdPuesto['id']}'.")
                else:
                    print(f"Error inserting record for '{Nombre}' with IdPuesto '{IdPuesto['id']}'. Error Code: {out_result_code} Error Message: {error[out_result_code]}")
        
        except Exception as e:
            print(f"\n\n\nError: {e}\n\n\n")

def buscar_empleado(engine, documento):
    try:
        sql_query = text("""
            DECLARE @OutResultCode INT;
            DECLARE @OutEmpleadoId INT;
            DECLARE @OutEmpleadoIdPuesto INT;
            DECLARE @OutEmpleadoNombre VARCHAR(256);
            DECLARE @OutEmpleadoFechaContratacion DATE;
            DECLARE @OutEmpleadoSaldoVacaciones INT;
            DECLARE @OutEmpleadoEsActivo BIT;
            
            EXEC BuscarEmpleado
                @ValorDocumentoIdentidad = :documento,
                @OutResultCode = @OutResultCode OUTPUT,
                @OutEmpleadoId = @OutEmpleadoId OUTPUT,
                @OutEmpleadoIdPuesto = @OutEmpleadoIdPuesto OUTPUT,
                @OutEmpleadoNombre = @OutEmpleadoNombre OUTPUT,
                @OutEmpleadoFechaContratacion = @OutEmpleadoFechaContratacion OUTPUT,
                @OutEmpleadoSaldoVacaciones = @OutEmpleadoSaldoVacaciones OUTPUT,
                @OutEmpleadoEsActivo = @OutEmpleadoEsActivo OUTPUT;
            
            SELECT @OutResultCode AS OutResultCode, @OutEmpleadoId AS OutEmpleadoId, @OutEmpleadoNombre AS OutEmpleadoNombre, @OutEmpleadoFechaContratacion AS OutEmpleadoFechaContratacion, @OutEmpleadoSaldoVacaciones AS OutEmpleadoSaldoVacaciones, @OutEmpleadoEsActivo AS OutEmpleadoEsActivo;
        """)
        with engine.begin() as connection:
            result = connection.execute(sql_query, {'documento': documento})
            output = result.fetchone()
            
            # Check if the query returned a valid result
            if output is None:
                print(f"Error: No result found for employee with document {documento}.")
                return None

            id = output.OutEmpleadoId
            nombre = output.OutEmpleadoNombre
            fecha_contratacion = output.OutEmpleadoFechaContratacion
            saldo_vacaciones = output.OutEmpleadoSaldoVacaciones
            es_activo = output.OutEmpleadoEsActivo
            
            print(f"Found Employee '{nombre}' with Id '{id}', FechaContratacion '{fecha_contratacion}', SaldoVacaciones '{saldo_vacaciones}', EsActivo '{es_activo}'.")
            salida = {'id': id, 'nombre': nombre, 'fecha_contratacion': fecha_contratacion, 'saldo_vacaciones': saldo_vacaciones, 'es_activo': es_activo}
            print(salida)
            return salida

    except Exception as e:
        print(f"\n\n\nError in buscar_empleado: {e}\n\n\n")
        return None



def get_error_by_code(engine, codigo):
    pass
    #HACER Y SUSTITUIR EN LINEA 144
    
buscar_empleado(conexion_sql_server(), '1011123')

