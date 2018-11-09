from flask_restful import abort, Resource, reqparse
import simplejson as json
from psycopg2 import DatabaseError
from textwrap import dedent
from common.BD import BD
from flask import make_response, jsonify, request
from datetime import datetime
#base  de datos
import psycopg2


class TeachersInsertInitial(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    # Postgres
    PSQL_HOST = "localhost"
    PSQL_PORT = "5432"
    PSQL_USER = "postgres"
    PSQL_PASS = "0000"
    #PSQL_PASS = "123456"
    PSQL_DB   = "docente"
    connstr = "host=%s port=%s user=%s password=%s dbname=%s" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
    conn = psycopg2.connect(connstr)
    cur = conn.cursor()
    def get(self):
        try:
            # consultar OtroEstudio
            resultOtroEstudio = self.queryAll(dedent("""SELECT O.Id ,D.cedula,O.Nomtitulo FROM OtroEstudio O,docente D,DocenteRealizaOtroEstudio R WHERE R.IdOtroEstudio=O.id and R.CedulaPersona=D.cedula"""))
            # consultar Publicaciones
            resultPublicacion = self.queryAll(dedent("""SELECT P.Id,D.cedula,P.NumeroCitaciones,P.UrlCitacion,P.TituloPublicacion,P.UrlPublicacion FROM Publicacion P ,docente D , DocenteTienePublicacion R WHERE R.IdPublicacion=P.id and R.CedulaPersona=D.cedula"""))
            # consultar Proyecto
            resultProyecto = self.queryAll(dedent("""SELECT P.Id,D.cedula,P.titulo FROM Proyecto P ,docente D,DocenteParticipaProyecto R WHERE R.IdProyecto=P.id and R.CedulaPersona=D.cedula"""))
            # consultar Titulos
            resultTitulo = self.queryAll(dedent("""SELECT P.Id,D.cedula,P.Nomtitulo,P.Nivel FROM Titulo P,docente D ,DocenteTieneTitulo R WHERE R.IdTitulo=P.id and R.CedulaPersona=D.cedula"""))
             # consultar Premios
            resultPremio = self.queryAll(dedent("""SELECT P.Id,D.cedula,P.Nombre FROM Premio P, docente D , DocenteTienePremio R WHERE R.IdPremio=P.id and R.CedulaPersona=D.cedula"""))
            # consultar docentes
            resultTeacher = self.queryAll(dedent("""\
            SELECT Cedula, PirmerNombre, SegundoNombre, PirmerApellido, SegundoApellido, Sexo, correo, Nacionalidad, Facultad, Tipo,AreaDeInvestigacion,Escalafon 
            FROM docente"""))
            
               
            response = {
                "dim-docente": {"items": resultTeacher},
                "dim-docente-otro-estudio": {"items": resultOtroEstudio}, 
                "dim-docente-publicacion": {"items":resultPublicacion},
                "dim-docente-proyecto": {"items":resultProyecto},
                "dim-docente-titulo": {"items":resultTitulo},
                "dim-docente-premio": {"items":resultPremio}
               
                        
            }  
        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

        
        
class TeacherstUpdate(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    
    def get(self, date_update):

        try:
            date_update = datetime.strptime(date_update, '%Y-%m-%d %H:%M:%S')
            print(date_update)
             # consultar OtroEstudio
            resultOtroEstudio = self.queryAll(dedent("""SELECT O.Id ,D.cedula,O.Nomtitulo FROM OtroEstudio O,docente D,DocenteRealizaOtroEstudio R WHERE R.IdOtroEstudio=O.id and R.CedulaPersona=d.cedula and O.FechaActualizacion >= %s""")), [date_update]
            # consultar Publicaciones
            resultPublicacion = self.queryAll(dedent("""SELECT P.Id,D.cedula,P.NumeroCitaciones,P.UrlCitacion,P.TituloPublicacion,P.UrlPublicacion FROM Publicacion P ,docente D , DocenteTienePublicacion R WHERE R.IdPublicacion=P.id and R.CedulaPersona=D.cedula and P.FechaActualizacion >= %s""")), [date_update]
            # consultar Proyectos
            resultProyecto = self.queryAll(dedent("""SELECT P.Id,D.cedula,P.titulo FROM Proyecto P ,docente D,DocenteParticipaProyecto R WHERE R.IdProyecto=P.id and R.CedulaPersona=D.cedula and P.FechaActualizacion >= %s""")), [date_update]
            # consultar Titulos
            resultTitulo = self.queryAll(dedent("""SELECT P.Id,D.cedula,P.Nomtitulo,P.Nivel FROM Titulo P,docente D ,DocenteTieneTitulo R WHERE R.IdTitulo=P.id and R.CedulaPersona=D.cedula and P.FechaActualizacion >= %s""")), [date_update]
            # consultar Premios
            resultPremio = self.queryAll(dedent("""SELECT P.Id,D.cedula,P.Nombre FROM Premio P, docente D , DocenteTienePremio R WHERE R.IdPremio=P.id and R.CedulaPersona=D.cedula and P.FechaActualizacion >= %s""")), [date_update]
            # consultar docentes
            resultTeacher = self.queryAll(dedent("""\
            SELECT Cedula, PirmerNombre, SegundoNombre, PirmerApellido, SegundoApellido, Sexo, correo, Nacionalidad, Facultad, Tipo,AreaDeInvestigacion,Escalafon 
            FROM docente WHERE FechaActualizacion >= %s""")), [date_update]
           
            response = {
                "dim-docente": {"items": resultTeacher},
                "dim-docente-otro-estudio": {"items": resultOtroEstudio}, 
                "dim-docente-publicacion": {"items":resultPublicacion},
                "dim-docente-proyecto": {"items":resultProyecto},
                "dim-docente-titulo": {"items":resultTitulo},
                "dim-docente-premio": {"items":resultPremio}
                        
            }  
            
        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return jsonify(response), 200, { 'Access-Control-Allow-Origin': '*' }



    

