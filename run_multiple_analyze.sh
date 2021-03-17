#!/bin/bash

dates=("20190701" "20190704")

for i in ${dates[@]};
do
  python main.py --csv /home/maurice/aisdk_${i}/classA.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_cargo.log --yaml-file analyze_vessel_cargo.yaml &
  P1=$!
  python main.py --csv /home/maurice/aisdk_${i}/classA.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_fishing.log --yaml-file analyze_vessel_fishing.yaml &
  P2=$!
  python main.py --csv /home/maurice/aisdk_${i}/classA.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_passenger.log --yaml-file analyze_vessel_passenger.yaml &
  P3=$!
  python main.py --csv /home/maurice/aisdk_${i}/classA.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_tanker.log --yaml-file analyze_vessel_tanker.yaml &
  P4=$!
  wait $P1 $P2 $P3 $P4
done
