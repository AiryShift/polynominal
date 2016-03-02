# Polynomial root finder

Uses binary search to find roots given a range

Run root_finder.py and follow instructions to use

Have some EBNF
```
digit = "0" | 1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
number = digit, {digit} ;
sign = "+" | "-" ;
coefficient = [number] ;
power = [number] ;
term = sign, { " " }, coefficient, "x", power ;
polynomial = [ sign ], coefficient, "x", power, { { " " }, term } ;
```
