# circuit-simulator
Personal notes for the time being...

Need to port over the generator code from previous project for test vector
generation. I'm pretty sure I can just use the code directly...

~Finish the BFS for circuit simulation~

A lot of user experience thing need to be refined. I also need to give
some consideration to how to design the code. I think I should put most,
if not all of the code that is related to getting user input into main()

Features to add:

1) Fault simulation
    - Basically D-algorithm support
2) Fault coverage
3) Timing simulation
    - Will need to determine "level" of each node
4) Backtracking algorithm for relevant info (like satisfiability)
5) Critical path
    - I think this is just adding a super source and source sink, then getting longest path
