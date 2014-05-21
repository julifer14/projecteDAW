window.onload = transformarText();

function transformarText() {
	var preguntetes = new Array();
	var idPreguntes = new Array();
	preguntes = document.getElementsByClassName('preguntes');
	for ( i = 0; i < preguntes.length; i++) {
		p = preguntes[i].innerHTML;
		for(j=0;j<p.length;j++){
			preguntetes = p.split(".");
			
		
			//idPreguntes.push(preguntes[i].id);
			//preguntetes.push(preguntes[i].innerHTML);
		}
	}
	//tinc un array de preguntes gat | gata - gos | gossa
	for(i=0;i<preguntetes.length;i++){
		console.log(preguntetes[i]);
	}
	
	
	alert("completar gramatica");
}