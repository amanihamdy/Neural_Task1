import numpy as np

class Learning :
    def sigmoid(self , n):
        return 1 / ( 1 + np.exp(-n) )
    # input dataset
    training_inputs = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
     
    # output dataset
    training_outputs = np.array([[0,1,1,0]]).T
    
    np.random.seed(1)
    random_weights = 2 * np.random.random((3,1))-1
    print("Random starting weights : \n")
    print(random_weights)
    print ("\n************************\n")
    print("The Final Output :\n")
    def func(self):
        for iterx in range(1):
          output = np.dot(self.training_inputs , self.random_weights)
          activiation_output = self.sigmoid(output)
          print(activiation_output)


obj = Learning()
obj.func()


