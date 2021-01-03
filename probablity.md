# MINI LOTO (JPN)

MINI LOTO, the lottery numbers consist of five numbers from 1 to 31 and one jackpot number with the same range.

Winning a prize is determined by the number of application numbers that match the lottery numbers. 

the first prize if all the application numbers and a jacpot number are guessed correctly. 
the second prize is with one less application number, the third prize is the same as the second but without a jackpot number. 
the 4th is with 3 application numbers. 

## How to calculate the probablity 

formula : n! / r! (n-r)!

n is the numerical value of a number to select from the pool. 
r is the set of numbers to select.

## r's numbers are guessed to win a prize

### The probability of winning a first prize (5 numbers + 1 jackpot number)
The ood of winning a jackpot is 1 in 5,267,241 as the following.

The combination of all numbers from the pool set of 31 numbers

```
31! / 5! * (31 - 5)! = 169911
```

The above is the combination of all five numbers are guessed.
Calculate how many of jackpot number is in the set of 169,911.

```
1! / 169,911 * 31 = 1 / 5267241
```

### The probability of winning a second prize (4 numbers + 1 jackpot number)
The ood of winning a jackpot is 1 in 1,950,830 as the following.

``` 
31! / 4! * (31 - 4)! = 62930
```

```
1! / 62930 * 31 = 1 / 1950830
```

### The probability of winning a second prize (4 numbers )
The ood of winning a jackpot is 1 in 62,930 as the following.

```
31! / 4! * (31 - 4)! = 62930
```

### The probability of winning a second prize (3 numbers )
The ood of winning a jackpot is 1 in 4,495 as the following.

```
31! / 3! * (31 - 3)! = 4495
```

### The probability of guessing none of correct numbers out of five numbers
The odd of completly mis-guessing numbers is 1 in 662,400

```
5! / (0! * 5!) * (26! / 21! * 5!) =  662400
```
