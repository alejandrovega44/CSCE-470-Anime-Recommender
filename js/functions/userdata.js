// function that gets users anime list from animelist
//parammeters are the username and a function
//return values
//the function will be preformmed if the call is done sucessfully and data is retrieved.
function getUserList(username, callback)
{
	url="http://myanimelist.net/malappinfo.php?u="+username +"&status=all&type=anime";
	query ='select * from xml where url="'+url+'"';
	 var yqlAPI = 'https://query.yahooapis.com/v1/public/yql?q=' + encodeURIComponent(query) + ' &format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=?';

	$.getJSON(yqlAPI, function(){
	      //console.log("sucess");
	  })
	.success(function(r){
	  console.log("sucess")
	  //console.log(r.query.results);
	  if (typeof r.query.results.myanimelist == 'undefined') 
	  {
	  	//add throw an error
	  	console.log("returned null: data wasn't found for specific user")
	  }
	  else
	  	callback(r.query.results.myanimelist)
	  
	})  
	.fail(function(r){
	  console.log("fail");
	  console.log(r);
	});

}
//function will recursively create a list of all the animes the user watches
//takes an in array of animenames that has been formated for the call
//callback function that will taken in all the data
function RetrieveAnimeData(ArrayAnimeNames,callback)
{
	
	if ($.isArray(ArrayAnimeNames))
	{

	}
	else
		getAnimeData(ArrayAnimeNames,callback);

}

//function that will retrieve more detail information for each anime
//a string with the names of animes alrady formated for this specific api call
//a callback function
//and when its done doing all calls send the data to call back function
//returns the data
function getAnimeData(animelist, callback)
{
	var debug=1;
	//http://goessner.net/download/prj/jsonxml/
	url="http://cdn.animenewsnetwork.com/encyclopedia/api.xml?"+animelist;
	 if(debug)console.log(animelist);
	/*$.getJSON(url, function(){
	      //console.log("sucess");
	  })*/
	var request = $.ajax({
    url: url,
    type: 'GET',
    dataType: 'xml',
	});
	request.success(function(r){
	  console.log("sucess")
  	  if (r == null) 
	  {
	  	//add throw an error
	  	console.log("returned null: data wasn't found for specific anime/s")
	  }
	  else
	  {
	  	if(debug) console.log(r);
		if(debug) console.log(xmlToJson(r));
	  	callback(xmlToJson(r).ann)
	  }
	  
	})  
	request.fail(function(r){
	  console.log("fail");
	  console.log(r);
	});

}
function Create_UserAnime_Objects(animelist)
{
	var objects={};
	$.each(animelist,function(){
		 var temp={};
		 temp.a_name =this["@attributes"].name;
		 temp.desc =RetrieveDesc(this["info"]) ;
		 
		 if(typeof this["credit"].company == "Object") 
		 	temp.company =this["credit"].company["#text"]; 
		 //have to account for mutiple companies
		  temp.ppl=RetrieveStaff(this["staff"]);
		  temp.userRating =this.rating;
		  temp.a_genres =RetrieveGenre(this["info"]);
		  objects[temp.a_name]= temp;
	});
		return objects;
}