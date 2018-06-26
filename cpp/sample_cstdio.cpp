// *memo_sample_cstdio*
#include <stdio.h>

#define BUFFER_SIZE 1024

const char *g_text[] = {
    "example program.\n",
    "\n",
    "data 0\n",
    "data 1\n",
    "data 2.0\n",
    "\0"};

void f_write_text_file(const char *fname) {
    FILE *fp = fopen(fname, "w");
    for (int i = 0; g_text[i][0]; i++) {
        fputs(g_text[i], fp);
    }
    fclose(fp);
}

void f_read_text_file(const char *fname) {
    FILE *fp = fopen(fname, "r");
    char line[BUFFER_SIZE];
    while (fgets(line, BUFFER_SIZE, fp)) {
        printf("%s", line);
    }
    fclose(fp);
}

void f_write_binary_file(const char *fname) {
    FILE *fp = fopen(fname, "wb");
    //size_t r = fwrite(data, size, n, fp);
    fclose(fp);
}

void f_read_binary_file(const char *fname) {
    FILE *fp = fopen(fname, "rb");
    //size_t r = fread(data, size, n, fp);
    fclose(fp);
}

int main(int argc, char *argv[]) {
    const char *fname = "data_cstdio.txt";

    f_write_text_file(fname);
    f_read_text_file(fname);

    return 0;
}
