Probability of a pair, a block, a v or one face existing in scrambled Pyraminxes.
I only count states that require at least 6 moves to solve, based on WCA Regulations.

||cases|%|
|:--|--:|--:|
|no pair|28,191,525|37.32 %|
|pair|40,747,903|53.94 %|
|block|6,367,680|8.43 %|
|v|226,119|0.30 %|
|1 face|10,692|0.01 %|
|||
|total|75,543,919|100.00 %|

Number of cases per number of moves required to make v.

|depth|cases|%|
|--:|--:|--:|
|0|236,811|0.31 %|
|1|1,341,840|1.78 %|
|2|6,256,144|8.28 %|
|3|22,997,430|30.44 %|
|4|36,407,736|48.19 %|
|5|8,263,701|10.94 %|
|6|38,880|0.05 %|
|7|1,377|0.00 %|
||||
|total|75,543,919|100.00 %|

Seven moves required if and only if all edges are flipped or all centers rotated.

Examples:

```
Gen: B R B R L' R B' U L R' L' (11)
V: L R L' R L B' R' (7)

RRLFF R LLRDD
 LFL FRF RDR
  F DDFRR D

    LLDFF
     DLD
      L

Gen: B U B' R U' B R' U R L' (10)
V: L R' L' R' L U' R (7)

RRLFF R LLRDD
 LFL FRF RFR
  F DDFDD F

    LLDRR
     DLD
      L

Gen: B R' L' B R' L' B R' L' (10)
V: L R B' R L' B' R (7)

LLRLL F RRLRR
 DLF LFR FRD
  L FFDFF R

    DDFDD
     LDR
      D
```

Log.

