/*
   
   The method CalcTerm (m, n) computes 3*m-2*n using only arithmetic 
   operations +3, -1, and -2. 

   Fix the 'invariant' and 'decreases' annotations such that it verifies
   
*/
function method abs(m: int): nat
{ if m>0 then m else -m }

method CalcTerm(m: int, n: nat) returns (res: int)
  ensures res == 3*m-2*n;
{ 
  var m1: nat := abs(m);
  var n1: nat := n;
  res := 0;
  
  while (m1!=0)
    invariant 0 <= m1 <=abs(m)
    invariant res == 3* abs(m) - 3 * abs(m1)
    decreases m1
  { 
    res := res+3; 
    m1 := m1-1;
  }

  if (m<0) { res := -res; }
  
  while (n1!=0)
    invariant res == 3 * m - 2 * (n - n1)
    invariant 0 <= n1 <= n
    decreases n1
  {
    res := res-2; 
    n1 := n1-1;
  }
}
