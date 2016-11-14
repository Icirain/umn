<!DOCTYPE html>
<html lang="en">
<head>
 <link rel="stylesheet" type="text/css" href="scheduleStyle.css">
 <title>Rui's Calendar</title>
 <meta charset="UTF-8">

 <style type="text/css">
      html, body { height: 100%; margin: 0; padding: 0; }
      div.map{ height: 100%;
      margin-left: 200px;
      margin-right: 200px;
      margin-top: 50px;
       }
    </style>
</head>
 <body>
  <h1>Rui's Calendar</h1>

   <nav>
     <button onclick="{location.href='calendar.php'}">My Calendar</button>
     <button onclick="{location.href='input.php'}">Form Input</button>
   </nav>
  <div class="calendar">
    <?php
    $event_list = array(
      "Mon" => array(),
      "Tue" => array(),
      "Wed" => array(),
      "Thu" => array(),
      "Fri" => array()
      );
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
     function cmp ($a,$b)
     {
      if ($a[Start]>$b[Start])
      {
        return 1;
      }
      else if ($a[Start]<$b[Start])
      {
        return -1;
      }
      else
      {
        return 0;
      }  
     }
     foreach ($event_list as $key => $value) 
     {
       usort($event_list[$key], 'cmp');
     }
     if ($empty != 0)
     {        
             echo "<table>";
             
             foreach ($event_list as $day_event) 
             {
               if (count($day_event) != 0)
               {
                echo "<tr>";
                echo "<th>";
                echo $day_event[0]["Weekday"];
                echo "</th>";
                foreach ($day_event as $single_event ) 
                {
                   echo "<td>";
                   echo "<span>";
                   echo $single_event["Event"];
                   echo "</span>";
                   echo "<br>";
                   echo "<span>";
                   echo $single_event["Start"];
                   echo "</span>";
                   echo "<br>";
                   echo "<span>";
                   echo $single_event["End"];
                   echo "</span>";
                   echo "<br>";
                   echo "<span class='location'>";
                   echo $single_event["Location"];
                   echo "</span>";
                   echo "<br>";
                   echo "<img  class='hidden_img' src='Error-404.png' alt='photo'>";
                   echo "</td>";
                }

               }  
             }
             echo "</table>";
      }
      else 
      {
        echo "<span>";
        echo "No events in the Calendar";
        echo "</span>";
      }
     ?>
  </div>
  <div class="mapSearch">
    <input type="text" value="Keller Hall,MN" class="address">
    <input type="button" value="search" class="search">
    
    <input type="text" value='input radius' class="radius">
    <input type="button" value='search' class="seek">
  </div>
  <div class='map'>
  </div>
  <script type="text/javascript">
    var initLoc=[{lat:44.9753029,lng:-93.23229500000002},//akerman
                 {lat:44.9739602,lng:-93.2330897},//amundson
                 {lat:44.9740787,lng:-93.23738839999999},//bruinks
                 {lat:44.9755702,lng:-93.2373867}//fraser_hall               
                ];
    var bound = {
                  west: -93.244254,
                  east: -93.223162,
                  south:44.971960 ,
                  north:44.971961
                 };
    var initContent=['CSCI 4041 in Akerman Hall','CSCI 4041 Dis in Amundson Hall','CSCI 4131 in Bruininks Hall','CSCI 4707 in Fraser Hall'];
    var test1=[{lat:44.9739602,lng:-93.2330897}];
    var map;
    var loc;
    var publicWin;
    function search_img(temp)
    {
      var index = 0;
      var img_set = document.getElementsByClassName('hidden_img');
      for (var i = 0; i<img_set.length; i++) 
      {
        if(temp == img_set[i])
        {
          index = i;
        }
      }
      temp.style.opacity=1;
      destination = document.getElementsByClassName('location')[index];
      var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
               if(this.responseText != '')
              {
               document.getElementsByClassName('hidden_img')[index].src = this.responseText;
              }
            }
        };
        xmlhttp.open("GET", "get_img.php?q=" + destination.innerHTML, true);
        xmlhttp.send();
      

    }
    function img_SetListener()
    {
      var img=document.getElementsByClassName('hidden_img');
      var len=img.length;
      for (var i = 0; i < len; i++) {
        var temp=img[i];
        temp.addEventListener('mouseover',function(){
        search_img(this);
        });
      }
      for (var i = 0; i < len; i++) {
        var temp=img[i];
        temp.addEventListener('mouseout',function(){
        this.style.opacity=0;
        });
      }
      
    }
    //var img=document.getElementsByClassName('img_hidden');
    //img[0].addEventListener('mouseover',function(){
      //img[0].style.opacity=1;
    //});
    img_SetListener();
    function initMap() {
     map = new google.maps.Map(document.getElementsByClassName('map')[0], {
     center: {lat: 44.9745476, lng: -93.23223189999999},
     zoom: 16
     });
    var marker=new Array();
    var geocoder = new google.maps.Geocoder();
    init_Marker(geocoder,map);
      
    var infowindow = new google.maps.InfoWindow({
     content: 'Amundson Hall'
     });
    publicWin= new google.maps.InfoWindow({
     content: 'default'
     });
    document.getElementsByClassName('search')[0].addEventListener('click', function() {
     geocodeAddress(geocoder, map);
     //GetName('address')[0].value=loc.lat();
    });
    var service=new google.maps.places.PlacesService(map);
     //service.nearbySearch({location:test1,radius:500,type:['store']},callback);
    document.getElementsByClassName('seek')[0].addEventListener('click',function(){
      service.nearbySearch({location:loc,radius:GetName('radius')[0].value,type:['restaurant']},callback1);
    });
  }
    function initMarker(){
      var marker=new Array();
      for (var i = 0; i < 4; i++)
        {
            marker[i]=new google.maps.Marker({
             position:initLoc[i],
            map:map,
            title:'1',
            animation: google.maps.Animation.BOUNCE
             });
        }
        marker[1].addListener('click',function(){
          publicWin.open(map,marker[1]);
          publicWin.setContent(initContent[1]);
        });
        marker[2].addListener('click',function(){
          publicWin.open(map,marker[2]);
          publicWin.setContent(initContent[2]);
        });
        marker[0].addListener('click',function(){
          publicWin.setContent(initContent[0]);
          publicWin.open(map,marker[0]);
        });
        marker[3].addListener('click',function(){
          publicWin.setContent(initContent[3]);
          publicWin.open(map,marker[3]);
        });

    }
    function callback1(results,status){
      if(status===google.maps.places.PlacesServiceStatus.OK){
        /*var marker=new google.maps.Marker({map:map,position:results[0].geometry.location,title:'a store'});*/
        setMarker(results);
      }
     }
    function setMarker(results){
      for (var i = 0; i<results.length; i++) {
        var service=new google.maps.places.PlacesService(map);
        service.getDetails({placeId:results[i].place_id},callback2);
      }
     }
     function callback2(place,status){
      if (status === google.maps.places.PlacesServiceStatus.OK){
        var marker=new google.maps.Marker(
                                         {position:place.geometry.location,
                                          map:map,
                                          title:place.name}
                                         );
        //var infowindow=new google.maps.InfoWindow( {content:'default'} );
        marker.addListener('click',
                            function(){
                              publicWin.setContent(place.formatted_address);
                              publicWin.open(map,marker);
                            }
                          );
      }
     }
    function geocodeAddress(geocoder, resultsMap) {
     var address = document.getElementsByClassName('address')[0].value + ',Minneapolis';
     geocoder.geocode({'address': address,bounds : bound}, function(results, status) {
      if (status === google.maps.GeocoderStatus.OK) {
       resultsMap.setCenter(results[0].geometry.location);
       var marker = new google.maps.Marker({
                                            map: resultsMap,
                                            position: results[0].geometry.location,
                                            title:results[0].formatted_address
                                          });
       
       marker.addListener('click', function(){
        publicWin.setContent(results[0].formatted_address);
        publicWin.open(map,marker);
       });
       loc=results[0].geometry.location;
      } else {
      alert('Geocode was not successful for the following reason: ' + status);
      }
     });
    }
    function init_Marker(geocoder, resultsMap) {
         
         var location = document.getElementsByClassName('location');
         for (var i = 0; i<location.length; i++) 
         {
             var address = location[i].innerHTML+ ',Minneapolis';
             geocoder.geocode({'address': address,bounds : bound}, function(results, status) {
              if (status === google.maps.GeocoderStatus.OK) {
               resultsMap.setCenter(results[0].geometry.location);
               var marker = new google.maps.Marker({
                                                    map: resultsMap,
                                                    position: results[0].geometry.location,
                                                    title:results[0].formatted_address
                                                  });
               
               marker.addListener('click', function(){
                publicWin.setContent(results[0].formatted_address);
                publicWin.open(map,marker);
               });
               loc=results[0].geometry.location;
              } else {
              alert('Geocode was not successful for the following reason: ' + status);
              }
             });
        }
    }
  </script>
  <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDP7pA-7IosVJE6hnZ2yME6vdCsjRNTh2M&callback=initMap&libraries=places" >
  </script>
 </body>
</html>