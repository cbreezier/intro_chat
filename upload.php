<?php
  $fromPage = "index.php";
  if (isset($_POST['chatbot_type'])) {
    if ($_POST['chatbot_type'] == 'group') {
      $folder = 'group_chatbots/';
    } else if ($_POST['chatbot_type'] == 'single') {
      $folder = 'chatbots/';
    } else if ($_POST['chatbot_type'] == 'text_game') {
      $folder = 'text_game/';
    } else if ($_POST['chatbot_type'] == 'graphical') {
      $folder = 'graphical/';
    } else if ($_POST['chatbot_type'] == 'bouncingball') {
      $folder = 'bouncingball/';
      $fromPage = "bouncing.html";
      $bouncecount = file_get_contents("bouncingball/count.txt");
      foreach (explode("\n", $bouncecount) as $line) {
        $info = explode(' ', $line);
        if (strlen($line) > 0) {
          $count[$info[0]] = intval($info[1]);
        }
      }
      $filename = $_FILES["file"]["name"];
      if (isset($count[$filename])) {
        $count[$filename]++;
      } else {
        $count[$filename] = 1;
      }

      $newfilecontents = "";
      foreach (array_keys($count) as $key) {
        $newfilecontents .= $key." ".$count[$key]."\n";
      }
      file_put_contents("bouncingball/count.txt", $newfilecontents);
    } else {
      $message = "<b>Error:</b> Chatbot type unrecognized - this is not your fault we screwed up.";
    }
  } else {
    $message = "<b>Error:</b> Refreshing this page does nothing.";
  }
  if (isset($folder)) {
    if ($_FILES["file"]["error"] > 0) {
      $message = "<b>Error: ".$_FILES["file"]["error"]."</b> Please select a file to upload.";
    } else {
      // echo "Upload: " . $_FILES["file"]["name"] . "<br>";
      // echo "Type: " . $_FILES["file"]["type"] . "<br>";
      // echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
      // echo "Stored in: " . $_FILES["file"]["tmp_name"];
      $extension = explode(".", $_FILES["file"]["name"]);
      $extension = end($extension);
      if ($extension !== 'py') {
        $message = "You must upload a valid .py file, not a ".$_FILES["file"]["type"]." .".$extension." file. Please try again.<br>";
      } else {
        $message = "Your file is OK and has been uploaded to $folder!<br>";
        move_uploaded_file($_FILES["file"]["tmp_name"], $folder.$_FILES["file"]["name"]);
      }
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
      <br>
      <a href="<?=$fromPage;?>">Return</a>
    </div>
  </body>
</html>
