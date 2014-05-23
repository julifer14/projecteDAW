var preguntetes = new Array();
var idPreguntes = new Array();
var respostes = new Array();
$(document).ready(function() {
	
	/*
	 * ******************Generar inputs**************************
	 */
	preguntes = document.getElementsByClassName('preguntes');
	for ( i = 0; i < preguntes.length; i++) {
		idPreguntes.push(preguntes[i].id);
		preguntetes.push(preguntes[i].innerHTML);
	}
	//Un cop tinc les frases les esborro
	$('#preguntes').empty();
	$('#taulaResultats').hide();
	comptador = 1;
	for ( i = 0; i < preguntetes.length; i++) {
		pregunta = preguntetes[i];
		//alert(pregunta);
		resultat = new Array();
		variable = "";
		comenca = false;
		resposta = "";
		acabat = true;

		$('#preguntes').append("<p id='" + i + "'class='list-group-item'>Emplena els buits</p><p class='preguntes list-group-item text-justify' id='" + idPreguntes[i] + "'>");
		for ( j = 0; j < pregunta.length; j++) {

			if (pregunta[j] == "[") {
				comenca = true;
			}

			if (comenca == true) {
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
			if (acabat == false) {
				resposta = resposta + pregunta[j];
			}
			if (pregunta[j] == "]") {
				$('#' + idPreguntes[i]).append("<input class='resposta' type='text'>");
				acabat = true;
			}
		}
		$('#' + idPreguntes[i]).append("<span>" + variable + "</span>");
		respostes.push(resposta);
	}
	
	/*
	 * ********************************************
	 */
	
	
	
	$('#validarPreguntes').click(function() {
		res = document.getElementsByClassName('resposta');
		//Array de totes les respostes de l'suauri
		respostesUsuari = new Array();
		for ( i = 0; i < res.length; i++) {
			respostesUsuari.push(res[i].value.trim());
		}
		console.log(res);
		/*
		 * Primer preparem l'array de respostes que haviem guardat abans
		 */
		for(i= 0; i<respostes.length;i++){
			respostesCorrectes = respostes[i].split("]");
			
			for(j=0;j<respostesCorrectes.length;j++){
				if(respostesCorrectes[j] != ""){
					respostesCorrectes[j] = respostesCorrectes[j].substr(1);
				}
			}
			respostes[i] = respostesCorrectes;
		}
		//console.log(respostes);
		correctes = 0;
		comptador = 0;
		for(r = 0;r<respostes.length;r++){
			for(e = 0; e<respostes[r].length-1;e++){
				if(respostes[r][e]== respostesUsuari[comptador]){
					console.log("correcte");
					console.log(res);
					console.log(respostes[r][e] + " "+ respostesUsuari[comptador]);
					correctes++;
				}else{
					
					console.log("-----incorrecte");
					console.log(res);
					console.log(respostes[r][e] +" - " +respostesUsuari[comptador]);
				}
				console.log("--------------------------");
				comptador++;
			}
		}
		nota = 0;
		notaPregunta = 10/comptador;
		nota=trunc(correctes*notaPregunta);
	
		$('.resposta').attr('disabled','disabled');
		$('#taulaResultats').show();
		$('#nota').text(nota);
		$('#correctes').text(correctes);
		$('#incorrectes').text(comptador-correctes);
		$('#validarPreguntes').attr('class','disabled btn btn-lg btn-info col-md-2 col-md-offset-5');
		
		/*$.ajax({
                 type:"POST",
                 url:"/preguntes/",
                 data: {
                        'video': $('#test').val() // from form
                        },
                 success: function(){
                     $('#message').html("<h2>Contact Form Submitted!</h2>") 
                 }
            });*/
		
	});
});

function trunc(num) {
	num = num * 100;
	num = Math.floor(num);
	num = num / 100;
	return num;
}

