sentence(Word1, Word2, Word3, Word4, Word5) :-
        word(article, Word1),
        word(noun, Word2),
        word(verb, Word3),
        word(article, Word4),
        word(noun, Word5).
word(article, a).
word(article, every).
word(noun, criminal).
word(noun, doctor).
word(verb, eats).
word(verb, likes).
