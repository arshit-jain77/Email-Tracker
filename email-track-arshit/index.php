<?php

//index.php

$connect = new PDO("mysql:host=localhost;dbname=talenq", "root", "");
$base_url = 'https://daccce2c1d86.ngrok.io/email-track-arshit/'; //

$message = '';

if(isset($_POST["send"]))
{
	require 'class/class.phpmailer.php';
	$mail = new PHPMailer(true);
	$mail->IsSMTP();
	$mail->Host = 'smtp.gmail.com';
	$mail->Port = 465;
	$mail->SMTPAuth = true;
	$mail->Username = 'tigersem4D@gmail.com';
	$mail->Password = 'xxxxxxx';
	$mail->SMTPSecure = 'ssl';
	$mail->From = 'tigersem4D@gmail.com';
	$mail->FromName = 'Tiger X';
	$mail->AddAddress($_POST["receiver_email"]);
	$mail->WordWrap = 50;
	$mail->IsHTML(true);
	$mail->Subject = $_POST['email_subject'];

	$track_code = md5(rand());

	$message_body = $_POST['email_body'];

	$message_body .= '<img src="'.$base_url.'email_track.php?code='.$track_code.'" width="1" height="1">';
	// $message_body .= '<a href="'.$base_url.'email_track.php?code='.$track_code.'">link</a>';

	$mail->Body = $message_body;

	if($mail->Send())
	{
		$data = array(
			':email_subject'			=>		$_POST["email_subject"],
			':email_body'				=>		$_POST["email_body"],
			':email_address'			=>		$_POST["receiver_email"],
			':email_track_code'			=>		$track_code
		);
		$query = "
		INSERT INTO email_data 
		(email_subject, email_body, email_address, email_track_code) VALUES 
		(:email_subject, :email_body, :email_address, :email_track_code)
		";

		$statement = $connect->prepare($query);
		if($statement->execute($data))
		{
			$message = '<label class="text-success">Email Send Successfully</label>';
		}
	}
	else
	{
		$message = '<label class="text-danger">Email Send Successfully</label>';
	}

}

function fetch_email_track_data($connect)
{
	$query = "SELECT * FROM email_data ORDER BY email_id";
	$statement = $connect->prepare($query);
	$statement->execute();
	$result = $statement->fetchAll();
	$total_row = $statement->rowCount();
	$output = '
	<div class="table-responsive">
		<table class="table table-bordered table-striped">
			<tr>
				<th width="25%">Email</th>
				<th width="45%">Subject</th>
				<th width="10%">Status</th>
				<th width="20%">Open Datetime</th>
			</tr>
	';
	echo $total_row;
	if($total_row > 0)
	{
		foreach($result as $row)
		{
			$status = '';
			if($row['email_status'] == 'yes')
			{
				echo "inside if";
				$status = '<span class="label label-success">Open</span>';
			}
			else
			{
				echo "inside else";
				$status = '<span class="label label-danger">Not Open</span>';
			}
			$output .= '
				<tr>
					<td>'.$row["email_address"].'</td>
					<td>'.$row["email_subject"].'</td>
					<td>'.$status.'</td>
					<td>'.$row["email_open_datetime"].'</td>
				</tr>
			';
		}
	}
	else
	{
		$output .= '
		<tr>
			<td colspan="4" align="center">No Email Send Data Found</td>
		</tr>
		';
	}
	$output .= '</table>';
	return $output;
}


?>
<!DOCTYPE html>
<html>
	<head>
		<title>How to Track Email Open or not using PHP</title>
		<script src="jquery.min.js"></script>
		<link rel="stylesheet" href="bootstrap.min.css" />
		<script src="bootstrap.min.js"></script>
	</head>
	<body>
		<br />
		<div class="container">
			<h3>How to Track Email Open or not using PHP</h3>
			<br />
			<?php
			
			echo $message;

			?>
			<form method="post">
				<div class="form-group">
					<label>Enter Email Subject</label>
					<input type="text" name="email_subject" class="form-control" required />
				</div>
				<div class="form-group">
					<label>Enter Receiver Email</label>
					<input type="email" name="receiver_email" class="form-control" required />
				</div>
				<div class="form-group">
					<label>Enter Email Body</label>
					<textarea name="email_body" required rows="5" class="form-control"></textarea>
				</div>
				<div class="form-group">
					<input type="submit" name="send" class="btn btn-info" value="Send Email" />
				</div>
			</form>
			
			<br />
			<h4>Sending Email Open or not status</h4>
			<?php 
			
			echo fetch_email_track_data($connect);

			?>
		</div>
		<br />
		<br />
	</body>
</html>
