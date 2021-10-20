<?php
          include "../../../mysql_conn.php";

          header('Content-Type: text/csv; charset=utf-8');  
          header('Content-Disposition: attachment; filename=data.csv');  
          $output = fopen("php://output", "w");
          fputcsv($output, array('id', 'username', 'email', 'phoneNumber', 'rank'));  
          $query = "SELECT `id`, `username`, `email`, `phoneNumber`, `rank` FROM users";  
          $result = mysqli_query($conn, $query);  
          while($row = mysqli_fetch_assoc($result))  
          {  
               fputcsv($output, $row);  
          }  
          fclose($output);  
?>
