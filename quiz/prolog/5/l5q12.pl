inside(Min, Max, X) :- Min =< Max, X = Min.
inside(Min, Max, X) :-
    Min < Max,
    is(MinTwo, Min + 1),
    inside(MinTwo, Max, X).
test_answer :-
    inside(1, 3, 2),
    writeln('OK').
test_answer: -
    findall(X, inside(1, 3, X), List),
    writeln(List).
test_answer: -
    findall(X, inside(1, -1, X), List),
    writeln(List).
test_answer: -
    findall(X, inside(1, 1, X), List),
    writeln(List).