mirror(leaf(X), leaf(Y)) :- X = Y.
mirror(tree(X, Y), tree(Z, A)) :- mirror(X, A), mirror(Y, Z).
mirror(X, Y) :-
    X = tree(T1, T2), Y = tree(T3, T4), mirror(T1, T4), mirror(T2, T3);
    X = leaf(B1), Y = leaf(B2), B1 = B2.
test_answer1 :-
    mirror(leaf(foo), leaf(foo)),
    write('OK').
test_answer2 :-
    mirror(tree(leaf(foo), leaf(bar)), tree(leaf(bar), leaf(foo))),
    write('OK').
test_answer3 :-
    mirror(tree(tree(leaf(1),  leaf(2)),  leaf(4)), T),
    write(T).
test_answer4 :-
    mirror(tree(tree(leaf(1),  leaf(2)),  tree(leaf(3), leaf(4))), T),
    write(T).