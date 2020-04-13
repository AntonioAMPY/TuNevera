
    
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