<?php
function inverse($input){
    $string_to_array = explode(" ",$input);
       $string_in_array = array();
    foreach ($string_to_array as $key => $value) {
       $value = strrev($value);
       $string_in_array[$key] = $value;
    }
    $array_to_string = implode(" ",$string_in_array);
       return $array_to_string;
}

$input = "Many people spell MySQL incorrectly";
$output = inverse($input);
print_r($output);