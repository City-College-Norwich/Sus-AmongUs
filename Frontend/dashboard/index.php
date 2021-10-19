<?php include "../authentication/includes/checkAuth.php"; ?>
<?php include "./header.php"; ?>

<html lang="en">
  <div class="container-fluid">
    <div class="row">
      <?php include "./sidebarMenu.php"; ?>
      <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
        <?php 
        
        $selected = "IDLE";

        if(isset($_GET['selected'])) {
          $selected = $_GET['selected'];
        }

        switch($selected) {
          case "IDLE":
            break;
          case "GAMES_LOGS":
            include "./pages/pastGames/index.php";
            break;
        }
        
        ?>
      </main>
    </div>
  </div>
</html>