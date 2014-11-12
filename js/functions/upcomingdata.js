//https://phantomjscloud.com/site/docs.html#/demo#demo
function retrieveAnimeChart (callback) 
{
	season="winter"; //this will change, can be : winter/spring/summer/fall different anime seasons
	url="http://anichart.net/"+season;
	var yqlAPI = 'http://api.phantomjscloud.com/single/browser/v1/a-demo-key-with-low-quota-per-ip-address/?targetUrl=
	'+ url +'&requestType=json';
	//use following stuff in yql
	//select * from html where url="http://api.phantomjscloud.com/single/browser/v1/a-demo-key-with-low-quota-per-ip-address/?targetUrl=http://anichart.net/winter&requestType=text" and xpath='//div[@class="card ng-scope"]'
      
	$.getJSON(yqlAPI, function(){
	      //console.log("sucess");
	  })
	.success(function(r){
	  console.log(r.content); //r.content is html of website 
	  						//r.pageContentPlainText retursn the text of website
	  callback(r.content);
	  
	})  
	.fail(function(r){
	  console.log("fail on anichart.net data");
	});
}
//need to find what will use to parse this data
function parsehtml (html) {
	//need to retrieve the different anime names
	//basic info on them
	//and store that into something for every x found in the html
}