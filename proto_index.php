<?php
    session_start();
?>
<html>

<script type="text/javascript" src="./javascript/login.js"></script>

<head>
    <title>Premier Predictions</title>

    <meta charset="UFT-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link id="sheet" rel="stylesheet" href="./css/Main.css">
    <link id="sheet" rel="stylesheet" href="./css/Login.css">
</head>

<body>

    <div id="Whole">
        <br><br>
        <div id="Main">
            <div id="Top">
                <div class="container">
                   <img src="./images/pitch.jpg" style="width:100%; height:100%">
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
                <!--<li id= "first"><a href="home.php">Home</a></li>-->
            </ul>

            <?php
                if(!isset($_SESSION["account"]))
                {
            ?>
                <div id= "Left">
                    <h1>Log in!</h1>
                    <?php
                        if(isset($_SESSION["error"]))
                        {
                            echo ("<p style='color:red'>".$_SESSION["error"]."</p>");
                            unset($_SESSION["error"]);
                        }
                    ?>
                    <p>Enter your details to access your account.<p>

                    <form id = "loginform" action="LoginCheck.php" method = "post">
                        <input id= "TextBox" type="text" name="username" placeholder=" Username" required>
                        <br><br>
                        <input id= "TextBox" type="password" name="password" placeholder=" Password" required>
                        <br><br>
                        <input id="button" type="submit" value="Login">
                    </form>
                    <br>

                </div>

                <div id="SignUp">
                    <h1>Sign Up!</h1>
                    <p>New to us? Create an account here!</p>
                    <?php
                        if(isset($_SESSION["regError"]))
                        {
                            echo ("<p style='color:red'>".$_SESSION["regError"]."</p>");
                            unset($_SESSION["regError"]);
                        }
                    ?>
                    <form id = "register_form" action = "register.php" method ="POST" onclick=" return validateForm()">
                        <table align="center" border="0">
                            <tbody>
                            <tr>
                                <td class="data">
                                    <input class = "textbox" type="text" name="user_text" id="user_text" placeholder= "Username" maxlength="50">
                                    <div id = "user_error"></div>
                                    <br>
                                </td>
                            </tr>
                            <tr>
                                <td class="data">
                                    <input class = "textbox" type="password" name="pass_text" id="pass_text" placeholder= "Password" maxlength="50">
                                    <div id = "pass_error"></div>
                                    <br>
                                </td>
                            </tr>
                            <tr>
                                <td class="data">
                                    <input id= "textbox" type="password" name="confirmPassword" id="confirmPassword" placeholder="Confirm Password" required
                                    maxlength="50">
                                    <div id = "pass_error"></div>
                                    <br>
                                </td>
                            </tr>
                            <tr>
                                <td class="name">
                                    <input id = "button" class = "textbox" type="submit" value="Sign Up">
                                </td>
                            </tr>
                        </tbody></table>
                    </form>
                </div>

            <?php
            }
            else
            {
                echo '<div id= "Center">';
                    echo "<h1 id=\"Heading\">Welcome " . $_SESSION["account"] . "!</h1>";

                    echo "<br><br><br><br>";

                    echo "<a href=\"Settings.php\" class=\"button\">Settings</a>";
                    echo "&nbsp&nbsp <a href=\"results.php\" class=\"button\">Results</a>";
                    echo "&nbsp&nbsp <a href=\"leagues.php\" class=\"button\">Leagues</a>";
                    echo "&nbsp&nbsp <a href=\"fixtures.php\" class=\"button\">Upcoming Fixtures</a>";
                    echo "&nbsp&nbsp <a href=\"logout.php\" class=\"button\">Log Out</a>";
                echo "</div>";
            }
            ?>           
        </div>
        <div id="footer">
            <p align = "left" id = "pp">Premier Predictions</p>
        </div>
    </div>
</body>

</html>