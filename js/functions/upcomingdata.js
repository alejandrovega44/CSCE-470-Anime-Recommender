//https://phantomjscloud.com/site/docs.html#/demo#demo
function retrieveAnimeChart (callback) 
{
	season="winter"; //this will change, can be : winter/spring/summer/fall different anime seasons
	url="http://anichart.net/"+season;
	debug=0;
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
	  if(debug) console.log(r.query.results.div); //r.content is html of website 
	  						//r.pageContentPlainText retursn the text of website
	  callback(parseData(r.query.results.div));
	  
	})  
	.fail(function(r){
	  console.log("fail on anichart.net data");
	});
}

//creates objects that contain all the data need for each anime
function CreateData (callback) {
	retrieveAnimeChart(function(data){
		retrievePics(function(picsdata){
			$.each(data, function(){
				this.picUrl =picsdata[this.i];
			})
			console.log(data);
			callback(data);
		});
	});

}

//parse html from anichart and creates objects with data about each anime
function parseData (data) {

	var temp=0;
	var Data={};
	var debug=0;

	$.each(data, function(){
		if(this.div[5] != null)
		{
			var temp_data={};
			if(debug)console.log(temp);
			temp_data.a_name = this.div[3].a.content;
			temp_data.i = temp;
			if(debug)console.log(this.div[0].p); // generes
	        temp_data.generes = this.div[0].p;
			if(debug)console.log(this.div[3].a.content); //name of anime
			if(debug)console.log(this.div[3].a.href); //link to more data in anichart
			temp_data.moreInfo=this.div[3].a.href;
			temp_data.company={"name": this.div[4].div[0].a.content, "link": this.div[4].div[0].a.href};
			if(debug)console.log(this.div[4].div[0].a.content); //company wrote anime
			if(debug)console.log(this.div[4].div[0].a.href); //company link
			if(this.div[4].div[2] != null)
			{
				//if(this.div[4].div[0].a.href != null)
				if(this.div[4].div[1].p.content != null)
				{
					if(debug)console.log(this.div[4].div[1].p.content); //desc
					temp_data.desc = this.div[4].div[1].p.content;
				}
				else
				{
					if(debug)console.log(this.div[4].div[1].p); //this is second season 
					temp_data.desc = this.div[4].div[1].p;
				}
	         	temp_array=[];
				$.each(this.div[4].div[2].span,function(){
					if(debug)console.log(this.content); //return type Example: "Action" | ", ecchi" <--- with comaa
					temp_array.push(this.content);
				});
	          	temp_data.a_generes=temp_array;
			}
			PPL_data={};
			$.each(this.div[5].div, function(){
				var temp =retrieveData(this);
				if (temp != null)
				{
					if(debug) console.log(temp);
	             	PPL_data[temp.name]=temp.title;
				}
			}) ; //contains an array of objects insid
	        temp_data.ppl = PPL_data;
        	Data[this.div[3].a.content]=temp_data;
		}
		temp++;
	});// close of main each
	return Data;
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
function retrievePics(callback){
	//found using the following
	//https://phantomjscloud.com/site/docs.html#/demo#demo
	//var yqlAPI = 'http://api.phantomjscloud.com/single/browser/v1/a-demo-key-with-low-quota-per-ip-address/?targetUrl=http://anichart.net/fall&requestType=json';
	season="winter"; //this will change, can be : winter/spring/summer/fall different anime seasons
	url="http://anichart.net/"+season;
	var yqlAPI = 'http://api.phantomjscloud.com/single/browser/v1/a-demo-key-with-low-quota-per-ip-address/?targetUrl='+ url +'&requestType=json';

	$.getJSON(yqlAPI, function(){
	      //console.log("sucess");
	  })
	.success(function(r){
	 var string =r.pageContent;
	 var found_strings =string.match(/background-image:url\('(.+\')/g);
	 var configuered_s=[];
	  $.each(found_strings, function(){
	    temp = this.replace('background-image:url(\'','');
	    temp = temp.substr(0,temp.length-1);
	    configuered_s.push(temp);
	 }); 
	  callback(configuered_s);
	})  
	.fail(function(r){
	  console.log("fail on anichart.net data");
	});

}
function Create_RetrievedAnime_Objects(animelist)
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