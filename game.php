<?php
  if (isset($_GET['game'])) {
    $game = $_GET['game'];
  } else {
    $game = '';
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
    <title><?=$game ? 'Playing '.$game : 'No game selected' ?></title>
  </head>
  <body>
    <?php if ($game): ?>
      <div class="custom-container">
       <h1>Playing <?=$game?></h1>
       <div id="messages"></div>
        <input type="text" id="message" class="form-control" placeholder="Message" autofocus maxlength="60"></input>
      </div>
      <script>
        var game = '<?=$game?>';
        
        $("#message").on("keyup", function (e) {
          if (e.keyCode == 13) {
            e.preventDefault();
            var newMessage = $("#message").val();
            $("#message").val('');
            
            $("#messages").append('<div class="userInput">'+newMessage+'</div>');
            
            var messages = [];
            $(".userInput").each(function () {
              messages.push($(this).text());
            });
            
            console.log(messages);

            //$.post("receiver.py", {botname: game, messages: messages}, function (data) {
            //  console.log(data);
            //  $("#messages").append('<div class="botInput">'+data+'</div>');
            //});
          }
        });
      </script>
    <?php else: ?>
      <div class="container">
        <h1>Please select a game</h1>
      </div>
    <?php endif; ?>
  </body>
</html>

