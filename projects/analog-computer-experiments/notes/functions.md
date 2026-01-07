# Functions

## Trig

### Approximate Sine

```excel
=[@radian]-EXP(EXP(LN(LN([@radian]))+LN(2.827))-LN(6.28))
```

### Approximate Cosine

```excel
=1-EXP(LN(2.35)+LN([@radian]))-EXP(EXP(LN(LN([@radian]))+LN(1.504))-LN(1.445))
```

### Approximate Degrees to Radians

```excel
=EXP(LN([@degree])+LN(3.14)-LN(180))
```
