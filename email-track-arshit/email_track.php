<?php

//email_track.php

$connect = new PDO("mysql:host=localhost;dbname=talenq", "root", "");

// header('Content-Type: image/gif');
// readfile("tracking.gif");

// $date = date('Y-m-d H:i:s', $_SERVER['REQUEST_TIME']);
// $txt = $date.",". $_SERVER['REMOTE_ADDR'];
// $myfile = file_put_contents('log.txt', $txt.PHP_EOL , FILE_APPEND);
// exit;

if(isset($_GET["code"]))
{
	echo "inside email_track";
	$query = "
	UPDATE email_data 
	SET email_status = 'yes', email_open_datetime = '".date("Y-m-d H:i:s", STRTOTIME(date('h:i:sa')))."' 
	WHERE email_track_code = '".$_GET["code"]."' 
	AND email_status = 'no'
	";
	$statement = $connect->prepare($query);
	$statement->execute();
}

?>