<?php 
include "../globals.php";
include "ipInfo.php";
include "includes/header.php";

?>

<?php 
  $refferer = isset($_POST['refferer']) ? $_POST['refferer'] : 'N/A';
  $postedRefferer = $refferer; 

  if(isset($_POST['refferer']))
  {
    $refferer = $_POST['refferer'];
    if($debugMode) echo "<br>posted refferer: " . $refferer;
  }
  else if(isset($_SERVER['HTTP_REFERER'])) {
    if($debugMode) echo "<br>HTTP_REFERER: " . $_SERVER['HTTP_REFERER'];
    $refferer = parse_url($_SERVER['HTTP_REFERER'], PHP_URL_PATH);
  } else {
    $refferer = "";
  }

  $calculatedRefferer = $refferer;
  $forward = "/index.php";
  
  // If theres a valid predefined refferer then just use this :|
  //    invalidates the code above but /shrug am i going to do anything about it not rn
  if($refferer != "") {
    $forward = $refferer;
  }

  // Debugging stuff, very handy.
  if($debugMode) {
    echo "sent refferer: " . $postedRefferer;
    if(isset($_SERVER['HTTP_REFERER'])) {
      echo "<br>HTTP_REFERER: " . $_SERVER['HTTP_REFERER'];
      echo "<br>HTTP_REFERER: " . parse_url($_SERVER['HTTP_REFERER'], PHP_URL_PATH);
    }
    echo("<br>Final Calculated Refferer: " . $refferer);
    echo "<br>Forwarding to: " . $forward;
  }

  // I honestly hate this code so bad, 
  //  All it does it create a invis Form fills it with data and then clicks it,
  //  Its annoying because i cant think of a better way to do it.
  function forwardError($url, $error) {
           echo    '<form method="POST" action="' . $url . '" name="forwardForm" style="display:none">
                        <input name="ERROR" value=' . $error . '>
                        <button type="submit" name="submit" id="forwardForm-submit-btn"></button>
                    </form>';
                    ?>        <script>
                    $('#forwardForm-submit-btn').click();
                    </script><?php
  }

// Simply redirects the user. when errored.
function forward($url, $error) {
  echo "<br> forwaring to location: " . $url . "?ERROR=" . $error;
  header("location: " . $url . "?ERROR=" . $error );
}

function login($leftSideInput, $hash, $forward) {
  echo $hash;

  // This is only here for local testing as we cant install mysql server on the college computers :|
  if(null !== defined("mysqli")) {
    $arr = array("Test"=>"098f6bcd4621d373cade4e832627b4f6");

    echo ("SQL Isnt installed on the server defaulting to local login array");

    try {
      echo "<br>" . $leftSideInput;
      echo "<br>" . $hash;
      echo "<br>" . $forward;
      echo "<br>" . $arr[$leftSideInput];
      echo "<br> dumb person thing" . $calculatedRefferer;

      if(isset($arr[$leftSideInput])) {
        echo "<br> Valid login";
        if($hash == $arr[$leftSideInput]) {
          $_SESSION['UserData']['Username'] = $leftSideInput;

          // Probably not needed but maybe handy in future, commenting out for now
          // $_SESSION['UserData']['db_entry'] = $row;
          $_SESSION['UserData']['RANK'] = "Administrator";
          //forwardError($calculatedRefferer, "LOGIN_SUCCESS");
          echo $forward;
          return;
        }
      }
      //forwardError("/", "LOGIN_FAILED");
    } 
    catch (exception $e) {

    }
    return;
  }
  include "../mysql_conn.php"; // Import the sql connection

    $leftSideInput = filter_var($leftSideInput, FILTER_SANITIZE_STRING);
    $sql = 
    "SELECT 
              * 
     FROM 
              users 
     WHERE 
              email='$leftSideInput' AND hash='$hash' 
          OR 
              username='$leftSideInput' AND hash='$hash'";
              
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
      $row = $result->fetch_assoc();
      $_SESSION['UserData']['Username'] = $row["username"];

      // Probably not needed but maybe handy in future, commenting out for now
      // $_SESSION['UserData']['db_entry'] = $row;
      $_SESSION['UserData']['RANK'] = $row["rank"];
      forward($forward, "LOGIN_SUCCESS");
    }
    else {
      forward($forward, "LOGIN_FAILED");
    }
    $conn->close();
}

if(!isset($_COOKIE["PHPSESSID"]))
{
  session_start();
}
$_SESSION['UserData']['IP'] = getUserIP();

$Username = isset($_POST['email']) ? $_POST['email'] : '';
$Password = isset($_POST['password']) ? md5($_POST['password']) : '';
login($Username, $Password, $forward);

?>


