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
	  	callback(r)
	  }
	  
	})  
	request.fail(function(r){
	  console.log("fail");
	  console.log(r);
	});

}