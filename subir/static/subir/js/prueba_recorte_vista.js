window.onload=function(){
    
    mandar()
}


function conversion(){
    
var canvas = document.getElementById('canvas');
var cambiarimg= document.getElementById("nuevoimg")
cambiarimg.src = canvas.toDataURL();
    
}


function mandar(){    
    // Cache a reference to the html element
    var ruta =document.getElementById("imagenrecortada").src
    var elemento =document.getElementById("imagenrecortada")
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
