<?php
// Check if the current user is authenticated or even logged in :| simple really.
    session_start();
    if(!isset($_SESSION['UserData']['Username'])){
        header("location:/authentication/login.php");
        exit;
    }
?>
