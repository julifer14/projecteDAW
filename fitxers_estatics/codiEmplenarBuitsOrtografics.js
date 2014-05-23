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
	comptador = 1;
	for ( i = 0; i < preguntetes.length; i++) {
		pregunta = preguntetes[i];
		//alert(pregunta);
		resultat = new Array();
		variable = "";
		comenca = false;
		resposta = "";
		acabat = true;

		$('#preguntes').append("<p id='" + i + "'class='list-group-item'>Emplena els buits</p><p class='preguntes list-group-item text-center' id='" + idPreguntes[i] + "'>");
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
			respostesUsuari.push($.trim(res[i].value.trim()));
		}
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
					console.log(respostes[r][e] + " "+ respostesUsuari[comptador]);
					correctes++;
				}else{
					console.log("-----incorrecte");
					console.log(respostes[r][e] +" - " +respostesUsuari[comptador]);
				}
				console.log("--------------------------");
				comptador++;
			}
		}
		nota = 0;
		if(correctes == 0){
			nota=trun(0);
		}else if(comptador>correctes&&correctes!=0){
			nota=trunc(10-(eval(comptador/correctes)));
		}else{
			nota=(trunc(10));
		}
		
		alert(nota);
		

	});
});

function trunc(num) {
	num = num * 100;
	num = Math.floor(num);
	num = num / 100;
	return num;
}

