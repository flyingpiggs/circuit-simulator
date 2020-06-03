class Node:
    def __init__( self, _name, _inputs, _outputs, _type ):
        self.name = _name             #used to access the graph dict
        self.inputs = _inputs         #list of keys correspond to the input nodes
        self.outputs = _outputs       #same as above, except for outputs
        self.type = _type             #string
        self.outputReady = False
        self.allInputsReady = False
        self.whichInputsReady = set()
        self.values = []              #array of values, for parallel TV simulation

    def PerformOp( self ):
        pass 

def MakeNodes( benchName ):
    pass

def GetTestVectors( fileName ):
    pass

def Simulate( circuit, testVectors ):
    pass

def main():
    # Read-in circuit benchmark and create circuit nodes
    userInput = input()
    circuit = MakeNodes( userInput )
    # Read-in test vectors
    userInput = input()
    testVectors = GetTestVectors( userInput )
    # Performance simulation/breadth-first search through the circuit
    # Simultaneously do some other stuff depending on what the assignment calls for?
    # Ex: Calculate the critical path (longest delay path)
    outputs = Simulate( circuit, testVectors )

if __name__ == "__main__":
    main()
