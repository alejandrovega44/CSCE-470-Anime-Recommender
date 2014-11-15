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
	  "<td><img src='" + data.picUrl +"'></td><td><h4>"+ data.a_name +"</h4><div class='divider'></div><b>Genre:</b> "+
	  data.generes;
	  if(data.desc != null)
	  string+="<textarea style='height:100px;'>"+ data.desc +"</textarea>";
	 
	 string+= "</td>"+
	  "</tbody>"+
     "</table></div>";
     return string;
}