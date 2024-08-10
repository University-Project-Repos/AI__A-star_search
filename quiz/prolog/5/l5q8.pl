remove(X, [X|T], ListOut) :- remove(X, T, ListOut).
remove(X, ListIn, ListIn) :- \+ member(X, ListIn).
remove(X, [H|T], [H|T1]) :- X \= H, remove(X, T, T1).
test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).
test_answer :- 
    remove(1, [1, 2, 1, 4, 3, 3], Result),
    writeln(Result).
test_answer :-
    remove(2, [2], L),
    writeln(L).
test_answer :-
    remove(d, [a, b, c], L),
    write(L).
test_answer :-
    remove(a, [], L),
    write(L).
test_answer :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').