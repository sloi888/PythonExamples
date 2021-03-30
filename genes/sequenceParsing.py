import os
def countRepeatingSequences(filepath, subSequenceLength, threshold):
    # open the designated file in read mode
    f = open(os.path.abspath(filepath), "r")
    # read the file and save its contents to a string
    sequence = f.read()
    # get rid of newline char
    sequence = sequence.replace("\n", "")
    # print(sequence)
    # length of the whole gene sequence
    length = len(sequence)
    # start from 0
    seqStart = 0
    # create an empty dictionary that we will add entries to later
    seqDict = {}
    # the last sequence will be from [length - subSequenceLength - 1:end]
    # so we will continue to crawl the sequence until then
    while seqStart < length - subSequenceLength - 1:
        # set the end to be the start + desired length
        seqEnd = seqStart + subSequenceLength
        # grab the substring from the big sequence
        subSeq = sequence[seqStart:seqEnd]
        # if the subsequence we grabbed isn't in the dictionary already
        # then add it, with its location, and set its occurrence to 1
        if subSeq not in seqDict:
            seqDict[subSeq] = [[seqStart],1]
        else:
        # if it already exists in the dictionary, add this occurrence to the list of occurrence locations
        # and add 1 to the number of occurrences
            seqDict[subSeq][0].append(seqStart)
            seqDict[subSeq][1] += 1
        # advance where we are in the sequence by 1
        seqStart += 1
    # create another empty dictionary
    filteredDict = {}
    # for every key value pair in the original dictionary
    for key in seqDict:
        # if the occurrence value surpasses our given threshold
        if seqDict[key][1] >= threshold:
            # copy it to the filtered dictionary
            filteredDict[key] = seqDict[key]
    # return the filtered dictionary
    return filteredDict

# simple saving of user input to variables
path = input("Where is the sequence text located?: ")
seqLength = int(input("How long of a subsequence are you looking for?: "))
occurrences = int(input("How many occurrences minimum are you looking for?: "))
# call the function with the given user input
print(countRepeatingSequences(path, seqLength, occurrences))
