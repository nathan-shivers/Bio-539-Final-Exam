#!/usr/bin/env python3

import sys

def observed_substrings(sequence, k):
    """
    Returns the total count of unique k-mers for a given sequence and k-mer length.
    
            Parameters:
                sequnce (str): A single sequence as a string
                k (int): A whole number integer 
            Returns:
                total (int): An integer of the count of unique k-mers
    """
    if type(sequence) != str or type(k) != int: ## Check to see if sequence is a string and if k is a integer if not print error message
        return("Sequence needs to be a string and/or k needs to be a integer")
    if k > len(sequence): ## Check to if k is larger than sequence length if it is print error message 
        return("k needs to be smaller or equal to the length of the sequence")
    else:
        sub = [] 
        for i in range(len(sequence) - k + 1): ## Creates a long for the maximum amount sequence can be cut by k
            sub.append(sequence[i:i+k]) ## slice k lenth substrings and appends them into the sub list
        dic = {}
        for i in sub: ## Loops through sub adding each unique substring into a dictionary and the total count for each
            if i not in dic :
                dic[i] = 1
            else:
                dic[i] += 1
    total = len(dic)
    return(total) ## Returns the total number of unique substrings in sequence

def possible_substrings(sequence):
    """
    Returns the total possible number of k-mers for a given sequence.
    
        Parameters
            sequence (str): A single sequence as a string
        Returns:
            total (int): An integer of the count of all possible length k-mers for a sequence     
    """
    if type(sequence) != str: ## Checks if sequence is a string and if not prints error message
        return("Sequence needs to be a string")
    else:
        sub = []
        for i in range(1, len(sequence) + 1): ## loops through all possible lenghts of k starting at 1
            if 4**i <= len(sequence): ## If 4k is smaller than total length of sequence than 4k is used for total possible substrings
                sub.append(4 ** i)
            else: ## If 4k is larger than total length of sequence than n - k + 1 is used instead
                sub.append((len(sequence) - i) + 1)
        total = sum(sub)
        return(total) ## Returns the total sum of the list
    
def linguistic_complexity(sequence):
    """
    Returns the linguistic complexity for a given sequence.
    
        Parameters:
            sequence (str): A single sequence as a string
        Returns:
            proportion (float): Proportion of substrings of all sizes that are observed compared to the total number that are theoretically possible
    """
    if type(sequence) != str: ## Checks if sequence is a string and if not it prints an error message
        return("Sequence needs to be a string")
    else:
        p = possible_substrings(sequence) ## Runs total possible substrings on sequence
        sub = []
        for i in range(1, len(sequence) + 1): ## Loops through all possible k lenghts starting at 1
            sub.append(observed_substrings(sequence, i)) ## Appends the observed substring totals into a list
        o = sum(sub) ## Sums all observed substrings with all k lengths 
        proportion = o/p
        return(proportion) ## Returns the proportion of substrings of all sizes that are observed 
                    ## compared to the total number that are theoretically possible

def main():
    with open(sys.argv[1]) as file: ## Opens file from terminal and adds each line into a list called lines
        lines = [line.strip() for line in file]
    for i in range(len(lines)): ## Loops through each sequence from the inputted file and prints the linguistic complexity for each
        print("Sequence", i+1, ":",linguistic_complexity(lines[i]))

if __name__ == "__main__":
    main()