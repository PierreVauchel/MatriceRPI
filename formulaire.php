<?php

if (isset($_POST['modifMatrice'])) {
    $msg = $_POST['msg'];

    $file = fopen('msg.txt', 'w');
    fwrite($file , $msg);
    fclose($file);
    header("location:congrats.html");
    exit();
}
?>