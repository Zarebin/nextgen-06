from __future__ import division
import pandas as pd
import ntpath
import random
import sys
import time
import binascii


csv_path = "C:\\Users\\Behnam\\data_all.csv"


def read_csv_data(csv_path):
    df = pd.read_csv(csv_path)
    df_txt = df[df.extension.isin(['txt'])]
    df_prepared_1 = df_txt.drop_duplicates(subset='md5', keep="last")
    df_prepared_2 = df_prepared_1.drop_duplicates(subset='name', keep="last")
    return df_prepared_2


fs_df = read_csv_data(csv_path)


def get_text(path):
    file = open(path, "r", encoding="utf-8")
    file_text = file.read()
    return file_text


numHashes = 10;

numDocs = len(fs_df['name'])


print("Shingling articles...")

curShingleID = 0

docsAsShingleSets = {};

docNames = []

t0 = time.time()

totalShingles = 0
try:
    dataFile = fs_df['path']

    for i in range(0, numDocs):

        f = open(str(fs_df['path'][i]), "r", encoding="utf-8")

        words = f.read().split(" ")

        docID = str(fs_df['name'][i])

        docNames.append(docID)

        shinglesInDoc = set()

        for index in range(0, len(words) - 2):
            shingle = words[index] + " " + words[index + 1] + " " + words[index + 2]

            crc = binascii.crc32(str.encode(shingle)) & 0xffffffff

            shinglesInDoc.add(crc)

        docsAsShingleSets[docID] = shinglesInDoc

        totalShingles = totalShingles + (len(words) - 2)

    f.close()
except Exception as e:
    print(e)
print('\nShingling ' + str(numDocs) + ' docs took %.2f sec.' % (time.time() - t0))

print('\nAverage shingles per doc: %.2f' % (totalShingles / numDocs))

numElems = int(numDocs * (numDocs - 1) / 2)

JSim = [0 for x in range(numElems)]
estJSim = [0 for x in range(numElems)]


def getTriangleIndex(i, j):
    if i == j:
        sys.stderr.write("Can't access triangle matrix with i == j")
        sys.exit(1)
    if j < i:
        temp = i
        i = j
        j = temp

    k = int(i * (numDocs - (i + 1) / 2.0) + j - i) - 1

    return k


if numDocs <= 2500:
    print("\nCalculating Jaccard Similarities...")

    t0 = time.time()

    for i in range(0, numDocs):

        if (i % 100) == 0:
            print(str(i), "/", str(numDocs))

        s1 = docsAsShingleSets[docNames[i]]

        for j in range(i + 1, numDocs):
            s2 = docsAsShingleSets[docNames[j]]


            JSim[getTriangleIndex(i, j)] = (len(s1.intersection(s2)) / len(s1.union(s2)))

    elapsed = (time.time() - t0)

    print("\nCalculating all Jaccard Similarities took %.2fsec" % elapsed)

del JSim

t0 = time.time()

print('\nGenerating random hash functions...')

maxShingleID = 2 ** 32 - 1

nextPrime = 4294967311

def pickRandomCoeffs(k):
    randList = []

    while k > 0:
        randIndex = random.randint(0, maxShingleID)

        while randIndex in randList:
            randIndex = random.randint(0, maxShingleID)

        randList.append(randIndex)
        k = k - 1

    return randList


coeffA = pickRandomCoeffs(numHashes)
coeffB = pickRandomCoeffs(numHashes)

print('\nGenerating MinHash signatures for all documents...')

signatures = []

for docID in docNames:

    shingleIDSet = docsAsShingleSets[docID]

    signature = []

    for i in range(0, numHashes):

        minHashCode = nextPrime + 1

        for shingleID in shingleIDSet:
            hashCode = (coeffA[i] * shingleID + coeffB[i]) % nextPrime

            if hashCode < minHashCode:
                minHashCode = hashCode

        signature.append(minHashCode)

    signatures.append(signature)
    m = open("./min_hash_res.txt", "a", encoding="utf-8")
    m.write(docID, signatures)
    m.close()

elapsed = (time.time() - t0)


print("\nGenerating MinHash signatures took %.2fsec" % elapsed)


print('\nComparing all signatures...')

t0 = time.time()

for i in range(0, numDocs):
    signature1 = signatures[i]

    for j in range(i + 1, numDocs):

        signature2 = signatures[j]

        count = 0
        for k in range(0, numHashes):
            count = count + (signature1[k] == signature2[k])

        estJSim[getTriangleIndex(i, j)] = (count / numHashes)

elapsed = (time.time() - t0)

print("\nComparing MinHash signatures took %.2fsec" % elapsed)

tp = 0
fp = 0

threshold = 0.2
print("\nList of Document Pairs with J(d1,d2) more than", threshold)
print("Values shown are the estimated Jaccard similarity and the actual")
print("Jaccard similarity.\n")

for i in range(0, numDocs):
    for j in range(i + 1, numDocs):
        estJ = estJSim[getTriangleIndex(i, j)]

        if estJ > threshold:

            s1 = docsAsShingleSets[docNames[i]]
            s2 = docsAsShingleSets[docNames[j]]
            J = (len(s1.intersection(s2)) / len(s1.union(s2)))

            print("  %5s --> %5s   %.2f     %.2f" % (docNames[i], docNames[j], estJ, J))
