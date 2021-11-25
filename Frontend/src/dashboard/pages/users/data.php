        <?php 
          include "../mysql_conn.php";

          $sql = "SELECT * FROM users";
          $result = $conn->query($sql);
          
          if ($result->num_rows > 0) {
            // output data of each row
            while($row = $result->fetch_assoc()) {
              ?>
              <tr>
              <td><?php echo $row["id"]; ?></td>
              <td><?php echo $row["username"]; ?></td>
              <td><?php echo $row["email"]; ?></td>
              <td><?php echo $row["phoneNumber"]; ?></td>
              <td><?php echo $row["rank"]; ?></td>
              <td><a class="btn btn-primary" role="button" href="http://<?php echo $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"]?>_EDIT&user=<?php echo $row["id"]; ?> ">Edit</a></td>
              </tr>
          <?php }
          } else {
            // TODO: This should display under the table headers not above them 
            echo "0 results";
          }
          $conn->close();
        ?>
</div>
