function callDatabase(UserAnime, RetrievedAnime)
{
	var hostname = document.location.origin;
	var folder_path = document.location.pathname;
	temp = folder_path.lastIndexOf("/");
	folder_path = folder_path.substr(0, temp+1);

	console.log(hostname+folder_path+"app.py");
	$.ajax({
	   //url: "http://uakk632bb565.av512.koding.io/project/app.py",
	   url: hostname+folder_path+"app.py",
	    type: "POST",
	    data: {"UserAnime": JSON.stringify(UserAnime), "RetrievedAnime": JSON.stringify(RetrievedAnime)},
	    success: function(response){
	       console.log("Sucess");
	       //return an array containing the index's of the recommended anime from (RetrievedAnime)
	       if(response != null)
	       {
	       	var temp=[];
	       	var self;
	       	$.each(response,function(){
	       		self= this;
	       		$.each(RetrievedAnime,function(){
	       			if(this.i == self )
	       			{
	       				temp.push(this);
	       				return false;
	       			}
	       		});
	       	});
	       	PopulateWithAnimeData(temp);
	       }
	       console.log(response);
	       
	   }
	});
        
}