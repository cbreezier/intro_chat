<?php
  $clientBotList = $_POST['bot_list'] ? $_POST['bot_list']:array();
  function array_in_array($arr1, $arr2) {
    foreach ($arr1 as $item) {
      if (!in_array($item, $arr2)) {
        return false;
      }
    }
    return true;
  }

  $attempts = 0;
  while ($attempts < 20) {
    $bots = scandir("group_chatbots");

    if (sizeof($bots) !== sizeof($clientBotList) || !array_in_array($bots, $clientBotList)) {
      break;
    }
    sleep(1);
    $attempts++;
  }

  echo '<h3>Bots in Main Lobby</h3>';
  $bots = scandir("group_chatbots");
  foreach ($bots as $bot) {
    if ($bot == '.' || $bot == '..') {
      continue;
    }
    echo '<span class="mainLobbyBot">'.$bot.'</span><br>';
  }
?>