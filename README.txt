The project is meant to implement a program, which outputs
the set of all possible causes of an event given an arbitrary event, a causal graph, and a distance.

The project is useful, because it produces a statement of the set of all possibilities, enabling future decision making.

Input : (Event : String, path : String, distance = infty : Int)
Output : A .txt file containing the set of all possible primary events in the first line and all paths described in natural language from primamry events to the Event given as input.

Assumptions:
    1) The input path is given as a path in a non-Windows filesystem.