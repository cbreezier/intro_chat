<?php
  session_start();
  if (isset($_GET['room'])) {
    $_SESSION['room'] = $_GET['room'];
  }
  $room = isset($_SESSION['room']) ? $_SESSION['room']:'Main';
  if (isset($_GET['user'])) {
    $_SESSION['user'] = $_GET['user'];
  }
  $user = isset($_SESSION['user']) ? $_SESSION['user']:'User';
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
    <title>Chatbot Room <?=$room?></title>
  </head>
  <body>
    <div class="container">
      <div class="row">
        <div class="col-sm-3">
          <div id="botList">
            <ul class="nav nav-pills nav-stacked">
              <li><a data-name="Main" href="?room=Main">Main</a></li>
            </ul>
            <div id="uploadFile">
              <form action="upload.php" method="post" enctype="multipart/form-data">
                <input type="file" id="fileSelect" name="file"></input>
                <br>
                <button type="submit" id="btnUpload" class="btn btn-primary">Upload</button>
              </form>
              <a href="notes.html">Need some pointers to make your own chatbot?</a>
            </div>
          </div>
        </div>
        <div class="col-sm-9">
          <h1>Room <?=$room?> - Welcome <?=$user?></h1>
          <div id="messages"></div>

          <div class="row">
            <div class="col-sm-4">
              <div class="input-group">
                <span class="input-group-btn">
                  <button id="changeUser" class="btn btn-primary" type="button">Change</button>
                </span>
                <input type="text" id="user" class="form-control" value="<?=$user?>"></input>
              </div>
            </div>
            <div class="col-sm-8">
              <input type="text" id="message" class="form-control" placeholder="Message" autofocus></input>
            </div>
          </div>
        </div>
      </div>
    </div>
    <script>
      var room = '<?=$room?>';

      $("#changeUser").click(function (e) {
        var user = $("#user").val();
        window.location.href = '?user='+user;
      });
      
      $("#message").on("keyup", function (e) {
        if (e.keyCode == 13) {
          e.preventDefault();
          var message = $("#message").val();
          $("#message").val('');

          $.post("receiver.py", {room: room, user: '<?=$user?>', message: message}, function (data) {
            console.log(data);
          });
        }
      });

      function markActiveBotList() {
        $("#botList li").removeClass('active');
        $("#botList a").filter(function () {
          return $(this).data('name') === room;
        }).parent().addClass('active');
      }

      function updateBotList() {
        var botList = [];
        $("#botList a").each(function () {
          var name = $(this).data('name');
          var time = $(this).data('time');
          if (name == 'Main') {
            return;
          }
          botList.push({name: name, time: time});
        });
        $.post("bot_status.php", {bot_list: botList}, function (data) {
          if (data) {
            var botList = JSON.parse(data);
            botList.forEach(function (bot) {
              if (bot.status == 'deleted') {
                $("#botList a").filter(function () {
                  return $(this).data('name') === bot.name;
                }).parent().remove();
              }
              if (bot.status == 'updated') {
                $("#botList a").filter(function () {
                  return $(this).data('name') === bot.name;
                }).data('time', bot.time).empty().append(bot.name+'<span class="badge pull-right">Updated</span>');
              }
              if (bot.status == 'new') {
                $("#botList ul").append('<li><a data-time="'+bot.time+'" data-name="'+bot.name+'" href="?room='+bot.name+'">'+bot.name+'<span class="badge pull-right">New</span></a></li>');
              }
              if (bot.status == 'first') {
                $("#botList ul").append('<li><a data-time="'+bot.time+'" data-name="'+bot.name+'" href="?room='+bot.name+'">'+bot.name+'</a></li>');
              }
            });
          }
          markActiveBotList();
          setTimeout(updateBotList, 1000);
        });
      }

      function checkMessages() {
        var num_messages = $(".message").length;
        console.log('Checking for new messages - current messages:', num_messages);
        $.post("sender.py", {room: room, num_messages: num_messages}, function (data) {
          if (data == 'No new messages') {
            console.log('No new messages\n');
          } else {
            console.log(data);
            var messages = JSON.parse(data);
            console.log('Received', messages.length, 'new messages\n');
            messages.forEach(function (message) {
              $("#messages").prepend('<div class="message"><i>('+message.message_time+') </i><b>'+message.user+': </b>'+message.message+'</div>');
            });
          }
          checkMessages();
        });
      }

      $(document).ready(function() {
        checkMessages();
        updateBotList();
      });
    </script>
  </body>
</html>