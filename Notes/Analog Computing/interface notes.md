# Pin Out Controls

## Details

| System | Name      | Usage                 |  User Port | Control Port | Bus Port | Minion |
| ------ | --------- | --------------------- | ---------- | ------------ | -------- | ------ |
|  DB-25 |           |                       |     GX16-8 |         DB-9 |    DB-15 |   2x05 |
|      1 | +15       | Positive Power        |            |            1 |        1 |        | 
|      2 | -15       | Negative Power        | White  - 8 |            2 |        2 |        |
|      3 | GND       | Ground                |            |            3 |        3 |  1&2&3 |
|      4 | +Ref      | Positive Machine Unit |            |            4 |        4 |        |
|      5 | -Ref      | Negative Machine Unit |            |            5 |        5 |        |
|      6 | Axis W    | User W                | Green  - 7 |              |          |        |
|      7 | Axis X    | User X                | Brown  - 2 |              |          |        |
|      8 | Axis Y    | User Y                | Orange - 4 |              |          |        |
|      9 | Axis Z    | User Z                | Black  - 1 |              |          |        |
|     10 | Axis A    | User A                | Yellow - 5 |              |          |        |
|     11 | Axis B    | User B                | Blue   - 6 |              |          |        |
|     12 | +Logic    | Positive Logic Power  | Red    - 3 |            6 |          |        |
|     13 | Over Volt | Over-volt Signal      |            |            7 |          |        |
|     14 | /Mode IC  | Integrate Mode        |            |            8 |          |      6 |
|     15 | /Mode OP  | Operate Mode          |            |            9 |          |      8 |
|     16 | Bus 1     | Bus Link 1            |            |              |        6 |        |
|     17 | Bus 2     | Bus Link 2            |            |              |        7 |        |
|     18 | Bus 3     | Bus Link 3            |            |              |        8 |        |
|     19 | Bus 4     | Bus Link 4            |            |              |        9 |        |
|     20 | Bus 5     | Bus Link 5            |            |              |       10 |        |
|     21 | Bus 6     | Bus Link 6            |            |              |       11 |        |
|     22 | Bus 7     | Bus Link 7            |            |              |       12 |        |
|     23 | Bus 8     | Bus Link 8            |            |              |       13 |        |
|     24 | Bus 9     | Bus Link 9            |            |              |       14 |        |
|     25 | Bus 10    | Bus Link 10           |            |              |       15 |        |
|        | /Potset   | Coefficient Set       |            |              |          |      4 |
|        |           | Not Connected!        |            |              |          |      7 |
|        |           | Not Connected! (Vcc)  |            |              |          |   9&10 |
|        |           | Minion In             |            |              |          |      5 |