<?php
$self = "gyudon-hand.php";
$base_dir = dirname(__FILE__). "/image";
$unknown_dir = "gyudon";
$dirs = array(
  "일반 규동" => "normal",
  "생강 규동" => "beni",
  "양파 규동" => "negi",
  "치즈 규동" => "cheese",
  "김치 규동" => "kimuti",
  "기타" => "other",
);
// 필요한 폴더 생성하기
foreach ($dirs as $key => $dir) {
  $path = $base_dir."/$dir";
  if (!file_exists($path)) {
    mkdir($path); chmod($path, 0777);
  }
}
// 분류하거나 입력 양식 제공하기
$m = isset($_GET["m"]) ? $_GET["m"] : "";
if ($m == "mv") { // 분류하기
  $target = $_GET["target"]; // 요청 매개변수 추출하기
  $to = $_GET["to"];
  $path = $base_dir."/$unknown_dir/$target";
  // 요청 매개변수 확인하기
  if ($target == "") { echo "error..."; exit; }
  if (!file_exists($path)) {
    echo "<a href='$self'>already ...</a>"; exit;
  }
  if (!file_exists("$base_dir/$to")) {
    echo "system error : no dir $to"; exit;
  }
  // 파일 이동(복사한 뒤에 제거하기)
  $path_to = "$base_dir/$to/$target";
  copy($path, $path_to);
  if (file_exists($path_to)) {
    unlink($path);
  } else {
    echo "Sorry, could not move."; exit;
  }
  // 선택 화면으로 리다이렉트
  header("location: $self");
  echo "<a href='$self'>Thank you, moved.</a>";
} else {
  // 규동 선택 입력 양식 만들기
  $files = glob("$base_dir/$unknown_dir/*.jpg"); // 이미지 가져오기
  if (count($files) == 0) {
    echo "<h1>완료</h1>"; exit;
  }
  shuffle($files); // 적당한 파일을 선택합니다.
  $target = basename($files[0]); 
  $remain = count($files); // 남은 파일 수
  $buttons = ""; // 선택지 생성하기
  foreach ($dirs as $key => $dir) {
    $fs = glob("$base_dir/$dir/*.jpg"); // 분류한 파일 수
    $cnt = count($fs);
    $api = "$self?m=mv&target=$target&to=$dir";
    $buttons .= "[<a href='$api'>$key($cnt)</a>] ";
  }
  echo <<< EOS
    <html><head><meta charset="utf-8">
      <meta name="viewport" content="width=320px">
      <style> body { text-align:center;
                     font-size: 24px; }
      </style></head><body>
      <h3 style="font-size:12px">선택해주세요(남은 파일 수: $remain)</h3>
      <img src="./image/$unknown_dir/$target" width=300><br>
      $buttons
    </body></html>
EOS;
}