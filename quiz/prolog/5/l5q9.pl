split_odd_even([H], [H], []).
split_odd_even([], [], []).
split_odd_even([H1, H2|T], [H1|T1], [H2|T2]) :- split_odd_even(T, T1, T2).
test_answer :-
    split_odd_even([a], A, B),
    write(A),
    writeln(B).
test_answer :-
    split_odd_even([a,b,c,d,e,f,g], A, B),
    write(A),
    writeln(B).
test_answer :-
    split_odd_even([1,2,3,5], A, B),
    write(A),
    writeln(B).