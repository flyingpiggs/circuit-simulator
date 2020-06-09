# It's the Pretty Printer! Just lke Pretty Patties without the tongue coloring
# Documentation: https://docs.python.org/3/library/pprint.html
from copy import copy
import pprint
pp = pprint.PrettyPrinter(indent=4)

class Node:
    def __init__( self, _name, _inputs, _type ):
        self.name = _name             #used to access the graph dict
        self.inputs = _inputs         #list of keys correspond to the input nodes
        self.outputs = []             #same as above, except for outputs
        self.type = _type             #string
        self.outputReady = False
        self.allInputsReady = False
        self.whichInputsReady = set()
        self.values = []              #array of values, for synchronous TV simulation
    # ---------------------------------------------------------------------------- #
    def PerformOp( self, nodes ):
        if ( self.type == 'INPUT' or self.type == 'OUTPUT' ):
            print("Error, type cannot be 'INPUT' or 'OUTPUT' for operations")
            return False
        if not self.allInputsReady:
            print("Error, not all the inputs for node %s are ready!" % self.name )
            return False


        op = self.type
        inputs = self.inputs
        inputCount = len(inputs)
        outputValues = copy( nodes[ inputs[0] ].values )
        TV_Count = len( outputValues )

        for i in range( 1, inputCount ):
            currentValues = nodes[inputs[i]].values
            for j in range( TV_Count ):
                if op == "AND":
                    outputValues[j] = outputValues[j] & currentValues[j]
                elif op == "NAND":
                    outputValues[j] = ~( outputValues[j] & currentValues[j] )
                elif op == "OR":
                    outputValues[j] = outputValues[j] | currentValues[j]
                elif op == "NOR":
                    outputValues[j] = ~( outputValues[j] | currentValues[j] )
                elif op == "XOR":
                    outputValues[j] = outputValues[j] ^ currentValues[j]
                elif op == "XNOR":
                    outputValues[j] = ~( outputValues[j] ^ currentValues[j] )
                elif op == "NOT":
                    outputValues[j] = ~currentValues[j]
                elif op == "BUFF":
                    outputValues[j] = currentValues[j]
                else:
                    print("Error, unsupported operation at node: " + self.name )
                    return False
        self.values = outputValues
        return True    #just indicating success
    # ---------------------------------------------------------------------------- #
