<?php
	session_start();
    include_once 'dbconnect.php';
?>
<html>

<head>
    <title>Premier Predictions</title>
    <link id="sheet" rel="stylesheet" href="./css/Main.css">
	<link rel="stylesheet" href="./css/Login.css">
</head>

<body>

	<div id="Whole">
		<div id="Empty">
		</div>
		<div id="Main">
			<div id="Top">
				<div class="container">
					<img src="./images/pitch.jpg" style="width:100%; height: 160px;">
				</div>
			</div>

			<ul id="Banner">
				<a id="pp">Premier Predictions</a>
      			<?php
                if(isset($_SESSION["account"]))
                {             
                    echo "<li id= \"first\"><a class = \"active\" href=\"play.php\">Play Now</a></li>";
                    echo "<li><a href=\"leagues.php\">Leagues</a></li>";
                    echo "<li id= \"last\"><a class = \"active\" href=\"proto_index.php\">My Account</a></li>";

                }
                else
                { 
                    echo "<li id= \"first\"><a class = \"active\" href=\"home.php\">Home</a></li>";
                    echo "<li><a href=\"fixtures.php\">Upcoming Fixtures</a></li>";
                    echo "<li id= \"last\"><a class = \"active\" href=\"proto_index.php\">Register/Login</a></li>";
                }
                ?>
			</ul>

			<a href="login_register.php"><img id="Escape" src="./images/X.png" name="Back"></a>
			
			<?php
				echo '<div id= "Center">';
				echo '<h1 id="Heading">&nbsp&nbspSettings</h1>';


				
				// Check connection
				if (mysqli_connect_errno())
				{
					echo "Failed to connect to MySQL: " . mysqli_connect_error();
				}

				$result = mysqli_query($con,"SELECT * FROM users Where Username='".$_SESSION['account']."'");


				mysqli_close($con);
				
				echo "<br><br><br>";
				echo "<a href=\"PassChange.php\" class=\"button\">Change Password</a>";
				echo "&nbsp&nbsp <a href=\"Delete.php\" class=\"button\">Delete Account</a>";
			?>
				
				<script>
					function Function() 
					{
						var txt;
						
						if(confirm("Your account will be permanently Deleted. Are you sure you want to wish to continue?"))
						{
							txt="delete";
							<?php
							if (isset($_POST['Delete'])) 
							{
								echo "<span>**You have deleted your account.**</span>";
								header("Location: Delete.php");
								exit;
							}
							?>
						}
						else
						{
							<?php
								echo "<span>**You have cancelled the delete operation.**</span>";
							?>
						}
					}
				</script>
			</div>
            <br>


		</div>
        <div id="footer">
			<p align = "left" id = "pp">Premier Predictions</p>
		</div>
		


</body>

</html>