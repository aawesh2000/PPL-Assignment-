flight(madrid, iberia, barcelona, 120, 65).
flight(barcelona, iberia, madrid, 120, 65).

flight(barcelona, iberia, valencia, 110, 75).
flight(valencia, iberia, barcelona, 110, 75).

flight(madrid, iberia, valencia, 40, 50).
flight(valencia, iberia, madrid, 40, 50).

flight(madrid, iberia, malaga, 50, 30).
flight(malaga, iberia, madrid, 50, 30).

flight(valencia, iberia, malaga, 80, 120).
flight(malaga, iberia, valencia, 80, 120).

flight(toronto, iberia, madrid, 800, 480).
flight(madrid, iberia, toronto, 800, 480).

flight(barcelona, iberia, london, 220, 240).
flight(london, iberia, barcelona, 220, 240).

flight(toronto, aircanada, london, 500, 360).
flight(london, aircanada, toronto, 500, 360).

flight(toronto, aircanada, madrid, 900, 480).
flight(madrid, aircanada, toronto, 900, 480).

flight(madrid, aircanada, barcelona, 100, 60).
flight(barcelona, aircanada, madrid, 100, 60).

flight(toronto, united, madrid, 950, 540).
flight(madrid, united, toronto, 950, 540).

flight(toronto, united, london, 650, 420).
flight(london, united, toronto, 650, 420).

flight(paris, united, toulouse, 35, 120).
flight(toulouse, united, paris, 35, 120).

airport(toronto, 50, 60).
airport(madrid, 75, 45).
airport(malaga, 50, 30).
airport(barcelona, 40, 30).
airport(valencia, 40, 20).
airport(london, 75, 80).
airport(paris, 50, 60).
airport(toulouse,40,30).


is_flight(A,B) :-
    flight(A,X,B,Y,Z).


is_cheap(A,X,B) :-
    flight(A,X,B,Y,Z),Y < 400.

two_flights(A,B) :-
(flight(A,X,B,Y,Z),flight(A,C,B,D,E),X\==C).

is_prefered(A,B) :-
    (flight(A,X,B,Y,Z)),(Y < 400 ; X = aircanada).

then_flight(A,B) :-
    (flight(A,X,B,Y,Z), X = united) -> (flight(A,C,B,D,E), C = aircanada).
