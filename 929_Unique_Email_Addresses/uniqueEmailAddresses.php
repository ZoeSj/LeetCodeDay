<?php
$array= ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"];
$outputResult = array();
foreach ($array as $key => $value) {
	if (preg_match("/^\w+([-+.]\w+)*@\w+([-]\w+)*\.\w+([-]\w+)*$/", $value)) {
			$out = sscanf($value, '%[^.].%[^@]%s', $fpart1, $fpart2, $fpart3);
	$out1 = sscanf($fpart2, '%[^+]%s',$part1,$part2);
	$test = preg_replace("/[.]*/", '', $part1);
	$output = $fpart1.$test.$fpart3;
	array_push($outputResult, $output);
	}
}
$count = count($array);
var_dump($outputResult);
