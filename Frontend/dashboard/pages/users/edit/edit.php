
<body class="bg-light">
    
<div class="container">
  <main>
    <div class="row g-3">
      <div class="col-md-5 col-lg-8">
        <h4 class="mb-3"></h4>
        <form action="./pages/users/edit/publishData.php" method="post">
          <div class="row g-3">

            <div class="col-12">
              <label for="username" class="form-label">Username</label>
              <div class="input-group has-validation">
                <span class="input-group-text">@</span>
                <input type="text" class="form-control" id="username" value="niN" placeholder="Username" required>
                  <div class="invalid-feedback">
                      Valid Username Is Requireds
                    </div>
              </div>
            </div>

            <div class="col-12">
              <label for="email" class="form-label">Email <span class="text-muted">(Optional)</span></label>
              <input type="email" class="form-control" id="email" value="niN" placeholder="you@example.com">
              <div class="invalid-feedback">
                Please enter a valid email address.
              </div>
            </div>

            <div class="col-12">
              <label for="number" class="form-label">Phone Number </label>
              <input type="number" class="form-control" id="number" value="niN" placeholder="071111111">
              <div class="invalid-feedback">
                Please enter a valid phone number.
              </div>
            </div>
            
            <div class="col-12">
              <label for="password" class="form-label">Password </label>
              <input type="password" class="form-control" id="password" value="" placeholder="Enter New Password">
              <div class="invalid-feedback">
                Enter a valid password
              </div>
            </div>
          </div>

          <hr class="my-4">

          <button class="w-20 btn btn-success btn-lg" type="submit">Submit</button>
          <button class="w-20 btn btn-danger btn-lg" href="../../">Cancel</button>
        </form>
      </div>
    </div>
  </main>
</div>


      <script src="form-validation.js"></script>
  </body>
</html>
