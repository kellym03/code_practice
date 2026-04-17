## Conditional Selection with which()

#> # Call rows that have col1 > 2
#> dat[which(dat$col1 > 2),]
#  col1 col2 col3
#3    3    c    1
#4    4    d    1
#> 
#> # Call rows that have col2 == "b" or "d"
#> dat[which(dat$col2 == "b" | dat$col2 == "d"),]
#  col1 col2 col3
#2    2    b    1
#4    4    d    1


## Adding column values to a data frame
#> # Single value
#> dat$col4 <- "b"

#> # Vector whose length equals the number of rows
#> dat$col5 <- c("e", "f", "g", "h")

#> # Vector whose length is a factor of the number of rows
#> dat$col6 <- c(1, 2)

#> # Print data frame
#> dat

#  col1 col2 col3 col4 col5 col6
#1    1    a    1    b    e    1
#2    2    b    1    b    f    2
#3    3    c    1    b    g    1
#4    4    d    1    b    h    2

## Appending rows to a data frame
> # Single value that will fill across the entire row
> dat <- rbind(dat, 1) 

> # Vector whose length equals the number of columns
> dat <- rbind(dat, c(5, "a", 3, "e", 1, "i"))

> # Vector whose length is a factor of the number of columns
> dat <- rbind(dat, c("x", "z"))

> # Print data frame
> dat

  col1 col2 col3 col4 col5 col6
1    1    a    1    b    e    1
2    2    b    1    b    f    2
3    3    c    1    b    g    1
4    4    d    1    b    h    2
5    1    1    1    1    1    1
6    5    a    3    e    1    i
7    x    z    x    z    x    z

## Modifying values in a data frame
> # Change the whole 3rd column to equal "!"
> dat[,3] <- "!"
 
> # Change the 4th and 5th rows to equal "?"
> dat[4:5,] <- "?"
 
> # Change the bottom right value to equal "%"
> dat$col6[7] <- "%"
 
> # Print dat
> dat
  col1 col2 col3 col4 col5 col6
1    1    a    !    b    e    1
2    2    b    !    b    f    2
3    3    c    !    b    g    1
4    ?    ?    ?    ?    ?    ?
5    ?    ?    ?    ?    ?    ?
6    5    a    !    e    1    i
7    x    z    !    z    x    %

## Using a which() statement to modify values
> # Change any rows that have "a" in col2 to "+"
> dat[which(dat$col2 == "a"),] <- "+"
 
> # Print dat
> dat
  col1 col2 col3 col4 col5 col6
1    +    +    +    +    +    +
2    2    b    !    b    f    2
3    3    c    !    b    g    1
4    ?    ?    ?    ?    ?    ?
5    ?    ?    ?    ?    ?    ?
6    +    +    +    +    +    +
7    x    z    !    z    x    %

## Removing data from a data frame
Removing data
There are a few methods we can use to remove rows or columns from data sets. The basic idea is that we are reassigning the data frame using a selected subset of the data.

Specify rows or columns to keep
This method is convenient when there are not many rows or columns to keep, or if the rows or columns we want to remove are together in a sequence.

dat <- dat[1:3,] only keeps rows 1 through 3.
dat <- dat[,c("col2", "col4")] only keeps columns 2 and 4. Alternatively, dat <- dat[,c(2,4)]
Specify rows or columns to remove
This method is convenient when there are not many rows or columns to remove, or if the rows or columns we want to remove are together in a sequence.

dat <- dat[-c(1,3,6),] removes rows 1, 3, and 6.
dat <- dat[,-c(2:5)] removes columns 2 through 5.
Specify rows using a logical statement
This method is convenient when the rows we want to remove share a common characteristic.

dat <- dat[which(dat$col3 == "!"),] keeps only rows with "!" in col3.
dat <- dat[-which(dat$col3 != "!"),] does the same, but by REMOVING the rows without a "!" in col3.
```{r}
```{r}
## Import data
dat <- read.csv("df_class.csv")
head(dat)
```

```{r}
# Try code here
nrow(dat)
ncol(dat)
dim(dat)

colnames(dat) <- c("test1a", "test2a")
print(dat)
colnames(dat)[1] <- c("test1b")
colnames(dat)[2] <- c("test2b")
colnames(dat)[3] <- c("Attendanceb")
colnames(dat)[4] <- c("Participationb")
print(dat)

dat[3:4, 1]
dat[3:4]
dat[3:4,]

dat <- dat[which(dat[1] > 90),]
dat <- dat[which(dat[2] > 90),]
print(dat)
```