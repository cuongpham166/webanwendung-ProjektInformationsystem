var rows = document.querySelectorAll("#myTable tr");
var bearbeitenkunden = document.getElementById("bearbeitenkunden");
var deletekunden = document.getElementById("deletekunden");

for (var i=1; i < rows.length; i++){

	rows[i].addEventListener('click', function(){
		[].forEach.call(rows,function(el){
			//alert(rows[i]);
			el.classList.remove("highlight");
		});
		this.className += 'highlight';
	},false);
}

bearbeitenkunden.addEventListener("click", function(){
	var elx_o = document.querySelector(".highlight");
	if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } 
         else{
         	var d = document.getElementById("bearbeitenkunden");
         	alert("/editKunden/"+elx_o.id);
         	d.setAttribute("href", "/editKunden/"+elx_o.id); 
         }
});

deletekunden.addEventListener("click",function(){
	var elx_o = document.querySelector(".highlight");
	if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } 
         else{
         	var loschen = document.getElementById("deletekunden");
         	alert("/deleteKunden/"+elx_o.id);
         	loschen.setAttribute("href", "/deleteKunden/"+elx_o.id); 
         }
});

