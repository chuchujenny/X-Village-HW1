import random

from copy import deepcopy


class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        i=1
        j=1
        m=[]
        self.matrix=[]
        while i <= int(nrows):        
            while j<= int(ncols):     
                m+=[random.randint(0,9)]                    
                j+=1
            self.matrix+=[m]
            j=1
            m=[]
            i+=1
    def __list__(self):
        return self.matrix

    def add(self, m):
        """return a new Matrix object after summation"""
        self.matrixm=m.__list__()
        self.matrix=matrix_Aorg
        print("========== A + B ==========")
        if len(self.matrix[0]) == len(self.matrixm[0]) and len(self.matrix) == len(self.matrixm):
            self.matrix= [[self.matrix[i][j]+self.matrixm[i][j] for j in range(len(self.matrixm[0]))] for i in range(len(self.matrixm))] 
            return self.matrix
        else:
            print("Matrix' size should be in the same size")
            self.matrix = None

    def sub(self, m):
        """return a new Matrix object after substraction"""
        self.matrixm=m.__list__()
        self.matrix=matrix_Aorg
        print("========== A - B ==========")
        if len(self.matrix[0]) == len(self.matrixm[0]) and len(self.matrix) == len(self.matrixm):
            self.matrix= [[self.matrix[i][j]-self.matrixm[i][j] for j in range(len(self.matrixm[0]))] for i in range(len(self.matrixm))]
            return self.matrix
        else:
            print("Matrix' size should be in the same size")
            self.matrix = None

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        self.matrixm=m.__list__()
        self.matrix=matrix_Aorg
        print("========== A * B ==========")
        if len(self.matrix[0]) == len(self.matrixm):
            self.matrix= [[sum(self.matrix[k][j]*self.matrixm[j][i] for j in range(len(self.matrix[0]))) for i in range(len(self.matrixm[0]))] for k in range(len(self.matrix))]
            return self.matrix
        else:
            print("List index out of range")
            self.matrix = None

    def transpose(self):
        """return a new Matrix object after transpose"""
        print("========== the transpose ==========")
        if self.matrix != None:
            b=[[self.matrix[i][j] for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
            self.matrix=b
            return self.matrix
        else:
            print(" 'NoneType' object is not subscriptable")
            return None
    
    def display(self):
        """Display the content in the matrix"""
        if self.matrix is None:
            return 
        else:    
            i=0
            j=0
            while i <len(self.matrix):
                while j< len(self.matrix[0]):
                    print(self.matrix[i][j],end=" ")
                    j+=1
                print("")
                j=0
                i+=1

nrows_A=input("Enter A matrix's rows:") 
ncols_A=input("Enter A matrix's cols:") 
matrix_A=Matrix(nrows_A,ncols_A)
matrix_Aorg=deepcopy(matrix_A.__list__())
print("Matrix A({},{}):".format(nrows_A,ncols_A))
matrix_A.display()
nrows_B=input("Enter B matrix's rows:") 
ncols_B=input("Enter B matrix's cols:")
matrix_B= Matrix(nrows_B,ncols_B)
print("Matrix B({},{}):".format(nrows_B,ncols_B))
matrix_B.display()

matrix_A.add(matrix_B)
matrix_A.display()
matrix_A.sub(matrix_B)
matrix_A.display()
matrix_A.mul(matrix_B)
matrix_A.display()
matrix_A.transpose()
matrix_A.display()
