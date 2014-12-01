function callDatabase(UserAnime)
{
	var debug =0;
	var hostname = document.location.origin;
	var folder_path = document.location.pathname;
	temp = folder_path.lastIndexOf("/");
	folder_path = folder_path.substr(0, temp+1);
	$.ajax({
	   url: hostname+folder_path+"../py/app.py",
	    type: "POST",
	    data: {"UserAnime": JSON.stringify(UserAnime)},
	    //dataType: 'json',
	    success: function(response){
	       console.log("Sucess");
	       if (debug) document.write(response);
	       if(response != null)
	       {
	       	relevantNewAnime=JSON.stringify(response)
//	       	PopulateWithAnimeData(relevantNewAnime);
	       }
	       
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
	   url: hostname+folder_path+"../py/monodb/save.py", ///monodb/save.py
	    type: "POST",
	    data: {"RetrievedAnime": JSON.stringify(RetrievedAnime)},
	    success: function(response){
	       console.log("Sucess");
	      if(response == "Db created succesfully")
		alert(response);
	      else
		{
			alert("error/duplicates check console.log for details");
			console.log(response);
		}
	       
	   }
	});
        
}

