<?php
session_start();

$con=mysqli_connect("localhost","root","","premierpredictions");
	
// Check connection
if (mysqli_connect_errno())
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$oldPass= $_POST['oldPassword'];
$newPass1 = $_POST['newPassword'];
$newPass2 = $_POST['confirmPassword'];
$username = $_SESSION['account'];

$sql = (mysqli_query($con, "SELECT password from users WHERE username='$username'"));

$row=mysqli_fetch_row($sql);

$CurrentPassword = $row[0];

if($CurrentPassword == $oldPass)
{
	if ($newPass1 <> $newPass2)
	{
		echo "your passwords do not match";
	}
	else if (mysqli_query($con, "UPDATE users SET password='$newPass1' WHERE username='$username'"))
	{
		echo "You have successfully changed your password.";
		header("Location:proto_index.php");
		return;
	}
	else
	{
		mysqli_error($con);
	}
	mysqli_close($con);
}
else
{
	echo "The current password was incorrect. Please Try Again.";
}
?>