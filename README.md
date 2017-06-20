# TextId

TextID is a forensic author-analysis tool useful for those wanting to determine authorship of an unknown work. This project was inspired by the successful efforts to identify the author of "The Cuckoo's Calling." Though "The Cuckoo's Calling" was published under the pseudonym "Robert Garbialit," but its actual author was found to be J. K. Rowling. See: http://www.salon.com/2013/08/23/how_j_k_rowling_was_exposed_as_robert_galbraith_partner/

TextID does a mathematical analysis of the degree of similarity across several features, including:
1. The distribution of words used by an author 
2. The distribution of word lengths (noted above) 
3. The distribution of word-stems used (e.g., "spam" and "spamming" would have the same stem, PORTER used as suffix-stripping algorithm) 
4. The distribution of sentence-lengths used 
5. The distribuction of puctuation marks used
6. The distribution of conjuctions used
7. The distribution of capital letters
8. The distribution of independent clauses
9. The distribution of "high frequency" words (determination of what is "high frequency" done by proprietary algorithm
10. Several more analysis tolls

To use TextID, simply upload two text samples from known authors (preferbly greater than 500 words each, to insure accuracy) to "train" the program. Then, upload an unknown work and run the program. The program will return whether the unknown work is more similar to model 1 or model 2, the degree of confidence, and the results of each test.
