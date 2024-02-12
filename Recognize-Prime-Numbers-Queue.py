import math
class main_queue:
    lst = []
    def __init__(self, n):
        self._N = n
        self._data = [None] * self._N
        self.front = -1
        self.rear = -1

    
    def is_empty(self):
        return self.front == -1

    
    def is_full(self):
        return self.rear + 1 == self._N

    
    def push(self, e):
        if not self.is_full():
            self._data[self.rear + 1] = e
            self.rear += 1
            if self.front == -1:
                self.front += 1
            return 1
        else:
            return 0

    
    def pop(self):
        if self.is_empty():
            return 0, None
            
        else:
            x = self._data[self.front]
            self.front += 1
            print(self.front)
            if self.front > self.rear:
                self.front = -1
                self.rear = -1
                
            else:
                # Shift elements to the left
                for i in range(self.front, self.rear + 1):
                    self._data[i - self.front] = self._data[i]
                # Reset the last element
                self._data[self.rear] = None
                self.rear -= 1
            return x

    
    def is_prime(self):
        lprime=[]
        for i in self._data:
            k=2
            s=0
            while k<i:
                if i%k==0:
                    s += 1
                k += 1
            if s==0:
                lprime.append(i)
            else:
                continue
        return ("There are " , len(lprime) , " prime numbers and they are:" , lprime)
    
    def show(self):
        for x in self._data:
            print("", x, "<", end="")
        print()
        return "Done"


count = int(input("How many number?"))
if count > 30 or count<10:
    print("Number out of range!") 
main = main_queue(count)
for i in range(count):
    e = int(input("number:"))
    main.push(e)


print(main.show())
print(main.is_prime())
