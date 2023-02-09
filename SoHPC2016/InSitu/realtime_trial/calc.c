#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <time.h>
#include <math.h>

int main(int argc, const char **argv)
{
  int shmid,size_byte,dim;
  int *buffer;
  key_t key;
  char *shared_memory;

  // take argouments
  key = atoi(argv[1]);
  dim = atoi(argv[2]);

  //allocate memory
  size_byte = dim*sizeof(int);
  buffer = (int*) malloc(size_byte);

  // Setup shared memory
  if ((shmid = shmget(key, size_byte, IPC_CREAT | 0666)) < 0)
  {
    printf("Error getting shared memory id");
    exit(1);
  }

   // Attached shared memory
  if ((shared_memory = shmat(shmid, NULL, 0)) == (char *) -1)
  {
    printf("Error attaching shared memory id");
    exit(1);
  }

  struct timespec ts;
  ts.tv_sec = 0;
  ts.tv_nsec = 2000000L;

  for(int i=0;i<dim;i++)
  {
    buffer[i] = i*i;
    memcpy(shared_memory, buffer, size_byte);
    nanosleep(&ts, NULL);

  }

   // Detach and remove shared memory
  shmdt(shmid);
  shmctl(shmid, IPC_RMID, NULL);
}
