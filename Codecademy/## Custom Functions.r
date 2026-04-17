## Custom Functions
# In R, custom functions can only return one object. 
#If we wanted to return multiple objects, we would have to combine them into a single object. 
#This single object could be a single dataframe or tibble if the different objects have compatible dimensions. 
#Another option could be to save multiple objects as separate items in a single list.

## apply() function
#applies a function to either each row or column of a dataframe or matrix.

The syntax of apply() is:

apply(X, MARGIN, FUN)

The MARGIN specification determines whether the function FUN is applied across the rows (1) or down the columns (2) of the object X.

Let’s try this on the following matrix:

test_mat

Output:

     [,1] [,2] [,3]
[1,]    1    1    1
[2,]    2    2    2

If we were to sum across the rows, we would get 3 and 6. If we were to sum down the columns, we would get 3, 3, and 3. Let’s try this using apply().

Apply the sum() function over each row (margin value 1):

apply(X = test_mat, MARGIN = 1, FUN = sum)

Output:

[1] 3 6

Apply the sum() function down each column (margin value 2):

apply(X = test_mat, MARGIN = 2, FUN = sum)

Output:

[1] 3 3 3

The functions we can use in apply() are mean, median, sum, min, or max as well as other existing or user-defined functions. 