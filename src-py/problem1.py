# Found here:
#   https://www.glassdoor.com/Interview/Recently-I-attended-the-interview-at-Google-and-I-was-asked-You-are-given-a-sorted-list-of-disjoint-intervals-and-an-inter-QTN_345488.htm
# You are given a sorted list of disjoint intervals and an interval,
# e.g. [(1, 5), (10, 15), (20, 25)] and (12, 27). Your task is to
# merge them into a sorted list of disjoint intervals: [(1, 5), (10, 27)]
import operator


def algo1(intervals, new_interval):
    if len(intervals) == 0:
        return [(min(new_interval), max(new_interval))]

    # First of all sort the intervals. The problem is says that we are given a sorted list,
    # but let's consider more general case
    # alternatively, we could just remove 'bad' intervals
    intervals = [(min(v), max(v)) for v in intervals]
    intervals = sorted(intervals, key=operator.itemgetter(0, 1))
    a = min(new_interval)
    b = max(new_interval)

    #
    n = len(intervals)
    k = 0

    # the are two things that should be cleared:
    # 1) current interval - interval from the list we are pointing now: intervals[k]
    # 2) new interval - interval to be added to the list: (a, b)

    while k < n:
        # if the left end of the current interval is greater than the right end of
        # the new interval => add new interval to the list before the current interval
        # and finish
        if b < intervals[k][0]:
            intervals.insert(k, (a, b))
            break

        # if the right end of the new interval is within the current interval =>
        # => set the right end of the new interval equal to the right end of the
        # current interval
        # the left end of the new interval is a min between left ends of current and
        # new intervals
        #
        if intervals[k][0] <= b <= intervals[k][1]:
            a1, b = intervals.pop(k)
            # print intervals, k
            a = min(a, a1)
            intervals.insert(k, (a, b))
            break

        # if the right end of the new interval is greater than the right end of the current
        # interval, then the current interval is either within the new interval, or
        # it the new interval is larger than the current interval
        #
        if intervals[k][1] <= b:
            # if within
            if a < intervals[k][1]:
                a = min(a, intervals[k][0])
                intervals.pop(k)
                n -= 1

                # case when new interval contains all the given intervals
                if n == 0:
                    intervals.append((a, b))
                    break
            else:
                k += 1

                if k == n:
                    intervals.append((a, b))
                    break

    return intervals


def print_res(in_1, in_2, out):
    print('\tInput:  {} -- {}\n\tOutput: {}\n'.format(in_1, in_2, out))


def main_f():
    # case 1
    print('Case 1')
    input_ = {'intervals': [(4, 12), (14, 17), (22.5, 23), (30, 45.2)],
              'new_interval': (0, 1)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 2
    print('Case 2')
    input_ = {'intervals': [(4, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (0, 6)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 3
    print('Case 3')
    input_ = {'intervals': [(4, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (0, 13)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 4
    print('Case 4')
    input_ = {'intervals': [(4, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (0, 15)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 5
    print('Case 5')
    input_ = {'intervals': [(10, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (11, 18)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 6
    print('Case 6')
    input_ = {'intervals': [(12, 10), (7, 2), (14, 17), (22, 23), (30, 45)],
              'new_interval': (1, 50)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 7
    print('Case 7')
    input_ = {'intervals': [],
              'new_interval': (0, 1)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 8
    print('Case 8')
    input_ = {'intervals': [(2, 7), (10, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (18, 20)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 9
    print('Case 9')
    input_ = {'intervals': [(2, 7), (10, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (50, 55)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 10
    print('Case 10')
    input_ = {'intervals': [(2, 7), (10, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (5, 15)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 11
    print('Case 11')
    input_ = {'intervals': [(2, 7), (10, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (5, 50)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 12
    print('Case 12')
    input_ = {'intervals': [(2, 7), (10, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (5, 40)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))

    # case 13
    print('Case 13')
    input_ = {'intervals': [(2, 7), (10, 12), (14, 17), (22, 23), (30, 45)],
              'new_interval': (0, 40)
              }
    print_res(input_['intervals'], input_['new_interval'], algo1(**input_))


if __name__ == '__main__':
    main_f()
