/* 
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */


$(document).ready(function()
{
    $("#btBusca_valor_p").click(function()
    {

       var data;
       var conta = $("[name=conta_p]").val()
       var forma_pagamento = $("[name=forma_pagamento_p]").val()
       var data_vencimento = $("[name=data_vencimento_p]").val()
       var descricao = $("[name=descricao_p]").val()
       var parcela_inicio = $("[name=parcela_inicio]").val()
       var parcela_fim = $("[name=parcela_fim]").val()
       var valor = $("[name=valor_p]").val()

       var qtd_dias = parcela_fim - parcela_inicio

   
       //$('.dynamic-pagamento_set').remove()
       totalForms = $("#id_pagamento_set-TOTAL_FORMS").val()
       for(var i=totalForms;i<=(qtd_dias+parseInt(totalForms));i++)
       {
            addRow()
            if (!data)
            {
                data = data_vencimento.split("/")[2] +","+ data_vencimento.split("/")[1]+","+data_vencimento.split("/")[0]
                data = new Date(data);  
            }         
                           
            $("#id_pagamento_set-"+i+"-data_vencimento").val($.format.date(data, "dd/MM/yyyy"))
             $("#id_pagamento_set-"+i+"-conta").val(conta)
             $("#id_pagamento_set-"+i+"-formaPagamento").val(forma_pagamento)
             $("#id_pagamento_set-"+i+"-valor").val(valor)
             $("#id_pagamento_set-"+i+"-descricao").val(descricao)
 

            data.setMonth(data.getMonth()+1);
       }


     
    })
})