eats(X, Y) :- likes(X, Y).
eats(X, Y) :- hungry(X), edible(Y).
likes(bob, chocolate).
hungry(alice).
test_answer :- eats(bob, chocolate),
               writeln('Bob eats chocolate.').
edible(crisps).
hungry(bob).
likes(bob, sushi).
test_answer :- eats(bob, crisps),
               writeln('Bob eats crisps.').
likes(alice, rock).
likes(alice, jazz).
edible(pizza).
hungry(bob).
test_answer :- eats(alice, rock),
               writeln('Alice eats rock!').