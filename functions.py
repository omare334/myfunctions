# see if a is within 10 percent of b
from turtle import pd
import pandas as pd

def within_10_percent(a,b):
 if abs( (a - b) / float(a) ) <= 0.10:
    print('True')
 else:
    print('False')


"""Return a grammatically correct human readable string (with an Oxford comma)."""
 # Ref: https://stackoverflow.com/a/53981846/
from typing import Any, List

def readable_list(seq: List[Any]) -> str:
    """Return a grammatically correct human readable string (with an Oxford comma)."""
    # Ref: https://stackoverflow.com/a/53981846/
    seq = [str(s) for s in seq]
    if len(seq) < 3:
        return ' and '.join(seq)
    return ', '.join(seq[:-1]) + ', and ' + seq[-1]



def readable_list2(_s):
  if len(_s) < 3:
    return ' and '.join(map(str, _s))
  *a, b = _s
  return f"{', '.join(map(str, a))}, and {b}"




def collatz_sequence(a, numOfDiv):
    if (a % 2) == 0:
        while a > 0:
            a = a // 2
            numOfDiv += 1
    else:
        while a > 0:
            a = (a * 3) + 1
            numOfDiv += 1

# filter through someone data best on thier charactristics
start = time.time()
df_to_match = pd.DataFrame(data=[['AfricanAmerican', 'Male', '[70-80)']],
                           columns=['race', 'gender', 'age'])
results = df.merge(df_to_match, on=['race', 'gender', 'age'])
count = len(results)
print('{0} records were found with matching features.'.format(count))
print('It took {0:.2f} seconds.'.format(time.time() - start))
#also allows you to time this stuff

#upload picture of dmg with change in colour map
base = r"C:\Users\omare\OneDrive\Documents\HDA\Clinical data managment\Week 6 privacy\CDM_Week6\practical_06"
pass_dicom = "image.dcm"
filename = pydicom.data.data_manager.get_files(base, pass_dicom)[0]
ds = pydicom.dcmread(filename)

