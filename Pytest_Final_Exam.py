def observed_substrings(sequence, k):
    if type(sequence) != str or type(k) != int: ## Check to see if sequence is a string and if k is a integer if not print error message
        return("Sequence needs to be a string and/or k needs to be a integer")
    if k > len(sequence): ## Check to if k is larger than sequence length if it is print error message 
        return("Sequence length needs to be larger or equal to k")
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
    return(len(dic)) ## Returns the total number of unique substrings in sequence

def possible_substrings(sequence):
    if type(sequence) != str: ## Checks if sequence is a string and if not prints error message
        return("Sequence needs to be a string")
    else:
        sub = []
        for i in range(1, len(sequence) + 1): ## loops through all possible lenghts of k starting at 1
            if 4*i <= len(sequence): ## If 4k is smaller than total length of sequence than 4k is used for total possible substrings
                sub.append(4 * i)
            else: ## If 4k is larger than total length of sequence than n - k + 1 is used instead
                sub.append((len(sequence) - i) + 1)
        return(sum(sub)) ## Returns the total sum of the list
    
def linguistic_complexity(sequence):
    if type(sequence) != str: ## Checks if sequence is a string and if not it prints an error message
        return("Sequence needs to be a string")
    else:
        p = possible_substrings(sequence) ## Runs total possible substrings on sequence
        sub = []
        for i in range(1, len(sequence) + 1): ## Loops through all possible k lenghts starting at 1
            sub.append(observed_substrings(sequence, i)) ## Appends the observed substring totals into a list
        o = sum(sub) ## Sums all observed substrings with all k lengths 
        return(o/p) ## Returns the proportion of substrings of all sizes that are observed 
                    ## compared to the total number that are theoretically possible
        
        
def test1_observed_substring():
    sequence = 26
    k = 4
    actual_output = observed_substrings(sequence, k)
    expected_output = "Sequence needs to be a string and/or k needs to be a integer"
    assert actual_output == expected_output

def test2_observed_substring():
    sequence = "ATTTGGATT"
    k = 12
    actual_output = observed_substrings(sequence, k)
    expected_output = "Sequence length needs to be larger or equal to k"
    assert actual_output == expected_output
    
def test3_observed_substring():
    sequence = "ATTTGGATT"
    k = 2
    actual_output = observed_substrings(sequence, k)
    expected_output = 5
    assert actual_output == expected_output
    
def test1_possible_substring():
    sequence = ["AGTAT", "AGTAGTAGT"]
    actual_output = possible_substrings(sequence)
    expected_output = "Sequence needs to be a string"
    assert actual_output == expected_output

def test2_possible_substring():
    sequence = "ATTTGGATT"
    actual_output = possible_substrings(sequence)
    expected_output = 40
    assert actual_output == expected_output
    
def test3_possible_substring():
    sequence = "AGA"
    actual_output = possible_substrings(sequence)
    expected_output = 6
    assert actual_output == expected_output
    
def tes1_linguistic_complexity():
    sequence = "ATTTGGATT"
    actual_output = linguistic_complexity(sequence)
    expected_output = 0.875
    assert actual_output == expected_output
    
def test1_linguistic_complexity():
    sequence = 7500
    actual_output = linguistic_complexity(sequence)
    expected_output = "Sequence needs to be a string"
    assert actual_output == expected_output

