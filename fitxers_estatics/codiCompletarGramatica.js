window.onload = transformarText();

function transformarText() {

	preguntes = document.getElementsByClassName('preguntes');
	for ( i = 0; i < preguntes.length; i++) {
		//Agafar el primer exercici
		p = preguntes[i].innerHTML;
		var preguntetes = new Array();
		var idPreguntes = new Array();
		for ( g = 0; g < p.length; g++) {
			preguntetes = p.split(".");
		}
		//Cada exercici té diferents "lletres" (a,b,c...)
		for ( j = 0; j < preguntetes.length - 1; j++) {
			//Ara cada "frase" s'ha de diferenciar la part masculina de la femenina
			pregunta = preguntetes[j].split("|");
			masculi = pregunta[0].trim();
			femenins = new Array();
			//Si hi ha alguna cosa vol dir que hi ha més d'una opcio de femeni'
			if (pregunta[1].indexOf(",") != -1) {
				pregunta[1] = pregunta[1].trim();
				f = pregunta[1].split(",");
				for ( h = 0; h < f.length; h++) {
					femenins.push(f[h].trim());
				}
			} else {
				femenins.push(pregunta[1].trim());
			}
			
			console.log(masculi);
			for ( q = 0; q < femenins.length; q++) {
				console.warn(femenins[q]);
			}
			console.log(".-----.");
		}

	}
}