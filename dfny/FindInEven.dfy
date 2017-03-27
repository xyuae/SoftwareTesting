/* The method findInEven (a, x) either returns an index r of array a such that 
    (a) r is even
    (b) the value of cell r of a is x
   Otherwise, it returns -1. 
   The method assumes that the array a is non-null.

   Write pre- and post-conditions for the method.
   Annotate the loop with invariants such that the method verifies.
*/
method findInEven (a: array<int>, x:int) returns (r:int)
requires a != null
ensures  r != -1 ==> 0 <= r < a.Length;
ensures  r != -1 ==> a[r] == x;
ensures r != -1 ==>  r % 2 == 0
ensures r == -1 ==> 
 forall k::0 <= k < a.Length && k % 2 == 0 ==> a[k] != x;
{
  r := -1;
  var i := 0;
  while (i < a.Length)
  invariant 0 <= i <= a.Length + 1
  invariant i % 2 == 0 
  invariant r == -1 || r % 2 == 0
  invariant r < a.Length
  invariant r != -1 ==> a[r] == x
  invariant r == -1 && 0 < i < a.Length ==> forall y:: 0<= y < i && y % 2 == 0 ==> a[y] != x
  invariant r == -1 && i >= a.Length ==> forall y:: 0 <=y < a.Length && y % 2 == 0 ==> a[y] != x
  decreases a.Length - i
  {
    if (x == a[i]) { r := i; }
    i := i + 2;
  }
}
