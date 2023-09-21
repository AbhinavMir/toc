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

A minimal Pythonic implementation can be found [here](https://raw.githubusercontent.com/AbhinavMir/toc/main/code/compression/compression.py) and a C implementation can be found [here](https://raw.githubusercontent.com/AbhinavMir/toc/main/code/compression/compression.c). However, for whatever reason, my C compression is larger than original data - which is not ... compressed, but the Python one works perfectly.

## Lower Entropic Bounds

A lower entropy bound, in the context of information theory and probability theory, is a mathematical constraint that establishes the minimum amount of entropy or uncertainty in a given probability distribution or information source. Entropy, often represented by the letter "H," measures the randomness or unpredictability of a set of outcomes. It quantifies the average amount of information needed to describe or represent those outcomes.

The concept of a lower entropy bound is significant because it sets a fundamental limit on how much uncertainty or randomness can be reduced or compressed in a particular context. In other words, it defines the minimum level of uncertainty that must be preserved or transmitted when encoding information or processing data. This limit is typically expressed as a lower bound on the entropy value and is useful in various applications, including:

1. Data Compression: In data compression algorithms, a lower entropy bound helps determine the minimum size of compressed data. It ensures that no compression method can achieve a smaller compressed size without violating the lower bound. Shannon's entropy coding, such as Huffman coding, takes advantage of this concept to design efficient compression schemes.

2. Communication Theory: Lower entropy bounds are essential in communication theory to assess the efficiency of data transmission and encoding. They indicate the minimum number of bits required to represent messages accurately, considering the inherent uncertainty in the data.

3. Information Security: In cryptography and information security, understanding lower entropy bounds is crucial for assessing the strength of encryption methods. It ensures that encrypted data remains sufficiently random and secure. (More about this on my other blog, [Ciphertxt)](https://www.ciphertxt.xyz/introduction/pseudrandom-generators))

To establish a lower entropy bound for a specific probability distribution, mathematical techniques, inequalities, and properties of the distribution are used. The bound serves as a theoretical benchmark that guides the design of algorithms, protocols, and systems that process or transmit information.

For example, in the context of a fair coin toss (a binary probability distribution), the lower entropy bound would be 1 bit because, in the worst-case scenario, you need one bit to represent each outcome (heads or tails). Any encoding scheme that tries to represent the outcomes in fewer than 1 bit would violate this lower bound and result in information loss.

Overall, a lower entropy bound provides a fundamental constraint on the processing, representation, and communication of information, ensuring that certain levels of uncertainty are preserved or accounted for in various applications.

## Proving the lower entropy bound

1. **Random Permutation:** We have a set of [$ n $] elements, and we choose a random permutation of these elements with a uniform distribution. The entropy of this random permutation is given by [$ H[ X ] = \log_2(n!) $], which measures the uncertainty or information content associated with the possible orderings.

2. **Comparisons:** We perform a series of pairwise comparisons [$ (Y_1, Y_2, \ldots, Y_t $]) to determine the order of these elements. These comparisons are dependent on the actual permutation, which we denoted as [$ X $].

3. **Reconstruction:** When we have enough comparisons [$ (t $] is sufficiently large), we can reconstruct the original permutation [$ X $] from these comparisons. In other words, [$ X $] is a function of [$ Y_1, Y_2, \ldots, Y_t $].

Now, the crucial insight here is that the entropy (uncertainty) associated with the reconstructed permutation [$ X $] cannot be greater than the entropy of the comparisons themselves. This intuitively makes sense because the information content required to describe the order of elements should not exceed the information content of the comparisons.

To formalize this, we use Stirling's formula \[$ log_2(n!) \approx n \log_2(n) $]. Therefore, we can conclude that \[$ \Omega(n \log_2(n)) $] comparisons are required to reconstruct the random permutation [$ X $] accurately.

In simpler terms, this lower bound tells us that as the number of elements [$ (n $]) grows, the number of necessary comparisons to reconstruct a random permutation increases at least as fast as [$ n \log_2(n) $]. This is a fundamental result with implications in various areas, including sorting algorithms and information theory.