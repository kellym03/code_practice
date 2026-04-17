## mutate function
mutate(tib, 
    # create age column
    age = c(20, 21, 22, 19, 20, 22, 19, 18, 21, 20),
    # create test1_letter column
    test1_letter = case_when(
        # assign letter based on test1 score
        test1 < 80 ~ "C",
        test1 >= 80 & test1 < 90 ~ "B",
        test1 >= 90 ~ "A"))

## select function
# select only quiz1 and quiz2 columns from tib
select(tib, quiz1, quiz2)

## Filter function
# filter tib to only rows where test1 > 90
filter(tib, test1 > 90)

## summarise function
# create a new tibble that has a column for the average of all of 
# quiz1 and the standard deviation of all of quiz1
summarise(tib, quiz1_avg = mean(quiz1), quiz1_sd = sd(quiz1))

Output:

A tibble: 1 x 2
  quiz1_avg quiz1_sd
      <dbl>    <dbl>
1       8.8     1.03


## summary statistics using dplyr package on tibbles
```{r, message = FALSE}
library(dplyr)
store <- read.csv("prices3.csv")

head(store)
```

```{r}
store_summary <- summarize(store, 
# add items
items = n(),
maximum = max(price),
mean = mean(price),
minimum = min(price))

store_summary
```

## Arrange function
# arrange tib from highest to lowest scores of test1, default is ascending
arrange(tib, desc(test1))

## Piping
# The tidyverse utilizes the pipe operator %>% to string multiple functions together. The pipe operator takes the tibble output from one function and inputs it as the first argument in the next function. 

tib %>% 
  # make a new tibble that has a column for the 
  # averages of test1 and test2
  summarize(avg_test1 = mean(test1), avg_test2 = mean(test2)) %>% 
  # add new columns test1_letter and test2_letter
  mutate(
    # assign test1_letter based on test1 average score
    test1_letter = case_when(
      avg_test1 < 80 ~ "C",
      avg_test1 >= 80 & avg_test1 < 90 ~ "B",
      avg_test1 >= 90 ~ "A"),
    # assign test2_letter based on test2 average score
    test2_letter = case_when(
      avg_test2 < 80 ~ "C",
      avg_test2 >= 80 & avg_test2 < 90 ~ "B",
      avg_test2 >= 90 ~ "A")) %>% 
  # reorder the columns to be by test1 then test2
  select(avg_test1, test1_letter, avg_test2, test2_letter)

A tibble: 1 x 4
  avg_test1 test1_letter avg_test2 test2_letter
      <dbl> <chr>            <dbl> <chr>       
1      85.3 B                 86.6 B  
  #Note that for each operation — summarize(), mutate(), and select() — we did not call the tibble tib as the first parameter.

##Piping exercise
```{r, message = FALSE}
library(dplyr)

store <- read.csv("prices1.csv")

head(store)
```

```{r}
# your code here
store_summary <- store %>%
  mutate(category = case_when(
    price < 30 ~ "cheap",
    price >= 30 & price < 50 ~ "low moderate",
    price >= 50 & price < 75  ~ "high moderate",
    price > 75 ~ "expensive"
  )) %>%
  filter(category == 'expensive') %>%
  summarize(items=n(), minimum=min(price), mean=mean(price), maximum=max(price))

print(store_summary)
  ```