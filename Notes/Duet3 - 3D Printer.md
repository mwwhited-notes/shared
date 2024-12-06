
## Logging from Server

```shell
sudo journalctl -u duetcontrolserver -e
```

## Pinout

```
Pin out
Step a
Step b
Step a
Step b
Step c
Step d
Step c
Step d

Heat p
Heat m
Heat p
Heat m
Heat p
Heat m

Fan p
Fan m
Fan tach p
Fan tach m

Temp p
Temp m

Step sense
Heater sense
Fan sense
Temp sense

Ground



Step abcd 
Heat pm
Temp pm

Fan pmts

4 4 4 *3

Abcd i1234 a1234 * 3 (14*3)
 
36+42+4+2
84

4 2 * 3
4 * 3
2
18+12+2

2 4 * 3
10 * 3
2
18+30+2

30
```

