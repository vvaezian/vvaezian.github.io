Suppose you are given a table of currency exchange rates, represented as a 2D array.  
Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make,  
starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

### First Method: O(n^3) time, O(n) space
Solution: `https://www.dailycodingproblem.com/blog/how-to-find-arbitrage-opportunities-in-python/`

Regarding the currencies as nodes and exchange rates as edges weights, we can regard the given 2D array as a directed graph.  
The question whether there is a cycle that multiplication of weights in it is bigger than 1.  
If we transform the array by taking the negative log, the question becomes whether there is a negative cost cycle.  
This can be solved using Bellman-Ford algorithm in O(n^3) time.  
We can do the transformation in-place, so we just need O(n) extra space for running the Bellman-Ford algorithm.

### Second Method: O(n^3) time, O(1) space
- Definition: A sequence of currencies `<a_1, ..., a_n>` is *fair* if `r_1,2 * ... * r_n-1,n * r_n,1 = 1`
, where `r_m,n` is the exchange ratio between currencies `a_m` and `a_n`
- Theorem: A sequense of currencies `<a_1, ..., a_n>` is not fair iff there exists currencies `a_i`, `a_j`, `a_k` such that `r_i,j * r_j,k != r_i,k`.  
Proof. Left as an exercise.  

So we just need to check this transitivity condition for all tripples of currencies.
