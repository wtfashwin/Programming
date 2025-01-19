'''
Given an array citations[] of size n such that citations[i] 
is the number of citations a researcher received for ith paper, the task is to find the H-index. H-index(H) is the largest value such that the researcher has published at least H papers that have been cited at least H times.

'H' stands for Hirsch index as it was proposed by the J.E. Hirsch in 2005. The H-index is defined as the author-level metric that attempts to measure both the productivity and the citation impact of the publication of the scientist or the scholar.

Examples:

Input: citations[] = [5, 0, 2, 0, 2]
Output: 2
Explanation: There are at least 2 papers (5, 2, 2) with at least 2 citations.

Input: citations[] = [6, 0, 3, 5, 3]
Output: 3
Explanation: There are at least 3 papers (6, 5, 3, 3) with at least 3 citations.
'''

def hIndex(citations):
    n = len(citations)
    freq = [0] * (n + 1)

    for citation in citations:
        if citation >= n:
            freq[n] += 1
        else:
            freq[citation] += 1

    idx = n
    
    s = freq[n]
    while s < idx:
        idx -= 1
        s += freq[idx]
    
    return idx

if __name__ == '__main__':
    citations = [6, 0, 3, 5, 3]
    print(hIndex(citations))