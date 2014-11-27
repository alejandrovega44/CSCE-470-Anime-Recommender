<?php
$username = "root";
$password = "1";
$hostname = "localhost"; 

//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password) or die('could not connect to mysql' . mysql_error());
//echo "Connected to MySQL<br>";
//select a database to work with
$selected = mysql_select_db("UpcomingData",$dbhandle) or die('could not connect to UpcomingData db' . mysql_error());

?>
