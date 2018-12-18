<template>

<div class="container">
   <div  class="row" id="submenu">
      <div class="col">
        <div class="nav nav-item nav-pills text-center fondo"   role="tablist" aria-orientation="vertical">
          <a class="nav-link active" id="LinkArchivo" @click="cambiar2()"href="#" >CARGA DE ARCHIVO</a>
          <a class="nav-link" id="LinkFecha"   @click="cambiar()" href="#" >FECHAS TOPES</a>
          <a class="nav-link" id="FechasA" @click="ultima()" href="#" >ULTIMAS ACTUALIZACIONES</a>
        </div>
      </div>
    </div
  <h3></h3>
  <div id="carga" >
  <h2>Carga de archivos con informacion docente de la UC</h2>
    <div class="large-12 medium-12 small-12 cell" >
      <div id= "i" class="alert alert-secondary" role="alert">
      </div>
    </div>
        
        <div class="row">
          <div class="col-xl-8 col-md-8 col-sm-12">
            <div class="archivo normal rounded" id="archi">
              <h5>Archivo</h5>
              <label>
                <input type="file" id="file" ref="file"   @click="CambiarBoton()" v-on:change="handleFileUpload()"/>
              </label>
              <button class="btn btn-light" id="enviar"  v-on:click="submitFile()">Procesar</button>
            </div>
          </div>
          <div class="col-xl-4 col-md-4 col-sm-0">
            <div class="intru">
              <h4 >Ayuda</h4>
              <p >¿No sabe que archivo subir?</p>
              <button class="btn btn-light" id="centar" @click="Ver()" >Ver ejemplo archivo </button>     
             
              </div>
          </div>
        </div>
  </div>
  <div id="fecha" >
    <h2>Fechas tope de subida de archivos</h2>
     <div class="large-12 medium-12 small-12 cell" >
      <div id= "e" class="alert alert-secondary" role="alert">
      </div>
    </div>
  <div class="row">
    <div class="col-xl-3 col-md-3 col-sm-0">
 
    </div>
    <div class="col-xl-6 col-md-6 col-sm-0 ">
      <form class="">
      <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label">Faces</label>
                        <div class="col-md-12">
                          <input type="date"  id="fechaFaces" value="2010-10-01"  class="form-control" >
                        </div>
                      </div>
                    <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label ">Facyt</label>
                        <div class="col-md-12">
                          <input type="date" id="fechaFacyt" value="2010-10-01" class="form-control" >
                        </div>
                      </div>
                      <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label text-md-right">Face</label>
                        <div class="col-md-12">
                          <input type="date" id="fechaFace" value="2010-10-01" class="form-control" >
                        </div>
                      </div>
                    
                    <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label text-md-right">Fcs</label>
                        <div class="col-md-12">
                          <input type="date"  id="fechaDerecho" value="2010-10-01" class="form-control" >
                        </div>
                      </div>
                        <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label ">Fcjp</label>
                        <div class="col-md-12">
                          <input type="date" id="fechaFcjp" value="2010-10-01" class="form-control" >
                        </div>
                      </div>
                    <div class="form-group row">
                        <label for="first_name" class="col-sm-5 col-form-label text-md-left">Facultad de odontologia</label>
                        <div class="col-md-12">
                          <input type="date"  id="fechaOdontologia" value="2010-10-01"  class="form-control" >
                        </div>
                      </div>
                      <div class="form-group row">
                        <label for="first_name" class="col-sm-5 col-form-label text-md-left">Facultad de  Ingieneria</label>
                        <div class="col-md-12">
                          <input type="date"  id="fechaIngieneria" value="2010-10-01" class="form-control" >
                        </div>
                      </div>
      </form>
       <button class="btn btn-primary" id="centar2"  @click="submitFile2()"  >Guardar</button>
    </div>
        <div class="col-xl-3 col-md-3 col-sm-0 ">
 
    </div>
  </div>
                  
  </div>

<!-- Modal -->
<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        El archivo a sido procesado con exito..
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
  <div id="Ver">
    <h2>Ejemplo</h2>
    <div id="imagen" class="zoom"><img src="/static/Screenshot_1.png" ></div>
     <button class="btn btn-light" id="centar" @click="Regresar()" >Regresar </button>

  </div>
  <div id="UltimaFecha">
    <h2>Últimas fechas de actualización </h2>
