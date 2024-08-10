merge_sort([], []).
merge_sort([H], [H]).
merge_sort(L1, L2) :-
    split_odd_even(L1, Odd, Even),
    merge_sort(Odd, Odd_sort),
    merge_sort(Even, Even_sort),
    merge(Odd_sort, Even_sort, L2).
min([H|T], A, Min) :- H < A, min(T, H, Min).
min([H|T], A, Min) :- H >= A, min(T, A, Min).
min([], A, A).
remove(X, [X|T], ListOut) :- remove(X, T, ListOut).
remove(X, ListIn, ListIn) :- \+ member(X, ListIn).
remove(X, [H|T], [H|T1]) :- X \= H, remove(X, T, T1).
merge_sort([], []).
merge_sort(L1, [Min|T]) :- min(L1, 9999, Min), remove(Min, L1, L2),
    merge_sort(L2, T).