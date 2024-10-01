USE [Tarea Programada 2]
GO
/****** Object:  StoredProcedure [dbo].[FetchEmpleados]    Script Date: 01/10/2024 03:50:27 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO




ALTER PROCEDURE [dbo].[FetchEmpleados]
    @OutResultCode INT OUTPUT
	,@input NVARCHAR(100)

AS

BEGIN
	SET NOCOUNT ON;

	BEGIN TRY
	BEGIN
		SELECT [Nombre]
				  ,[ValorDocumentoIdentidad]
				  ,[IdPuesto]
			FROM dbo.Empleado
			WHERE (@input = '' OR [Nombre] LIKE '%' + @input + '%')
			   OR (@input = '' OR [ValorDocumentoIdentidad] LIKE '%' + @input + '%');
	END;
	END TRY

	BEGIN CATCH
		INSERT INTO dbo.DBErrors    VALUES (
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
