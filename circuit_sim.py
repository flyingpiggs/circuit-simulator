class Node:
    def __init__( self, _name, _inputs, _type, _value ):
        self.name = _name            #string
        self.inputs = _inputs        #list of strings that correspond to the input nodes names
        self.type = _type            #string
        self.value = _value          #string, although limited to one character
        self.outputReady = False

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
    Simulate( circuit, testVectors )

if __name__ == "__main__":
    main()
