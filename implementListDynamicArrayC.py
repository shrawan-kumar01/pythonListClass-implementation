#  build a class which behaves as it is oythin list function behave . 
# also implement functions 
# use c - array 


import ctypes
class myList:
    # create a constructor
    def __init__(self) -> None:
        self.size = 1
        self.n = 0

        # create a ctype array of size = self.size

        self.A = self.__make_array(self.size)

    # code for printing an list [1,2,3]
    def __str__(self) -> str:
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ","

        return '[' + result[:-1] + "]"       # [:-1] exclude last 
    
    # slicing code 
    def __getitem__(self,index):
        if 0<index <self.n:
             return self.A[index]
        else:
             return "ArrayIndexOutOfBoundException" 
        
              

    def __make_array(self,capacity):
        # create a ctype array(static and refantial array) with size capacity
            return (capacity*ctypes.py_object)()
# fuction for length use magic function __len__
    def __len__(self):
         return self.n  
    
# implement append function to muList
    
    def append(self,item):
        if(self.n == self.size):
            #   resize
              self.__resize(self.size*2)
            #   append
        self.A[self.n] = item
        self.n +=1
        
#  implementation for insert function in the list 
    def insert(self,position,item):
         if self.n == self.size:
            self.__resize(self.size*2)
        
        # iterste
            for i in range(self.n,position,-1):
                self.A[i] = self.A[i-1]
            self.A[position] = item
            self.n =self.n+1


    #  code for deleting an item from the list 
    def __delitem__(self,position):
        # delete
        if 0<= position <self.n:
            for i in range(position,self.n-1):
                self.A[i] = self.A[i+1]
        self.n = self.n-1
    
    # resize code 
               
    def __resize(self,newCapicity):
        B= self.__make_array(newCapicity)
        self.size  =newCapicity
        # copy content of A to B
        for i in range(self.n):
            B[i] = self.A[i]

            # resign A
        self.A = B

    # pop function delete 
    def pop(self):
        if self.n ==0:
            return "Empity List"
        print(self.A[self.n-1])
        self.n = self.n-1

    # function for clear item in list 
        
    def clear(self):
        self.n = 0
        self.size = 1

    # function for finding item on index 
    def find(self,item):
        
        for i in range(self.n):
            if self.A[i] == item:
                 return i
            
        return "value error item not in list "
    
    #  implementation for remove function 

    def remove(self,item):
        position = self.find(item)
        if type(position) == int:
            self.__delitem__(position)
        else:
            return position 
             
     
             
L = myList()
L.append(3.4)
L.append("hello")
L.append(True)
L.append("ram")
# print(len(L))
# print(L) 
# print(L[1])     #<__main__.myList object at 0x0000024001D6FAD0> o/p
# print(L[3])
# print(L[100])
# L.pop()
# print(L)
# L.clear()
# print(L)

print(L.insert(1,100))
print(L)
L.insert(3,"ram")
print(L)
        



L.insert(2,100)
print(L)
L.__delitem__(100)
print(L)
L.remove(100)
print(L)
L.remove("hellowwww")
print(L)





    