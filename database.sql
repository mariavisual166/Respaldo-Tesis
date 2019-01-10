CREATE DATABASE docente;

\c docente

/*Creacion de etidades*/
CREATE TABLE Docente(
	Cedula int ,
	primernombre varchar(50) ,
	SegundoNombre varchar(50) ,
	primerapellido varchar(50) ,
	SegundoApellido varchar(50) ,
	Sexo varchar(2),
	correo varchar(50) ,
	Nacionalidad varchar(2),
	Facultad varchar(30) ,
	Tipo varchar(50) ,
	AreaDeInvestigacion varchar(50) ,
	Escalafon varchar(50) ,
	FechaActualizacion timestamp,
		PRIMARY KEY (Cedula));

CREATE TABLE Publicacion(
	Id  serial,
	NumeroCitaciones int ,
	UrlCitacion varchar(200) ,
	TituloPublicacion varchar(200),
	UrlPublicacion varchar(200),
	FechaActualizacion timestamp,
		PRIMARY KEY (Id));

CREATE TABLE Titulo(
	Id serial,
	Nomtitulo varchar(50) ,
	Nivel varchar(50) ,
	FechaActualizacion timestamp,
		PRIMARY KEY (Id)	);

CREATE TABLE OtroEstudio(
	Id serial,
	Nomtitulo varchar(50) ,
	FechaActualizacion timestamp,
		PRIMARY KEY (Id));

CREATE TABLE Proyecto(
	Id  serial,
	titulo  varchar(50) ,
	FechaActualizacion timestamp,
		PRIMARY KEY (Id));

CREATE TABLE Premio(
	Id  serial,
	Nombre varchar(50) ,
	FechaActualizacion timestamp,
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

CREATE TABLE FechaTope(
	Facultad varchar(50) ,
	Fecha timestamp,
		PRIMARY KEY (Facultad));
CREATE TABLE FechaAPi(
	Fecha timestamp
		);
CREATE TABLE CorreoEnviado(
	Facultad varchar(50) ,
	Logico varchar(50),
		PRIMARY KEY (Facultad));
INSERT INTO FechaAPi(Fecha) VALUES ('2019-01-01 00:00:00');
INSERT INTO FechaTope(Facultad,Fecha) VALUES ('Facyt','2210-10-01 00:00:00');
INSERT INTO FechaTope(Facultad,Fecha) VALUES ('Faces','2210-10-01 00:00:00');
INSERT INTO FechaTope(Facultad,Fecha) VALUES ('Face','2210-10-01 00:00:00');
INSERT INTO FechaTope(Facultad,Fecha) VALUES ('Odontologia','2210-10-01 00:00:00');
INSERT INTO FechaTope(Facultad,Fecha) VALUES ('Fcjp','2210-10-01 00:00:00');
INSERT INTO FechaTope(Facultad,Fecha) VALUES ('Ingieneria','2210-10-01 00:00:00');
INSERT INTO FechaTope(Facultad,Fecha) VALUES ('Fcs','2210-10-01 00:00:00');

INSERT INTO CorreoEnviado(Facultad) VALUES ('Facyt');
INSERT INTO CorreoEnviado(Facultad) VALUES ('Faces');
INSERT INTO CorreoEnviado(Facultad) VALUES ('Face');
INSERT INTO CorreoEnviado(Facultad) VALUES ('Odontologia');
INSERT INTO CorreoEnviado(Facultad) VALUES ('Fcjp');
INSERT INTO CorreoEnviado(Facultad) VALUES ('Ingieneria');
INSERT INTO CorreoEnviado(Facultad) VALUES ('Fcs');