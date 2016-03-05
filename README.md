# Polynomial root finder

Uses binary search to find roots given a range

Run root_finder.py and follow instructions to use

Have some EBNF
```
digit = "0" | 1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
integer = {digit} ;
decimal number = {digit}, digit, ".", {digit} | {digit}, ".", digit, {digit} | integer ;
sign = "+" | "-" ;
term = decimal number, "x", integer | decimal number ;
polynomial = [ sign ], term, { { " " }, sign, { " " }, term } ;
```
