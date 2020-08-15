<?php

$connect = new PDO("mysql:host=localhost;dbname=talenq", "root", "");

if(isset($_GET["code"]))
{
	echo "inside email_track";
	$query = "
	UPDATE mail
	SET email_status = 'yes' 
	WHERE email_track_code = '".$_GET["code"]."' 
	AND email_status = 'no'
	";
	$statement = $connect->prepare($query);
	$statement->execute();
}

?>
