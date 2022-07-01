#include <stdio.h>


main() {  
   	FILE *fp;
   	FILE *nf;
	char buff[255];
	fp = fopen("F:\\D\\hochanh\\DoAn\\TTDN\\mobilog.txt", "r");
	nf = fopen("F:\\D\\hochanh\\DoAn\\TTDN\\newfile.txt", "w+");
	while (fscanf(fp, "%s", buff) != EOF) {
		fprintf(nf, "%s\n",buff);
		fprintf(nf, "length: %d \n",strlen(buff));
    	printf("%s\n", buff);
    }
    
    
   	fclose(fp);
}
