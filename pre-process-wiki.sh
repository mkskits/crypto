#!/bin/bash
FILES=./*.gz
for f in $FILES
do
    echo "$f"
    FULL_FILENAME=$f
    FILENAME=${FULL_FILENAME##*/}
    echo ${FILENAME%%.*}
    output_name=$(echo ${FILENAME%%.*} | cut -c1-17)
    echo $output_name
    zgrep -H "en Bitcoin " "$f" >> $output_name
done
