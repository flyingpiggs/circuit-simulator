# This module is meant to take the Circuit class from the circuit simulator code
# and use the information contained within a circuit object to make a file
# that can be executed using graphviz to make a drawing of the graph

# Example for DOT that they gave
# 1:  digraph G {
# 2:      main -> parse -> execute;
# 3:      main -> init;
# 4:      main -> cleanup;
# 5:      execute -> make_string;
# 6:      execute -> printf
# 7:      init -> make_string;
# 8:      main -> printf;
# 9:      execute -> compare;
# 10: }

# I do not need to actually write out all the path
# but I do need get all the out-edges

def CircuitToDOT( circuit, outFile ):
    edges = []
    # '->'
    nodes = circuit.nodes
    keys = circuit.nodeKeys
    for key in keys:
        node = nodes[key]
        # the key should correspond to the source node
        if node.type == 'OUTPUT':
            continue
        for dest in node.outputs:
            line = key + '->' + dest
            edges.append(line)

    print( "digraph circuit {\n", file = outFile )
    for edge in edges:
        print( edge, file = outFile )
    print( '}\n', file = outFile )
