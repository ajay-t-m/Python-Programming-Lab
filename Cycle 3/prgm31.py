import statistics
import  math
import  time
print("The value of pi is ",math.pi)
sec=time.time()
print("Seconds since epoch is ",sec)
l=[1,2,3,4,5,6]
print("The average of list is ",statistics.mean(l))
localt=time.ctime(sec)
print("Local time is",localt)