import math
import sys

def shannon_entropy(data):
    # Calculate the probability distribution of symbols in the data
    symbol_counts = {}
    total_symbols = len(data)
    
    for symbol in data:
        if symbol in symbol_counts:
            symbol_counts[symbol] += 1
        else:
            symbol_counts[symbol] = 1
    
    probabilities = [count / total_symbols for count in symbol_counts.values()]
    
    # Calculate Shannon entropy from formula
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    
    return entropy

def compress_with_entropy(data, threshold=1.0):
    # Calculate the Shannon entropy of the input data
    entropy = shannon_entropy(data)
    
    # Check if the data is compressible based on the threshold
    if entropy < threshold:
        return data, True  # Data is not compressed
    else:
        compressed_data = data.encode('utf-8')
        return compressed_data, False  # Data is encoded using UTF-8 (not efficient compression)

def decompress_with_entropy(compressed_data, is_compressed):
    if is_compressed:
        return compressed_data  # No compression applied
    else:
        return compressed_data.decode('utf-8')  # Decode using UTF-8

# Example usage:
original_data = "hello world, hello world, hello world!"
print(f"Original Data Size: {sys.getsizeof(original_data)} bytes")

compressed_data, is_compressed = compress_with_entropy(original_data)
print(f"Compressed Data Size: {sys.getsizeof(compressed_data)} bytes")

decompressed_data = decompress_with_entropy(compressed_data, is_compressed)
print(f"Decompressed Data Size: {sys.getsizeof(decompressed_data)} bytes")

print(f"Original Data: {original_data}")
print(f"Decompressed Data: {decompressed_data}")
