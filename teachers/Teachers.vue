<template>
	<div class="container">
		<div class="large-12 medium-12 small-12 cell">
      <div id= "i" class="alert alert-secondary" role="alert">
      Seleccione un archivo csv
    </div>
    <p >Fecha tope de subida: 2-11-2018</p>
    <div class="archivo normal rounded" id="archi">
     <img src="https://image.flaticon.com/icons/svg/29/29102.svg"
		  <label>Archivo
		    <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
		  </label>
		  <button class="btn btn-light" id="enviar"v-on:click="submitFile()">Enviar</button>
      
      </div>
      <div class="intru">
       <h4 >Pasos a seguir</h4>
        <p >1-haga click en el boton seleccionar archivo.</p>
        <p >2-seleccione el archivo csv que desea ingresar en el sistema.</p>
        <p >3-Presione el boton de enviar.</p>
        <p >4-En caso que ocurra  un error , modifique el archivo y vuelva a intentarlo.</p>
        
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
            const path = 'http://localhost:8083/upload';
          

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
          padding: 50px 40px;
          width: 70%;
          min-width: 500px;
          float:left;
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
         border: 1px solid rgba(0,128,0,0.2);
        }
    .normal{
           border: 1px solid rgba(155,155,155,0.1);
         
        } 
    #enviar  {
          
          width: 20%;
        }
      .copyright{
          
          display:none;
        }
        .intru{
          
             padding: 10px 40px;
           
        }
   .intru h4, .intru p{
          

         text-align: center;
        }
@media (max-width: 1000px) { 


   .intru {
          

         display:none;
        }
  .archivo{
          
        
          padding: 50px 40px;
          width: 90%;
          min-width: 500px;
          float:none;
         
        }

 }
</style">

