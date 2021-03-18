#!/bin/bash


dates=("20200701" "20200702")

for i in ${dates[@]};
do
  python main.py --csv /home/maurice/aisdk_${i}/classA.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_cargo.log --yaml-file extract_class_a_vessel_type.yaml
done
