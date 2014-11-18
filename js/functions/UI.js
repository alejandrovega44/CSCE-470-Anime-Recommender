function CreateTable(animelist)
{
	maxRows = 0; 
	var $contents=$(".table > tbody");
	$contents.empty();
	var temp = "<tr>";
	for(i = 0; i < animelist.length; i++)
	{
		temp += '<td>' + animelist[i] + '</td>';
		maxRows += 1;
		if(maxRows == 3)
		{
			temp += '</tr>';
			temp += '<tr>'; 
			maxRows = 0; 
		}
	
	}
	$contents.append(temp);
		
}

//draws tables with pics
function PopulateWithAnimeData(animelist)
{
	maxRows = 0; 
	var $contents=$(".table > tbody");
	$contents.empty();
	var temp = "<tr>";
	// <img src="pic_mountain.jpg" alt="Mountain View" style="width:304px;height:228px">
	$.each(animelist,function()
	{
		//temp += '<td><div class="well"><img src="' + this.picUrl + '">'+ this.a_name +'</div> </td>';
		temp += '<td>'+ createRow(this) + '</td>';
		maxRows += 1;
		if(maxRows == 3)
		{
			temp += '</tr>';
			temp += '<tr>'; 
			maxRows = 0; 
		}
	
	});
	$contents.append(temp);
		
}
//http://jsbin.com/heyixonoho/1/edit?output
function createRow(data)
{
	string =
	"<div>"+ //class='well'
	"<table class='table table-striped'> " +
	  "<tbody>"+
	  "<td><img src='" + data.picUrl +"'></td><td><a href='"+ data.moreInfo +"'><h4>"+ data.a_name +"</h4></a><div class='divider'></div><b>Genre:</b> "+
	  data.generes + "<br>";
	  if(data.desc != null)
	  	string+="<textarea style='height:100px;'>"+ data.desc +"</textarea>";
	  if(data.company != null)
	  	string+= "<br> <b>Company: </b><a href='"+ data.company.link + "'>"+ data.company.name +"</a>";
	  if(data.ppl != null)
	  	string+="<br> Other"+ CreateOtherData(data.ppl);
	 string+= "</td>"+
	  "</tbody>"+
     "</table></div>";
     return string;
}
//goes through all the keys inside the ppl_info
//creates a string to output
function CreateOtherData(ppl_object)
{
	var string="";
	for (var key in ppl_object)
	{
		string+="<br> <b>"+ ppl_object[key] + ": </b>" + key;
	}
	return string;
}

//visualize current data
function CreateTable_v(animelist)
{
	maxRows = 0; 
	var $contents=$(".table > tbody");
	$contents.empty();
	var temp = "<tr>";
	$.each(animelist,function(){
		temp += '<td>' + this["@attributes"].name +
		 '<br> desc: <br>' +
		 RetrieveDesc(this["info"]) +
		 '<br> company: <br>'; 
		 if(typeof this["credit"].company == "Object") 
		 	temp+=this["credit"].company["#text"]; 
		 //have to account for mutiple companies
		  temp+='<br>Staff <textarea style=\'height:100px;\'>' +
		  RetrieveStaff(this["staff"]) +
		  '</textarea>'+
		  '<br> userRating:'+ this.rating +
		  '<br> Genres: ' + JSON.stringify(RetrieveGenre(this["info"])) + 
		  '</td>';
		maxRows += 1;
		if(maxRows == 3)
		{
			temp += '</tr>';
			temp += '<tr>'; 
			maxRows = 0; 
		}
	
	});
	$contents.append(temp);
		
}
	
function RetrieveDesc(info)
{
	var string;
	$.each(info,function(){
		if(this["@attributes"].type != null)
			if(this["@attributes"].type == "Plot Summary")
			{
				string = this["#text"];
				return false;
			}	
	});
	return string;
}
function RetrieveGenre(info)
{
	var Genre=[];
	$.each(info,function(){
		if(this["@attributes"].type != null)
			if(this["@attributes"].type == "Genres")
			{
				Genre.push(this["#text"]);
			}	
	});
	return Genre;
}
function RetrieveStaff(staff)
{
	var string="";
	$.each(staff, function(){
		string+="\n"+this.task["#text"] +" : "+this.person["#text"];
	});
	return string;
}