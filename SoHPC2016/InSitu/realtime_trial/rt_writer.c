#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>

unsigned int sleep(unsigned int seconds);

int main(int argc, const char **argv)
{
   int shmid;

   key_t key = atoi(argv[1]);
   char *shared_memory;

   // Setup shared memory
   if ((shmid = shmget(key, 11, IPC_CREAT | 0666)) < 0)
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


   memcpy(shared_memory, "Hello World", sizeof("Hello World"));
   sleep(5);
   memcpy(shared_memory, "Hello Marco", sizeof("Hello Marco"));
   sleep(5);
   memcpy(shared_memory, "Hello Fabio", sizeof("Hello Fabio"));
   sleep(5);
   memcpy(shared_memory, "Hello Serena", sizeof("Hello Serena"));
   sleep(5);
   memcpy(shared_memory, "Hello Eric", sizeof("Hello Eric"));
   sleep(5);
   memcpy(shared_memory, "Hello Pippo", sizeof("Hello Pippo"));
   sleep(5);
   memcpy(shared_memory, "Hello Pluto", sizeof("Hello Pluto"));
   sleep(5);
   memcpy(shared_memory, "Hello Giulia", sizeof("Hello Giulia"));
   sleep(5);
   memcpy(shared_memory, "Hello Maria", sizeof("Hello Maria"));
   sleep(5);

   // Detach and remove shared memory
   shmdt(shmid);
   shmctl(shmid, IPC_RMID, NULL);
}
