USE [Tarea Programada 2]
GO
/****** Object:  StoredProcedure [dbo].[InsertarMovimiento]    Script Date: 29/09/2024 06:28:34 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[InsertarMovimiento]
	-- Add the parameters for the stored procedure here
	@IdEmpleado INT,
	@IdTipoMovimiento INT,
	@IdPostByUser INT,
	@Fecha DATE,
	@Monto INT,
	@NuevoSaldo MONEY,
	@PostInIP VARCHAR(16),
	@PostTime TIME(7),
	@OutResulTCode INT OUTPUT
AS
BEGIN

	SET NOCOUNT ON;

	SET @OutResulTCode=0;

	BEGIN TRY
	
	IF (@NuevoSaldo < 0)
		SET @OutResulTCode=50011;   --Revisar que codigo agregar
        RETURN;

    INSERT INTO dbo.Movimiento(IdEmpleado, IdTipoMovimiento,Fecha, Monto, NuevoSaldo, IdPostByUser, PostInIP, PostTime)
		VALUES(@IdEmpleado, @IdTipoMovimiento, @Fecha, @Monto, @NuevoSaldo, @IdPostByUser, @PostInIP, @PostTime)

	SELECT @OutResulTCode AS OutResulTCode;  -- Este codigo se agrega solo si hay problemas para obtener este  valor como parametro
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

END
