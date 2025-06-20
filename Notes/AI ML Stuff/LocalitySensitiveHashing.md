# Embedding Indexing

## Summary

[Embedding vectors][7] are persisted values that represent a point in multi-dimensional 
space. To compare to given points multiple calculates must be computed between each 
point to find the nearest neighbors. Embeddings may contain hundreds of values in a 
given vector and with hundreds of thousands of points this can easily cause 
millions if not billions of calculations.  

To improve performance you can instead perform an [approximate nearest neighbor 
search (ANNS)][5].  One technique is [Locality-sensitive hashing (LSH)][1]. LSH is
used to precompute a hash values with the intention for collisions that will allow 
similar values to have nearly identical hashes.  Then using [Hamming Distance][5]
the search may be used to only compare vectors that have a similar hash.  This
reduces from having to compare every embedding to a much smaller subset dramatically
reducing the number of required calculations to find similar values.

## Hashing Technique

When using [cosine Similarity][2] calculate your LSH value by normalizing your vector 
with an ordered set of [hyperplanes][6]. To normalize the embedding calculate the 
[dot product][3] of your embedding against each of the hyperplane.  If the resulting 
value from the calculate is great than zero (0) then the bit position in the hash 
should be set to 1.  The sum of these normal values may then per persisted as the 
LSH value.

### Calculate Hash Pseudocode

```
hyperplanes = float[16][] 

calculateLsh(float[] searchVector)
    lshValue = 0

    foreach hyperplane,index in hyperplanes
        normal = dotproduct(searchVector, hyperplane)
        if (normal > 0)
            lshValue += power(2, index)

    return lshValue
```

**Notes**

- hyperplanes must be of the same length as the embedding vectors 
- each hyperplane element should be a value of uniform distribution for a given
  elements in the embedding vector (typically 0.0 to 1.0)
- the number of hyperplanes should be equal to the desired bit length of the hash
- the same hyperplanes must be used in the same order to calculate related hashes

## Search Technique

Once you have LSH values for each of your embeddings you can perform [approximate 
nearest neighbor searches (ANNS)][5].  To do this you calculate the embedding for 
your search term, then calculate the hash for this embedding, expand your hash by
a given [Hamming distance][4], collect all embeddings that match the expanded set
of hashes, then calculate the distance to the subset of embeddings.  Once you have 
these distance values you may filter and sort the similarity based on your needs.

### Search Pseudocode

```
haystack = (float[] embedding,int lsh)[]

matchedEmbeddings(float[] needle, int maxHammingDistance = 4)

    needleLsh = calculateLsh(needle)
    int[] needleLshs = generateHammingValues(needle, maxHammingDistance)

    matches =   from item in haystack
                join lsh in needleLshs on item.lsh equals lsh
                select item.embedding

    return matches
```

**Notes**

- embedding target (needle) must match length of searched (haystack) embeddings


  [1]: https://en.wikipedia.org/wiki/Locality-sensitive_hashing
  [2]: https://en.wikipedia.org/wiki/Cosine_similarity
  [3]: https://en.wikipedia.org/wiki/Dot_product
  [4]: https://en.wikipedia.org/wiki/Hamming_distance
  [5]: https://en.wikipedia.org/wiki/Nearest_neighbor_search
  [6]: https://en.wikipedia.org/wiki/Hyperplane
  [7]: https://en.wikipedia.org/wiki/Word_embedding