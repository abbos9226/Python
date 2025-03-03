import concurrent.futures
import collections
import re

def process_chunk(chunk):
    """Counts word occurrences in a chunk of text."""
    word_count = collections.Counter()
    words = re.findall(r'\b\w+\b', chunk.lower())  # Extract words and normalize case
    word_count.update(words)
    return word_count

def read_file_in_chunks(filename):
    """Reads the file in chunks."""
    with open(filename, 'r') as file:
        while True:
            chunk = file.read()
            if not chunk:
                break
            yield chunk

def threaded_word_count(filename, num_threads=4):
    """Counts word occurrences in a large file using multiple threads."""
    word_counts = collections.Counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(process_chunk, read_file_in_chunks(filename))
    
    for result in results:
        word_counts.update(result)  # Merge word counts from all threads

    return word_counts

# Example usage
filename = "large_text_file.txt"  # Replace with the actual file path
word_counts = threaded_word_count(filename)

# Display the most common words
print("Top 10 most common words:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")
