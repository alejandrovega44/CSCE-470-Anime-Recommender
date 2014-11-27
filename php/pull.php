<?php
include_once 'connect.php';
  $result = mysql_query("SELECT * FROM '$table'") or die(mysql_error());

?>