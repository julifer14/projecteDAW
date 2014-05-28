/*function validarDades(){
 numPreguntes = document.getElementsByClassName('preguntes').length;
 //alert("Hi han " + numPreguntes + " preguntes");
 respostes = document.getElementsByClassName('resposta');
 respostetes = new Array();
 for ( i = 0; i < respostes.length; i++) {
 respostetes.push(respostes[i].value);
 }
 console.log(respostetes);
 }

 $(document).ready(function(){
 $('#validarPreguntes').click(function(){

 });
 });*/
$(document).ready(function() {
	$('#afegirTema').click(function() {
		console.log($('#id_nom').val());
		$.ajax({
			
			type : "POST",
			url : "/preguntes/crearTema",
			dataType : 'json',
			data : {
				'csrfmiddlewaretoken' : $.cookie("csrftoken"),
				'nom' : $('#id_nom').val(),
			},
			success : function(json) {
				//console.log("sss" + json);
				//$('#message').html("<h2>Form Submitted!</h2>");
			},
			error : function(xhr, errmsg, err) {
				alert(xhr.status + ": " + xhr.responseText);
			}
		});

	});
});
