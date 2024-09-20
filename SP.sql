USE [Puesto]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

--  @outResultCode: codigo de resultado de ejecucion. 0 Corrio sin errores, 
--  codigos de errores entre 0 y 50000 son errores reservados, mayores a 50000 son definidos por el programador.
--
CREATE PROCEDURE [dbo].[InsertarPuesto]
    @Nombre VARCHAR(128),
    @Salario MONEY,
	@OutResulTCode INT OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	BEGIN TRY
	-- ejemplo de ejecucion del SP

	-- DECLARE @OutResulTCode int
	-- EXECUTE @RC = [dbo].[ListarEmpleado] @OutResulTCode OUTPUT
	--SELECT @OutResulTCode

	-- se hacen declaraciones

	-- se hacen inicializacion
	SET @OutResulTCode=0;

	-- se hacaen validaciones

        IF EXISTS (
            SELECT 1 FROM dbo.Puesto 
            WHERE Nombre=@Nombre)
            BEGIN
                SET @OutResulTCode=50001;
                RETURN;
            END

        INSERT INTO dbo.Puesto (Nombre, SalarioxHora)
        VALUES (@Nombre, @Salario);

        SELECT @OutResulTCode AS OutResulTCode;  -- Este codigo se agrega solo si hay problemas para obtener este  valor como parametros
        
    END TRY

	BEGIN CATCH
		INSERT INTO dbo.DBErrors	VALUES (
			SUSER_SNAME(),
			ERROR_NUMBER(),
			ERROR_STATE(),
			ERROR_SEVERITY(),
			ERROR_LINE(),
			ERROR_PROCEDURE(),
			ERROR_MESSAGE(),
			GETDATE()
		);

		SET @OutResulTCode=50005  ;  -- Codigo de error standar del profe para informar de un error capturado en el catch

	END CATCH;

	SET NOCOUNT Off;
END;