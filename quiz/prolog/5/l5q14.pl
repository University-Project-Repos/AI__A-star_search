py_triple(A, B, C, Min, Max) :-
	between(Min, Max, A),
	between(Min, Max, B),
	between(Min, Max, C),
	0 < A, A =< B, B =< C, A^2 + B^2 =:= C^2.
test_answer :-
    findall([A, B, C], py_triple(A, B, C, 1, 10), List),
    writeln(List).