        <?php 
          include "../mysql_conn.php";

          $sql = "SELECT * FROM past_games";
          $result = $conn->query($sql);

          if ($result->num_rows > 0) {
            // output data of each row
            while($row = $result->fetch_assoc()) {
              ?>
              <tr>
              <td><?php echo $row["id"]; ?></td>
              <td><?php echo $row["time_date"]; ?></td>
              <td><?php echo $row["player_count"]; ?></td>
              <td><?php echo $row["match_length"]; ?></td>
              <td><?php echo $row["winner_id"]; ?></td>
                <td><?php echo $row["win_method"]; ?></td>
              </tr>
          <?php }
          } else {
            // TODO: This should display under the table headers not above them 
            echo "0 results";
          }
          $conn->close();
        ?>
</div>
