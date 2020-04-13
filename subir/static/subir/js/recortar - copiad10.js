var elemento =document.getElementById("preview")
var condicion = true


$(function() {

  // We can attach the `fileselect` event to all file inputs on the page
  $(document).on('change', ':file', function() {
    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);
  });

  // We can watch for our custom `fileselect` event like this
  $(document).ready( function() {
      $(':file').on('fileselect', function(event, numFiles, label) {

          var input = $(this).parents('.input-group').find(':text'),
              log = numFiles > 1 ? numFiles + ' files selected' : label;

          if( input.length ) {
              input.val(log);
          } else {
              if( log ) alert(log);
          }

      });
  });
  
});

function convertir(){
    
var canvas = document.getElementById('canvas');
var cambiarimg= document.getElementsByClassName("xd")[0] // input
//var img = new Image();
cambiarimg.src = canvas.toDataURL();
    
}
document.getElementById('activo').disabled=true
function mandar(){    
    
        
    if(condicion){
     jcrop_api.disable();
        condicion=!condicion
        document.getElementById("texto").innerHTML="Recortar"
        document.getElementById("activo").disabled=false
       
    }
    
    
    else{
        jcrop_api.enable();
        condicion=!condicion
        document.getElementById("texto").innerHTML="Aplicar recorte"
         document.getElementById('activo').disabled=true
        
    }
    
    // Cache a reference to the html element
    var ruta =document.getElementById("preview").src
    var elemento =document.getElementById("preview")
    var canvas = document.getElementById('canvas');
    var x=document.getElementById("x")
    var y=document.getElementById("y")
    var w=document.getElementById("w")
    var h=document.getElementById("h")
    // Set the drawing surface dimensions to match the canvas
    canvas.width  = w.value;
    canvas.height = h.value

    // Get a reference to the 2d drawing context / api
    var ctx = canvas.getContext('2d');

    // Create a new image object
    var image = new Image();
    var convertir = new Image();

    // Callback, executed when the image is loaded
    // See previous video for a more flexible solution 
    image.onload = function(){

      // Select a rectangle from the source image,
      // and then draw is as normal.768px669px   image.naturalWidth /2,   image.naturalHeight/2
      // (image, srcX, srcY, srcWidth, srcHeight, x, y, width, height)
      ctx.drawImage(image, x.value, y.value, w.value, h.value,0,0, w.value, h.value);
    }
    // Start the image loading
    image.src=ruta;
    
    
}

            
function bytesToSize(bytes) {
    var sizes = ['Bytes', 'KB', 'MB'];
    if (bytes == 0) return 'n/a';
    var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
    return (bytes / Math.pow(1024, i)).toFixed(1) + ' ' + sizes[i];
};




function updateInfo(e) {
    $('#x').val(e.x);
    $('#y').val(e.y);
    $('#w').val(e.w);
    $('#h').val(e.h);
};

function clearInfo() {
    $('.info #w').val('');
    $('.info #h').val('');
};


     // Create variables (in this scope) to hold the Jcrop API and image size
            var jcrop_api, boundx, boundy;

                 

                 
function fileSelectHandler() {
    // get selected file
    
    var oFile = $('input:file')[0].files[0];

    // hide all errors
    $('.error').hide();

    // check for image type (jpg and png are allowed)
    var rFilter = /^(image\/jpeg|image\/png)$/i;
    if (! rFilter.test(oFile.type)) {
        alert("selecciona un archivo de imagen");
        return;
    }

    // check for file size
    if (oFile.size > 250 * 1024) {
        alert("error, imagen demasiado grande")
        return;
    }

    // preview element
    var oImage = document.getElementById('preview');

    // prepare HTML5 FileReader
    var oReader = new FileReader();
        oReader.onload = function(e) {

        // e.target.result contains the DataURL which we can use as a source of the image
        oImage.src = e.target.result;
          
    
            
                //Start the image loading
              
        oImage.onload = function () { // onload event handler

            // display step 2
            $('.step2').fadeIn(500);

            // display some basic image info
            var sResultFileSize = bytesToSize(oFile.size);
            $('#filesize').val(sResultFileSize);
            $('#filetype').val(oFile.type);
            $('#filedim').val(oImage.naturalWidth + ' x ' + oImage.naturalHeight);

       
            // destroy Jcrop if it is existed
            if (typeof jcrop_api != 'undefined'){ 
                jcrop_api.destroy();
                jcrop_api = null;
                $('#preview').width(oImage.naturalWidth);
                $('#preview').height(oImage.naturalHeight);
            }


            setTimeout(function(){

                // initialize Jcrop

           $('#preview').Jcrop({
                    setSelect:[ 100, 100, 50, 50 ],
                    maxSize:[600,600],
                    bgFade: true, // use fade effect
                    bgOpacity: .3, // fade opacity
                    onChange: updateInfo,
                    onSelect: updateInfo,
                    onRelease: clearInfo,
                    boxWidth: 650,
                    boxHeight: 400,
                    aspectRatio: 1,

                }, function(){

                    // use the Jcrop API to get the real image size

                    var bounds = this.getBounds();

                    boundx = bounds[0];

                    boundy = bounds[1];

                    // Store the Jcrop API in the jcrop_api variable

                    jcrop_api = this;

                });

            },1);

        };
            
            
            
            

    };

    // read selected file as DataURL


   
        
           oReader.readAsDataURL(oFile);
   

   
}




function parar(){
    
    
    if(condicion){
     jcrop_api.disable();
        condicion=!condicion
    }
    
    
    else{
        jcrop_api.enable();
        condicion=!condicion
    }
}
