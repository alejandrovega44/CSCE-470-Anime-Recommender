function CreateTable(animelist)
{
	maxCols = 0; 
	row=1;
	var $contents=$(".table > tbody");
	$contents.empty();
	//class="success" green
	//class="info"
	var temp = "<tr class=\'info\'>";
	for(i = 0; i < animelist.length; i++)
	{
		temp += '<td>' + animelist[i] + '</td>';
		maxCols += 1;
		if(maxCols == 3)
		{
			row++;
			temp += '</tr>';
			temp += '<tr';
			if(row%2==0)
				 temp+=' class=\'success\' >';
			else
				 temp+=' class=\'info\' >';

			maxCols = 0; 
		}
	
	}
	$contents.append(temp);
		
}
