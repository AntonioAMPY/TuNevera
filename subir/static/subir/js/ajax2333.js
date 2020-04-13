
    
    function bb(){
                           
        $.ajax({
                           
             type: "POST",
             url: "/indexex/ve_a_cocinar/",
             data: {
                            
                  'texto_buscar' : $('#buscador').val(),
                  'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
             },
            
            success : busquedaSuccess,
            dataType : 'html'
                              
        });
                           
    };



function busquedaSuccess(data,textStatus,jqXHR){
    
    $('#buscador_resultados').html(data);
}