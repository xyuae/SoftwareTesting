havoc x, y;
assume y >= 0;
c := 0;
r := x;
while c < y 
inv c <= y 
do 
{ r := r + 1; c := c + 1 }; 
assert r = x + y

