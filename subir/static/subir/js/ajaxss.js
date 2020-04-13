$(function(){
    
    $('#buscador').keyup(function(){
                           
        $.ajax({
                           
             type: "POST",
             url: "/subir/indexex/buscador/",
             data: {
                            
                  'texto_buscar' : $('#buscador').val(),
                  'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
             },
            
            success : busquedaSuccess,
            dataType : 'html'
                              
        });
                           
    });
    
});


function busquedaSuccess(data,textStatus,jqXHR){
    
    $('#buscador_resultados').html(data);
}