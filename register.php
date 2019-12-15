<?php
 session_start();
 include_once 'dbconnect.php';
 unset($_SESSION["account"]);
 unset($_SESSION["regError"]);
 unset($_SESSION["success"]);


$sql="INSERT INTO users (username, password)
VALUES
('$_POST[user_text]','$_POST[pass_text]')";

if(!mysqli_query($con,$sql))
{
	$_SESSION["regError"] = "**Error: Username Taken**";
	header("Location:proto_index.php");
	return;
}
else
{
	$_SESSION["account"] = $_POST['user_text'];
	$_SESSION["success"] = "Logged in";
	header("Location:proto_index.php");
	return;
}
mysqli_close($con);

?>