plt.imshow(ds.pixel_array, cmap=plt.cm.bone)  # set the color map to bone
plt.show()
#meta data of pic
print(ds)
#odd numbers
import sys
def collatz (a):
    if a % 2 == 0:  # Even number
        result = a // 2
    elif a % 2 == 1:  # Odd number
        result = 3 * a + 1

    while result == 1:  # It would not print the number 1 without this loop
        print(result)
        sys.exit()  # So 1 is not printed forever.

    while result != 1:  # Goes through this loop until the condition in the previous one is True.
        print(result)
        number = result  # This makes it so collatz() is called with the number it has previously evaluated down to.
        return collatz(number)
    # see if a is within 10 percent of b
    from turtle import pd
    import pandas as pd

    def within_10_percent(a, b):
        if abs((a - b) / float(a)) <= 0.10:
            print('True')
        else:
            print('False')

    """Return a grammatically correct human readable string (with an Oxford comma)."""
    # Ref: https://stackoverflow.com/a/53981846/
    from typing import Any, List

    def readable_list(seq: List[Any]) -> str:
        """Return a grammatically correct human readable string (with an Oxford comma)."""
        # Ref: https://stackoverflow.com/a/53981846/
        seq = [str(s) for s in seq]
        if len(seq) < 3:
            return ' and '.join(seq)
        return ', '.join(seq[:-1]) + ', and ' + seq[-1]

    def readable_list2(_s):
        if len(_s) < 3:
            return ' and '.join(map(str, _s))
        *a, b = _s
        return f"{', '.join(map(str, a))}, and {b}"

    def collatz_sequence(a, numOfDiv):
        if (a % 2) == 0:
            while a > 0:
                a = a // 2
                numOfDiv += 1
        else:
            while a > 0:
                a = (a * 3) + 1
                numOfDiv += 1

    # filter through someone data best on thier charactristics
    start = time.time()
    df_to_match = pd.DataFrame(data=[['AfricanAmerican', 'Male', '[70-80)']],
                               columns=['race', 'gender', 'age'])
    results = df.merge(df_to_match, on=['race', 'gender', 'age'])
    count = len(results)
    print('{0} records were found with matching features.'.format(count))
    print('It took {0:.2f} seconds.'.format(time.time() - start))
    # also allows you to time this stuff

    # upload picture of dmg with change in colour map
    base = r"C:\Users\omare\OneDrive\Documents\HDA\Clinical data managment\Week 6 privacy\CDM_Week6\practical_06"
    pass_dicom = "image.dcm"
    filename = pydicom.data.data_manager.get_files(base, pass_dicom)[0]
    ds = pydicom.dcmread(filename)

    plt.imshow(ds.pixel_array, cmap=plt.cm.bone)  # set the color map to bone
    plt.show()
    # meta data of pic
    print(ds)
    # odd numbers
    import sys
    def collatz(a):
        if a % 2 == 0:  # Even number
            result = a // 2
        elif a % 2 == 1:  # Odd number
            result = 3 * a + 1

        while result == 1:  # It would not print the number 1 without this loop
            print(result)
            sys.exit()  # So 1 is not printed forever.

        while result != 1:  # Goes through this loop until the condition in the previous one is True.
            print(result)
            number = result  # This makes it so collatz() is called with the number it has previously evaluated down to.
            return collatz(number)

    # smallest integer outside of array 100
    def solution(A):
        B = set(A)
        C = max(A) + 2
        for N in range(1, C):
            if N not in B:
                return N
        return 1

    # longest binary gap in positive integer
    def solution(N):
        bint = bin(N)[2:]
        L_arr = 0
        C_arr = 0
        for digit in bint:
            if digit == '0':
                C_arr += 1
            else:
                L_arr = max(L_arr, C_arr)
                C_arr = 0
        return L_arr

    # rotate and array to the right K times
    def solution(A, K):
        if len(A) == 0:
            return A
        K = K % len(A)
        return A[-K:] + A[:-K]

    # odd occurences in array
    def solution(A):
        for i in A:
            if A.count(i) % 2 != 0:
                return i

    # unpaired odd number in array
    def solution(A):
        A = sorted(A)
        return abs(sum(A[::2]) - sum(A[1::2]))

    # frog jump question
    def solution(X, Y, D):
        distance = Y - X
        if distance % D == 0:
            return distance // D
        else:
            return distance // D + 1

    # find missing element in permutation
    def solution(A):
        N = len(A)
        return (N + 1) * (N + 2) // 2 - sum(A)

    # tempperm
    def solution(numbers):
        """Solution method implementation."""
        # compute the sum of all numbers beforehand
        total_sum = sum(numbers)
        # initialize left sum variable to 0
        left_sum = 0
        # initialize the minimum difference
        min_dif = 99999001
        # initialize the current difference
        crt_dif = 0
        # iterate through the list of numbers
        # the iteration's done from the first to the second-to-last
        for item in numbers[:-1]:
            # increment the left sum by the element
            left_sum += item
            # get the current difference between left and right sum
            # notice the right sum is total_sum - left_sum
            # so left_sum - right_sum = total_sum - (2 * left_sum)
            crt_dif = abs(total_sum - (2 * left_sum))
            # update the minimum difference
            min_dif = min(min_dif, crt_dif)
        # return the minimum difference
        return min_dif

    # earliest time frog can cross river
    def solution(X, A):
        # write your code in Python 3.6
        N = len(A)
        if N < X:
            return -1
        else:
            B = [0] * X
            for i in range(N):
                if B[A[i] - 1] == 0:
                    B[A[i] - 1] = 1
                    X -= 1
                    if X == 0:
                        return i
            return -1

    # is array A in permutation
    def solution(A):
        A.sort()
        for i in range(len(A)):
            if A[i] != i + 1:
                return 0
        return 1

    # value of counter after all operations
    def solution(N, A):
        counter = [0] * N
        max_counter = 0
        for i in A:
            if i <= N:
                counter[i - 1] += 1
                max_counter = max(max_counter, counter[i - 1])
            else:
                counter = [max_counter] * N
        return counter

    mzx
    counter

    def solution(no_of_counters, operations):
        # initialize the list of counters
        counters = [0] * no_of_counters
        # initialize the max value
        max_val = 0
        # initialize the carry variable
        carry = 0
        # start the loop
        for item in operations:
            # operation - increment(x)
            if 1 <= item <= no_of_counters:
                # apply the carry, if necessary
                counters[item - 1] = max(counters[item - 1], carry)
                # apply the increment(x) operation
                counters[item - 1] += 1
                # update the max value
                max_val = max(max_val, counters[item - 1])
            # operation - max counter
            elif item == no_of_counters + 1:
                # set the carry to hold the max value
                carry = max_val
        # max out-of-date counters
        counters = [max(i, carry) for i in counters]
        # return the result
        return counters

    # number of cars passing on the road
    def solution(A):
        _l = len(A)
        base = 0
        res = 0
        for i in range(_l):
            # increment local base whenever meet cars head to east
            if A[i] == 0:
                base += 1
            # increment global accumulation whenever meet cars head to west
            else:
                res += base
            if res > 1000000000: return -1
        return res

    # retunr the number of integers divisible by k in range a to b
    def solution(A, B, K):
        # write your code in Python 3.6
        if A % K == 0:
            return (B - A) // K + 1
        else:
            return (B - (A - A % K)) // K

    # dna sequence
    def solution(seq, seq_beg, seq_end):
        """Solution method implementation."""
        # initialization of variables
        factors = {
            "A": 1,
            "C": 2,
            "G": 3,
            "T": 4
        }
        result = []
        count_states = [[0, 0, 0, 0]]
        # build counter states timeline
        for i, nucleotide in enumerate(seq):
            count_states.append(list(count_states[i]))
            count_states[i + 1][factors[nucleotide] - 1] += 1
        # main query processing loop
        for i, _ in enumerate(seq_end):

            # query substring is of length 1
            if seq_beg[i] == seq_end[i]:
                result.append(factors[seq[seq_beg[i]]])

            else:

                # get counter states before and after
                state_after_end = count_states[seq_end[i] + 1]
                state_before_beg = count_states[seq_beg[i]]
                # find minimum impact nucleotide in query substring
                for j in range(4):
                    if state_after_end[j] > state_before_beg[j]:
                        result.append(j + 1)
                        break

        return result

    # minimum average of slice
    def solution(A):
        # write your code in Python 3.6
        min_avg = (A[0] + A[1]) / 2
        min_idx = 0
        for i in range(2, len(A)):
            avg = (A[i] + A[i - 1]) / 2
            if avg < min_avg:
                min_avg = avg
                min_idx = i - 1
            avg = (A[i] + A[i - 1] + A[i - 2]) / 3
            if avg < min_avg:
                min_avg = avg
                min_idx = i - 2
        return min_idx





