<?php
  $clientBotList = $_POST['bot_list'] ? $_POST['bot_list']:array();
  function in_client_bot_list($bot, $list) {
    foreach ($list as $item) {
      $item = (array) $item;
      if ($bot === $item['name']) {
        return true;
      }
    }
    return false;
  }

  $attempts = 0;
  $returnList = array();
  while ($attempts < 20) {
    $bots = scandir("chatbots");

    $returnList = array();

    // Any bots deleted or updated
    foreach ($clientBotList as $clientBot) {
      $clientBot = (array) $clientBot;
      if (in_array($clientBot['name'], $bots)) {
        // In array, check if updated
        if ($clientBot['time'] != filectime("chatbots/".$clientBot['name'])) {
          $botInfo = array('name' => $clientBot['name'], 'time' => filectime("chatbots/".$clientBot['name']), 'status' => 'updated');
          $returnList[] = $botInfo;
        }
      } else {
        // Not in array, must have been deleted
        $botInfo = array('name' => $clientBot['name'], 'time' => 0, 'status' => 'deleted');
        $returnList[] = $botInfo;
      }
    }

    // Any new bots
    foreach ($bots as $bot) {
      if ($bot === '.' || $bot === '..') {
        continue;
      }
      if (!in_client_bot_list($bot, $clientBotList)) {
        $botInfo = array('name' => $bot, 'time' => filectime("chatbots/".$bot), 'status' => $clientBotList ? 'new':'first');
        $returnList[] = $botInfo;
      }
    }
    if ($returnList) {
      break;
    }
    sleep(1);
    $attempts++;
  }

  echo json_encode($returnList);
?>