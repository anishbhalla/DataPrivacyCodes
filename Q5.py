# Python program that generates a password using a random combination of words from a dictionary file.
import random

def load_words_from_file(file_path):
    with open(file_path, 'r') as file:
        
        words = [line.strip() for line in file if line.strip()]
    return words

def generate_password(word_list, num_words=4):
  
    return ''.join(random.choices(word_list, k=num_words))

dictionary_file_path = "dictionary.txt"  
try:
    word_list = load_words_from_file(dictionary_file_path)
    
    password = generate_password(word_list, num_words=4)
    print("Generated Password:", password)
except FileNotFoundError:
    print("The dictionary file was not found. Please check the file path.")

