<?php
include_once 'connect.php';
//https://gist.github.com/jonsuh/3739844
$debug = false;
$W_O =false;
if(!$debug) $q = $_POST['RetrievedAnime'];
if($debug && $W_O)
{
	echo "writing to file" ;
	file_put_contents('incomingdata.txt',$q); 
}
if($debug && !$W_O)
{
 $q= file_get_contents('./incomingdata.txt');
}
//convert q to a php object
 $converted = json_decode( $q);
//use the php object and create it to a string 
//and send that to to the insert for each item
//using hash so it wont accept duplicates
//add a title column and add it as a primary key
$temp = false;
 foreach($converted as $value) {
	$value= mysql_real_escape_string(json_encode($value));
	$hash= sha1($value);
	$query="INSERT INTO $table (data,hash) VALUES ('$value', '$hash')";
	$result=mysql_query($query)or die(mysql_error());
	if(mysql_errno())
	{
    		$temp=true;
		echo "MySQL error ".mysql_errno().": "
         	.mysql_error()."\n<br>When executing <br>\n$query\n<br>";

	}
}
if(!$temp)
{
	echo "successfully inserted data";
}

// we will then have a db full of the records that have the data we want

?>