# -------------------------End of Class Declaration------------------------------ #
class Circuit:
    def __init__( self, _benchName ):
        self.gateCount, self.inputWidth, self.outputWidth = self.MakeNodes( _benchName )
        #self.inputs = self._FindInputs()
        #self.outputs = self._FindOutputs()
        #I need to grab the strings for the two above lists in the MakeNodes function
        #Otherwise, the bit order of the output vector won't match the benchmark file
        #Note: self.nodes is made in MakeNodes
        self.readyForOp = []
        self.waitingForInputs = self.nodes.keys()
    # ---------------------------------------------------------------------------- #
    def MakeNodes( self, benchName ):
        bench = open( benchName, 'r' )
        nodes = {}
        # In terms of a directed acyclic graph
        primaryInputs = []      #source nodes
        primaryOutputs = []     #sink nodes
        gateCount = 0
        inputCount = 0
        outputCount = 0

        # Make the nodes and connect the graph
        # Each line of the benchmark only provides information about the in-edges
        # so I need to establish the sources' out-edges afterwards
        # The primary output nodes should share a name with gates...this will cause collison
        # Just call it name_out for the primary output nodes
        for line in bench:
            name = ''
            inputs = []
            type = ''
            node = None

            # Ignoring empty lines and comments, and removing spaces or newline
            if (line == "\n"):
                continue
            line = line.replace(" ", "")
            line = line.replace("\n", "")
            if (line[0] == "#"):
                continue

            # @ Here it should just be in one of these formats:
            # INPUT(x)
            # OUTPUT(y)
            # z=LOGIC(a,b,c,...)

            # Removing everything but the line variable name
            if (line[0:5].upper() == "INPUT"):
                inputCount += 1
                line = line.replace("INPUT", "")
                line = line.replace("(", "")
                line = line.replace(")", "")
                name = line
                primaryInputs.append(name)
                node = Node( name, None, 'INPUT' )
            elif line[0:6].upper() == "OUTPUT":
                outputCount += 1
                line = line.replace("OUTPUT", "")
                line = line.replace("(", "")
                line = line.replace(")", "")
                name = line + '_out'
                primaryOutputs.append(name)
                inputs.append( line )
                node = Node( name, inputs, 'OUTPUT' )
            elif '=' in line:
                gateCount += 1
                op = ''
                splitAtEq = line.split("=")
                name = splitAtEq[0]
                toGetOp = splitAtEq[1].split("(")
                op = toGetOp[0].upper()
                toGetInputs = toGetOp[1].replace(")", "")
                inputs = toGetInputs.split(",")
                node = Node( name, inputs, op )
            nodes[name] = node
            #Comment out below lines to get rid of the print statements about the nodes
            print("The key, %s, maps to the node: " % nodes[name].name)
            pp.pprint( vars ( node ) )
            #end of for loop

        # This loop is used to establish the out-edges
        # The benchmark file only holds in-edge information so
        # I need to infer the out-edges after connecting in-edges
        # Primary inputs have no in-edges
        for key in nodes:  # Iterators through dict are the keys, not the values
            node = nodes[key]
            if node.type == 'INPUT':
                continue
            for input in node.inputs:
                nodes[input].outputs.append( node.name )
            #end of inner for loop
        #end of outer for loop

        self.primaryInputs = primaryInputs
        self.primaryOutputs = primaryOutputs
        self.nodes = nodes
        bench.close()
        return gateCount, inputCount, outputCount
    # ---------------------------------------------------------------------------- #
    # return a list of strings corresponding to the input node keys
    # def _FindInputs( self ):
    #     inputs = []
    #     for node in self.nodes:
    #         if node.type == 'INPUT':
    #             inputs.append( node.name )
    #     return inputs
    # ---------------------------------------------------------------------------- #
    # return a list of strings corresponding to the output node keys
    # def _FindOutputs( self ):
    #     outputs = []
    #     for node in self.nodes:
    #         if node.type == 'OUTPUT':
    #             outputs.append( node.name )
    #     return outputs
    # ---------------------------------------------------------------------------- #
    # Should return a list of strings
    # bit ordering within each string/vector is MSB <--- LSB
    # bit ordering in the benchmark file should go
    # LSB
    # |
    # |
    # V
    # MSB
    # This above order should be paralled by the primary inputs list
    def FetchTestVectors( self, fileName ):
        testVectors = []
        return testVectors
    # ---------------------------------------------------------------------------- #
    # Helper function:
    # output values should be packaged in a dict of lists
    # the keys into the dict will be the same as the node names
    # the order of each list will correspond to the order of the TV file
    def _GetOutputValues( self ):
        values = []
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
    def _ToggleWhichInputsReady( self, name ):
        node = self.nodes[name]
        size = len( node.outputs )
        for i in range(size):
            whichInputsReady = self.nodes[node.outputs[i]].whichInputsReady
            if node.name not in whichInputsReady:
                whichInputsReady.add( node.name )
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
    circuit.FetchTestVectors( userInput )
    # Performance simulation/breadth-first search through the circuit
    # Simultaneously do some other stuff depending on what the assignment calls for?
    # Ex: Calculate the critical path (longest delay path)
    pp.pprint( vars ( circuit ) )
    if ( circuit.Simulate( None ) ):
        print("Simulation complete!")
    else:
        print("Simulation failed!!!")

if __name__ == "__main__":
    main()
# ---------------------------------------------------------------------------- #
