<!DOCTYPE html>
<html>
<head>
	<title>Form Input</title>
	<link rel="stylesheet" type="text/css" href="Style.css">
	<meta charset="UTF-8">
</head>
<body>
 <?php
    session_start();
    if(empty($_SESSION["login_name"]))
    {
      header("Location:login.php");
    }
    else
    {
      $login_name = $_SESSION["login_name"];
    }
    $src = array("bruininks" => "bruininks_hall.jpg", "fraser" => "fraser_hall.jpg" , "willey" => "willey_hall.jpg" , "hanson" => "hanson_hall.jpg", "blegen" => "blegen_hall");
    $img = $Event=$Start=$End=$Location=$Weekday="";
    $Condition = 1;

    if($_SERVER["REQUEST_METHOD"] == "POST")
    {
      if($_POST["log_out"] == "log_out")
      {
        header("Location:logout.php");
      }
      if ($_POST["clear"]=="clear")
      {
        $myfile = fopen("calendar.txt","w");
        fclose($myfile);
        header("Location:calendar.php");
      }
      if (empty($_POST["Event"]))
      {
        $Eventerr = "Event name is requested";
        $Condition = 0;
      }
      else
      {
        $Event=$_POST["Event"];
      }
      if (empty($_POST["Start"]))
      {
        $Starterr = "Start time is requested";
        $Condition = 0;
      }
      else
      {
        $Start = $_POST["Start"];
      }
      if (empty($_POST["End"]))
      {
        $Enderr = "Ending name is requested";
        $Condition = 0;
      }
      else
      {
        $End = $_POST["End"];
      }
      if (empty($_POST["Location"]))
      {
        $Locationerr = "Location is requested";
        $Condition = 0;
      }
      else
      {
        $Location=$_POST["Location"];
      }
      if (empty($_POST["Weekday"]))
      {
        $Eventerr = "Weekday is requested";
        $Condition = 0;
      }
      else
      {
        $Weekday = $_POST["Weekday"];
      }
      if (empty($_POST['img']))
      {
        $imgerr = 'URL is requested';
        $Condition = 0;
      }
      else
      {
        $img = $_POST['img'];
      }
      if($Condition == 1 && $_POST["submit"] =="submit")
      {
        $myfile=fopen("calendar.txt", a);
        $data=array(
                    "Weekday" =>$Weekday,
                    "Start" => $Start,
                    "End" => $End,
                    "Event" => $Event,
                    "Location" => $Location,
                    "img" => $img
                   );
        fwrite($myfile,json_encode($data));
        fwrite($myfile,"\n");
        fclose($myfile);
        header("Location:calendar.php");
      }
    }
  ?>
 <h1><?php  echo "Welcome   ".$login_name; ?></h1>
 <form action = <?php echo $_SERVER["PHP_SELF"]; ?> method="post">
    <button name="log_out" type="submit" value="log_out">Log out</button>
  </form>
 <table class="banner">
   <tr>
   <td class="banner"><img alt="button" class="buttonPrev" src="prev_blue.png" ></td>
   <td class="banner"><div class="imagebox">
   <a class="adLink" href="http://sua.umn.edu/events/calendar/event/14781/"><img alt="banner" src="Nerve.jpg" class="ad" title="Nerve Friday,Sept 30 7:00PM"></a>
   </div></td>
   <td class="banner"><img alt="button" class="buttonNext" src="next_blue.png" ><td>
   </tr>
 </table>
 <table class="bulletSet">
   <tr>
   <td><img alt="bullet" src="bullet_blue.png" class="bullet"></td>
   <td><img alt="bullet" src="bullet_gray.png" class="bullet"></td>
   <td><img alt="bullet" src="bullet_gray.png" class="bullet"></td>
   </tr>
 </table>
 <H1 class="printer">Form Input</H1>
 <nav>
 	<button onclick="{location.href='calendar.php'}">My Calendar</button>
  <button onclick="{location.href='input.php'}">Form Input</button>
 </nav>
 <div class="other">
 	<form action = <?php echo $_SERVER["PHP_SELF"]; ?> method="post">
   	 Event Name: &nbsp;&nbsp;
   	 <input type="text" name="Event">
     <span class="error">
     <?php echo $Eventerr ; ?>
     </span>
     <br>

   	 Start Time: &nbsp;&nbsp;
   	 <input type="time" name="Start">
     <span class="error">
     <?php echo $Starterr ; ?>
     </span>
     <br>

   	 Ending Time: &nbsp;&nbsp;
   	 <input type="time" name="End">
     <span class="error">
     <?php echo $Enderr ; ?>
     </span>
     <br>

     Location: &nbsp;&nbsp;&nbsp;
     <input type="text" name="Location">
     <span class="error">
     <?php echo $Locationerr ; ?>
     </span>
     <br>
     URL: &nbsp;&nbsp;&nbsp;
     <input type="text" name="img">
     <span class="error">
     <?php echo $imgerr ; ?>
     </span>
     <br>

     Day of the week:&nbsp;&nbsp;&nbsp;
      <select name="Weekday">
      <option>Mon</option>
      <option>Tue</option>
      <option>Wed</option>
      <option>Thu</option>
      <option>Fri</option>
      </select>
      <?php echo $_POST["submit"]; echo $Condition; ?>
      <br>

      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <button name="clear" type="submit" value="clear">clear</button>
      <button name="submit" type="submit" value="submit">submit</button>
 	</form>
 </div>
 <script type="text/javascript">
    var index=0;
    var clock;
    var hover=[0,0,0];
    function getName(name)
    {
      return document.getElementsByClassName(name);
    }
    var source=["Nerve.jpg",
                 "secret-life-of-pets.jpg",
                 "suicide-squad.jpg",
                 "prev_orange.png",
                 "next_orange.png",
                 "next_blue.png",
                 "prev_blue.png"
               ]

    function bulletShift(num){
      var bullet=getName("bullet");
      for (var i = 0; i < 3; i++) {
        if(hover[i]==0)
        {
          bullet[i].src="bullet_gray.png";
        }
        else
        {
          bullet[i].src="bullet_orange.png";
        }
      }
      bullet[num].src="bullet_blue.png";
    }
    function shift1(){
      bulletShift(0);
      var image=document.getElementsByClassName("ad");
        image[0].src=source[0];
        index=0;
        clock=setTimeout(shift2,7000);
    }
    function shift2(){
      bulletShift(1);
      var image=document.getElementsByClassName("ad");
        image[0].src=source[1];
        image[0].title="secret-life-of-pets Fri,Oct7 7:00PM";
        getName("adLink")[0].href="http://sua.umn.edu/events/calendar/event/14786/";
        index=1;
        clock=setTimeout(shift3,5000);
    }
    function shift3(){
      bulletShift(2);
      getName("adLink")[0].href="http://sua.umn.edu/events/calendar/event/14794/";
      var image=document.getElementsByClassName("ad");
        image[0].src=source[2];
        image[0].title="suicide-squad,Fri,Oct 14 8:00PM";
        index=2;
        clock=setTimeout(shift1,3000);
    }
    function Rotator(){
      setListener();
      clock=setTimeout(shift2,7000);

    }
    function bulletListener(element,number,command){
      if(command=="mouseover")
      {
        hover[number]=1;
      }
      else if(command=="mouseout")
      {
        hover[number]=0;
      }
      if(number!=index)
      {
        if(command=="mouseover")
        {
          element.src="bullet_orange.png";
        }
        else if(command=="mouseout")
        {
          element.src="bullet_gray.png";
        }
        else
        {
          clearTimeout(clock);
          if(number==0)
          {
          clock=setTimeout(shift1,0);
          }
          else if(number==1)
          {
          clock=setTimeout(shift2,0);
          }
          else
          {
          clock=setTimeout(shift3,0);
          }
        }
      }

    }
    function setListener(){
      var a=document.getElementsByClassName("buttonPrev")[0];
      a.addEventListener("mouseover",function(){
        buttonHover(a,"prev","mouseover");
      });
      a.addEventListener("mouseout",function(){
        buttonHover(a,"prev","mouseout");
      });
      var b=getName("buttonNext")[0];
      b.addEventListener("mouseover",function(){
        buttonHover(b,"next","mouseover");
      });
      b.addEventListener("mouseout",function(){
        buttonHover(b,"next","mouseout");
      });
      a.addEventListener("click",function(){
        buttonHover(a,"prev","click");
      });
      b.addEventListener("click",function(){
        buttonHover(b,"next","click");
      });
      a.addEventListener("click",function(){
        buttonHover(a,"prev","click");
      });
      var b0=getName("bullet")[0];
      var b1=getName("bullet")[1];
      var b2=getName("bullet")[2];
      b0.addEventListener("mouseover",function(){
        bulletListener(b0,0,"mouseover");
      });
      b0.addEventListener("mouseout",function(){
        bulletListener(b0,0,"mouseout");
      })
      b0.addEventListener("click",function(){
        bulletListener(b0,0,"click");
      })
      b1.addEventListener("mouseover",function(){
        bulletListener(b1,1,"mouseover");
      });
      b1.addEventListener("mouseout",function(){
        bulletListener(b1,1,"mouseout");
      })
      b1.addEventListener("click",function(){
        bulletListener(b1,1,"click");
      })
      b2.addEventListener("mouseover",function(){
        bulletListener(b2,2,"mouseover");
      });
      b2.addEventListener("mouseout",function(){
        bulletListener(b2,2,"mouseout");
      })
      b2.addEventListener("click",function(){
        bulletListener(b2,2,"click");
      })
    }
    function adShift(element,command)
    {
     if(command=="next")
     {
      clearTimeout(clock);
      if(index==0)
      {
        clock=setTimeout(shift2,0);
      }
      else if(index==1)
      {
        clock=setTimeout(shift3,0);
      }
      else if(index==2)
      {
        clock=setTimeout(shift1,0);
      }
     }
     else if(command=="prev")
     {
      clearTimeout(clock);
      if (index==0)
      {
        clock=setTimeout(shift3,0);
      }
      else if(index==1)
      {
        clock=setTimeout(shift1,0);
      }
      else
      {
        clock=setTimeout(shift2,0);
      }
     }
    }
    function buttonHover(element,name,event)
    {
      if(event=="mouseover")
      {
        if(name=="prev")
        {

          element.src=source[3];
        }
        else
        {
          element.src=source[4];
        }
      }
      else if(event=="mouseout")
      {
        if(name=="prev")
        {
          element.src=source[6];
        }
        else
        {
          element.src=source[5];
        }
      }
      else
      {
        var ad=getName("ad")[0];
        if(name=="next")
        {
          adShift(ad,"next");
        }
        else if(name=="prev")
        {
          adShift(ad,"prev");
        }
      }
    }

    window.onload= function () {
    new Rotator();
    }
  </script>
</body>
</html>
