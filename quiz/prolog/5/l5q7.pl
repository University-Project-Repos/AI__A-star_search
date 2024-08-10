element([Element|_], 0, Element).
element([_|T], Index, Element) :- element(T, I, Element), is(Index, I + 1).
test_answer :-
    element([a, b, c, d, e, f], 2, X),
    writeln(X).
test_answer :-
    element([a, b, c, d], I, d),
    writeln(I).
test_answer :-
    element([a, b, c, d], 6, X),
    writeln('Wrong answer!').
test_answer :-
    writeln('OK').
test_answer :-
    element(L, I, X),
    writeln('OK').