# It's the Pretty Printer! Just lke Pretty Patties without the tongue coloring
# Documentation: https://docs.python.org/3/library/pprint.html
import pprint
pp = pprint.PrettyPrinter(indent=4)

# The name of a node correspond to its output wire, so something like
#              ____
#         --->|Gate|  name
#         --->|____|---------->
class Node:
    def __init__( self, _name, _inputs, _type, _value ):
        self.name = _name            #string
        self.inputs = _inputs        #list of strings that correspond to the input nodes names
        self.type = _type            #string
        self.value = _value          #string, although limited to one character
        self.outputReady = False

    def PerformOp( self, nodes ):
        if ( self.type == 'INPUT' or self.type == 'OUTPUT' ):
            print("Error, type cannot be 'input' or 'output' for operations")
            return False

        op = self.type
        if ( op == 'AND' ):
            for inputName in self.inputs:
                val = GetVal( inputName, nodes )
                if not val:
                    print( "No name match found when getting value for: " + inputName )
                    return False
                if ( val == '0' ):
                    self.value = '0'
                    return True
                elif ( val == '1' ):
                    continue
                else:
                    print("Error, unsupported value at node: " + inputName )
                    return False
            self.value = '1'
        elif ( op == 'OR' ):
            for inputName in self.inputs:
                val = GetVal( inputName, nodes )
                if not val:
                    print( "No name match found when getting value for: " + inputName )
                    return False
                if ( val == '1' ):
                    self.value = '1'
                    return True
                elif ( val == '0' ):
                    continue
                else:
                    print("Error, unsupported value at node: " + inputName )
                    return False
            self.value = '0'
        elif ( op == 'NOR' ):
            for inputName in self.inputs:
                val = GetVal( inputName, nodes )
                if not val:
                    print( "No name match found when getting value for: " + inputName )
                    return False
                if ( val == '1' ):
                    self.value = '0'
                    return True
                elif ( val == '0' ):
                    continue
                else:
                    print("Error, unsupported value at node: " + inputName )
                    return False
            self.value = '1'
        elif ( op == 'NAND' ):
            for inputName in self.inputs:
                val = GetVal( inputName, nodes )
                if not val:
                    print( "No name match found when getting value for: " + inputName )
                    return False
                if ( val == '0' ):
                    self.value = '1'
                    return True
                elif ( val == '1' ):
                    continue
                else:
                    print("Error, unsupported value at node: " + inputName )
                    return False
            self.value = '0'
        elif ( op == 'XOR' ):
            onesCount = 0
            for inputName in self.inputs:
                val = GetVal( inputName, nodes )
                if not val:
                    print( "No name match found when getting value for: " + inputName )
                    return False
                if ( val == '1' ):
                    onesCount += 1
                elif ( val == '0' ):
                    continue
                else:
                    print("Error, unsupported value at node: " + inputName )
                    return False
            if ( ( onesCount % 2 ) == 1 ):   #odd number of 1s
                self.value = '1'
            else:
                self.value = '0'
        elif ( op == 'XNOR' ):
            onesCount = 0
            for inputName in self.inputs:
                val = GetVal( inputName, nodes )
                if not val:
                    print( "No name match found when getting value for: " + inputName )
                    return False
                if ( val == '1' ):
                    onesCount += 1
                elif ( val == '0' ):
                    continue
                else:
                    print("Error, unsupported value at node: " + inputName )
                    return False
            if ( ( onesCount % 2 ) == 0 ):   #odd number of 1s
                self.value = '1'
            else:
                self.value = '0'
        elif ( op == 'NOT' ):
            val = GetVal( inputs[0], nodes )
            if not val:
                print( "No name match found when getting value for: " + inputName )
                return False
            if ( val == '1' ):
                val = '0'
            elif ( val == '0' ):
                val = '1'
            else:
                print("Error, unsupported value at node: " + inputName )
                self.value = '?'
                return False
            self.value = val
        elif ( op == 'BUFF' ):
            val = GetVal( inputs[0], nodes )
            if not val:
                print( "No name match found when getting value for: " + inputName )
                return False
            self.value = val
        else:
            print("Error, unsupported operation at node: " + self.name )
            return False
        return True     #just to indicate success
    # ------------------------------------------------------------------------------- #

# -------------------------End of Class Declaration------------------------------ #

def MakeNodes( benchName ):
    bench = open( benchName, 'r' )
    circuit = []

    for line in bench:
        node = None
        name = ''
        inputs = []
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
            line = line.replace("INPUT", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            #name = "wire_" + line
            name = line
            node = Node( name, None, 'INPUT', 'U' )
        elif line[0:6].upper() == "OUTPUT":
            line = line.replace("OUTPUT", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            #name = "wire_" + line
            name = line
            node = Node( name, None, 'OUTPUT', 'U' )
        elif '=' in line:
            op = ''
            splitAtEq = line.split("=")
            #name = "wire_" + splitAtEq[0]
            name = splitAtEq[0]
            toGetOp = splitAtEq[1].split("(")
            op = toGetOp[0].upper()
            toGetInputs = toGetOp[1].replace(")", "")
            inputs = toGetInputs.split(",")
            node = Node( name, inputs, op, 'U' )
        circuit.append( node )
        pp.pprint( vars ( node ) )

        #end of for loop
    return circuit

# ------------------------------------------------------------------------------- #
# This function traverses the graph looking for a name match
# Once a match is found, it returns the value
def GetVal( name, nodes ):
    for node in nodes:
        if ( node.name == name and node.type != 'OUTPUT' ):
            return node.value
    return None   #This indicates an error since there should always be a match

# ------------------------------------------------------------------------------- #
def GetTestVectors( fileName ):
    pass

# ------------------------------------------------------------------------------- #
def Simulate( circuit, testVectors ):
    pass

# ------------------------------------------------------------------------------- #
def main():
    # Read-in circuit benchmark and create circuit nodes
    print("Enter benchmark file name: ")
    userInput = input()
    circuit = MakeNodes( userInput )
    # Read-in test vectors
    print("Enter input file name: ")
    userInput = input()
    testVectors = GetTestVectors( userInput )
    # Performance simulation/breadth-first search through the circuit
    # Simultaneously do some other stuff depending on what the assignment calls for?
    # Ex: Calculate the critical path (longest delay path)
    print("Starting circuit simulation...")
    Simulate( circuit, testVectors )
    print("Simulation done!")

if __name__ == "__main__":
    main()
