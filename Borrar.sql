USE [Tarea Programada 2]
GO
/****** Object:  StoredProcedure [dbo].[InsertarEmpleado]    Script Date: 28/09/2024 05:17:26 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO



--  @outResultCode: codigo de resultado de ejecucion. 0 Corrio sin errores, 
--  codigos de errores entre 0 y 50000 son errores reservados, mayores a 50000 son definidos por el programador.
--
ALTER PROCEDURE [dbo].[InsertarEmpleado]
    @IdPuesto INT
    ,@ValorDocumentoIdentidad VARCHAR
	,@Nombre VARCHAR
	,@FechaContratacion DATE
	,@SaldoVacaciones INT
	,@EsActivo BIT
	,@OutResulTCode INT OUTPUT
AS
BEGIN
	SET NOCOUNT ON;

	-- ejemplo de ejecucion del SP

	-- DECLARE @OutResulTCode int
	-- EXECUTE @RC = [dbo].[ListarEmpleado] @OutResulTCode OUTPUT
	--SELECT @OutResulTCode

	-- se hacen declaraciones

	-- se hacen inicializacion
	SET @OutResulTCode=0;
	SET @EsActivo=1
	SET @SaldoVacaciones=0

	-- se hacaen validaciones
	-- Data sets se especifican al final y todos juntos


        IF EXISTS (
            SELECT 1 FROM dbo.Empleado 
            WHERE ValorDocumentoIdentidad=@ValorDocumentoIdentidad)
            BEGIN
                SET @OutResulTCode=50001;   --Revisar que codigo agregar
                RETURN;
            END

        INSERT INTO dbo.Empleado(IdPuesto, ValorDocumentoIdentidad,Nombre,FechaContratacion,SaldoVacaciones, EsActivo)
			VALUES(@IdPuesto, @ValorDocumentoIdentidad, @Nombre, @FechaContratacion,@SaldoVacaciones, @EsActivo)

		SELECT @OutResulTCode AS OutResulTCode;  -- Este codigo se agrega solo si hay problemas para obtener este  valor como parametros
        


	SET NOCOUNT Off;
END;
