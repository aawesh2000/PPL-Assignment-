;function'fr' for gettting factorial of a number without recursion
(defun fr(n)
    (defvar *m* 1)                        ;variable m
    (loop for x from 1 to n               ; looping 
	    do(setf *m* (* *m* x))			  ;updating the value of m after every call						
    )              
    (return-from fr *m*)                  ; returning the value
)
;m setf (m * x)

;calling function fr for checking its working
(format t "~a ~%"(fr 3))
