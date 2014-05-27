$(document).ready(function() {

	var preguntes = document.getElementsByClassName('preguntes');
	//Cada pregunta el numero d'apartats que té
	var apartatsPerPregunta = new Array();
	//Enunciat de les preguntes masculi | femeni
	var enunciatPreguntes = new Array();
	//L\'id de cada pregunta amb sintonia amb l'array d\'enunciats
	var idPreguntes = new Array();
	//Tots els masculins del exercici (els que es mostren)
	masculins = new Array();
	//Tots els femenins (els no es mostren), util per a corregir
	femenins = new Array();

	for ( a = 0; a < preguntes.length; a++) {

		enunciatPreguntes.push(preguntes[a].innerHTML);
		idPreguntes.push(preguntes[a].id);
		//console.log(enunciatPreguntes[a]);
	}

	$('#preguntes').empty();
	$('#taulaResultats').hide();

	/*
	 * Guardar les dades correctes
	 */
	for ( i = 0; i < enunciatPreguntes.length; i++) {
		//Agafar el primer exercici
		p = enunciatPreguntes[i];
		var preguntetes = new Array();
		preguntetes = p.split(".");
		apartatsPerPregunta.push(preguntetes.length);
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
	//ES GUARDEN BÉ
	/*
	 * Generar inputs
	 */
	var comptador = 0;
	for ( p = 0; p < enunciatPreguntes.length; p++) {
		//Genero un p per cada pregunta
		$('#preguntes').append("<p class='list-group-item-info list-group-item'>Completa amb la paraula o paraules que falten</p>" + "<p class='preguntes list-group-item text-justify' id='" + idPreguntes[p] + "'>");

		for ( i = 0; i < apartatsPerPregunta[p] - 1; i++) {
			//Per cada masculi creo un span i l'id serà la posició que té a l'array per poder corregir
			$('#' + idPreguntes[p]).append("<span>" + masculins[comptador] + "</span>");
			for ( j = 0; j < femenins[comptador].length; j++) {
				$('#' + idPreguntes[p]).append("<input class='resposta seguit' type='text' id='" + comptador + "-" + j + "'><br>");
			}
			comptador++;
		}

	}

	$('#validarPreguntes').click(function() {
		res = document.getElementsByClassName('resposta');
		console.log(res);
		comptador = 0;
		//de totes les variables corregire primer un exercici em quedo el valor d'elles i el comparo amb el correcte
		for ( i = 0; i < masculins.length; i++) {
			for ( j = 0; j < femenins[i].length; j++) {
				console.log(res[j].value.trim() + " - " + femenins[i][j]);	
				if (res[i].value.trim() == femenins[i][j]) {
					
				}
			}
		}

		//Array de totes les respostes de l'suauri
		/*var comptador = 0;
		 for ( p = 0; p < enunciatPreguntes.length; p++) {
		 respostesUsuari = new Array();
		 for ( i = 0; i < apartatsPerPregunta[p]; i++) {
		 respostesUsuari.push(res[comptador].value.trim());
		 comptador++;
		 }
		 console.log(respostesUsuari);
		 console.log("-------");
		 }*/
	});

});
