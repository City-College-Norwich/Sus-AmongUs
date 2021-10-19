<?php 
  include "../globals.php";

  // An interesting way to detect how and what method was used 
  //    to get to the page currently being displayed
  //
  // This is done by checking if a varible called "refferer" was POSTed to the page,
  //  if so this will contain the url of the previous page, simplifiying this alot
  //  if thats not the case it will then check for the http header "HTTP_REFERER",
  //  checks for anything interesting or cool, if that doesnt turn up anything interesting,
  //  the script then it will default to "/index.php" as thats the default url page,

  $refferer = isset($_POST['refferer']) ? $_POST['refferer'] : 'N/A';

  if(isset($_POST['refferer'])) {
    $refferer = $_POST['refferer'];
  }
  else if(isset($_SERVER['HTTP_REFERER'])) {
    $refferer = parse_url($_SERVER['HTTP_REFERER'], PHP_URL_PATH);
  } else {
    $refferer = "";
  }

  $calculatedRefferer = $refferer;
  $forward = "/index.php";
  
  if($refferer != "") {
    $forward = $refferer;
  }

  // This is the most helpful debugging info out of this entire script
  if($debugMode) {
    if(isset($_SERVER['HTTP_REFERER'])) { // Simple check prevents error when this header doesnt exist as sometimes it wont exist. (this happens alot)
      echo "posted refferer: " . $refferer;
      echo "<br>HTTP_REFERER: " . $_SERVER['HTTP_REFERER'];
      echo "<br>HTTP_REFERER: " . parse_url($_SERVER['HTTP_REFERER'], PHP_URL_PATH);
    }
    echo("<br>Final Calculated Refferer: " . $refferer);
    echo "<br>Forwarding to: " . $forward;
  }

?>