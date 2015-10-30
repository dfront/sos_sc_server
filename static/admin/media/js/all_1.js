


$(document).ready(function()
{


  
   $("input[name='tipo']").change(function(){
        var valor = $(this).val()
        if (valor == "F")
        {
            $("#dados_fisico").show()
            $("#dados_juridico").hide()
        }
        else if (valor == "J")
        {
            $("#dados_fisico").hide()
            $("#dados_juridico").show()
        }
    })

})