var rows = document.querySelectorAll("#myTable tr");
var bearbeitenmitarbeiter = document.getElementById("bearbeitenmitarbeiter");
var deletemitarbeiter = document.getElementById("deletemitarbeiter");

for (var i=1; i < rows.length; i++){

	rows[i].addEventListener('click', function(){
		[].forEach.call(rows,function(el){
			//alert(rows[i]);
			el.classList.remove("highlight");
		});
		this.className += 'highlight';
	},false);
}

bearbeitenmitarbeiter.addEventListener("click", function(){
	var elx_o = document.querySelector(".highlight");
	if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } 
         else{
         	var d = document.getElementById("bearbeitenmitarbeiter");
         	alert("/editMitarbeiter/"+elx_o.id);
         	d.setAttribute("href", "/editMitarbeiter/"+elx_o.id); 
         }
});

deletemitarbeiter.addEventListener("click",function(){
	var elx_o = document.querySelector(".highlight");
	if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } 
         else{
         	var loschen = document.getElementById("deletemitarbeiter");
         	alert("/deleteMitarbeiter/"+elx_o.id);
         	loschen.setAttribute("href", "/deleteMitarbeiter/"+elx_o.id); 
         }
});