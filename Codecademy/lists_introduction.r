```{r}
# Initiate list1 (unnamed)
list1 <- list(7, c("z", "y", "x", "w"), c(0.5, 0.21, 0.65, 0.77, 0.9), list(1,1,0))

# Initiate list2 (named)
list2 <- list(names = c("Penny", "Jake", "Ji-Hoon", "Hasan"), age = c(24, 20, 19, 22), scores = list(
  test1 = c(9, 7, 7, 8),
  test2 = c(8, 8, 7, 10),
  test3 = c(6, 10, 9, 9)))
```

```{r}
# Try code here
print(list1)
str(list1)
list1[[4]][[3]]
list1[[4]][[3]] <- 3
list1[[4]][[3]]
list2$names[3]
scores_list <- list2$scores
scores_matrix <- do.call(rbind, scores_list)
print(scores_matrix)
student_info <- data.frame(Name = list2$names, Age = list2$age, Scores = list2$scores)
print(student_info)
```