<?php
  if ($_FILES["file"]["error"] > 0) {
    echo "<pre>Error: " . $_FILES["file"]["error"] . "</pre>";
  } else {
    // echo "Upload: " . $_FILES["file"]["name"] . "<br>";
    // echo "Type: " . $_FILES["file"]["type"] . "<br>";
    // echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
    // echo "Stored in: " . $_FILES["file"]["tmp_name"];
    $message = '';
    $extension = end(explode(".", $_FILES["file"]["name"]));
    if ($_FILES["file"]["type"] !== 'text/plain' || $extension !== 'py') {
      $message = "You must upload a valid .py file, not a ".$_FILES["file"]["type"]." .".$extension." file. Please try again.";
    } else {
      $message .= "Your file is OK and has been uploaded!<br>";
      move_uploaded_file($_FILES["file"]["tmp_name"], "chatbots/" . $_FILES["file"]["name"]);
    }
  }
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="main.css">

    <script src="https://code.jquery.com/jquery.js"></script>
  </head>
  <body>
    <div class="container">
      <h1>Upload File Page</h1>
      <p class="lead"><?=$message?></p>
    </div>
  </body>
</html>