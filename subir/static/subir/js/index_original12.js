




function llamarbb(){
    
    
    bb()
}
function bb(){
                           
        $.ajax({
                           
             type: "POST",
             url: "/indexex/buscadoring/",
             data: {
                            
                  'texto_buscar' : $('#buscador2').val(),
                  'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
             },
            
            success : busquedaSuccess,
            dataType : 'html'
                              
        });
                           
    };



function busquedaSuccess(data,textStatus,jqXHR){
    
    $('#buscador_resultados').html(data);
    

}




               
$(document).ready(function()
    {
    
    
    for (var i=0; i<1000; i++) {
        
        setTimeout(function() {
            
           
            $('.efectoflip').toggleClass("efectimagen") 

            
        }, 5000*i);
        
    
$(".hoverperfil").hover(
  function() {
      
    $(this).removeClass("text-primary")  
    $(this).addClass('text-white')
    $(this).addClass('bg-primary')
  },
function(){
    
      $(this).addClass("text-primary")  
    $( this ).removeClass('text-white')
    $(this).removeClass('bg-primary')
}    
    
);    
        
        
}
    
    $("#ollita").hover(
        function()
        {
            $(this).attr("src", "../../static/subir/img/ollita-animacion.gif");
        },
        function()
        {
            $(this).attr("src", "../../static/subir/img/ollita-static.png");
        }                         
    );  
    
    
    $(".quitarflip").mouseover(

        function()
        {
            $('.efectoflip').toggleClass("efectimagen") 
        }
    )
    
});



    
function bs_input_file() {
	$(".input-file").before(
		function() {
			if ( ! $(this).prev().hasClass('input-ghost') ) {
				var element = $("<input type='file' class='input-ghost' style='visibility:hidden; width:'0px'>");
				element.change(function(){
					element.next(element).find('input').val((element.val()).split('\\').pop());
				});
				$(this).find("button.btn-choose").click(function(){
					element.click();
				});
				$(this).find('input').css("cursor","pointer");
				$(this).find('input').mousedown(function() {
					$(this).parents('.input-file').prev().click();
					return false;
				});
				return element;
			}
		}
	);
}
$(function() {
	bs_input_file();
});
    


Vue.component('mostraringredientes',{
    template:`    
<div class="row justify-content-around my-2 py-2 mx-1 ui-state-default bg-faded rounded" style="cursor:move;-webkit-box-shadow: -1px 1px 12px -1px rgba(0,0,0,0.75);-moz-box-shadow: -1px 1px 12px -1px rgba(0,0,0,0.75);box-shadow: -1px 1px 12px -1px rgba(0,0,0,0.75);overflow:auto;">


            <div class="col-auto mx-1 py-2">
                <i class="fas fa-arrows-alt"></i>
            </div>

            <div class="col-12 col-sm-3">
                <input name="" @keyup="llamar" type="text" class="form-control cantidading" placeholder="Cantidad" id="">
            </div>

            <div class="col-12 col-sm-3">
                <input name="" @keyup="llamar" type="text" class="form-control cantidading" placeholder="Cuantificador" id="">
            </div>
            <h4 class="mt-1">de</h4>
            <div class="col-12 col-sm-3">
                <input name="" @keyup="llamar" type="text" class="form-control cantidading" placeholder="Nombre de ingrediente" id="">
            </div>


            <div class="col-12 col-sm-12 col-md-auto">
                <button type="button" class="btn btn-secondary btn-block" @click="$emit(\'remove\')">X</button>
            </div>

</div>
  `,
    
    data(){
        
        return{
            variable:'hola'
            
        }
    },
    
    methods:{
        
        llamar(){
            
            instancia.mandar()
        }
    }
    
})   

Vue.component('categorias', {
  props: ['listacategorias', 'value'],
  template: '#categorias-template',
  mounted: function () {
    var vm = this
    $(this.$el)
      // init select2
      .select2({ data: this.listacategorias })
      .val(this.value)
      .trigger('change')
   
      // emit event on change.
      .on('change', function () {
        vm.$emit('input', this.value)
      })
  },
  watch: {
    value: function (value) {
      // update value
      $(this.$el)
      	.val(value)
      	.trigger('change')
  
    },
    listacategorias: function (listacategorias) {
      // update options
      $(this.$el).empty().select2({ data: options })
    }
  },
  destroyed: function () {
    $(this.$el).off().select2('destroy')
  }
})