<div class="row">
    <div class="col-xl-3 col-md-3 col-sm-0">
 
    </div>
    <div class="col-xl-6 col-md-6 col-sm-0 ">
      <form class="margen">
     <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label text-md-right"> Faces</label>
                        <div class="col-md-12">
                          <input type="text"  id="fechaAFaces" value="2010-10-01" disabled class="form-control" >
                        </div>
                      </div>
                    <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label "> Facyt</label>
                        <div class="col-md-12">
                          <input type="text" id="fechaAFacyt" value="2010-10-01" disabled class="form-control" >
                        </div>
                      </div>
                      <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label text-md-right">Face&nbsp</label>
                        <div class="col-md-12">
                          <input type="text" id="fechaAFace" value="2010-10-01" disabled class="form-control" >
                        </div>
                      </div>
                    
                    <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label text-md-right">Fcs&nbsp&nbsp</label>
                        <div class="col-md-12">
                          <input type="text"  id="fechaADerecho" value="2010-10-01" disabled class="form-control" >
                        </div>
                      </div>
                    <div class="form-group row">
                        <label for="first_name" class="col-sm-1 col-form-label text-md-right">Fcjp</label>
                        <div class="col-md-12">
                          <input type="text" id="fechaAFcjp" value="2010-10-01" disabled class="form-control" >
                        </div>
                      </div>
                    <div class="form-group row">
                        <label for="first_name" class="col-sm-5 col-form-label text-md-left"> Facultad de Odontologia</label>
                        <div class="col-md-12">
                          <input type="text"  id="fechaAOdontologia" value="2010-10-01" disabled class="form-control" >
                        </div>
                      </div>
                      <div class="form-group row">
                        <label for="first_name" class="col-sm-5 col-form-label text-md-left">Facultad de Ingieneria &nbsp&nbsp</label>
                        <div class="col-md-12">
                          <input type="text"  id="fechaAIngieneria" value="2010-10-01" disabled class="form-control" >
                        </div>
                      </div>
                      
                      <div class="form-group row">
                        <label for="first_name" class="col-sm-4 col-form-label text-md-left">Citaciones&nbsp&nbsp</label>
                        <div class="col-md-12">
                          <input type="text" id="API" value="2010-10-01" disabled class="form-control" >
                        </div>
                      </div>
             
     <button class="btn btn-light" id="centar" @click="Regresar()" >Regresar </button>
      </form>
     
    </div>
    <div class="col-xl-3 col-md-3 col-sm-0 ">
 
    </div>
  </div>
  
  </div>
</div>


</template>

<script>


