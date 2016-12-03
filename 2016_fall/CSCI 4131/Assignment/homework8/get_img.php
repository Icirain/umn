<?php
  $q = $_REQUEST["q"];
  $event_list = array(
      "Mon" => array(),
      "Tue" => array(),
      "Wed" => array(),
      "Thu" => array(),
      "Fri" => array()
      );
   $response='';
    $empty = 1;
    $myfile = fopen ("calendar.txt","r");
    $all = fread($myfile, filesize("calendar.txt"));
    fclose($myfile);
    $event = explode("\n", $all);
    if ($event[count($event)-1] == "")
     {
      unset($event[count($event)-1]);
     }
    if(count($event) == 0)
    {
      $empty = 0;
    }
    foreach ($event as $key) 
     {
      $element= json_decode($key,true);
      array_push($event_list[$element["Weekday"]], $element);
     }
    foreach ($event_list as $day_event) 
     {
     	foreach ($day_event as $single_event ) 
        {
        	if($single_event['Location'] == $q)
        	{
              $response = $single_event['img'];
        	}
        }
     }
     echo $response;
?>