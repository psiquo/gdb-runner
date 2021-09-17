#include <stdio.h>
#include <unistd.h>

char input;
char output; 

char AES_encrypt(char input) { return input; }

int main(int argc, char** argv) {
    int counter = 1; 
    
    printf("nRF51822 Booting...\n");
    printf("Chip is up, waiting for keyboard input...\n");

    while(1) {
        printf("\n\n === [ AES Encryption ] ===\n");
        
        // Read input from STDIN
        printf("\nReading input: ");
        input = getc(stdin);

        // Skip newline!
        getchar();

        // AES encryption
        output = AES_encrypt(input);

        printf("Input %c\nOutput %c\n\n", input, output);
                
        // Send encrypted packet
        printf("Sending packet (%d): %c", counter, output);
         
        sleep(1);
        counter++;
    }

    return 0;
}
