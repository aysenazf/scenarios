#code for matrix multiplier

#matrix_a = [[1,2,3],[4,5,6]]
#matrix_b = [[7,8],[9,10],[11,12]]

matrix_a = [[4,2,4],[8,3,1]]
matrix_b = [[3,5],[2,8],[7,9]]
    
def multiply(matrix_a, matrix_b):

    
#assumes that matrices a and b are initialised as 2d arrrays and can be indexed matrix[row,column]

    #if (condition to check if arrays are 3*3 or less = true):
    if (len(matrix_a[0]) == len(matrix_b)):   #checking that the number of columns in 
            
            #initialise new matrix = result              #matrix_a is equal to the number of rows in matrix_b.
            #rows(result) =  rows(a)
            
            result = [[],[]]

            for x in range(0,len(result)):          #x-loop iterates over the rows in the result
                for y in range(0,len(matrix_b[0])):         #y-loop iterates over the columns in the result
                    result[x].append(0)                 #z-loop makes sure that there is the correct number (a*b)'s
                    for z in range(0,len(matrix_a[0])):
                        result[x][y] = result[x][y] + (matrix_a[x][z] * matrix_b[z][y])

                        #for this part the x's and y's match up to obey the order of regular matrix multiplication
                        #e.g. result[1,3] would be = (a[1,1] * b[1,3]) + (a[1,2] * b[2,3]) + (a[1,3] * b[3,3])
            
            for i in range(0,len(result)):
                print(result[i])
                
            return result

    else:
            return "Not multipliable"

multiply(matrix_a,matrix_b)