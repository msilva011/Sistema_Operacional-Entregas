#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void info(void){
	printf("Meu ID de processo: %u\n", getpid());
	printf("ID do meu pai     : %u\n", getppid());

}
//teste