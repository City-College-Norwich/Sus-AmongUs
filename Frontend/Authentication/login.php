<?php
    include "includes/header.php";
    include "includes/reffererHandler.php";
    $Err = isset($_GET['ERROR']) ? $_GET['ERROR'] : '';

?>

<!-- Used to overlay notifications such as login failed etc. -->
<div id="overlay">
  
</div>

<script>
  function errorToColour(err) {
    <?php #include "warnings_colours.php"; ?>
    var arr = {"LOGIN_SUCCESS": "GREEN", "LOGIN_FAILED": "RED"};
    console.log(arr);
    return(arr[err] ? arr[err] : err);
  }
  function errorToText(err) {
    <?php #include "warnings_text.php"; ?>
    var arr = {
      "LOGIN_SUCCESS": "Successfully Logged In", 
      "LOGIN_FAILED": "Failed to login, Username/Email or Password is invalid! Please try again!"
    };
    console.log(arr);
    return(arr[err] ? arr[err] : err);
  }
  function colourTOtype(colour) {
    switch(colour){
      case("BLUE"):
        return("alert alert-primary");
      case("LIGHT_GREY"):
        return("alert alert-secondary");
      case("GREEN"):
        return("alert alert-success");
      case("RED"):
        return("alert alert-danger");
      case("YELLOW"):
        return("alert alert-warning");
      case("CYAN"):
        return("alert alert-info");
      case("WHITE"):
        return("alert alert-light");
      case("GREY"):
        return("alert alert-dark");
    }
  }
  function createNotification(title, colour) {
    
    const newDiv = document.createElement("div");
          newDiv.setAttribute("class", colourTOtype(colour));
          newDiv.setAttribute("role", "alert");

    // Could probably shorten even more, but honestly does it matter?? also do i care??? no.
    newDiv.appendChild(document.createTextNode(title));

    var divthing = document.getElementById("overlay").appendChild(newDiv);
  }
  <?php
  $Err = isset($_GET['ERROR']) ? $_GET['ERROR'] : '';

  if($Err != "") { ?>
    createNotification(errorToText("<?php echo $Err; ?>"), errorToColour("<?php echo $Err; ?>"));
  <?php } ?>
</script>

  <body class="text-center">  
    <main class="form-signin">
      <form data-bitwarden-watching="1" action="./login_handler.php" method="post" name="Login_Form">
        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
        <div class="form-floating">
          <input name="email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
          <label for="floatingInput">Email address</label>
        </div>
        <div class="form-floating">
          <input name="password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">Password</label>
        </div>    
        <div class="form-floating">
          <input hidden="True" name="refferer" value="<?php echo $forward; ?>" id="refferer" placeholder="<?php echo $forward; ?>">
        </div>
        <div class="checkbox mb-3">
          <label>
            <!-- Its funny because this doesnt have any function as i dont do anything to index this posted data
                could easily create a cookie with session tokens, But someone else can do that. -->
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
      </form>
    </main>
  </body>
</html>
