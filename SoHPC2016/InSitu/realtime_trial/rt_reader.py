import sysv_ipc
import time
import subprocess

key = 12345
p = subprocess.Popen(["./rt_writer.x",str(key)])
time.sleep(1)
# Create shared memory object
memory = sysv_ipc.SharedMemory(key)
completed = False

while not completed:
    frameCount = memory.read()
    print(frameCount)
    time.sleep(2)
    if p.poll() is not None:
        completed = True


print("Complete!")
# Find the 'end' of the string and strip
# i = frameCount.find('\0')
#    frameCount = frameCount[:i]
