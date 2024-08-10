addone([], []).
addone([H1|T1], [H2|T2]) :- is(H2, H1 + 1), addone(T1, T2).
test_answer :-
    addone([3, 6, 7], L),
    writeln(L).
test_answer :-
    addone([1, 2, 3, 4], [2, 3, 4, 5]),
    writeln('OK').
test_answer :-
    addone([], []),
    writeln('OK').