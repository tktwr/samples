#include <stdio.h>
#include <iostream>

const char* g_text[] = {
    "example program.\n",
    "\n",
    "data 0\n",
    "data 1\n",
    "data 2.0\n",
    "\0"
};

void f_write_text_file(const char* fname) {
    FILE* fp = fopen(fname, "w");
    fclose(fp);
}

void f_read_text_file(const char* fname) {
    FILE* fp = fopen(fname, "r");
    fclose(fp);
}

int main(int argc, char *argv[]) {
    return 0;
}

