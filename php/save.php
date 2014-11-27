<?php
include_once 'connect.php';
//https://gist.github.com/jonsuh/3739844
$q = intval($_GET['RetrievedAnime']);
 //var_dump(json_decode($q));
 echo "connection established";
//convert q to a php object
//use the php object and create it to a string 
//and send that to to the insert for each item
// we will then have a db full of the records that have the data we want

//$result=mysql_query("INESRT INTO '$table' (data) Values('$data')")or die(mysql_error());
//echo json_encode($result);
?>
