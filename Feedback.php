<html>
    <head>
        <link rel="stylesheet" href="HomePage.css" type="text/css">
        <link rel="icon" href="Logo.png" type="image/icon">
        <title>.PYjus</title>
    </head>

        <body>


            <div class="FirstScreen">

                <div class="Navigation">

                    <a href="#"><img src="Logo.png" class="Logo"></a>

                    <ul>
                        <a href="#"><li class="Active">HomePage</li></a>
                        <a href="#"><li>Let's Study!</li></a>
                        <a href="#"><li>Forum</li></a>
                        <a href="#"><li>Feedback</li></a>
                        <a href="#"><li>Contact Us</li></a>
                    </ul>

                </div>
                <form method="post">
                    <label>Username: </label>
                    <input type="text" name="user" placeholder="Eg: Sparsh"></input>
                    
                    <label>Was the website easy to navigate through? </label>
                    <input type="text" name="navigationfb" placeholder="Eg: no.. because...."></input>
                    
                    <input type="submit"></input>

                    </form>
                    
                    <?php
                    $server = "localhost"
                    $user = "admin"
                    $database = "pypvideogames"
                    $password = ""
                    
                    $conn = new mysqli($servername, $username, $password, $database);

                    if($conn){
                        echo "connection successful";
                    }
                    else
                    {
                        echo "connection failed";
                    }

                    $User = $_POST['user']
                    $Navigationfb = $_POST['navigationfb']

                    
                    ?>
            </div>


        </body>
</html>