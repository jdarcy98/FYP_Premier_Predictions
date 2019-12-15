<?php
session_start();

$con=mysqli_connect("localhost","root","","premierpredictions");
	
// Check connection
if (mysqli_connect_errno())
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$Pass1 = $_POST['Password'];
$Pass2 = $_POST['confirmPassword'];
$username = $_SESSION['account'];

$sql = (mysqli_query($con, "SELECT password from users WHERE username='$username'"));

$row=mysqli_fetch_row($sql);


if($Pass1 == $Pass2)
{
	if ($Pass1 <> $Pass2)
	{
		echo "your passwords do not match";
	}
	else if (mysqli_query($con, "UPDATE users SET password='$Pass1' WHERE username='$username'"))
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