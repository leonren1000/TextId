# TextId

TextID is a author-analysis tool useful for those wanting to determine authorship of an unknown work. This project was inspired by the successful efforts to identify the author of "The Cuckoo's Calling." Though "The Cuckoo's Calling" was published under the pseudonym "Robert Garbialit," but its actual author was found to be J. K. Rowling. See: http://www.salon.com/2013/08/23/how_j_k_rowling_was_exposed_as_robert_galbraith_partner/

TextID does a mathematical analysis of the degree of similarity across several features, including:
1. The distribution of words used by an author 
2. The distribution of word lengths (noted above) 
3. The distribution of word-stems used (e.g., "spam" and "spamming" would have the same stem, PORTER used as suffix-stripping algorithm) 
4. The distribution of sentence-lengths 
5. The distribuction of puctuation marks used
6. The distribution of conjuctions used
7. The distribution of capital letters
8. The distribution of independent clauses
9. The distribution of "high frequency" words (determination of what is "high frequency" done by proprietary algorithm
10. Several other analysis tools

To use TextID, simply upload two text samples from known authors (preferbly greater than 500 words each, to insure accuracy) to "train" the program. Then, upload an unknown work and run the program. The program will return whether the unknown work is more similar to model 1 or model 2, the degree of confidence, and the results of each test.

Output is something like this:

 +++++++++++ Model1 +++++++++++
 +++++++++++ Model2 +++++++++++
 +++++++++++ Unknown text +++++++++++
Overall comparison of Unknown (trial) vs Model1 and Model2

                name      vsTM1       vsTM2        winning model
                ----      -----       -----        -------------
               words  -10189.16    -9757.60               Model2
         wordlengths   -3535.48    -3477.34               Model2
               stems  -10073.37    -9622.22               Model2
     sentencelengths    -406.56     -375.87               Model2
         punctuation    -350.14     -316.67               Model2
        conjunctions     -17.93      -15.29               Model2
      captialization    -414.39     -399.96               Model2
  independentClauses     -52.89      -47.78               Model2
  highFrequencyWords    -622.66     -580.34               Model2

  --> Model1 wins on 0 features
  --> Model2 wins on 9 features

  OVERALL RESULT:
  ++++++     Model2 is the better match!     +++++

  Confidence Level (out of 100) [<0.5 is low, >3 is high]:  3.3850713196119027
