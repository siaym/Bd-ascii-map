#include <stdio.h>
#include <string.h>

/**
 * Run-Length Encoded ASCII Map of Bangladesh
 *
 * Algorithm Explanation:
 * - The encoded 'magic' string represents alternating run-lengths of characters.
 * - Each character byte 'c' in the string stores a run length: length = 126 - c.
 * - Even indices (i % 2 == 0) represent spaces (' ').
 * - Odd indices (i % 2 == 1) represent stars ('*').
 * - Characters are wrapped to a new line every 64 columns (counter == 64).
 */
int main(void) {
    const char *magic =
        "y}@z?{|{HtJpy|TgUhQjPlKqIphynJsHw}}JuGwG}}tLmOhXe[`]b[tzn\\tzl]xvn["
        "xwj_}}zvl[}tlOm]}pn_zqmd{}xsmer{|xmfr}zxmfmxm||phwm||z}|{{gwl}WxCxF|y}"
        "=";

    const size_t len = strlen(magic);
    int counter = 0;

    for (size_t i = 0; i < len; ++i) {
        int run_length = 126 - (unsigned char)magic[i];
        char symbol = (i & 0x1) ? '*' : ' ';

        for (int j = 0; j < run_length; ++j) {
            putchar(symbol);
            if (++counter == 64) {
                counter = 0;
                putchar('\n');
            }
        }
    }

    putchar('\n');
    return 0;
}
