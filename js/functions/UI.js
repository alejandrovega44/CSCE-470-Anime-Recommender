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
		temp += '<td><div class="well"><img src="' + this.picUrl + '">'+ this.a_name +'</div> </td>';
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