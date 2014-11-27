<?php
$username = "root";
$password = "1";
$hostname = "localhost"; 
$db= "UpcomingData";
$table = "info";
//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password) or die('could not connect to mysql' . mysql_error());
//echo "Connected to MySQL<br>";
//select a database to work with
$selected = mysql_select_db($db,$dbhandle) or die('could not connect to UpcomingData db' . mysql_error());

?>
