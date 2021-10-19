<?php
// A very nice cool script to handle 
//  IPv4 Public, Private and or Reserved Address Blocks (such as 10.0.0.0/8, 127.0.0.0/8 or even 255.255.255.255/32 )

  // Used to check if an IP is Private or Reserved.
  function isPrivIP($ip) {
    if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4 | FILTER_FLAG_NO_PRIV_RANGE |  FILTER_FLAG_NO_RES_RANGE) === false) {
      return true;
    }
    return false;
  }

  // Used to check if the given IPv4/6 Address is even valid
  function isValidIpAddress($ip) {
    if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4 | FILTER_FLAG_IPV6) === false) {
      return false;
    }
    return true;
  }

  // Get ip geo info
  function getIP_Info($ip) {
    if(isPrivIP($ip)) {
      return("PRIVATE_IP");
    }
    return json_decode(file_get_contents("http://ipinfo.io/{$ip}/json"));
  }
  
  // Get ip geo info... BUT JSON  
  function getIP_Info_JSON($ip) {
    if(isPrivIP($ip)) {
      return("PRIVATE_IP");
    }
    return file_get_contents("http://ipinfo.io/{$ip}/json");
  }

  // Standard function to get an IP of a user, pretty standard, 
  //    Checks as many headers as possible to try get the most accurate ip 
  //      without being invasive eg using WebRTC
  function getUserIP() {
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
      return($_SERVER['HTTP_CLIENT_IP']);
    }
    if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
      return($_SERVER['HTTP_X_FORWARDED_FOR']);
    }
    return($_SERVER['REMOTE_ADDR']);
  }
?>