-- Table: Puesto
CREATE TABLE Puesto (
    [Id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
    [Nombre] VARCHAR(128) NOT NULL,
    [SalarioxHora] MONEY NOT NULL
);

-- Table: Empleado
CREATE TABLE Empleado (
    [Id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
    [IdPuesto] [int],
    [ValorDocumentoIdentidad] VARCHAR(64) NOT NULL,
    [Nombre] VARCHAR(255) NOT NULL,
    [FechaContratacion] DATE NOT NULL,
    [SaldoVacaciones] INT NOT NULL,
    [EsActivo] BIT NOT NULL,
    FOREIGN KEY (IdPuesto) REFERENCES Puesto(Id)
);

-- Table: TipoMovimiento
CREATE TABLE TipoMovimiento (
    [Id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
    [Nombre] VARCHAR(255) NOT NULL,
    [TipoAccion] VARCHAR(255) NOT NULL
);

-- Table: Movimiento
CREATE TABLE Movimiento (
    [Id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
    [IdEmpleado] [int],
    [IdTipoMovimiento] [int],
    [Fecha] DATE NOT NULL,
    [Monto] MONEY NOT NULL,
    [NuevoSaldo] MONEY NOT NULL,
    [IdPostByUser] [int],
    [PostInIP] VARCHAR(16),
    [PostTime] TIMESTAMP NOT NULL,
    FOREIGN KEY (IdEmpleado) REFERENCES Empleado(Id),
    FOREIGN KEY (IdTipoMovimiento) REFERENCES TipoMovimiento(Id),
	FOREIGN KEY (IdPostByUser) REFERENCES Usuario(Id)
);

-- Table: Usuario
CREATE TABLE Usuario (
    [Id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
    [Username] VARCHAR(255) NOT NULL,
    [Password] VARCHAR(255) NOT NULL
);

-- Table: TipoEvento
CREATE TABLE TipoEvento (
    [Id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
    [Nombre] VARCHAR(255) NOT NULL
);

-- Table: BitacoraEvento
CREATE TABLE BitacoraEvento (
    [Id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
    [IdTipoEvento] [int],
    [Descripcion] TEXT NOT NULL,
    [IdPostByUser] [int],
    [PostInIP] VARCHAR(255),
    [PostTime] TIMESTAMP NOT NULL,
    FOREIGN KEY (IdTipoEvento) REFERENCES TipoEvento(Id),
    FOREIGN KEY (IdPostByUser) REFERENCES Usuario(Id)
);

CREATE TABLE [dbo].[DBErrors](
	[ErrorID] [int] IDENTITY(1,1) NOT NULL,
	[UserName] [varchar](100) NULL,
	[ErrorNumber] [int] NULL,
	[ErrorState] [int] NULL,
	[ErrorSeverity] [int] NULL,
	[ErrorLine] [int] NULL,
	[ErrorProcedure] [varchar](max) NULL,
	[ErrorMessage] [varchar](max) NULL,
	[ErrorDateTime] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
