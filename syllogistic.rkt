(define (penultimate x)
  (list-ref x (- (length x) 2)))

(define (copula prop)
  (car (set-intersect '(is are were was will be)
                 prop)))

(define (decopula prop)
  (remove (copula prop) prop))

(define (modal-words prop)
  (set-intersect '(possibly necessarily)
                      prop))

(define (quantifiers prop)
  (set-intersect '(all every any some no not)
                        prop))

(define (right-side x)
  (remove (copula x) (member (copula x) x)))

(define (left-side x)
  (reverse (remove (copula x) (member (copula x) (reverse x)))))

(define (is-universal? prop)
  (if (or (member 'all prop) (member 'none prop))
      #t
      #f))

(define (is-particular? prop)
  (if (member 'some prop)
      #t
      #f))

(define (is-affirmative? prop)
  (cond ((and (member 'all (left-side prop)) (not (member 'not (right-side prop)))) #t)
        ((and (member 'some (left-side prop)) (not (member 'not (right-side prop)))) #t)
        ((and (member 'no (left-side prop)) (member 'not (right-side prop))) #t)
        ((and (member 'not (left-side prop)) (member 'not (right-side prop))) #t)
        (true #f)))

(define (is-negative? prop)
  (cond ((and (member 'no (left-side prop)) (not (member 'not (right-side prop)))) #t)
        ((and (member 'some (left-side prop)) (member 'not (right-side prop))) #t)
        ((and (member 'not (left-side prop)) (not (member 'not (right-side prop)))) #t)
        ((and (member 'all (left-side prop)) (member 'not (right-side prop))) #t)
        (true #f)))

(define (is-categorical? prop)
  (if (and (not (member 'necessarily prop)) (not (member 'possibly prop)))
      #t
      #f))

(define (demodalize prop)
  (remove* (modal-words prop) prop))

(define (dequantify prop)
  (remove* (quantifiers prop) prop))

(define (subject prop)
  (demodalize (dequantify (left-side prop))))

(define (predicate prop)
  (demodalize (dequantify (right-side prop))))

(define (terms prop)
  (list (subject prop) (predicate prop)))

(define (distributed-terms prop)
  (cond ((and (is-universal? prop) (is-affirmative? prop)) (car (terms prop)))
        ((and (is-universal? prop) (is-negative? prop)) (terms prop))
        ((and (is-particular? prop) (is-affirmative? prop)) '())
        ((and (is-particular? prop) (is-negative? prop)) (cadr (terms prop)))
        (true null)))

(define (is-modal? prop)
  (if (or (member 'necessarily prop) (member 'possibly prop))
      #t
      #f))

(define (de-dicto? prop)
  (if (and (is-modal? prop) (or (equal? (car prop) 'necessarily) (equal? (car prop) 'possibly)))
      #t
      #f))

(define (de-re? prop)
  (if (and (is-modal? prop) (or (member 'possibly (right-side prop)) (member 'necessarily (right-side prop))))
  #t
  #f))

(define (valid? arg)
  (cond ((not (equal? (length arg) 3)) "Invalid: not the correct argument form")
        ((> (length (list (terms (car arg)) (terms (cadr arg)) (terms (cddr arg)))) 3) "Invalid: Fallacy of Four Terms")
        (true #f)))

(valid? '((all whales are mammals) (all mammals are animals) (some whales are animals)))
