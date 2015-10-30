
function changeUF(the_select){

        var uf = the_select.options[the_select.selectedIndex].value;      
	var uf_input_name = the_select.name;
	var uf_input_id = the_select.id;

        var municipio_input_name = uf_input_name.replace("uf","municipio");
	var municipio_input_id = uf_input_id.replace("uf","municipio");




       
	if(uf!="")
        {
        
           
            $("#"+municipio_input_id).attr('disabled', true).html('<option value="">Aguarde...</option>');
            $("#"+municipio_input_id).load('/municipios_app/ajax/municipios/'+uf+'/', null, function(){
                $("#"+municipio_input_id)[0].disabled=false;
            });
            $("#"+municipio_input_id).html('<option value="">--</option>');

	} 
        else
        {
		$("#"+municipio_input_id).html('<option value="">--</option>');
		$("#"+municipio_input_id).html("--");
	}
}
