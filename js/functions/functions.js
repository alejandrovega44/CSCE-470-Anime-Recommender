function callDatabase(UserAnime, RetrievedAnime)
{
	$.ajax({
	   url: "http://uakk632bb565.av512.koding.io/project/app.py",
	    type: "POST",
	    data: {"UserAnime": JSON.stringify(UserAnime), "RetrievedAnime": JSON.stringify(RetrievedAnime)},
	    success: function(response){
	       console.log("Sucess");
	       console.log(response);
	       //return an array containing the index's of the recommended anime from (RetrievedAnime)
	   }
	});
        
}