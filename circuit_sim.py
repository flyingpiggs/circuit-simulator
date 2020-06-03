class Node:
    def __init__( self, _name, _inputs, _outputs, _type, _value ):
        self.name = _name            #string
        self.inputs = _inputs        #list of strings that correspond to the input nodes names
        self.type = _type            #string
        self.value = _value          #string, although limited to one character
        self.outputReady = False     

def main():
    # Read-in circuit benchmark
    # Create the circuit graph
    # Read-in test vectors
    # Performance simulation/breath-first search through the circuit
    # Most likely do other things depending on what the assignment calls for
    # Ex: Calculate the critical path (longest delay path)
    pass

if __name__ == "__main__":
    main()
