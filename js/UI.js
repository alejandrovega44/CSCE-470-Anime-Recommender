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