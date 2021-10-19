<?php
          include "../../mysql_conn.php";

          header('Content-Type: text/csv; charset=utf-8');  
          header('Content-Disposition: attachment; filename=data.csv');  
          $output = fopen("php://output", "w");
          fputcsv($output, array('id', 'time_date', 'player_count', 'match_length', 'winner_id', 'win_method'));  
          $query = "SELECT * FROM past_games";  
          $result = mysqli_query($conn, $query);  
          while($row = mysqli_fetch_assoc($result))  
          {  
               fputcsv($output, $row);  
          }  
          fclose($output);  
?>
