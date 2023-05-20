
def tf_idf(sentences, words):
    """This function designed to calculate unigram words score for sentences,
    Input arguments are list of sentences in a document and a list contains
     unique words form whole of the document sentences."""
    tf_idf_dict = {}
    for word in words:
        tf_idf_dict[word] = 0
    for sentence in sentences:
        for word in words:
            if word in sentence:
                tf_idf_dict[word] += 1
    for word in words:
        tf_idf_dict[word] = tf_idf_dict[word] / len(sentences)
    return tf_idf_dict