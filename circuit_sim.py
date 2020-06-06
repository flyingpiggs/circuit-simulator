# It's the Pretty Printer! Just lke Pretty Patties without the tongue coloring
# Documentation: https://docs.python.org/3/library/pprint.html
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Node:
    def __init__( self, _name, _inputs, _outputs, _type ):
        self.name = _name             #used to access the graph dict
        self.inputs = _inputs         #list of keys correspond to the input nodes
        self.outputs = _outputs       #same as above, except for outputs
        self.type = _type             #string
        self.outputReady = False
        self.allInputsReady = False
        self.whichInputsReady = set()
        self.values = []              #array of values, for parallel TV simulation
    # ---------------------------------------------------------------------------- #
    def PerformOp( self, nodes ):
        pass
    # ---------------------------------------------------------------------------- #
# -------------------------End of Class Declaration------------------------------ #
class Circuit:
    def __init__( self, _benchName ):
        self.gateCount, self.inputWidth, self.outputWidth = self.MakeNodes( _benchName )
        self.inputs = self._FindInputs()
        self.outputs = self._FindOutputs()
    # ---------------------------------------------------------------------------- #
    def MakeNodes( self, benchName ):
        bench = open( benchName, 'r' )
        nodes = {}
        gateCount = 0
        inputCount = 0
        outputCount = 0

        #Establish names, in-edges
        for line in bench:
            name = ''
            inputs = []
            type = ''

        #The loop below should establish the out-edges
        for node in nodes:
            break

        self.nodes = nodes
        bench.close()
        return gateCount, inputCount, outputCount
    # ---------------------------------------------------------------------------- #
    # return a list of strings corresponding to the input node keys
    def _FindInputs( self ):
        inputs = []
        return inputs
    # ---------------------------------------------------------------------------- #
    # return a list of strings corresponding to the output node keys
    def _FindOutputs( self ):
        outputs = []
        return outputs
    # ---------------------------------------------------------------------------- #
    # Should return a list of strings
    def FetchTestVectors( self, fileName ):
        testVectors = []
        return testVectors
    # ---------------------------------------------------------------------------- #
    # output values should be packaged in a dict of lists
    # the keys into the dict will be the same as the node names
    # the order of each list will correspond to the order of the TV file
    def GetOutputValues( self ):
        values = {}
        return values
    # ---------------------------------------------------------------------------- #
    def PrintOutput( self, fileName ):
        #if ( fileName == '' ) then print to screen; else to fileName
        if ( fileName != '' ):
            outFile = open(fileName + '.txt', 'w')
        else:
            outFile = None
        pass
    # ---------------------------------------------------------------------------- #
    def Simulate( self, options ):  #add support for options down the road
        return True
    # ---------------------------------------------------------------------------- #

# -------------------------End of Class Declaration------------------------------ #

# ---------------------------------------------------------------------------- #
def main():
    # Read-in circuit benchmark and create circuit nodes
    print("Enter bench name: ")
    userInput = input()
    circuit = Circuit( userInput )
    # Read-in test vectors
    print("Enter test vector file name")
    userInput = input()
    testVectors = circuit.FetchTestVectors( userInput )
    # Performance simulation/breadth-first search through the circuit
    # Simultaneously do some other stuff depending on what the assignment calls for?
    # Ex: Calculate the critical path (longest delay path)
    if ( circuit.Simulate( None ) ):
        print("Simulation complete!")
    else:
        print("Simulation failed!!!")

if __name__ == "__main__":
    main()
# ---------------------------------------------------------------------------- #