import jsPDF from "jsPDF";
import axios from 'axios';

  export default {
    /*
      Defines the data used by the component
    */
    data(){
      return {
        file: '',
        fecha: '2010-01-01',
        Ultima:'',
      }
    },

    methods: {
      /*
        Submits the file to the server
      */
      submitFile2()
      {
          var Facesfecha=$(fechaFaces).val()
          var Facytfecha=$(fechaFacyt).val()
          var Facefecha=$(fechaFace).val()
          var Derechofecha=$(fechaDerecho).val()
          var Odontologiafecha=$(fechaOdontologia).val()
          var Fcjpfecha=$(fechaFcjp).val()
          var Ingieneriafecha=$(fechaIngieneria).val()
          let formData = new FormData();
         const path = 'http://localhost:8083/fechas/' +Facesfecha+ '/' +Facytfecha+ '/' +Facefecha+'/'+Odontologiafecha+'/'+Fcjpfecha+'/'+Ingieneriafecha +'/'+Derechofecha;
      
           axios.post(path,
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
                
              }
            ).then(function(res){
          
          var con = document.getElementById("e");
          con.textContent  = res.data["exitosa"];

       
             $( "#e" ).addClass( "verde" )
              console.log(res.data); 
              console.log('SUCCESS!!');
           
       
         
        })
        .catch(res=> {
        console.log(res);
        console.log('FAILURE!!');
        });


      },
      submitFile(){
        /*
                Initialize the form data
            */
            let formData = new FormData();

            /*
                Add the form data we need to submit
            */
            formData.append('file', this.file);

        /*
          Make the request to the POST /single-file URL
        */
                    
            const path = 'http://localhost:8083/upload/'+'Facyt_docente';
          

            axios.post(path,
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
                
              }
            ).then(function(res){
              var div = document.getElementById("i");
              var i=res.data["Erros"].length;
              div.textContent  = res.data["Erros"][i-1]["exitosa"];

           if(res.data["Erros"][i-1]["exitosa"]== "El Archivo csv ha sido procesado con exito!!!"){
               div.textContent  = "";
              $( "#archi" ).removeClass( "rojo" )
              $( "#archi" ).removeClass( "normal" )
              $('#exampleModalCenter').modal('show');
              $( "#i" ).removeClass( "alert alert-danger" )
              $( "#i" ).removeClass( "alert alert-secondary" ).addClass( "alert alert-secondary" )
              $('#enviar').attr("disabled", true); 
           }else
           {
            $( "#i" ).removeClass( "alert alert-secondary" ).addClass( "alert alert-danger" )

           }
           if(res.data["Erros"][i-1]["exitosa"]== "Error a procesar el archivo. Por favor revise el pdf LISTA_ERRORES para conocer los errores del archivo ingresado al sistema")
          {
              var doc = new jsPDF("l", "mm", "a4");
              doc.setFont("helvetica");
              doc.setFontType("bold");
              doc.setFontSize(12);
              doc.setProperties({
                title: "Lista de errores",
                subject: "Reporte",
                author: "UC Ranking",
                date: new Date()
              });
              let y = 30
              let index = 0
              doc.text(140, 20, "Lista de errores");
              res.data["Erros"].forEach(() => {
                if(index !==  res.data["Erros"].length - 1) {
                  doc.text(20, y, res.data["Erros"][index]["error"]);
                  y += 10
                  index += 1
                }
              })

              doc.addPage();
              doc.text(140, 20, "Sugerencias");
              doc.text(20, 40, "La columna Cedula solo puede contener valores numericos");
              doc.text(20, 50, "Las columnas primer_nombre,segundo_nombre,primer_apellido,area de invetigacion, titulo, y segundo_apellido   solo puede  ");
              doc.text(20, 60, "contener valores Alfabeticos");
              doc.text(20, 70, "La columna sexo solo puede contener los valores F (Femenino) o M (Masculino)");
              doc.text(20, 80, "La columna correo solo debe vontener valores con el formato @example.com o @uc.edu.ve");
            
              doc.text(20, 90, "La columna nacionalidad solo puede contener los valores V (Venezolano) o E (Extranjero)");
              doc.text(20, 100, "La columna tipo solo puede contener los valores Normal, Contratado o Investigador");
              doc.text(20, 110, "La columna area de invetigacion solo puede contener los valores Normal, Contratado o Investigador");
              doc.text(20, 120, "La columna tipo solo puede contener los valores Normal, Contratado o Investigador");
              doc.text(20, 130,"La columna Nivel solo puede contener los valores Pregrado, Postgrado, Maestia, Doctodado");
              doc.text(20, 140,"La columna escalafon solo puede contener los valores Instructor ,Asistente, Agregado,Asociado,Titular");
              doc.text(20, 150,"La columna escalafon solo puede contener los valores Faces, Facyt, Face, Fcs, Odontologia,Fcjp y Ingieneria");
                //Info for verification
            
              doc.setFont("helvetica");
              doc.setFontType("bold");
              doc.setFontSize(16);
              

              doc.save("LISTA_ERRORES" + ".pdf");

              $( "#enviar" ).removeClass( "btn btn-primaryt" ).addClass( "btn btn-light" )

            }

         
          console.log(res.data["Erros"][i-1]["exitosa"]); 
          console.log('SUCCESS!!');
        })
        .catch(res=> {
        console.log(res);
        console.log('FAILURE!!');
        });
      }, cambiar()
      {
        $( "#FechasA" ).removeClass( "active" )
        $( "#LinkArchivo" ).removeClass( "active" )
        $( "#LinkFecha" ).addClass( "active" )
        $("#carga").css("display", "none");
        $("#UltimaFecha").css("display", "none");
        $("#fecha").css("display", "block");
       
      },
      Ver() {
      $("#submenu").css("display", "none");
      $("#fecha").css("display", "none");
      $("#carga").css("display", "none");
      $("#Ver").css("display", "block");
  
      },
      cambiar2()
      {
       $("#UltimaFecha").css("display", "none");
       $( "#FechasA" ).removeClass( "active" )
      $( "#LinkFecha" ).removeClass( "active" )
      $( "#LinkArchivo" ).addClass( "active" )
      $("#fecha").css("display", "none");
      $("#carga").css("display", "block");
      },
      Regresar()
      {
      $("#submenu").css("display", "block");
      $("#Ver").css("display", "none");
      $("#UltimaFecha").css("display", "none");
      $("#carga").css("display", "block");
      }, ultima()
      {
        $( "#LinkFecha" ).removeClass( "active" )
        $( "#LinkArchivo" ).removeClass( "active" )
        $( "#FechasA" ).addClass( "active" )
        $("#fecha").css("display", "none");
        $("#carga").css("display", "none");
        $("#Ver").css("display", "none");
         $("#UltimaFecha").css("display", "block");
          
          let formData = new FormData();
           const path = 'http://localhost:8083/ultimaFecha' ;
        
             axios.post(path,
                  formData,
                  {
                  headers: {
                      'Content-Type': 'multipart/form-data'
                  }
                  
                }
              ).then(function(res){
            
           

            $(fechaAFaces).val(res.data["Faces"])
            $(fechaAFacyt).val(res.data["Facyt"])
            $(fechaAFace).val(res.data["Face"])
            $(fechaADerecho).val(res.data["Fcs"])
            $(fechaAOdontologia).val(res.data["Odontologia"])
            $(fechaAFcjp).val(res.data["Fcjp"])
            $(fechaAIngieneria).val(res.data["Ingieneria"])
            $(API).val(res.data["APi"])   
            console.log(res.data); 
            console.log('SUCCESS!!');
           
          })
          .catch(res=> {
          console.log(res);
          console.log('FAILURE!!');
          });


      },CambiarBoton(){
          
          $( "#enviar" ).removeClass( "btn btn-light" ).addClass( "btn btn-primary" )

      },
      /*
        Handles a change on the file upload
      */
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      }
    }
  }
