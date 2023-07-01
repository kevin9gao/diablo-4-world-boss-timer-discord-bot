<?php
session_start();
require_once("twitteroauth/twitteroauth/twitteroauth.php"); //Path to twitteroauth library

$twitteruser = "game8_d4boss";
$notweets = 5;
$consumerkey = "n7ytOH3AcZqnKJLGx3dy7ovPS";
$consumersecret = "Mrld0nPiTyM39MhZaquI1FF3Y3nbrbLtWdS1I1lJMqld1FL9of";
$accesstoken = "284952886-p92orZTjfV9vjv4cIXUp2XEJqL1BLjAEDIXS1PF5";
$accesstokensecret = "B6v6lSgkQkCVhkyv02tevJ14DB76ReZtaFwImVPXyly1c";

function getConnectionWithAccessToken($cons_key, $cons_secret, $oauth_token, $oauth_token_secret) {
  $connection = new TwitterOAuth($cons_key, $cons_secret, $oauth_token, $oauth_token_secret);
  return $connection;
}

$connection = getConnectionWithAccessToken($consumerkey, $consumersecret, $accesstoken, $accesstokensecret);
$tweets = $connection->get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=".$twitteruser."&count=".$notweets);

echo json_encode($tweets);
?>
