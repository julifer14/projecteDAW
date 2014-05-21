/*$(document).ready(function(){
 preguntes = $('.preguntes');
 alert(preguntes.length);
 for(i=0;i<preguntes.length;i++){
 pregunta = preguntes[i].value;
 alert(pregunta);

 }

 });

 *
 *
 * */
window.onload = transformarText();

function transformarText() {
	var preguntetes = new Array();
	preguntes = document.getElementsByClassName('preguntes');
	for ( i = 0; i < preguntes.length; i++) {
		preguntetes.push(preguntes[i].innerHTML);
	}
	//Un cop tinc les frases les esborro
	$('#preguntes').empty();
comptador = 1;
	for ( i = 0; i < preguntetes.length; i++) {
		pregunta = preguntetes[i];
		alert(pregunta);
		resultat = new Array();
		variable = "";
		comenca = false;
		
		acabat = true;
		$('#preguntes').append("<p class='preguntes list-group-item text-center' id='" + comptador + "'>");
		for ( j = 0; j < pregunta.length; j++) {

			if (pregunta[j] == "[") {
				comenca = true;
			}

			
			if (comenca==true) {
				$('#' + comptador).append("<span>" + variable + "</span>");
				acabat = false;
				comenca = false;
				variable = "";
			}
			if (comenca == false) {
				if (acabat == true) {
					console.log(variable);
					variable = variable + pregunta[j];
				}
			}
			if (pregunta[j] == "]") {
				$('#'+comptador).append("<input type='text'>");
				acabat = true;
			}
		}
		comptador = comptador + 1;
	}
}
