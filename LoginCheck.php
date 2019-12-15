<?php 
 session_start();
 unset($_SESSION["account"]);
 unset($_SESSION["error"]);
 unset($_SESSION["success"]);
 
 $con = mysqli_connect("localhost","root","","premierpredictions");
 
 $query = "SELECT * FROM users WHERE username='".$_POST['username']."' AND password='".$_POST['password']."'";
  
 $sql = $con->query($query);
 
 $n = $sql->num_rows;
  
 if($n > 0)
 {
	$_SESSION["account"] = $_POST['username'];
	$_SESSION["success"] = "Logged in"; 
	header("Location:proto_index.php");
	return;
 }
 else
 {	
	$_SESSION["error"] = "**Error: Incorrect Username or Password**";
	header("Location:proto_index.php");
	return;
 }
?>