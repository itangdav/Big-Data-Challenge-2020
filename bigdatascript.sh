#!/bin/sh

beginning="https://api.kbgeo.com/coastal-distance/v2/coord?lat=";
middle="&lng=";
apikey="71188bd7-ec89-4b02-a218-703fccda181e";
declare -a outputarr=();

for ((i=0;i<1;i++))
do
 read line;
 declare -a latlong=( $( echo $line | cut -d' ' -f1- ) );

 curlstuff="${beginning}${latlong[0]}${middle}${latlong[1]}";
 hstuff="kb-auth-token: ${apikey}";

 temp=$(curl "${curlstuff}" -H "${hstuff}");
 outputarr+=("${temp}");
done

for j in "${outputarr[@]}"
do 
 echo "$j"
done




