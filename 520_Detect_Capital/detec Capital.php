<?php
class Solution {

    /**
     * @param String $word
     * @return Boolean
     */
    function detectCapitalUse($word) {
        $patternLowerCase  = "/^[A-Z]{1}[a-z]+$|^[a-z]+$|^[A-Z]+$/";
        if(preg_match($patternLowerCase,$word)){
            return true;
        }else{
            return false;
        }
    }
}
