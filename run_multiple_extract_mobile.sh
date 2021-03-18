#!/bin/bash


dates=("20200701" "20200702")

for i in ${dates[@]};
do
  python main.py --csv /AIS/AIS/Denmark/aisdk_${i}.csv --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_mobile.log --yaml-file extract_type_of_mobile.yaml
done
