window.onload = transformarText();

function transformarText() {
	var preguntetes = new Array();
	var idPreguntes = new Array();
	preguntes = document.getElementsByClassName('preguntes');
	for ( i = 0; i < preguntes.length; i++) {
		idPreguntes.push(preguntes[i].id);
		preguntetes.push(preguntes[i].innerHTML);
	}
	//Un cop tinc les frases les esborro
	$('#preguntes').empty();
	comptador = 1;
	for ( i = 0; i < preguntetes.length; i++) {
		pregunta = preguntetes[i];
		//alert(pregunta);
		resultat = new Array();
		variable = "";
		comenca = false;
		resposta = "";
		acabat = true;
		
		$('#preguntes').append("<p id='"+i+"'class='list-group-item'>Emplena els buits</p><p class='preguntes list-group-item text-center' id='" + idPreguntes[i] + "'>");
		for ( j = 0; j < pregunta.length; j++) {

			if (pregunta[j] == "[") {
				comenca = true;
			}

			
			if (comenca==true) {
				$('#' + idPreguntes[i]).append("<span>" + variable + "</span>");
				acabat = false;
				comenca = false;
				variable = "";
			}
			if (comenca == false) {
				if (acabat == true) {
					//console.log(variable);
					variable = variable + pregunta[j];
				}
			}
			if(acabat == false){
				resposta = resposta+pregunta[j];
			}
			if (pregunta[j] == "]") {
				$('#'+idPreguntes[i]).append("<input class='resposta' type='text'>");
				acabat = true;
			}
		}
		$('#' + idPreguntes[i]).append("<span>" + variable + "</span>");
		//alert(resposta);
	}
}
