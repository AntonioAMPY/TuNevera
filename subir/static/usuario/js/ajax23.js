
var condicion=true

function lolseguimiento(){
    
        
        var botoncito = $('#botoncito')
       
        if(condicion){
            
            botoncito.html("seguir")
            botoncito.addClass("btn-success")
            botoncito.removeClass("btn-danger")
      
  
            
        }
        
        else{
            botoncito.html("dejar de seguir")
            botoncito.addClass("btn-danger")
            botoncito.removeClass("btn-success")
    
            
        }
}

    function seguimiento(){
        

        lolseguimiento()
        
                
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