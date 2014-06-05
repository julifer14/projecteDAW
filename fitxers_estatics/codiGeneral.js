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
				temet = JSON.stringify(data, ['id', 'nom']);
				var objec = $.parseJSON(temet);
				$('#id_tema').append('<option value="' + objec.id + '">' + objec.nom + '</option');
			},
			error : function(xhr, errmsg, err) {
				//alert(xhr.status + ": " + xhr.responseText);
			}
		});

	});

	$("#id_tipus").change(function() {
		var opcioTipus = "";
		$("#id_tipus option:selected").each(function() {
			opcioTipus += $(this).text() + " ";
		});
		//alert(opcioTipus);
		text = "";
		if(opcioTipus == "EmplenarBuitsOrtografics" ){
			text = "Exemple: La [v]ca menja her[b]a. El [b]ambú és [v]erd.";
		}else{
			text = "Exemple: Joan - [Joana]."+
							 "Senyor - [Senyora][Senyoreta]";
		}
		$('#textModalTipus').text(text);
		
	}).change();

});

/*
 * Marca pregunta erronia
 */
function marcarIncorrecte(idPreg) {
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
			$('#repor' + idPreg).hide();
			//alert(xhr.status + ": " + xhr.responseText);
		}
	});
}

/*
 * Si la notificació es incorrecte, es treuen de la BDD les entrades referents a la pregunta
 */

function treureNotificacio(idPreg) {
	$.ajax({
		type : "POST",
		url : "/preguntes/eliminarNotificacio",
		dataType : 'json',
		data : {
			'csrfmiddlewaretoken' : $.cookie("csrftoken"),
			'idPregunta' : idPreg,

		},
		success : function(data, page) {

		},
		error : function(xhr, errmsg, err) {
			$('#preg' + idPreg).remove();
			//alert(xhr.status + ": " + xhr.responseText);
		}
	});
}

/*
 * Corregeix la pregunta (envia a la servidor la nova versió)
 */
function corregirPreguntaInc(idPreg) {
	//alert(idPreg);
	alert('Proximament');
	//txt = $('#'+idPreg).val();
	//alert(txt);
	//console.log(respostesUsuari);

	/*$.ajax({
	 type : "POST",
	 url : "/preguntes/modificarPregunta",
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
	 });*/

}

/*
 * Validar preguntes
 */
function validarPreguntes(idPreg) {
	inputets = $('#' + idPreg + '>p>input');
	respostesUsuari = "";
	for ( i = 0; i < inputets.length; i++) {
		respostesUsuari = respostesUsuari + "," + inputets[i].value.trim();
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
			notes = JSON.stringify(data, ['idPregunta', 'nota', 'correctes', 'incorrectes']);
			var objec = $.parseJSON(notes);
			$('#nota' + objec.idPregunta).text(objec.nota);
			$('#correctes' + objec.idPregunta).text(objec.correctes);
			$('#incorrectes' + objec.idPregunta).text(objec.incorrectes);
			//$('.resposta').attr('disabled', 'disabled');
			$('#' + objec.idPregunta + '>p>input').attr('disabled', 'disabled');
			$('#taulaResultats' + objec.idPregunta).show();
			$('#' + objec.idPregunta + '>p>span>#valid' + objec.idPregunta).attr('class', 'disabled btn col-md-offset-2 btn-sm btn-info butonet  validarPreguntes');

			$('#twitter' + objec.idPregunta).show();
		},
		error : function(xhr, errmsg, err) {
			//alert(xhr.status + ": " + xhr.responseText);
		}
	});
}
