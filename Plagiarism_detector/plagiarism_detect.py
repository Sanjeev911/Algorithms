import re
import hashlib
import os
import sys
import argparse


def load_target_document(path):
    data = []
    with open(path,"rb") as f:
        for line in f.readlines():
            line = line.strip()
            if line !='':
                data.append(line)
    f.close()
    return " ".join(str(data))

def load_original_docs(directory,file_type = ".txt"):
    files = {}
    for filename in os.listdir(directory):
        if os.path.isfile(filename) and filename.endswith(file_type) and not filename in files:
            files[filename] = load_target_document(filename)
    return files


def extract_tokens(file):
    substring_length = 5
    token_set = set()
    tokens = re.sub("[^\w]", " ",  file).split()
    for i in range(len(tokens)-substring_length):
        to = tokens[i]
        for j in tokens[i+1:i+substring_length]:
            to+= ' '+ j
        token_set.add(to)
    return token_set

def create_hash(token_set):
    hash_table = map(hash,token_set)
    return hash_table

def return_hashes(files,data,data_path):
    dict_of_hashes = {}
    for filename,file in files.items():
        token_set = extract_tokens(file)
        dict_of_hashes[filename] = create_hash(token_set)
    dict_of_hashes[data_path] = create_hash(extract_tokens(data))
    return dict_of_hashes

def evaluate_plagiarism(dict_of_hashes,path):    # the first hash in the dict of hashes consist of the target document and the rest of the source documents
    Jaccard_similarity_coefficient = {}
    percentage_similarity = {}
    s1 = set(dict_of_hashes[path])
    for filename,hash_value in dict_of_hashes.items():
        if filename!=path:
            s2 = set(hash_value)
            intersection = s1.intersection(s2)
            union = s1.union(s2)
            similarity_coefficient = len(intersection)/len(union)
            Jaccard_similarity_coefficient[filename] = similarity_coefficient
            percentage_similarity[filename] = len(intersection)/len(s1)
    return Jaccard_similarity_coefficient,percentage_similarity




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error : enter the path of the file to be checked and the path to directory of Target files.")
        exit()
    source_path = sys.argv[2]
    if not os.path.isdir(source_path):
        print("Error: The enterd path ",source_path," is not a directory.Please enter a valid directory path.")
        exit()
    if not os.path.isfile(sys.argv[1]):
        print("Error: The enterd path ",sys.argv[1]," is not of a file.Please enter a valid path to a file.")
        exit()
    target_path = sys.argv[1]
    file_type = ""   # for listing all types of files . Change it to ".txt" for checking only .txt files
    files = load_original_docs(source_path,"")
    data = load_target_document(target_path)
    dict_of_hashes = return_hashes(files,data,target_path.split("/")[-1])   # extracting and passing the name of the "to be tested" file from its path name
    percentage_similarity,jaccardian_similarity = evaluate_plagiarism(dict_of_hashes=dict_of_hashes,path=target_path.split("/")[-1]) # extracting and passing the name of the "to be tested" file from its path name
    print("jaccardian_similarity is as follows :",'\n')
    for item in reversed(sorted(jaccardian_similarity.items(), key = lambda kv:(kv[1], kv[0]))):
        print(item[0]," Matches : ",item[1])
    print("----------------------------------------------------")

    print("Percentage Similarity as follows:",'\n')
    for i in reversed(sorted(percentage_similarity.items(), key = lambda kv:(kv[1], kv[0]))):
        print(i[0]," Matches : ","{:.3f}".format(i[1]*100) , "%")
