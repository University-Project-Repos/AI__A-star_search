merge([H1|T1], [H2|T2], [H1|T]) :- H1 =< H2, merge(T1, [H2|T2], T).
merge([H1|T1], [H2|T2], [H2|T]) :- H1 >= H2, merge([H1|T1], T2, T).
merge([], L2, L2).
merge(L1, [], L1).
merge([], [], []).
test_answer :-
    merge([3, 6, 7], [1, 2, 3, 5, 8], L),
    writeln(L).
test_answer :-
    merge([3, 6, 7], [], L),
    writeln(L).