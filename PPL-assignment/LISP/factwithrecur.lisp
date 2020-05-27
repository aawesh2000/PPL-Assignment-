;function 'factoria' for getting factorial of a number using recursion
(defun factoria (n)
    (cond
        ((= n 0) 1) ;; Special case, 0! = 1
        ((= n 1) 1) ;; Base case, 1! = 1
        (t
            ;; Recursive case
            ;; Multiply n by the factorial of n - 1.
            (* n (factoria (- n 1)))
            ;n * factoria(n-1)
        )
    )
)



;calling function factoria for checking its working
(format t "~a ~%"(factoria 5))
