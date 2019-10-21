var manual = false;
var camara = false;
var porta = false;
var incandescente = false;

function automaticoManual(){
	if(manual){
		httpGet("/api/v1/galineiro/desactivar_manual", function(jsonObj){
			if(jsonObj.manAuto){
				document.getElementById("btnAccionManual").style.borderColor = "black";
				document.getElementById("btnAccionManual").innerHTML = "Activar Manual";
				document.getElementById("btnAccionPortal").style.borderColor = "grey";
				document.getElementById("btnAccionPortal").disabled = true;
				manual = false;
			}
		});
	}
	else{
		httpGet("/api/v1/galineiro/parametros", function(jsonObj){
			document.getElementById("btnAccionPortal").style.borderColor = "grey";
			if(jsonObj.porta){
				document.getElementById("btnAccionPortal").innerHTML = "Cerrar Porta";
				porta = true;
			}
			else {
				document.getElementById("btnAccionPortal").innerHTML = "Abrir Porta";
				porta = false;
			}

			httpGet("/api/v1/galineiro/activar_manual", function(jsonObj){
				if(jsonObj.manAuto){
					document.getElementById("btnAccionManual").style.borderColor = "blue";
					document.getElementById("btnAccionManual").innerHTML = "Desactivar Manual";
					if(porta) {
						document.getElementById("btnAccionPortal").style.borderColor = "blue";
					}
					else{
						document.getElementById("btnAccionPortal").style.borderColor = "black";
					}
					document.getElementById("btnAccionPortal").disabled = false;
					manual = true;
				}
				else{
					document.getElementById("msg").innerHTML = "Operario Traballando!";
    				document.getElementById("informacion").style.display = "block";
    				setTimeout(function() {
    					document.getElementById("informacion").style.display = "none";
    				}, 2000);
				}
			});
		});
	}
}

function abrirCerrarPortal(){
	document.getElementById("btnAccionPortal").style.background = "yellow";
	if(porta){
		httpGet("/api/v1/galineiro/pechar_porta", function(jsonObj){
			document.getElementById("btnAccionPortal").style.background = "white";
			if(jsonObj.codigo){
				document.getElementById("msg").innerHTML = "Porta pechada";
				document.getElementById("informacion").style.display = "block";
				document.getElementById("btnAccionPortal").style.borderColor = "black";
				document.getElementById("btnAccionPortal").innerHTML = "Abrir Porta";
				setTimeout(function() {
					document.getElementById("informacion").style.display = "none";
				}, 2000);

				porta = false;
			}
			else{
				document.getElementById("msg").innerHTML = "Operario Traballando!";
				document.getElementById("informacion").style.display = "block";
				setTimeout(function() {
					document.getElementById("informacion").style.display = "none";
				}, 2000);
			}
		}, function(){
			document.getElementById("btnAccionPortal").style.background = "white";
			msgError();
		});
	}
	else{
		httpGet("/api/v1/galineiro/abrir_porta", function(jsonObj){
			document.getElementById("btnAccionPortal").style.background = "white";
			if(jsonObj.codigo){
				document.getElementById("informacion").style.display = "block";
				document.getElementById("msg").innerHTML = "Porta aberta";

				document.getElementById("btnAccionPortal").style.borderColor = "blue";
				document.getElementById("btnAccionPortal").innerHTML = "Cerrar Porta";
				setTimeout(function() {
					document.getElementById("informacion").style.display = "none";
				}, 2000);

				porta = true;
			}
			else{
				document.getElementById("btnAccionPortal").style.background = "";
				document.getElementById("msg").innerHTML = "Operario Traballando!";
				document.getElementById("informacion").style.display = "block";
				setTimeout(function() {
					document.getElementById("informacion").style.display = "none";
				}, 2000);
			}
		}, function(){
			document.getElementById("btnAccionPortal").style.background = "white";
			msgError();
		});
	}
}

