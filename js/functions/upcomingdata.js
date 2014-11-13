//https://phantomjscloud.com/site/docs.html#/demo#demo
function retrieveAnimeChart (callback) 
{
	season="winter"; //this will change, can be : winter/spring/summer/fall different anime seasons
	url="http://anichart.net/"+season;
	
	//var yqlAPI = 'http://api.phantomjscloud.com/single/browser/v1/a-demo-key-with-low-quota-per-ip-address/?targetUrl=
	//'+ url +'&requestType=json';

	//use following stuff in yql
	//select * from html where url="" and xpath='//div[@class="card ng-scope"]'
    mainurl='http://api.phantomjscloud.com/single/browser/v1/a-demo-key-with-low-quota-per-ip-address/?targetUrl='+ 
    url+'&requestType=text';  
	query ='select * from html where url="'+ mainurl+'" and xpath="//div[@class=\'card ng-scope\']"';
	var yqlAPI = 'https://query.yahooapis.com/v1/public/yql?q=' + encodeURIComponent(query) + ' &format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=?';
 
	$.getJSON(yqlAPI, function(){
	      //console.log("sucess");
	  })
	.success(function(r){
	  console.log(r.query.results.div); //r.content is html of website 
	  						//r.pageContentPlainText retursn the text of website
	  callback(r.query.results.div);
	  
	})  
	.fail(function(r){
	  console.log("fail on anichart.net data");
	});
}
//need to find what will use to parse this data
function parseData (data) {

	var temp=0;
	$.each(data, function(){

		if(this.div[5] != null)
		{
			console.log(temp);
			console.log(this.div[0].p); // generes
			console.log(this.div[3].a.content); //name of anime
			console.log(this.div[3].a.href); //link to more data in anichart
			console.log(this.div[4].div[0].a.content); //company wrote anime
			console.log(this.div[4].div[0].a.href); //company link
			if(this.div[4].div[2] != null)
			{
				if(this.div[4].div[0].a.href != null)
					console.log(this.div[4].div[1].p.content); //desc
				else
					console.log(this.div[4].div[1].p); //this is second season 
				$.each(this.div[4].div[2].span,function(){
					console.log(this.content); //return type Example: "Action" | ", ecchi" <--- with comaa
				});
			}
			$.each(this.div[5].div, function(){
				var temp =retrieveData(this);
				if (temp != null)
					console.log(temp);
			}) ; //contains an array of objects insid
		}
		temp++;
	});// close of main each
}
//used to retrieve data that is inside specific sections
//hopefully to retrieve data related to directo or char deisgn n such
function retrieveData(object)
{
  if (object.p != null)
    {
      if ($.isArray(object.p))
        {
          var title= object.p[0]; // position example: "Director", "Char Design"
          var name= object.p[1].content; //name of person that holds such position
          return {"title": title, "name": name};
        }
    }
}