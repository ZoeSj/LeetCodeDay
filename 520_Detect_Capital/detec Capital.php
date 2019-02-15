<?php

        $word1 = "USA";
        // $word1 = "USA";
        $patternLowerCase  = '/^[A-Z]{1}[a-z]+$|^[a-z]+$|^[A-Z]+$/';
        // $patternCapitalCase = '/^[A-Z]+$/';
        $patternCase = '/^[A-Z]{1}[a-z]+$/';
        if(preg_match($patternLowerCase,$word1)){
            echo "true";
        }else{
            echo "false";
        }