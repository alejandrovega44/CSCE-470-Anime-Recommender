<?php

$q = intval($_GET['q']);



$con = mysqli_connect('localhost','peter','abc123','my_db');

if (!$con) {

  die('Could not connect: ' . mysqli_error($con));

}



mysqli_select_db($con,"ajax_demo");

$sql="SELECT * FROM user WHERE id = '".$q."'";

$result = mysqli_query($con,$sql);



mysqli_close($con);
?>
