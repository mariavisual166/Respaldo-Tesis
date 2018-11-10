import simplejson as json
import csv, operator
import sys
import types
import psycopg2
from microservices.scholar import main
import time
import datetime
def Actualizar():
	PSQL_HOST = "localhost"
	PSQL_PORT = "5432"
	PSQL_USER = "postgres"
	
	PSQL_PASS = "123456"
	PSQL_DB   = "docente"
	connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
	conn = psycopg2.connect(connstr)
	cur = conn.cursor()

	if((int(time.strftime("%d"))==11 or int(time.strftime("%d"))==10 or int(time.strftime("%d"))==20) and int(time.strftime("%M"))==11 and int(time.strftime("%S"))==1 and int(time.strftime("%H"))==12 ):
		
		ListaDeNombresDelSistema=[]
		ListaDeprimerapellidoDelSistema=[]
		ListaDePublicaciones=[]
		ListaAux=[]
		sqlquery7 = "SELECT p.TituloPublicacion,d.primernombre,d.primerapellido FROM Docente d ,Publicacion p ,DocenteTienePublicacion t where t.IdPublicacion=P.id and t.CedulaPersona=d.Cedula ;"
		cur.execute(sqlquery7)
		rows=cur.fetchall()
		if(len(rows) > 0):
			for row in rows:
				ListaDePublicaciones.append(row[0]);
				ListaDeNombresDelSistema.append(row[1]);
				ListaDeprimerapellidoDelSistema.append(row[2]);
		j=0
	
		while j < len(ListaDePublicaciones) :
			
			autor=ListaDeNombresDelSistema[j]+" "+ListaDeprimerapellidoDelSistema[j]
			V=main(autor,ListaDePublicaciones[j])
			if(len(V)):
				sqlquery10 = "UPDATE Publicacion SET NumeroCitaciones='{}',UrlCitacion='{}',UrlPublicacion='{}',FechaActualizacion='{}' WHERE TituloPublicacion='{}';".format(int(V[0]),V[1],V[3],time.strftime('%Y-%m-%d %H:%M:%S'),ListaDePublicaciones[j])
				cur.execute(sqlquery10)
			#sqlquery8 = "INSERT INTO Publicacion(CedulaAutor,NumeroCitaciones,UrlCitacion,TituloPublicacion,UrlPublicacion,FechaActualizacion ) VALUES ('{}','{}','{}','{}','{}','{}' );".format(ListaDePublicaciones[j],int(V[i]),V[i+1],V[i+2],V[i+3],time.strftime('%Y-%m-%d %H:%M:%S'))
			#cur.execute(sqlquery8)
			
			j=j+1
		print("Se realizo una Actualizacion..")
		conn.commit() 
		cur.close()
		conn.close()

def main_():
	print("corriendo Actualizacion..")
	while (True):
		Actualizar()

main_()