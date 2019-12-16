#!/usr/bin/env bash

for i in {0,1};do 
    for j in {0,1}; do
        for k in {0,1}; do
            for l in {0,1}; do
                ./Blackbox $i $j $k $l >> Blackbox.txt
                done;
            done;
        done;
    done;



