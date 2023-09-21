---
title: "Shannon Entropy: Intuition, Proof and Applications"
draft: false
---

Ref: [A mathematical theory of communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)

Claude Shannon formulated the mathematical expression for entropy, which is now known as Shannon entropy, through a systematic development based on key principles from probability theory and information theory. Here's a step-by-step explanation of how he arrived at the formula:

1. **Basic Concepts:**
   - Shannon started with the idea of information and uncertainty. He wanted a measure of the amount of information in a message or a random variable.
   - He considered a discrete random variable [$ X $] with [$ n $] possible outcomes, denoted as [$ x_1, x_2, \ldots, x_n $].
   - Shannon introduced the concept of "self-information" (or "surprisal") for each outcome [$ x_i $]. He reasoned that less probable outcomes should carry more information.
   - 

2. **Self-Information:** Shannon defined self-information [$ I(x_i) $] as follows:
   
   [$ I(x_i) = -\log_b(P(x_i)) $]

   - [$ P(x_i) $] is the probability of outcome [$ x_i $].
   - [$ b $] is the base of the logarithm, which is typically 2 (for measuring information in bits) but can be other values as well.

   The negative sign ensures that self-information is a positive value that increases with decreasing probability.

   The logarithm in the information content [$ I(x_i) $] is chosen to represent the idea that less probable outcomes should carry more information (greater surprise), as the logarithm amplifies the effect of smaller probabilities. It also ensures that the information content is additive for independent events, making it a mathematically consistent measure of uncertainty.

3. **Entropy Definition:** Shannon recognized that the average information content of a random variable should be a measure of its uncertainty or entropy. He defined entropy [$ H(X) $] as the expected value (or mean) of self-information:

   [$ H(X) = \sum_{i=1}^{n} P(x_i) \cdot I(x_i) = -\sum_{i=1}^{n} P(x_i) \cdot \log_b(P(x_i)) $]

   This formula represents the average amount of information needed to describe the outcomes of the random variable [$ X $]. This also defines the fact that information content of each outcome [$ x_i $] is weighted by its probability [$ P(x_i) $]. Outcomes with higher probabilities contribute more to the overall uncertainty, while rare outcomes have a more substantial impact on the measure of entropy.

4. **Properties of Entropy:**
   - Shannon showed that entropy satisfied several important properties, including:
     - It is always non-negative: [$ H(X) \geq 0 $].
     - It is maximized when all outcomes are equally likely (maximum uncertainty).
     - It is additive for independent random variables: [$ H(XY) = H(X) + H(Y) $].
     - It increases with the number of possible outcomes.
     - It can be expressed in different units depending on the base of the logarithm.

5. **Applications:** Shannon's entropy concept found applications not only in communication theory but also in fields like data compression, cryptography, and information retrieval. It is especially useful in Huffman coding (which is in scope for discussion for this blog).

## Data compression

This field is non-trivial, we are only exploring an example from above, and then implementing a minimal data compression algorithm using Shannon's entropy.

In the context of data compression using Huffman coding, a "symbol" refers to a discrete unit or element of data that needs to be encoded. These symbols can represent characters, letters, numbers, or any other distinct elements within the data (like strings inside a binary dump of a file). Each symbol has an associated probability of occurrence (frequency), which is linked to its "information content." Information content, as determined by Shannon entropy, represents the amount of uncertainty or surprise associated with a particular symbol. Symbols with higher information content are less predictable and carry more uncertainty, requiring more bits to encode. Conversely, symbols with lower information content are more predictable and can be represented with shorter binary codes. Huffman coding exploits these information content differences to assign shorter codes to high-entropy symbols, resulting in efficient data compression by reducing the overall average code length.

A Huffman tree, also known as a Huffman coding tree, is a binary tree used in data compression to represent variable-length codes for symbols in a data stream. It is constructed based on the frequency or probability of occurrence of each symbol in the data. The tree-building process starts with each symbol as a leaf node and combines pairs of nodes (either leaf nodes or previously combined nodes) into new parent nodes. This process continues until all nodes are merged into a single root node, forming the Huffman tree. The depth of each leaf node in the tree corresponds to the length of its Huffman code, ensuring that more frequent symbols have shorter codes, optimizing compression efficiency. The tree is used for both encoding and decoding data, allowing for efficient compression and decompression while preserving the original information.

Decoding in Huffman coding operates by traversing the Huffman tree, which is constructed based on the probabilities or frequencies of symbols in the encoded data. Starting from the root of the tree, each binary digit read from the encoded stream guides the traversal: a '0' typically leads to a left branch, and a '1' to a right branch. The traversal continues until a leaf node is reached, at which point the corresponding symbol is identified. This process repeats sequentially, allowing the entire encoded message to be decoded symbol by symbol. Since Huffman coding ensures that no code is a prefix of another, the decoding process is unambiguous and efficient, making it possible to recover the original data from the compressed representation.

### A minimal data compression algorithm