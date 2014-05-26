$(document).ready(function() {

	var preguntes = document.getElementsByClassName('preguntes');
	var enunciatPreguntes = new Array();
	for(a = 0;a<preguntes.length;a++){
		enunciatPreguntes.push(preguntes.innerHTML);
	}
	
	masculins = new Array();
	var idPreguntes = new Array();
	femenins = new Array();

	$('#preguntes').empty();
	$('#taulaResultats').hide();

	/*
	 * Guardar les dades correctes
	 */
	for ( i = 0; i < preguntes.length; i++) {
		//Agafar el primer exercici
		p = preguntes[i].innerHTML;
		var preguntetes = new Array();
		idPreguntes.push(preguntes[i].id);
		for ( g = 0; g < p.length; g++) {
			preguntetes = p.split(".");
		}
		//Cada exercici té diferents "lletres" (a,b,c...)
		for ( j = 0; j < preguntetes.length - 1; j++) {
			//Ara cada "frase" s'ha de diferenciar la part masculina de la femenina
			pregunta = preguntetes[j].split("|");
			masculi = pregunta[0].trim();
			femen = new Array();
			//Si hi ha alguna cosa vol dir que hi ha més d'una opcio de femeni'
			if (pregunta[1].indexOf(",") != -1) {
				pregunta[1] = pregunta[1].trim();
				f = pregunta[1].split(",");
				for ( h = 0; h < f.length; h++) {
					femen.push(f[h].trim());
				}
			} else {
				femen.push(pregunta[1].trim());
			}
			masculins.push(masculi);
			femenins.push(femen);
		}
	}
	//ES GUARDEN BE
	/*
	 * Generar inputs
	 */
	for ( p = 0; p < enunciatPreguntes.length; p++) {
		alert(p);
		//Genero un p per cada pregunta
		$('#preguntes').append("<p id='p" + p + "'class='list-group-item-info list-group-item'>Emplena els buits</p>");
		//"<p class='preguntes list-group-item text-justify' id='" + idPreguntes[p] + "'>fff</p>");

		/*for(i=0;i<masculins.length;i++){
		 //Per cada masculi creo un span i l'id serà la posició que té a l'array per poder corregir
		 $('#'+idPreguntes[p]).append("<span id='"+i+"'>"+masculins[i]+"</span>");
		 }*/
	}
	
	
	
	
	
	$('#validarPreguntes').click(function() {
		res = document.getElementsByClassName('resposta');
		//Array de totes les respostes de l'suauri
		respostesUsuari = new Array();
		for ( i = 0; i < res.length; i++) {
			respostesUsuari.push(res[i].value.trim());
		}
		console.log(respostesUsuari);
	});

});
