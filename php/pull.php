<?php
include_once 'connect.php';
  $return="[";
  $result = mysql_query("SELECT * FROM $table") or die(mysql_error());
  $rowCount = mysql_num_rows($result);
  $i=1;
  while($row = mysql_fetch_array( $result )) {

	if($i==$rowCount)
	{
		$return.=stripslashes ($row['data']); 
	}
	else
	{
		$return.=stripslashes($row['data']) .",";

	}	
	$i++;
}
echo $return."]";
?>
