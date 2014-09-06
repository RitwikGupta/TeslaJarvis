<?php
$fp=fopen('sub.txt','a'); 
fwrite($fp,addslashes($_POST['web']). "\r\n"); 
fclose($fp); 
header('location: thanks.html'); 
exit();
?>