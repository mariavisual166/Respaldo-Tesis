<template>

<div class="container">
  <h2>Docentes</h2>
    <div class="large-12 medium-12 small-12 cell">
      <div id= "i" class="alert alert-secondary" role="alert">
      Carga de documentos con los datos docentes de la UC
    </div>
  <div class="row">
    <div class="col-xl-8 col-md-8 col-sm-12">
      <div class="archivo normal rounded" id="archi">
        <h5>Archivo</h5>
        <label>
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        </label>
        <button class="btn btn-light" id="enviar"v-on:click="submitFile()">Enviar</button>
      </div>
    </div>
    <div class="col-xl-4 col-md-4 col-sm-0">
      <div class="intru">
         <h4 >Pasos a seguir</h4>
          <p >1-haga click en el boton seleccionar archivo.</p>
          <p >2-seleccione el archivo csv que desea ingresar en el sistema.</p>
          <p >3-Presione el boton de enviar.</p>
          <p >4-En caso que ocurra  un error , modifique el archivo y vuelva a intentarlo.</p>
        </div>
    </div>
   
  </div>
</div>
		</div>

</template>

<script>
import axios from 'axios';

  export default {
    /*
      Defines the data used by the component
    */
    data(){
      return {
        file: ''
      }
    },

    methods: {
      /*
        Submits the file to the server
      */
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
            const path = 'http://localhost:8083/upload/'+'Facyt';
          

            axios.post(path,
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
                
              }
            ).then(function(res){
            var div = document.getElementById("i");

           div.textContent  = res.data["exitosa"];
           if(res.data["exitosa"]== "El Archivo csv ha sido procesado con exito!!!"){
            $( "#archi" ).removeClass( "rojo" )
            $( "#archi" ).removeClass( "normal" )
            $( "#archi" ).addClass( "verde" )
            $( "#i" ).removeClass( "alert alert-danger" )
            $( "#i" ).removeClass( "alert alert-secondary" ).addClass( "alert alert-success" )
            $('#enviar').attr("disabled", true); 
           }else
           {
            $( "#archi" ).removeClass( "normal" ).addClass( "rojo" )
            $( "#i" ).removeClass( "alert alert-secondary" ).addClass( "alert alert-danger" )
           }

         
          console.log(res.data); 
          console.log('SUCCESS!!');
        })
        .catch(res=> {
        console.log(res);
        console.log('FAILURE!!');
        });
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

      .copyright{
          
          
        }
        .intru{
          
             padding: 10px 40px;
           
        }
   .intru h4, .intru p{
          

         text-align: center;
        }
    h2{
      margin-top:40px;
      margin-bottom:40px;
      text-align: center;
      opacity :0.5;
        }
      h5{
      margin-bottom:15px;
      text-align: center;
      opacity :0.7;
        }
        #enviar {
       
          width:150px;
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

</style>