```
$ python3 pyraminx_v_prob.py
0 1
1 8
2 48
3 288
4 1728
5 9896
6 51808
7 220111
8 480467
9 166276
10 2457
11 32
R U' R U' R B' U' R B' R' L'
RRRLL F RRLDD
 DFF LFR FRD
  F DDDFF R

    LLFDD
     LLR
      L

U' B' L R B' L U' R L' R L'
RRRFF R LLLDD
 DLF LRR FRD
  L FFDFF R

    DDFDD
     LLR
      L

B L' R U' B U' L' R' B R' L'
LLRFF R LLLRR
 DLF LRR FDD
  L FFDRR D

    DDFFF
     LDR
      D

R U' B' R L' R B' R L' R' L'
RRRRR L FFLDD
 DLF LLR FRD
  L FFDFF R

    DDFDD
     LLR
      L

U' L R' U' R' L U' R' L R' L'
LLRLL F RRLRR
 DFF LFR FDD
  F DDDRR D

    LLFFF
     LDR
      D

U L' R B' U' L U R' L' R' L'
DDLFF R LLRLL
 LDL FRF RDR
  D LLFRR D

    FFDFF
     DRD
      R

R' B L B' U' R L' B L' R' L'
RRLRR L FFRDD
 LDL FLF RDR
  D LLFRR D

    FFDFF
     DLD
      L

U B' U' B' U R' U B' U R' L'
LLRLL F RRLRR
 DFF LFR FFD
  F DDDDD F

    LLFRR
     LDR
      D

B L U B' L U' B R' L' R' L'
RRRLL F RRLDD
 DLF LFR FFD
  L FFDDD F

    DDFRR
     LLR
      L

U' L' U' R L R' B' U L' R L'
DDLRR L FFRLL
 LDL FLF RFR
  D LLFDD F

    FFDRR
     DRD
      R

B R' L' U' R' U B R' L' R' L'
DDRLL F RRLLL
 DLF LFR FDD
  L FFDRR D

    DDFFF
     LRR
      R

B' R' L U R' B' R B' U R' L'
LLRRR L FFLRR
 DLF LLR FFD
  L FFDDD F

    DDFRR
     LDR
      D

U B' L B R B L' R L' R' L'
RRRFF R LLLDD
 DDF LRR FFD
  D LLDDD F

    FFFRR
     LLR
      L

B U L' U' R' L' B R' L' R' L'
DDRLL F RRLLL
 DFF LFR FRD
  F DDDFF R

    LLFDD
     LRR
      R

B' L U' L U' L R' U' L R' L'
DDRLL F RRLLL
 DLF LFR FFD
  L FFDDD F

    DDFRR
     LRR
      R

B L' R' U' B U' L R' B R' L'
LLRFF R LLLRR
 DFF LRR FRD
  F DDDFF R

    LLFDD
     LDR
      D

R U' R L' R U' B' R L' R' L'
DDRFF R LLLLL
 DLF LRR FRD
  L FFDFF R

    DDFDD
     LRR
      R

U L R' U L' R U R' L' R' L'
LLRLL F RRLRR
 DDF LFR FFD
  D LLDDD F

    FFFRR
     LDR
      D

B R B R L' R B' U L R' L'
RRLFF R LLRDD
 LFL FRF RDR
  F DDFRR D

    LLDFF
     DLD
      L

R' U R B U' R B' U L' R' L'
LLRFF R LLLRR
 DDF LRR FRD
  D LLDFF R

    FFFDD
     LDR
      D

U B' U L' U B' U' B' U R' L'
LLRLL F RRLRR
 DDF LFR FDD
  D LLDRR D

    FFFFF
     LDR
      D

B U B' U B R U B L' R' L'
DDRLL F RRLLL
 DDF LFR FRD
  D LLDFF R

    FFFDD
     LRR
      R

R' U B' L U' B L U L' R' L'
LLRFF R LLLRR
 DLF LRR FFD
  L FFDDD F

    DDFRR
     LDR
      D

B U' R B' U R B R' L' R' L'
RRRLL F RRLDD
 DDF LFR FRD
  D LLDFF R

    FFFDD
     LLR
      L

U R' U B U R' U' B L R' L'
DDRRR L FFLLL
 DLF LLR FRD
  L FFDFF R

    DDFDD
     LRR
      R

R' U B R' B' L' R' U L' R' L'
LLRRR L FFLRR
 DLF LLR FDD
  L FFDRR D

    DDFFF
     LDR
      D

B' U B' R L B U R' L' R' L'
DDRRR L FFLLL
 DFF LLR FDD
  F DDDRR D

    LLFFF
     LRR
      R

R' B R' L U' B' R B L' R' L'
RRLRR L FFRDD
 LFL FLF RFR
  F DDFDD F

    LLDRR
     DLD
      L

U R' L' U L' U' R' U L' R' L'
LLRRR L FFLRR
 DFF LLR FRD
  F DDDFF R

    LLFDD
     LDR
      D

U R U' B' L R' U R' L' R' L'
DDLFF R LLRLL
 LFL FRF RFR
  F DDFDD F

    LLDRR
     DRD
      R

B' L U' B' L U' L U' L R' L'
RRRLL F RRLDD
 DLF LFR FDD
  L FFDRR D

    DDFFF
     LLR
      L

U B R U B U' B U L' R' L'
LLRRR L FFLRR
 DDF LLR FRD
  D LLDFF R

    FFFDD
     LDR
      D

0 1 0 0 0 1 1
1 8 0 0 0 8 8
2 48 0 0 48 0 0
3 288 0 96 144 48 0
4 1728 0 960 624 144 0
5 9896 768 6536 2280 312 0
6 51808 7296 35272 8736 504 24
7 220111 53896 141567 23624 1024 80
8 480467 189592 255160 34916 799 28
9 166276 94519 63289 8348 120 0
10 2457 1950 407 88 12 0
11 32 32 0 0 0 0
[1, 8, 24, 32, 16]
0 1 0 0 0 1 1
1 16 0 0 0 16 16
2 136 0 0 48 88 88
3 896 0 96 528 272 224
4 5456 0 1728 2928 800 272
5 32296 768 16520 12264 2744 128
6 182432 13440 113672 47328 7992 24
7 931983 130696 612863 170504 17920 272
8 3829067 820440 2458736 516516 33375 1244
9 11108868 3150519 6735457 1170684 52208 2912
10 20736353 7149718 11725055 1800600 60980 3616
11 22907032 9213368 11952384 1696352 44928 2176
12 13067528 6105136 6117576 827904 16912 448
13 2739808 1575472 1025648 136384 2304 0
14 40336 32224 6512 1408 192 0
15 512 512 0 0 0 0
0 2972
1 16672
2 77408
3 284046
4 449504
5 102021
6 480
7 17
8 0
9 0
10 0
11 0
B R B R L' R B' U L R' L'
L R L' R L B' R'
RRLFF R LLRDD
 LFL FRF RDR
  F DDFRR D

    LLDFF
     DLD
      L

B U B' R U' B R' U R L'
L R' L' R' L U' R
RRLFF R LLRDD
 LFL FRF RFR
  F DDFDD F

    LLDRR
     DLD
      L

B R' L' B R' L' B R' L'
L R B' R L' B' R
LLRLL F RRLRR
 DLF LFR FRD
  L FFDFF R

    DDFDD
     LDR
      D

U' L' U' R L R' B' U L' R L'
L R L R U' B U'
DDLRR L FFRLL
 LDL FLF RFR
  D LLFDD F

    FFDRR
     DRD
      R

R' B R' L U' B' R B L' R' L'
L R B' R' U B R'
RRLRR L FFRDD
 LFL FLF RFR
  F DDFDD F

    LLDRR
     DLD
      L

B R' B' U L' R' L B' R L'
L R L R' B U' L'
DDLFF R LLRLL
 LFL FRF RDR
  F DDFRR D

    LLDFF
     DRD
      R

B U' R' U L' R U' L R' L'
L R L' R L B' R'
RRLRR L FFRDD
 LFL FLF RDR
  F DDFRR D

    LLDFF
     DLD
      L

R B' L R' B R U' L B L'
L R L U B' U R
RRLRR L FFRDD
 LDL FLF RFR
  D LLFDD F

    FFDRR
     DLD
      L

U R' L U' R U B' L R L'
L R L B' U B' R
DDLFF R LLRLL
 LDL FRF RFR
  D LLFDD F

    FFDRR
     DRD
      R

U R B L' R' B L U R' L'
L R L' R L B R'
DDLRR L FFRLL
 LFL FLF RDR
  F DDFRR D

    LLDFF
     DRD
      R

U R U' B' L R' U R' L' R' L'
L R L R' B U' L'
DDLFF R LLRLL
 LFL FRF RFR
  F DDFDD F

    LLDRR
     DRD
      R

U L' R B' U' L U R' L' R' L'
L R L' R' U' L' R
DDLFF R LLRLL
 LDL FRF RDR
  D LLFRR D

    FFDFF
     DRD
      R

R' B L B' U' R L' B L' R' L'
L R L' R' U L' R
RRLRR L FFRDD
 LDL FLF RDR
  D LLFRR D

    FFDFF
     DLD
      L

B' L U' B L' U B' U' R L'
L R B' R' U B R'
DDLRR L FFRLL
 LFL FLF RFR
  F DDFDD F

    LLDRR
     DRD
      R

B U' L B' U B R' L U L'
L R L R B U' B
RRLFF R LLRDD
 LDL FRF RDR
  D LLFRR D

    FFDFF
     DLD
      L

U' B' U R' B U' R B' R' L
L R L R U' B U'
DDLRR L FFRLL
 LDL FLF RDR
  D LLFRR D

    FFDFF
     DRD
      R

B R L' B' U' R B U' R' L'
L R L R B U' B
RRLFF R LLRDD
 LDL FRF RFR
  D LLFDD F

    FFDRR
     DLD
      L

0 236811
1 1341840
2 6256144
3 22997430
4 36407736
5 8263701
6 38880
7 1377
8 0
9 0
10 0
11 0
```
