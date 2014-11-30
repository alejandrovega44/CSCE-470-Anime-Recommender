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

//function will do multiple calls to api to retrieve data for various animes
//will take an array of strings that contain title=~name 
//callback
function animeDataCalls(array_animetitles,callback)
{
	var apiCallData=[]; 
	if(array_animetitles.length == 1)
		callback(getAnimeData(array_animetitles[0]))
	else if (array_animetitles.length == 0) 
	{
		alert("User has not watched/rated any anime");
		
	}
	else
	{
		for (var i = 0; i < array_animetitles.length; i++) {
			getAnimeData(array_animetitles[i], function(r){
				apiCallData.push(r);
			});
		};
		callback(apiCallData); 
	}

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
		 if($.isArray(this["credit"]))
		 {
		 	temp.company =RetrieveCompanies(this["credit"]);
		 }
		 else if(typeof this["credit"].company != "undefined") 
		 {
		 	temp.company =this["credit"].company["#text"]; 
		 }
		 else
		 {
		 	console.log("no company" +this["credit"]);
		 }
		 //have to account for mutiple companies
		  temp.ppl=RetrieveStaff_obj(this["staff"]);
		  temp.userRating =this.rating;
		  temp.a_genres =RetrieveGenre(this["info"]);
		  objects[temp.a_name]= temp;
	});
	console.log(objects);
		return objects;
}
function RetrieveStaff_obj(staff)
{
	var temp=[];
	$.each(staff, function(){
		temp.push( {"title": this.task["#text"] , "name": this.person["#text"] });
	});
	return temp;
}
function RetrieveCompanies(credits)
{
	var temp=[];
	$.each(credits, function(){
		if(typeof this.company != "undefined")
			temp.push(this.company["#text"]);
	});
	return temp;
}