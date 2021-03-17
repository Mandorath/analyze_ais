#!/bin/bash

dates=("20190826")

for i in ${dates[@]};
do
  python main.py --csv /home/maurice/aisdk_${i}/classA.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_cargo.log --yaml-file analyze_vessel_cargo.yaml
  python main.py --csv /home/maurice/aisdk_${i}/classA.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_fishing.log --yaml-file analyze_vessel_fishing.yaml
  python main.py --csv /home/maurice/aisdk_${i}/classA.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_passenger.log --yaml-file analyze_vessel_passenger.yaml
  python main.py --csv /home/maurice/aisdk_${i}/classA.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_tanker.log --yaml-file analyze_vessel_tanker.yaml
done
