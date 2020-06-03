class Gate:
    def __init__( self, _name, _inputs, _outputs, _op ):
        self.name = _name            #used to access the graph dict
        self.inputs = _inputs        #list of keys correspond to the input nodes
        self.outputs = _outputs      #same as above, except for outputs
        self.op = _op                #op should be a function
        self.allInputsReady = False  #Used with below to make breadth-first search a bit faster
        self.whichInputsReady = set()
        # Python doc on sets: https://docs.python.org/3/tutorial/datastructures.html#sets
        # When a gate's input wire is ready, its name (which is also the key into the dict),
        # gets added to the set. Once the size of the set is equivalent to the list of inputs,
        # all the input wires should be ready, thus we can change allInputsReady to True.

        # Other potential data members:
        #   1. gateDelay
        #   2. outputReady
        #   3. totalDelay
        #   4. Other useful things that I don't know about

class Output:
    def __init__( self, _values, _source, _name ):
        self.values = _values  #should be an array of values that correspond to the test vector set indices
        self.source = _source  #should be the name of the logic gate that outputs to this node
        self.name = _name


class Input:
    def __init__( self, _values, _name ):
        self.values = _values   #should be an array of values that correspond to the test vector set indices
        self.name = _name

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