function obterImaxe(){
	httpGet("/api/v1/galineiro/sacar_foto", function(jsonObj){
		var data = jsonObj.data.substr(2, jsonObj.data.length - 3);
		document.getElementById("imaxeCamara").src = "data:image/png;base64," + data;
		if(camara){
			obterImaxe();
		}
	}, function(){
		document.getElementById("imaxeCamara").style.display = "none";
		document.getElementById("encenderApagarCamara").style.borderColor = "black";
		document.getElementById("encenderApagarCamara").innerHTML = "Enceder Camara";
		document.getElementById("imaxeCamara").style.display = "none";
		document.getElementById("msg").innerHTML = "Erro de comunicación!";
    	document.getElementById("informacion").style.display = "block";
    	setTimeout(function() {
    		document.getElementById("informacion").style.display = "none";
    	}, 2000);

    	httpGet("/api/v1/galineiro/apagar_luz", function(jsonObj){
				document.getElementById("incandescente").style.backgroundColor = "gray";
				incandescente = false;
    	});

    	camara = false;
	});
}

function encenderApagarCamara(){
	if(camara){
		document.getElementById("encenderApagarCamara").style.borderColor = "black";
		document.getElementById("encenderApagarCamara").innerHTML = "Enceder Camara";
		document.getElementById("imaxeCamara").style.display = "none";

		httpGet("/api/v1/galineiro/apagar_luz", function(jsonObj){
			document.getElementById("incandescente").style.backgroundColor = "gray";
			incandescente = false;
		});

		camara = false;
	}
	else{
		httpGet("/api/v1/galineiro/encender_luz", function(jsonObj){
			document.getElementById("encenderApagarCamara").style.borderColor = "blue";
			document.getElementById("encenderApagarCamara").innerHTML = "Apagar Camara"
			document.getElementById("imaxeCamara").style.display = "block";
			document.getElementById("incandescente").style.backgroundColor = "yellow";

			obterImaxe();

			incandescente = true;
			camara = true;
    	}, function(){
    		document.getElementById("msg").innerHTML = "Erro de comunicación!";
    		document.getElementById("informacion").style.display = "block";

    		setTimeout(function() {
    			document.getElementById("informacion").style.display = "none";
    		}, 	10000);
    	});
	}
}

function actualizarGalineiro(){
	httpGet("/api/v1/galineiro/parametros", function(jsonObj){
			if(jsonObj.manAuto){
				document.getElementById("btnAccionManual").style.borderColor = "blue";
				document.getElementById("btnAccionManual").innerHTML = "Desactivar Manual";
				document.getElementById("btnAccionPortal").disabled = false;

				if(jsonObj.porta){
					document.getElementById("btnAccionPortal").style.borderColor = "blue";
					document.getElementById("btnAccionPortal").innerHTML = "Cerrar Porta";
					porta = true;
				}
				else {
					document.getElementById("btnAccionPortal").style.borderColor = "black";
					document.getElementById("btnAccionPortal").innerHTML = "Abrir Porta";
					porta = false;
				}

				manual = true;
			}
			else{
				document.getElementById("btnAccionManual").innerHTML = "Activar Manual";
				document.getElementById("btnAccionManual").style.borderColor = "black";
				document.getElementById("btnAccionPortal").disabled = true;
				document.getElementById("btnAccionPortal").style.borderColor = "grey";

				if(jsonObj.porta){
					document.getElementById("btnAccionPortal").innerHTML = "Cerrar Porta";
					porta = true;
				}
				else {
					document.getElementById("btnAccionPortal").innerHTML = "Abrir Porta";
					porta = false;
				}

				manual = false;
			}

			if(jsonObj.incandescente){
				document.getElementById("incandescente").style.backgroundColor = "yellow";
				incandescente = true;
			}
			else {
				document.getElementById("incandescente").style.backgroundColor = "gray";
				incandescente = false;
			}
		});
}
