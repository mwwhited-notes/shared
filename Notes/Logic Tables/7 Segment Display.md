# 7 Segment Display

```
   A
 F   B
   G
 E   C
   D   Dp
```

## Logic Table

| DEC | HEX |  BIN | A | B | C | D | E | F | G | Dp |
|-----|-----|------|---|---|---|---|---|---|---|----|
|   0 |   0 | 0000 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |  0 |
|   1 |   1 | 0001 | 0 | 1 | 1 | 0 | 0 | 0 | 1 |  0 |
|   2 |   2 | 0010 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |  0 |
|   3 |   3 | 0011 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |  0 |
|   4 |   4 | 0100 | 0 | 1 | 1 | 1 | 0 | 1 | 1 |  0 |
|   5 |   5 | 0101 | 1 | 0 | 1 | 1 | 0 | 1 | 1 |  0 |
|   6 |   6 | 0110 | 1 | 0 | 1 | 1 | 1 | 1 | 1 |  0 |
|   7 |   7 | 0111 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |  0 |
|   8 |   8 | 1000 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  0 |
|   9 |   9 | 1001 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |  0 |
|  10 |   A | 1010 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  0 |
|  11 |   B | 1011 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |  0 |
|  12 |   C | 1100 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |  0 |
|  13 |   D | 1101 | 0 | 1 | 1 | 1 | 1 | 0 | 1 |  0 |
|  14 |   E | 1110 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |  0 |
|  15 |   F | 1111 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |  0 |
