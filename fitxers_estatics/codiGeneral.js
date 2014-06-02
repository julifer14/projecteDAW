$(document).ready(function() {
	$('.taulaResultats').hide();
	$('.twitter').hide();
	$('#afegirTema').click(function() {
		$.ajax({

			type : "POST",
			url : "/preguntes/crearTema",
			dataType : 'json',
			data : {
				'csrfmiddlewaretoken' : $.cookie("csrftoken"),
				'nom' : $('#id_nom').val(),
			},
			success : function(data, page) {
				//console.log("sss" + json);
				//$('#message').html("<h2>Form Submitted!</h2>");
				temet = JSON.stringify(data,['id','nom']);
				var objec = $.parseJSON(temet);
				$('#id_tema').append('<option value="'+objec.id+'">'+objec.nom+'</option');
			},
			error : function(xhr, errmsg, err) {
				alert(xhr.status + ": " + xhr.responseText);
			}
		});

	});
	    

});

/*
 * Marca pregunta erronia
 */
function marcarIncorrecte(idPreg){
	$.ajax({
			type : "POST",
			url : "/preguntes/preguntesIncorrectes",
			dataType : 'json',
			data : {
				'csrfmiddlewaretoken' : $.cookie("csrftoken"),
				'pregunta' : idPreg,
			},
			success : function(data, page) {
			},
			error : function(xhr, errmsg, err) {
				alert(xhr.status + ": " + xhr.responseText);
			}
		});
}

/*
 * Validar preguntes
 */
function validarPreguntes(idPreg){
	inputets = $('#'+idPreg+'>p>input');
	respostesUsuari = "";
	for(i=0;i<inputets.length;i++){
		respostesUsuari = respostesUsuari+","+inputets[i].value.trim();
	}
	respostesUsuari = respostesUsuari.substr(1);
	$.ajax({
			type : "POST",
			url : "/preguntes/afegirResposta",
			dataType : 'json',
			data : {
				'csrfmiddlewaretoken' : $.cookie("csrftoken"),
				'idPregunta' : idPreg,
				'respostes' : respostesUsuari,
			},
			success : function(data, page) {
				notes = JSON.stringify(data,['idPregunta','nota','correctes','incorrectes']);
				var objec = $.parseJSON(notes);
				$('#nota'+objec.idPregunta).text(objec.nota);
				$('#correctes'+objec.idPregunta).text(objec.correctes);
				$('#incorrectes'+objec.idPregunta).text(objec.incorrectes);
				//$('.resposta').attr('disabled', 'disabled');
				$('#'+objec.idPregunta+'>p>input').attr('disabled', 'disabled');
				$('#taulaResultats'+objec.idPregunta).show();
				$('#'+objec.idPregunta+'>p>span>#valid'+objec.idPregunta).attr('class', 'disabled btn col-md-offset-2 btn-sm btn-info butonet  validarPreguntes');
				
				$('#twitter'+objec.idPregunta).show();
			},
			error : function(xhr, errmsg, err) {
				//alert(xhr.status + ": " + xhr.responseText);
			}
		});
	
}
