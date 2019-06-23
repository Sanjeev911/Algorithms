# Knapsack problem

# given a a Lmiting Weight,list of values and weights
# construct a matrix whose element at i,j denotes the maximum value possible by considering items 0 to item i 
# with maximum weight constraint  = j




# Final matrix to look something like this (if value and weights are used as defined):         
# weights                0   1   2   3    4   5   6   7   8   9   10
# Items included:  0    [0,  0,  0,  0,   0,  0,  0,  0,  0,  0,   0]
# Items included:  1    [0,  0,  0,  0,   0,  10, 10, 10, 10, 10, 10]
# Items included:  2    [0,  0,  0,  0,  40,  40, 40, 40, 40, 50, 50]
# Items included:  3    [0,  0,  0,  0,  40,  40, 40, 40, 40, 50, 70]
# Items included:  4    [0,  0,  0,  50, 50,  50, 50, 90, 90, 90, 90]

# adding '0' to beggining of values and weights to make the matrix include row and column indicating '0' values 
# of items considered and '0' value of weight considered. 
values = [0]+[10,40,30,50]
weights = [0]+[5,4,6,3]
max_weight = 10


def initialise_matrix(row,column):
    matrix = [[]]*(row)
    for i in range(row):
        matrix[i] = [0]*(column+1)
    return matrix

def Knapsack(matrix,values,weights,max_weight):
    for i in range(len(values)):
        for j in range(max_weight):
            # if the value of indices for calculating both inclde and exclude are greater than 0. i.e accessible values
            # as negative value would access the list from the reverse(backward indexing)
            if (j-weights[i])>=0 and  (i-1)>=0:
                include = values[i]+matrix[i-1][j - weights[i]]
                exclude = matrix[i-1][j]
            # if value of indices for calculating include is -ve ,make include = 0 
            elif (i-1)>=0 and (j-weights[i])<0:
                exclude = matrix[i-1][j]
                include = 0
            # value  of indices used for finding include and exclude both are -ve then set both of them to value 0
            elif (i-1)<0:
                exclude,include = 0,0
            matrix[i][j] = max(include,exclude)
    return matrix


matrix = initialise_matrix(len(values),max_weight)
result = Knapsack(matrix,values,weights,max_weight+1)
for r in range(len(result)):
    print("Items included: ",r,"  ",result[r])



