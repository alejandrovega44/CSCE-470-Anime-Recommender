<?php
include_once 'connect.php';
//https://gist.github.com/jonsuh/3739844
$debug = true;
$W_O =false;
if(!$debug) $q = $_POST['RetrievedAnime'];
 echo "connection established";

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

 foreach($converted as $value) {
	$value= mysql_real_escape_string(json_encode($value));
	echo $value;
	echo "\n";
	$result=mysql_query("INSERT INTO $table (data) VALUES ('$value')")or die(mysql_error());
}

// we will then have a db full of the records that have the data we want

//$result=mysql_query("INESRT INTO '$table' (data) Values('$data')")or die(mysql_error());
?>
