function callDatabase(UserAnime)
{
	var hostname = document.location.origin;
	var folder_path = document.location.pathname;
	temp = folder_path.lastIndexOf("/");
	folder_path = folder_path.substr(0, temp+1);
	$.ajax({
	   url: hostname+folder_path+"../py/app.py",
	    type: "POST",
	    data: {"UserAnime": JSON.stringify(UserAnime)},
	    success: function(response){
	       console.log("Sucess");
	       if(response != null)
	       {
	       	var temp=[];
	       	var self;
			console.log(response);
	       }
	       console.log(response);
	       
	   }
	});
        
}
//populate server with upcoming anime from ani chart
function PopulateDatabase(RetrievedAnime)
{
	var hostname = document.location.origin;
	var folder_path = document.location.pathname;
	temp = folder_path.lastIndexOf("/");
	folder_path = folder_path.substr(0, temp+1);

	$.ajax({
	   url: hostname+folder_path+"../php/save.php",
	    type: "POST",
	    data: {"RetrievedAnime": JSON.stringify(RetrievedAnime)},
	    success: function(response){
	       console.log("Sucess");
	      alert(response);
	       
	   }
	});
        
}

