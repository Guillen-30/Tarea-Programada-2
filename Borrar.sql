USE [Tarea Programada 2]
GO
/****** Object:  StoredProcedure [dbo].[InsertarMovimiento]    Script Date: 05/10/2024 01:58:34 a. m. ******/
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
	@PostTime DATETIME,
	@OutResulTCode INT OUTPUT
AS
BEGIN

	SET NOCOUNT ON;

	SET @OutResulTCode=0;

	BEGIN TRY
	
	IF (@NuevoSaldo < 0)
        BEGIN
            SET @OutResulTCode = 50011;   -- Error code for negative balance
        END
        ELSE
        BEGIN
            -- Insert the new movement
            INSERT INTO dbo.Movimiento(
                IdEmpleado, IdTipoMovimiento, Fecha, Monto, NuevoSaldo, 
                IdPostByUser, PostInIP, PostTime
            )
            VALUES (
                @IdEmpleado, @IdTipoMovimiento, @Fecha, @Monto, @NuevoSaldo, 
                @IdPostByUser, @PostInIP, @PostTime
            );
        END
		BEGIN 
		UPDATE dbo.Empleado
			SET SaldoVacaciones=@NuevoSaldo
			SELECT 1 FROM dbo.Empleado
				WHERE (@IdEmpleado=Id)
		END
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


