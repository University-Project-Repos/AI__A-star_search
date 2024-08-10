py_triple(A, B, C) :- 0 < A, A =< B, B =< C, A^2 + B^2 =:= C^2.
test_answer :-
    py_triple(3,4,5),
    write('OK').
test_answer :-
    py_triple(4,3,5),
    writeln('Incorrect, a Pythagorean triple is non-decreasing!').
test_answer :-
    py_triple(0,0,0),
    writeln('Incorrect, a Pythagorean triple contains only positive integers!').
test_answer :-
    py_triple(3,4,7),
    writeln('Incorrect!').
test_answer :-
    writeln('OK').
test_answer: -
py_triple(24, 45, 51),
write('OK').