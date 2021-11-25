<?php 
if(!isset($_GET["user"])) {
    echo "NOTHING SELECTED CALLING die()";
    die();
}
          include "../mysql_conn.php";

          $id = $_GET["user"];

          $sql = "SELECT * FROM users WHERE id=$id";
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
              </tr>
          <?php }
          } else {
            // TODO: This should display under the table headers not above them 
            echo "0 results";
          }
          $conn->close();
        ?>
</div>
