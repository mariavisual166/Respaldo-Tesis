CREATE DATABASE docente;

\c docente

/*Creacion de etidades*/
CREATE TABLE Docente(
	Cedula int ,
	PirmerNombre varchar(50) ,
	SegundoNombre varchar(50) ,
	PirmerApellido varchar(50) ,
	SegundoApellido varchar(50) ,
	Sexo varchar(2),
	correo varchar(50) ,
	Nacionalidad varchar(2),
	Facultad varchar(30) ,
	Tipo varchar(50) ,
	AreaDeInvestigacion varchar(50) ,
	Escalafon varchar(50) ,
	FechaActualizacion date,
		PRIMARY KEY (Cedula));

CREATE TABLE Publicacion(
	Id  serial,
	NumeroCitaciones int ,
	UrlCitacion varchar(200) ,
	TituloPublicacion varchar(200),
	UrlPublicacion varchar(200),
	FechaActualizacion date,
		PRIMARY KEY (Id));

CREATE TABLE Titulo(
	Id serial,
	Nomtitulo varchar(50) ,
	Nivel varchar(50) ,
	FechaActualizacion date,
		PRIMARY KEY (Id)	);

CREATE TABLE OtroEstudio(
	Id serial,
	Nomtitulo varchar(50) ,
	FechaActualizacion date,
		PRIMARY KEY (Id));

CREATE TABLE Proyecto(
	Id  serial,
	titulo  varchar(50) ,
	FechaActualizacion date,
		PRIMARY KEY (Id));

CREATE TABLE Premio(
	Id  serial,
	Nombre varchar(50) ,
	FechaActualizacion date,
		PRIMARY KEY (Id));	

CREATE TABLE DocenteTienePremio(
	CedulaPersona int,
	IdPremio int,
	PRIMARY KEY (CedulaPersona,IdPremio));			

CREATE TABLE DocenteTieneTitulo(
	CedulaPersona int,
	IdTitulo int,
	PRIMARY KEY (CedulaPersona,IdTitulo));

CREATE TABLE DocenteRealizaOtroEstudio(
	CedulaPersona int,
	IdOtroEstudio int,
	PRIMARY KEY (CedulaPersona,IdOtroEstudio));

CREATE TABLE DocenteTienePublicacion(
	CedulaPersona int,
	IdPublicacion int);

CREATE TABLE DocenteParticipaProyecto(
	CedulaPersona int,
	IdProyecto int,
		PRIMARY KEY (CedulaPersona,IdProyecto));
