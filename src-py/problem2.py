# Here is going to be the collection of different algorithms on integer number partition.
#
#
#


def partition_generator1(n, max_val):
    """
    Here is the algorithm that generates all possible partitions of a given number n
    with restriction:
         - partition doesn't contains numbers larger than max_val

    Advantage of this algorithm is that it doesn't involve a recursion.
    """

    div, rem = divmod(n, max_val)
    partition = [max_val] * div
    if rem:
        partition.append(rem)

    # if len(partition) == comb_length:
    yield partition

    target_ind = -1     # pointer to element that must be partitioned
    val1 = 0

    while len(partition) < n:
        # if ends with 1, find first non 1 element from the right
        if partition[-1] == 1:
            for k in range(len(partition)):
                if partition[-1-k] != 1:
                    val1 = sum(partition[-1-k:])                            # [5 1 1 1 1] -> 9
                    val2 = max(partition[-1-k:]) - min(partition[-1-k:])    # [5 1 1 1 1] -> 4
                    target_ind = -1-k                                       #
                    break
        else:
            val1 = partition[-1]        # [5 3] -> 3
            val2 = partition[-1] - 1    # [5 3] -> 2
            target_ind = -1             # pointer

        p, q = divmod(val1, val2)
        sub_comb = [val2]*p         # new tail

        if q > 0:       # add reminder if it is non-zero
            sub_comb.append(q)

        # remove old tail from partition
        for gg in range(target_ind, 0):
            partition.pop(-1)

        # add new tail to partition
        partition.extend(sub_comb)

        # return only combinations/partitions of required length
        # if len(partition) == comb_length:
        yield partition


def test_partition_generator1():
    for comb in partition_generator1(10, 10):
        print(comb)


if __name__ == '__main__':
    test_partition_generator1()