</script>

<style type="text/css">
#centar{
          display:block;margin:auto;
           margin-bottom:20px; margin-top:20px;
        }
#centar2{
          display:block;margin:auto;
           margin-bottom:20px; margin-top:-10px;
        }
  .archivo{
          
          background: rgba(155,155,155,0.3);
          padding: 40px 40px 60px 40px ;
          margin:auto;
          margin-top:12%;
          margin-bottom:8%;
        }
    #i{
        margin-top:10px;
         
        }
    .rojo{
         border: 1px solid rgba(255,0,0,0.5);
        }
    .verde{
       background:rgba(0,128,0,0.2);
        }
    .normal{
           border: 1px solid rgba(155,155,155,0.1);
         
        } 
      #fecha,#Ver,#UltimaFecha{
           display:none;
         
        }
      .copyright{
          
          
        }
        .intru{
          
             padding: 10px 40px;
           
        }
   .intru h4, .intru p{
          

         text-align: center;
        }
    h2{
      margin-top:10px;
      margin-bottom:20px;
      text-align: center;
      opacity :0.5;
        }
      h5{
      margin-bottom:15px;
      text-align: center;
      opacity :0.0;
        }
        #enviar {
       
          width:150px;
        }
        #submenu {
       
         margin-top:10px;
        margin-bottom:10px;
        }
        #imagen img{
             width:110%;
              margin-left:-90px;
        
        }

        label{
            text-align:center;
           
        }
@media (max-width: 1000px) { 


   .intru {
          
           padding: 0px 0px;
        }


 }
 @media (max-width: 768px) { 


   .intru {
          
          display:none;
        }

 

    


 }

  @media (max-width: 1000px) { 


  
     #enviar {
          margin-top:10px;
          width:100%;
        }

    


 }
  .margen{
          
         
          margin-top:5%;
          margin-bottom:8%;
        }
  #boton{
          display:bloack;
           margin:auto;

       
        }

    <style>
.zoom {
    padding: 50px;
    
    transition: transform .2s; /* Animation */
    width: 200px;
    height: 200px;
   
}

.zoom:hover {
    transform: scale(1.3); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
    margin-left:100px;
     margin-bottom:80px;
}

.form-group{
    margin-top:-10px;
}
</style>    


