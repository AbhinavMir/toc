#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Function to calculate Shannon entropy
double shannon_entropy(const char *data) {
    int frequency[256] = {0};
    int length = strlen(data);

    for (int i = 0; i < length; i++) {
        frequency[(int)data[i]]++;
    }

    double entropy = 0.0;
    for (int i = 0; i < 256; i++) {
        if (frequency[i] > 0) {
            double probability = (double)frequency[i] / length;
            entropy -= probability * log2(probability);
        }
    }

    return entropy;
}

// Function to compress data
char *compress_data(const char *data, double threshold, int *compressed_length) {
    double entropy = shannon_entropy(data);

    if (entropy < threshold) {
        // Data is not compressed
        *compressed_length = strlen(data);
        char *compressed = (char *)malloc(*compressed_length + 1);
        strcpy(compressed, data);
        return compressed;
    } else {
        // Data is encoded using a simple encoding (e.g., ASCII)
        *compressed_length = strlen(data) + 1; // +1 for null-terminator
        char *compressed = (char *)malloc(*compressed_length);
        strcpy(compressed, data);
        return compressed;
    }
}

// Function to decompress data
char *decompress_data(const char *compressed_data, int compressed_length, double threshold) {
    if (compressed_length == strlen(compressed_data)) {
        // Data was not compressed
        char *decompressed = (char *)malloc(compressed_length + 1);
        strcpy(decompressed, compressed_data);
        return decompressed;
    } else {
        // Data was encoded using a simple encoding (e.g., ASCII)
        char *decompressed = (char *)malloc(compressed_length);
        strcpy(decompressed, compressed_data);
        return decompressed;
    }
}

int main() {
    const char *original_data = "hello world, hello world, hello world!";
    double threshold = 1.0;

    int compressed_length;
    char *compressed_data = compress_data(original_data, threshold, &compressed_length);

    printf("Original Data Size: %zu bytes\n", strlen(original_data));
    printf("Compressed Data Size: %d bytes\n", compressed_length);

    char *decompressed_data = decompress_data(compressed_data, compressed_length, threshold);

    printf("Original Data: %s\n", original_data);
    printf("Decompressed Data: %s\n", decompressed_data);

    free(compressed_data);
    free(decompressed_data);

    return 0;
}
