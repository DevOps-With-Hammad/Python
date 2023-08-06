#!/bin/bash
# How to insert VARS In Bash.
var=Hello
echo $var
# END of VAR (1) Wonderfull.

# Here It Comes to String in Bash
STR="Welcome In Bash Mr Hammad and Try Not to Be Fast --- It always about time"
echo $STR
echo ${STR}
echo ${STR:5:15}
# End of String statement #1


# Array In Bash 
 
ARRAY=(one Two Three four Five)
# Index 0  1	2	3   4
echo ${ARRAY[@]} 
# Gettiing all Items from the array  using @ sign.

echo ${!ARRAY[@]} 
# TO print out all Index of The Array Using ! sign.

echo ${ARRAY[*]}
# To print out all the Items of the Array Using * sign.



