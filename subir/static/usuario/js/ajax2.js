

    function seguimiento(lacondicion){
        
                
                
        var botoncito = $('#botoncito').val() // capturar el valor para condicionar y cambiar el estilo del boton
        
        var botoncito2 = $('#botoncito') // capturar el boton para cambiar el estilo del boton
        
        
       
        if(botoncito=='seguir'){
            

            botoncito2.html("dejar de seguir")
            botoncito2.addClass("btn-danger")
            botoncito2.removeClass("btn-success")
            botoncito2.val("dejar de seguir")


  
            
        }
        
        else{
          
            botoncito2.html("seguir")
            botoncito2.addClass("btn-success")
            botoncito2.removeClass("btn-danger")
            botoncito2.val("seguir")
            
        }
    
                
        $.ajax({
                           
             type: "POST",
             url: "/usuario/follow/",
             data: {
                            
                  'seguir' : $('#elusuario').val(),
                  'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
             },
            
            success : seguir,
            dataType : 'html'
                              
        })
                           
    }



function seguir(data,textStatus,jqXHR){
    
    $('#seguirresult').html(data);
}