<!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script> -->

<div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
          <h1 class="h2">Past Games!</h1>
          <div class="btn-toolbar mb-2 mb-md-0">
            <div class="btn-group me-2">
              <script>
                // Ignore this, its not needed, will probably reuse at some point for clearing DBs etc later though.
                //
                // function clearMessageLog() {
                //     var xhr = new XMLHttpRequest();
                //     xhr.open("POST", "./clearMessageLog.php", true);
                //     xhr.setRequestHeader('Content-Type', 'application/html');
                //     xhr.send();
                //     setTimeout(() => {  reload() }, 100); // Dont say anything about this i stg
                // }
                function exportCSV() {
                    location.href = "./pages/pastGames/export.php";
                }
                function reload() {
                    location.reload(); 
                }
              </script>
              <!-- <button type="button" onclick="clearMessageLog()" class="btn btn-sm btn-outline-secondary">Clear</button> -->
              <button type="button" onclick="reload()" class="btn btn-sm btn-outline-secondary">Reload</button>
              <button type="button" onclick="exportCSV()" class="btn btn-sm btn-outline-secondary">Export</button>
            </div>
          </div>
        </div>
        <div class="table-responsive">
          <table class="table table-striped table-sm">
            <thead>
              <tr>
              <th scope="col">#</th>
              <th scope="col">Date</th>
                <th scope="col">Player Count</th>
                <th scope="col">Match Length</th>
                <th scope="col">WinnerID</th>
                <th scope="col">WinMethod</th>
              </tr>
            </thead>
            <tbody id="ENTRYS">
              <?php 
               include "data.php"; 
              ?>
            </tbody>
          </table>
        </div>
        