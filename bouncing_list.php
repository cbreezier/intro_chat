<?php
  $balls = scandir("bouncingball");
  $bouncecount = file_get_contents("bouncingball/count.txt");
  foreach (explode(PHP_EOL, $bouncecount) as $line) {
    $info = explode(' ', $line);
    $count[$info[0]] = intval($info[1]);
  }
  foreach ($balls as $ball) {
    if ($ball == '.' || $ball == '..' || !preg_match('/^.*\.py$/', $ball)) {
      continue;
    }
    if (isset($count[$ball])) {
      $numBounce = $count[$ball];
    } else {
      $numBounce = 0;
      $count[$ball] = 0;
    }
    // echo '<span class="ball">'.$ball.' has bounced '.$numBounce.' times</span><br>';
  }
  echo json_encode($count);
?>
