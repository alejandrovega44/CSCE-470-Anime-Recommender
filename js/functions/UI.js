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
function CreateOtherData(ppl_object)
{
	var string="";
	for (var key in ppl_object)
	{
		string+="<br> <b>"+ ppl_object[key] + ": </b>" + key;
	}
	return string;
}