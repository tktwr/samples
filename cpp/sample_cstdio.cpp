// *memo_cpp.cstdio*
#include <stdio.h>

#define BUFFER_SIZE 1024
#define ARRAY_SIZE 3

const char *g_text[] = {
    "example program.\n",
    "\n",
    "data 0\n",
    "data 1\n",
    "data 2.0\n",
    "\0"};
const int g_binary[ARRAY_SIZE] = {1, 2, 3};

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
    size_t r = fwrite(g_binary, sizeof(int), ARRAY_SIZE, fp);
    printf("f_write_binary_file: r: %d\n", r);
    fclose(fp);
}

void f_read_binary_file(const char *fname) {
    FILE *fp = fopen(fname, "rb");
    int data[ARRAY_SIZE];
    size_t r = fread(data, sizeof(int), ARRAY_SIZE, fp);
    printf("f_read_binary_file: r: %d\n", r);
    for (int i=0; i<ARRAY_SIZE; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");
    fclose(fp);
}

int main(int argc, char *argv[]) {
    const char *fname_text = "data_cstdio.txt";
    const char *fname_binary = "data_cstdio.bin";

    f_write_text_file(fname_text);
    f_read_text_file(fname_text);
    f_write_binary_file(fname_binary);
    f_read_binary_file(fname_binary);

    return 0;
}
