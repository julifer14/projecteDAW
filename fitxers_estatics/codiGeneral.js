function validarDades(){
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
		$.ajax({
			
		});
	});
});

