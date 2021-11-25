<?php
$host = "192.168.1.115";
$username = "web";
$password = "BUIOSDBfOAJDOPASdjal334VBUIOV89GVuiv";
$dbname = "among_db";

// Create connection
$conn = new mysqli($host, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

?>
