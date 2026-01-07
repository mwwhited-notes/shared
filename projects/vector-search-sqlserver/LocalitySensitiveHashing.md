# Embedding Indexing

## Summary

[Embedding vectors][7] are persistent values that represent a point in multi-dimensional
space. Comparing embeddings requires many calculations to find the nearest neighbors.
Since each embedding may contain hundreds of values and there may be thousands of embeddings
to compare, the total number of calculations may easily grow to millions or billions.

To improve performance you may instead perform an [approximate nearest neighbor search (ANNS)][5].
One technique is [Locality-sensitive hashing (LSH)][1]. LSH uses precomputed hashes to reduce
the number of calculations that may be performed allowing for a dramatic reduction in processing.
This allows for faster response as well as reduced demand on hardware.  

Additional techniques such as expanding the hash using [Hamming Distance][5] may increase the
search space while still reducing the possible number of comparisons.

## Hashing Technique

When using [cosine similarity][2], calculate your LSH value by projecting your vector
onto an ordered set of [hyperplanes][6]. Calculate a normal vector by using the [dot product][3]
of the embedding to each hyperplane. If the resulting value is greater than zero then the bit
position in the hash should be set to 1. The resulting value is a binary representation
of these normal values.

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

Once you have LSH values for all of your embeddings, you can perform [approximate
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