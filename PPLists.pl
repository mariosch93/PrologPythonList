/* Print all elements of a list ?-print_list([a,b,c]). a b c */
%print_list([]):-nl. %nl = newline
%print_list([H|T]):-write(H),write(' '),print_list(T).

/* 1.Addition of all the list elements */
sumlist([],0).
sumlist([Head|Tail],N) :- sumlist(Tail, K), N is Head+K.

/* 2.Delete an element from the list */
delete_el(_,[],[]).
delete_el(N,[N|T],U):-!,delete_el(N,T,U).
delete_el(N,[H|T],[H|U]):-delete_el(N,T,U).

/* 3.Randomly select some elements from the list */
remove_at(X,[X|Xs],1,Xs).
remove_at(X,[Y|Xs],K,[Y|Ys]) :- K > 1, 
   K1 is K - 1, remove_at(X,Xs,K1,Ys).
rnd_select(_,0,[]).
rnd_select(Xs,N,[X|Zs]) :- N > 0,
    length(Xs,L),
    I is random(L) + 1,
    remove_at(X,Xs,I,Ys),
    N1 is N - 1,
    rnd_select(Ys,N1,Zs).

/* 4.Remove unique elements [6,2,3,3,5,2,3,1,4] => [2,3,3,2,3] */
memberx(N,[N|_]).
memberx(N,[_|T]):-memberx(N,T).
delete_unique([],[]).
delete_unique([H|T],[H|Y]):-memberx(H,T),!,delete_unique(T,Y).
delete_unique([_|T],Y):-delete_unique(T,Y).

/* 5.Finding the lenght of a list */
list_length([],0).
list_length([_|Xs],L) :- list_length(Xs,N) , L is N+1 .

/* 6.Finding the average value */
average([],0).
average([Head|Tail],M):- sumlist([Head|Tail],S) , list_length([Head|Tail],L) , M is S/L.

/* 7.maximum function [1,-2,3] => 3 */
maximumx(P,D,V):- P>=D, V=P, !.
maximumx(_,D,V):-V=D.
max([H],H).
max([H|T],X):-max(T,S),maximumx(H,S,X).

/* 8.reverse all elements of a lists */
addtoend(H,[],[H]).
addtoend(X,[H|T],[H|T1]):-addtoend(X,T,T1).
reverse_list([],[]).
reverse_list([H|T],Y):- reverse_list(T,T1), addtoend(H,T1,Y).

/* 9.increment elements of list [5,6,7,8] => [6,7,8,9] */
increment([],[]).
increment([H|T],[X|Y]):-increment(T,Y), X is H+1.

/* 10.quick sort */
appendx([],A,A).
appendx([H|T],A,[H|U]):-appendx(T,A,U).
splittotwo(_,[],[],[]).
splittotwo(I,[H|T],[H|U],V):- H=<I, splittotwo(I,T,U,V),!.
splittotwo(I,[H|T],U,[H|V]):- splittotwo(I,T,U,V).
quick([],[]).
quick([H|T],L):-splittotwo(H,T,U,V), quick(U,X),quick(V,Y), appendx(X,[H|Y],L).

/* 11.implement insertion into a sorted list (the result is sorted as well) */
%need to also sort the list in python first!!!!!!!!!!!!!!!!!!!!!!!!!!
insertinto(N,[],[N]).
insertinto(N,[H|T],[N,H|T]):-H>=N,!.
insertinto(N,[H|T],[H|Y]):-insertinto(N,T,Y).

/* 12.Fibonacci numbers: print nth Fibonacci number. */
%mobify the list with the fibonaci numbers with range(1,len(list)).!!!!!!!!!!!!
fib(1,1).
fib(2,1).
fib(N,F):- N>2,
	   N1 is N-1, fib(N1,F1),
	   N2 is N-2, fib(N2,F2),
	   F is F1+F2.