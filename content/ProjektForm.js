

var create = document.getElementById("create");

create.addEventListener("click", function(){
	var anzahl = parseInt(document.getElementById("bearbeitungszeitraum_s").value,10);
	var container=document.getElementById("contain");
	while(container.hasChildNodes()){
		container.removeChild(container.lastChild);
	}
	for (var x=0; x < anzahl-1; x++){
		var input=document.createElement("input");
		input.type="number";
		input.setAttribute('placeholder','Die Aufwendung je Woche');
		input.setAttribute("name", "aufwendung_${i}_" + x );
		input.classList.add("input_number");
		container.appendChild(input);
		container.appendChild(document.createElement("br"));


	}
});



//for (var i=0; i<anzahl; i++){

//}