Vue.component('album', {
  props: ['listaalbum', 'value'],
  template: '#album-template',
  mounted: function () {
    var vm = this
    $(this.$el)
      // init select2
      .select2({ data: this.listaalbum })
      .val(this.value)
      .trigger('change')
   
      // emit event on change.
      .on('change', function () {
        vm.$emit('input', this.value)
      })
  },
  watch: {
    value: function (value) {
      // update value
      $(this.$el)
      	.val(value)
      	.trigger('change')
  
    },
    listaalbum: function (listaalbum) {
      // update options
      $(this.$el).empty().select2({ data: options })
    }
  },
  destroyed: function () {
    $(this.$el).off().select2('destroy')
  }
})



Vue.use(Buefy.default)
const instancia=new Vue({
    delimiters: ['[[', ']]'],
    el:'#TODO',
    data:{
        aparecerseccion:true,
        windowWidth: 0,
        nextTodoId: 0, 
        acom:'',
        cont:0,
        ing:[],
        ingselect:'',
        xd:'as',
        mailnom:'',
        time1:new Date(""),
        time2:new Date(""),
        nombremodal:'',
        mismo:'',
        ingredientesseleccionados:[],
        tags:[],
        condicioningselect:true,
        //listas de ingredientes
        frutas:[
        {id:0,esconder:false,mostrar:true,nombre:'banana',fotito:'../../static/subir/img/frutas/banana.png'},
        {id:1,esconder:false,mostrar:true,nombre:'carambola',fotito:'../../static/subir/img/frutas/carambola.png'},
        {id:2,esconder:false,mostrar:true,nombre:'cerezas',fotito:'../../static/subir/img/frutas/cerezas.png'},
        {id:3,esconder:false,mostrar:true,nombre:'coco',fotito:'../../static/subir/img/frutas/coco.png'},
        {id:4,esconder:false,mostrar:true,nombre:'frambruesa',fotito:'../../static/subir/img/frutas/frambruesa.png'},
        {id:5,esconder:false,mostrar:true,nombre:'fresa',fotito:'../../static/subir/img/frutas/fresa.png'},
        {id:6,esconder:false,mostrar:true,nombre:'granada',fotito:'../../static/subir/img/frutas/granada.png'},
        {id:7,esconder:false,mostrar:true,nombre:'higo',fotito:'../../static/subir/img/frutas/higo.png'},
        {id:8,esconder:false,mostrar:true,nombre:'kiwi',fotito:'../../static/subir/img/frutas/kiwi.png'},
        {id:9,esconder:false,mostrar:true,nombre:'mangostino',fotito:'../../static/subir/img/frutas/mangostino.png'},
        {id:10,esconder:false,mostrar:true,nombre:'manzana',fotito:'../../static/subir/img/frutas/manzana.png'},
        {id:11,esconder:false,mostrar:true,nombre:'melon',fotito:'../../static/subir/img/frutas/melon.png'},
        {id:12,esconder:false,mostrar:true,nombre:'moras',fotito:'../../static/subir/img/frutas/moras.png'},
        {id:13,esconder:false,mostrar:true,nombre:'naranja',fotito:'../../static/subir/img/frutas/naranja.png'},
        {id:14,esconder:false,mostrar:true,nombre:'papaya',fotito:'../../static/subir/img/frutas/papaya.png'},
        {id:15,esconder:false,mostrar:true,nombre:'pera',fotito:'../../static/subir/img/frutas/pera.png'},
        {id:16,esconder:false,mostrar:true,nombre:'piña',fotito:'../../static/subir/img/frutas/pinia.png'},
        {id:17,esconder:false,mostrar:true,nombre:'sandia',fotito:'../../static/subir/img/frutas/sandia.png'}   
        ],
        
        listaing:[
    {id:0,esconder:false,mostrar:true,nombre:'aguacate',fotito:'../../static/subir/img/vegetales/aguacate.png'},
    {id:1,esconder:false,mostrar:true,nombre:'alcachofa',fotito:'../../static/subir/img/vegetales/alcachofa.png'},
    {id:2,esconder:false,mostrar:true,nombre:'Berenjena',fotito:'../../static/subir/img/vegetales/Berenjena.png'},
    {id:3,esconder:false,mostrar:true,nombre:'brocoli',fotito:'../../static/subir/img/vegetales/brocoli.png'},
    {id:4,esconder:false,mostrar:true,nombre:'calabaza',fotito:'../../static/subir/img/vegetales/calabaza.png'},
    {id:5,esconder:false,mostrar:true,nombre:'cebolla',fotito:'../../static/subir/img/vegetales/cebolla.png'},
    {id:6,esconder:false,mostrar:true,nombre:'coliflor',fotito:'../../static/subir/img/vegetales/coliflor.png'},
    {id:7,esconder:false,mostrar:true,nombre:'hongo',fotito:'../../static/subir/img/vegetales/hongo.png'},
    {id:8,esconder:false,mostrar:true,nombre:'lechuga',fotito:'../../static/subir/img/vegetales/lechuga.png'},
    {id:9,esconder:false,mostrar:true,nombre:'maiz',fotito:'../../static/subir/img/vegetales/maiz.png'},
    {id:10,esconder:false,mostrar:true,nombre:'papa',fotito:'../../static/subir/img/vegetales/papa.png'},
    {id:11,esconder:false,mostrar:true,nombre:'pepino',fotito:'../../static/subir/img/vegetales/pepino.png'},
    {id:12,esconder:false,mostrar:true,nombre:'pimenton',fotito:'../../static/subir/img/vegetales/pimenton.png'},
    {id:13,esconder:false,mostrar:true,nombre:'rabano',fotito:'../../static/subir/img/vegetales/rabano.png'},
    {id:14,esconder:false,mostrar:true,nombre:'tomate',fotito:'../../static/subir/img/vegetales/tomate.png'},
    {id:15,esconder:false,mostrar:true,nombre:'zanahoria',fotito:'../../static/subir/img/vegetales/zanahoria.png'},
            
        ],
        
        mariscos:[
        {id:0,esconder:false,mostrar:true,nombre:'atun',fotito:'../../static/subir/img/mariscos/Atun.png'}, 
        {id:1,esconder:false,mostrar:true,nombre:'calamar',fotito:'../../static/subir/img/mariscos/calamar.png'}, 
        {id:2,esconder:false,mostrar:true,nombre:'camaron',fotito:'../../static/subir/img/mariscos/camaron.png'}, 
        {id:3,esconder:false,mostrar:true,nombre:'cangrejo',fotito:'../../static/subir/img/mariscos/cangrejo.png'}, 
        {id:4,esconder:false,mostrar:true,nombre:'langosta',fotito:'../../static/subir/img/mariscos/langosta.png'}, 
        {id:5,esconder:false,mostrar:true,nombre:'ostras',fotito:'../../static/subir/img/mariscos/ostras.png'}, 
        {id:6,esconder:false,mostrar:true,nombre:'pez',fotito:'../../static/subir/img/mariscos/pez.png'}, 
        {id:7,esconder:false,mostrar:true,nombre:'pulpo',fotito:'../../static/subir/img/mariscos/pulpo.png'}, 
        {id:8,esconder:false,mostrar:true,nombre:'sardina',fotito:'../../static/subir/img/mariscos/sardinas.png'}, 
            
        ],
        
        carnes:[
            
        {id:0,esconder:false,mostrar:true,nombre:'chicharron',fotito:'../../static/subir/img/Carnes/chicharron.png'},  
        {id:1,esconder:false,mostrar:true,nombre:'chorizo',fotito:'../../static/subir/img/Carnes/chorizo.png'},  
        {id:2,esconder:false,mostrar:true,nombre:'costilla',fotito:'../../static/subir/img/Carnes/costilla.png'},
        {id:3,esconder:false,mostrar:true,nombre:'filete',fotito:'../../static/subir/img/Carnes/filete.png'},  
        {id:4,esconder:false,mostrar:true,nombre:'jamon',fotito:'../../static/subir/img/Carnes/jamon.png'},  
        {id:5,esconder:false,mostrar:true,nombre:'mortadela',fotito:'../../static/subir/img/Carnes/mortadela.png'},  
        {id:6,esconder:false,mostrar:true,nombre:'pavo',fotito:'../../static/subir/img/Carnes/pavo.png'},  
        {id:7,esconder:false,mostrar:true,nombre:'pernil',fotito:'../../static/subir/img/Carnes/pernil.png'},  
        {id:8,esconder:false,mostrar:true,nombre:'pollo',fotito:'../../static/subir/img/Carnes/pollo.png'},  
        {id:9,esconder:false,mostrar:true,nombre:'salchichon',fotito:'../../static/subir/img/Carnes/salchichon.png'},  
        {id:10,esconder:false,mostrar:true,nombre:'tocino',fotito:'../../static/subir/img/Carnes/tocino.png'},  
        ], 
        
        lacteos:[
            {id:0,esconder:false,mostrar:true,nombre:'helado',fotito:'../../static/subir/img/Lacteos/helado.png'},
            {id:1,esconder:false,mostrar:true,nombre:'leche',fotito:'../../static/subir/img/Lacteos/leche.png'},
            {id:2,esconder:false,mostrar:true,nombre:'mantequilla',fotito:'../../static/subir/img/Lacteos/mantequilla.png'},
            {id:3,esconder:false,mostrar:true,nombre:'queso',fotito:'../../static/subir/img/Lacteos/queso.png'},
            {id:4,esconder:false,mostrar:true,nombre:'yogurt',fotito:'../../static/subir/img/Lacteos/yogurt.png'},
            
        ],        
        
        panaderia:[
            {id:0,esconder:false,mostrar:true,nombre:'ajonjoli',fotito:'../../static/subir/img/panaderia/ajonjoli.png'},
            {id:1,esconder:false,mostrar:true,nombre:'especies',fotito:'../../static/subir/img/panaderia/especies.png'},
            {id:2,esconder:false,mostrar:true,nombre:'harina',fotito:'../../static/subir/img/panaderia/harina-de-trigo.png'},
            {id:3,esconder:false,mostrar:true,nombre:'levadura',fotito:'../../static/subir/img/panaderia/levadura.png'},
            //cambiar nombre de pan frances a pan
            {id:4,esconder:false,mostrar:true,nombre:'pan frances',fotito:'../../static/subir/img/panaderia/pan-frances.png'},
            {id:5,esconder:false,mostrar:true,nombre:'pan tajado',fotito:'../../static/subir/img/panaderia/pan-tajado.png'},
            {id:6,esconder:false,mostrar:true,nombre:'polvo para hornear',fotito:'../../static/subir/img/panaderia/polvo-para-hornear.png'},
            
        ],
        
        lista:[]
        
        
     },
  mounted() {
      
      
    var self=this  
      
    this.$nextTick(function() {
      window.addEventListener('resize', this.getWindowWidth);

      //Init
      this.getWindowWidth()
        
         $(".sortable").on("sortupdate" ,function( event,ui ){
                     self.mandar()
        
        })  
    })
  

  },
    
    methods:{
        albunes(seccion){
            
            $('#albuminput').val=seccion
            
           
            
        },
        ingsearch(){
            //buscador por ingredientes en ve a cocinar
                           
            var valor = document.getElementById("buscaringren").value
            var valor2 = document.getElementById("buscaringren2").value
            var valor3 = document.getElementById("buscaringren3").value
   
            
                 // agregar lista a la matriz cuando agregue mas categorias
                 var listalista=[this.frutas,this.listaing,this.mariscos,this.carnes,this.lacteos,this.panaderia]
                 
                    for(total=0;total<listalista.length;total++){     

                        var laslistas = listalista[total]

                            for(o=0;o<laslistas.length;o++){
                                        
                                
                                if(valor==laslistas[o].nombre || valor2==laslistas[o].nombre || valor3==laslistas[o].nombre){
                                            
                                            if(laslistas[o].mostrar==false){

                                                    laslistas[o].mostrar=false
                                                    laslistas[o].esconder=true

                                            }
                                            
                                    else{
                                         laslistas[o].mostrar=!laslistas[o].mostrar
                                            laslistas[o].esconder=!laslistas[o].esconder
                                        
                                    }
                                                                            
                                           
                         
                                        }
                                
                        
                

                            }
                    }
            
           document.getElementById("buscaringren").value=""       
           document.getElementById("buscaringren2").value=""       
           document.getElementById("buscaringren3").value=""       
                
                
        },
             agregar(){
                    
        this.lista.push({
                    id: this.nextTodoId++
                })
                    
         },

    getWindowWidth(event){
        this.windowWidth=window.innerWidth
        if(this.windowWidth<=767){
                $("#cabezera").removeClass("fixed-top")
                $("body").addClass("py-0")
        }
        
        else{
                $("#cabezera").addClass("fixed-top")
                $("body").removeClass("py-0") 
            
        }
      },
        aparecersecionxd(){
            this.aparecerseccion=false
        },
        
              pruebaxx(id){

                  
                  //alert(id)
           
                  
    
                  var separar= id.split(" ")
                  
                  var ide=separar[0]
                  
                  var listadoing=separar[1]
                  
                  var sentencialista = eval(listadoing)
                  
                  sentencialista[ide].mostrar=!sentencialista[ide].mostrar
                  sentencialista[ide].esconder=!sentencialista[ide].esconder
                  
                  
                  
 
                   
                
                      //this.ingredientesseleccionados.splice(index, 1);
                      //this.condicioningselect=!this.condicioningselect
            
                  

                },
        
        //mandar texto de ingredientes de seccion de subir receta
        
        mandar(){
            

         
            var obtenercantidad = document.getElementsByClassName("cantidading")
            var inputid=document.getElementById("ppp")
            //var obtenercuantificador = document.getElementById("cuantificadoring")
            //var obtenernombre = document.getElementById("nombreing")
            var ll = []
            
            for(i=0;i<obtenercantidad.length;i++){
                var x = document.getElementsByClassName("cantidading")[i].value
                    
                ll.push(x)
        
            }
            
             this.acom=ll
            
            
    
        },
        
                // cambiar color al menu en amaño pequeño al dar click en alguna seccion
        activelism(id){
            
            var capturarcaja=document.getElementById("collapse1")
            
            var cambiarcolor=capturarcaja.getElementsByTagName("li")
            
            var cambiartextocolor=capturarcaja.getElementsByTagName('a')
            
            
            
            cambiarcolor[id].setAttribute("class","bg-info")
            cambiartextocolor[id].setAttribute("class","nav-link text-white")
            
            
   
            },
        mandartime(){
            
       var lol = this.time1
        
      	lol.getFullYear()-5
        lol.getMonth() -5 
            
        lol.getDate() - 5 
            
           this.time1=lol 
            
            
         var lol2 = this.time2
        
      	lol2.getFullYear()-5
        lol2.getMonth() -5 
            
        lol2.getDate() - 5 
            
        this.time2=lol2
                
            
           
            var horas = this.time1.getHours() 
            var horas2 = this.time2.getHours() 
            
            var minutos = this.time1.getMinutes()
            var minutos2 = this.time2.getMinutes()
    
            
            if(minutos<10){
                
                minutos='0'+minutos
                
                
            } 
            
            if(minutos2<10){
                
                minutos2='0'+minutos2
            }
            
            if(horas<10){
                
                horas='0'+horas
                
                
            }
            
            if(horas2<10){
                
                horas2='0'+horas2
            }
            
           
            
            var tt = document.getElementById("preparacion2").value=horas+":"+minutos
            var tt2 = document.getElementById("coccion2").value=horas2+":"+minutos2
            

            },
        
        //mandar ingredientes al input de ve a cocinar
        
        mandaringredientes(){
                
                $('#ollita').attr("src", "../../static/subir/img/olla-click.gif");
     
                                
                    
                var jejevalor=document.getElementById("buscador2")
                
                 var listaing=[]
                 
                 var listalista=[this.frutas,this.listaing,this.mariscos,this.carnes,this.lacteos,this.panaderia]
                 
                    for(total=0;total<listalista.length;total++){     

                        var laslistas = listalista[total]

                            for(o=0;o<laslistas.length;o++){
                                if(laslistas[o].esconder==true){
                                    listaing.push(laslistas[o].nombre)
                                }

                            }
                    }        
                
                     this.ingselect=listaing    
                    jejevalor.value=this.ingselect
            
            //animacion podio
            
               // this.animacionpodiouno()
                //this.animacionpodiodos()
                //this.animacionpodiotres()
            llamarbb()
            
                
        },
        

        
animacionpodiouno(){

        $("#uno").toggleClass("unosm")


            for (i=0; i<40; i++) {


                    var x = Math.floor((Math.random() * recetasimg.length-1)+1)

                    this.exuno(x+' uno')

                    if(x==3){  

                        break
                    }

            }
},
        
        
                animacionpodiodos(){
          
                $("#dos").toggleClass("dossm")
    
                    for (i=0; i<40; i++) {


                            var x = Math.floor((Math.random() * recetasimg.length-1)+1)

                            this.exuno(x+' dos')

                            if(x==8){  

                                break
                            }

                    }
        },
        animacionpodiotres(){
          
                $("#tres").toggleClass("tressm")
    
                    for (i=0; i<40; i++) {


                            var x = Math.floor((Math.random() * recetasimg.length-1)+1)

                            this.exuno(x+' tres')

                            if(x==5){  

                                break
                            }

                    }
        },
        
            exuno(azar){
                
                var separar=azar.split(" ")
                
                var random=separar[0]
                
                var ide=separar[1]
                
            
                
                   setTimeout(function(){


                        document.getElementById(ide).setAttribute("src",recetasimg[random])   
       
                    }, 100*i); 
            }

   

        }
    

        
        
        
    })
        

                      

    
