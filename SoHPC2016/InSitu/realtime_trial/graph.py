def memory_read(memory):
    frameCount = memory.read()
    ar = np.fromstring(frameCount, dtype=np.uint32)
    return ar

#main 
import sysv_ipc
import time
import subprocess
import numpy as np
import matplotlib.pyplot as plt

key = 123456
dim = 10000
p = subprocess.Popen(["./calc.x",str(key),str(dim)])
time.sleep(1)
# Create shared memory object
memory = sysv_ipc.SharedMemory(key)
completed = False

plt.ion() ## Note this correction
fig=plt.figure()
plt.axis([0,dim-1,0,dim*dim])
line, = plt.plot(0,0)

while not completed:

    if p.poll() is not None:
        completed = True
        time.sleep(2)

    line.remove()
    line, = plt.plot(np.arange(0,dim),memory_read(memory),'r')
    plt.pause(0.0001)
    plt.show()

print("Complete!")
plt.show(block=True)

# Find the 'end' of the string and strip
# i = frameCount.find('\0')
#    frameCount = frameCount[:i]
