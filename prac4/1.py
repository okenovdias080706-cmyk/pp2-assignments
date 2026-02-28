#1
iterator=("Atik","Dias","Bauka","Sanzhar")
it=iter(iterator)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#2
iterator=[10,20,30]
for iter in iterator:
    print(iter)

#3
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

obj = MyNumbers()
for x in obj:
    print(x)

#4
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))

#5
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)

#6
squares = (x*x for x in range(5))

for num in squares:
    print(num)