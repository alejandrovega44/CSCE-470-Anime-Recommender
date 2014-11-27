<?php
include_once 'connect.php';
//https://gist.github.com/jonsuh/3739844
$q = intval($_GET['AnimeData']);
 var_dump(json_decode($q));
//convert q to a php object
//use the php object and create it to a string 
//and send that to to the insert for each item
// we will then have a db full of the records that have the data we want

//INSERT INTO table_name (column1,column2,column3,...)VALUES (value1,value2,value3,...);
$sql="INESRT INTO info (data) Values('$data')"; or die(mysql_error());
//$sql="SELECT * FROM info WHERE * '";
/*  $result = mysql_query("SELECT * FROM info WHERE username ='$objUser[username]'") or die(mysql_error());

      $numRows = mysql_num_rows($result);

        if($numRows == 1) 

        {

          $row = mysql_fetch_array( $result );        

        }
*/
$result = mysql_query($sql);
echo json_encode($result);
?>
