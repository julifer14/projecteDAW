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
	$('.taulaResultats').hide();
	
	$('#afegirTema').click(function() {
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
				//alert(xhr.status + ": " + xhr.responseText);
			}
		});

	});
	/*
	 * Gràfic per pregunta
	 */
	$(function () {
        $('#container').highcharts({
            title: {
                text: 'Average Temperature',
                x: -20 //center
            },
            subtitle: {
                text: 'Source: WorldClimate.com',
                x: -20
            },
            xAxis: {
                categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            },
            yAxis: {
                title: {
                    text: 'Temperature (°C)'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: '°C'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Tokyo',
                data: ['7.0', 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
            }, {
                name: 'New York',
                data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
            }, {
                name: 'Berlin',
                data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
            }, {
                name: 'London',
                data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
            }]
        });
    });
    

});

/*
 * Validar preguntes
 */
function validarPreguntes(idPreg){
	inputets = $('#'+idPreg+'>p>input');
	respostesUsuari = "";
	for(i=0;i<inputets.length;i++){
		respostesUsuari = respostesUsuari+","+inputets[i].value.trim();
	}
	respostesUsuari = respostesUsuari.substr(1);
	$.ajax({
			type : "POST",
			url : "/preguntes/afegirResposta",
			dataType : 'json',
			data : {
				'csrfmiddlewaretoken' : $.cookie("csrftoken"),
				'idPregunta' : idPreg,
				'respostes' : respostesUsuari,
			},
			success : function(data, page) {
				notes = JSON.stringify(data,['idPregunta','nota','correctes','incorrectes']);
				var objec = $.parseJSON(notes);
				$('#nota'+objec.idPregunta).text(objec.nota);
				$('#correctes'+objec.idPregunta).text(objec.correctes);
				$('#incorrectes'+objec.idPregunta).text(objec.incorrectes);
				//$('.resposta').attr('disabled', 'disabled');
				$('#'+objec.idPregunta+'>p>input').attr('disabled', 'disabled');
				$('#taulaResultats'+objec.idPregunta).show();
				$('#'+objec.idPregunta+'>button').attr('class', 'disabled btn  btn-info col-md-3 col-md-offset-5 validarPreguntes');
						
			},
			error : function(xhr, errmsg, err) {
				alert(xhr.status + ": " + xhr.responseText);
			}
		});
	
}
