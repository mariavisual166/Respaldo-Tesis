# Amigo progrmador , si le va hacer mantenimineto a este codigo , le deseo suerte.
# Cuando este codigo fue creado solo dios y yo sabiamos como funcionaba , hoy en dia solo dios sabe
from flask import Flask, make_response, request
from microservices.scholar import main
from resources.ProcesarArchivoDocente import leerArchivoDocentes,Mensaje
from flask_cors import CORS
from flask_restful import Api
import os
from werkzeug.utils import secure_filename
from flask_restful import reqparse, abort, Api, Resource
import simplejson as json
import csv, operator
import sys
import types
import psycopg2
from microservices.Teachers import TeachersInsertInitial, TeacherstUpdate
import requests
UPLOAD_FOLDER = 'C:/Users\Mariangela Goncalves/Desktop/prueba/test-backend-apis-master'
ALLOWED_EXTENSIONS = set(['csv'])
app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class File(Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
   
    def post(self):
        file = request.files['file']
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            NombreArchivo=file.filename
            user="Facyt"
            Error= leerArchivoDocentes(NombreArchivo,user)
            os.remove(NombreArchivo) 
            if(Error=="El Archivo csv ha sido procesado con exito!!!"):
                #data1={"username":user,"action": "Carga de archivo", "module": "Docentes"}
                #r=requests.post("",dhttp://localhost:8084/api/v1/historyactionata= json.dumps(data1) )
                pass
            return json.dumps({'exitosa':Error}), 201, { 'Access-Control-Allow-Origin': '*' }
        else:
            # return error
            return json.dumps({'exitosa':'Error !!!. El formato del archivo ingresado no es csv'}), 201, { 'Access-Control-Allow-Origin': '*' }



# docentes route
api.add_resource(TeachersInsertInitial, '/docentes')
api.add_resource(TeacherstUpdate, '/docentes/<date_update>')
api.add_resource(File, '/upload')

if __name__ == '__main__':
   
    app.run(debug=True, port=int('8083'))



