#!/usr/bin/env bash
# Master raw Kokoro narration into the approved "B_room" sound.
# usage: master.sh IN.wav OUT.mp3
set -euo pipefail
CHAIN="asetrate=24000*0.917,aresample=48000,atempo=1.0905,highpass=f=70,equalizer=f=180:t=q:w=1:g=2.5,equalizer=f=6500:t=q:w=1.5:g=-3,deesser=i=0.4,acompressor=threshold=-20dB:ratio=2.2:attack=15:release=180,aecho=0.85:0.9:11|19:0.06|0.035"
ffmpeg -loglevel error -y -i "$1" -f lavfi -i "anoisesrc=color=pink:amplitude=0.0016:sample_rate=48000" \
  -filter_complex "[0:a]$CHAIN[v];[1:a]lowpass=f=6000[n];[v][n]amix=inputs=2:duration=first:weights=1 1:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11" \
  -ar 44100 -codec:a libmp3lame -q:a 2 "$2"
