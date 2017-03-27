/**
   Write a method that finds the maximum value of a given array 'a'.
   Write pre- and post-condition for the method FindMax.
   
   Annonate your implementation with invariant and decreases annotations so that it verifies.
*/
method FindMax (a:array<int>)  returns (max : int)
requires a != null;
requires a.Length > 1; 
ensures forall k:: 0 <= k < a.Length ==> a[k] <= max; 
{
  max := a[0];
  var i := 0;
  while (i < a.Length)
  invariant 0 <= i <= a.Length;
  decreases a.Length - i;
  invariant forall k:: 0 <= k < i ==> a[k] <= max;
  {
    if (a[i] > max) { max := a[i];} 
    i := i + 1;
  }
  return max;
  
}

