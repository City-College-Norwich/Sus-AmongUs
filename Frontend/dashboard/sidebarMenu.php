<?php 
// I love what this function does, the implementation is weird, but it works great.
function isActive($str) {
  if($str == $_SERVER['QUERY_STRING']) {
    echo " active";
  }
}
?>
<nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="position-sticky pt-3">
        <ul class="nav flex-column">

        <?php 
          $arr = array(
            ["IDLE", "Dashboard"],
            ["GAMES_LOGS", "Previous Games!"],
            ["Example", "EfgdfgxMPaspsdfo"],
            ["Example", "dfgxdgdfgMfsdfssdfo"],
            ["Example", "fgdExMdgdfgasssdfo"],
            ["Example", "EfgdfgxMPaspdmfgddsfsdo"],
            
          );
          foreach ($arr as &$value) {
            ?>
                    <li class="nav-item">
                      <a class="nav-link <?php isActive("selected=" . $value[0]); ?>" aria-current="page" 
                       href="./?selected=<?php echo $value[0]; ?>#">
                        <span data-feather="home"></span>
                        <?php echo $value[1]; ?>
                      </a>
                    </li>
            <?php
          }
          // $arr is now array(2, 4, 6, 8)
          unset($value); // break the reference with the last element
        ?>

        <?php if($_SESSION['UserData']["RANK"] == "Administrator") { ?>

          <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
            <span>Administrator panel</span>
          </h6>

          <ul class="nav flex-column mb-2">
            <li class="nav-item">
              <a class="nav-link" href="#">
                <span data-feather="file-text"></span>
                Users
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <span data-feather="file-text"></span>
                Authentication Log
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">
                <span data-feather="file-text"></span>
                Stats
              </a>
            </li>
          </ul>

        <?php } ?>
      </div>
    </nav>
    