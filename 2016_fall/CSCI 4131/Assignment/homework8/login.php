<!DOCTYPE html>
<html>
   <head>
      <meta charset = "utf-8">
      <title>Login Page</title>
   </head>
   <body>
   <?php
   include_once 'database_HW8F16.php';
   $passworderr = $loginerr = "";
   $Condition = 1;
   $password = $_POST["password"];
   $login_name = $_POST["login"];
   if($_SERVER["REQUEST_METHOD"] == "POST")
   {
      if(empty($_POST["login"]))
      {
         $loginerr = "Please enter a valid login value";
         $Condition = 0;
      }
      if(empty($_POST["password"]))
      {
         $passworderr = "Please enter a valid password value";
         $Condition = 0;
      }
      if($Condition == 1)
      {
         $conn=new mysqli($db_servername,$db_username,$db_password,$db_name,$db_port);
         if ( $conn->connect_error )
         {
              echo  die("Could not connect to database </body></html>" );
         }
         else
         {
              $squery = "SELECT * FROM tbl_accounts";
              $result = $conn->query($squery);
              $i = 1;
              while($row = mysqli_fetch_row($result))
              {
               echo $login_name."   ".$row[2]."  ";
               if ($login_name == $row[2])
               {
                  if(sha1($password) == $row[3])
                  {
                     $conn->close();
                     session_start();
                     $_SESSION["login_name"] = $login_name;
                     //echo $_SESSION["login_name"];
                     header("Location:calendar.php");
                  }
                  else
                  {
                     $passworderr = "your password is not correct";
                  }
               }

              }
              if(empty($passworderr))
              $loginerr = "This account doesn't exist";
              $conn->close();


         }

      }
   }
   ?>
      <h1>Please enter you login name and password. Both of them are case sensitive</h1>
      <form method = "post" action = <?php echo $_SERVER["PHP_SELF"]; ?>  >
         Login name: &nbsp;&nbsp;
         <input type="text" name="login">
         <span class="error"><?php echo $loginerr;  ?></span>
         <br>
         <input type="text" name="password">
         <span class="error"><?php echo $passworderr;  ?></span>
         <br>
         <p><input type = "submit" value = "submit" name="submit"></p>
      </form>
   </body>
</html>
