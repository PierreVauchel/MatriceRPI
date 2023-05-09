<?php

if (isset($_POST['modifMatrice'])) {
    $msg = $_POST['msg'];

    $file = fopen('msg.txt', 'a');
    fwrite($file , $content);
    fclose($file);
    exit();
}
?>