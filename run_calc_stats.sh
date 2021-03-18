#!/bin/bash

dates=("20190701" "20190704")

for i in ${dates[@]};
do
  python main.py --csv /home/maurice/aisdk_${i}/Cargo2.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_cargo_stats.log --yaml-file calc_stats_cargo.yaml --date ${i} &
  P1=$!
  python main.py --csv /home/maurice/aisdk_${i}/Fishing2.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_fishing_stats.log --yaml-file calc_stats_fishing.yaml --date ${i} &
  P2=$!
  python main.py --csv /home/maurice/aisdk_${i}/Tanker2.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_passenger_stats.log --yaml-file calc_stats_passenger.yaml --date ${i} &
  P3=$!
  python main.py --csv /home/maurice/aisdk_${i}/Passenger2.out --output-dir /home/maurice/aisdk_${i} --log-file aisdk_${i}_tanker_stats.log --yaml-file calc_stats_tanker.yaml  --date ${i}&
  P4=$!
  wait $P1 $P2 $P3 $P4
done
