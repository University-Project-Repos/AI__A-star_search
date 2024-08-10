normal_tear_rate(RATE) :- RATE >= 5.
low_tear_rate(RATE) :- RATE < 5.
young(AGE) :- AGE < 45.
diagnosis(hard_lenses, Age, Astigmatic, Tear_Rate) :- young(Age), Astigmatic == yes, normal_tear_rate(Tear_Rate).
diagnosis(soft_lenses, Age, Astigmatic, Tear_Rate) :- young(Age), Astigmatic == no, normal_tear_rate(Tear_Rate).
diagnosis(no_lenses, Age, Astigmatic, Tear_Rate) :- low_tear_rate(Tear_Rate).
test_answer1 :-
    diagnosis(hard_lenses, 21, yes, 11),
    writeln('OK').
test_answer2 :-
    diagnosis(X, 45, no, 4),
    writeln(X).
test_answer3 :-
    diagnosis(X, 19, no, 5),
    writeln(X).