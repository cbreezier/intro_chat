<?php
  echo '<h3>Current bouncing balls</h3>';
  $balls = scandir("bouncingball");
  $bouncecount = file_get_contents("bouncingball/count.txt");
  foreach (explode(PHP_EOL, $bouncecount) as $line) {
    $info = explode(' ', $line);
    $count[$info[0]] = $info[1];
  }
  foreach ($balls as $ball) {
    if ($ball == '.' || $ball == '..' || !preg_match('/^.*\.py$/', $ball)) {
      continue;
    }
    $numBounce = isset($count[$ball]) ? $count[$ball] : 0;
    echo '<span class="ball">'.$ball.' has bounced '.$numBounce.' times</span><br>';
  }
?>
