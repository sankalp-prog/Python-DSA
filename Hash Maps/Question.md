# Important Questions about Hash Maps 
### 1. Why is this important? `% len(self.data_map)` 
> **A:** So that the index/output of the hashing is in the range of the size we desire which is `len(self.data_map)`

### 2. Why is it important to look at every character in the string key? `for letter in key:`
> **A:** To Reduce collision by making the hashing of the key that much more unique.

### 3. Will this hash function always give the same hash output given the same input key? Why is that important?
> **A:** Yes it will always give the same output. It's important so that we can then search for it. This is the only reason why you can't use a random number generator. A random number generator fulfills all the properties you need for a hash function except this one.

### 4. Why is it important to add in prime numbers to mangle the output like `(my_hash + ord(letter) * 23)?` Why not just `(my_hash + ord(letter))`?
> **A:**  To reduce collision. If you simply added the words, then 'aab' and 'aba' and 'baa' would collide. 'cc' and 'bd' and 'ae' would also collide. This is why you should explode the number while keeping it within memory bounds. Add, multiply, exponentiate, torture each piece of the key until it looks like something totally different.

