;declaring list called as n
(defparameter *n* '(2 4 6 5 7))  
	
	
	
	
;declaring 'listn' function for getting the nth element of a list 	
(defun listn(l f)                          
    (return-from listn (nth (- f 1) l))       
)

;index nth list


;calling the function with a list and an index of the element required
(format t "3rd Item in the List = ~a ~%" (listn *n* 3)) 

