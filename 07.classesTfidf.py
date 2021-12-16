import math
class CountVectorizer:
    def __init__(self):
        self.vocabulary = []
        self.matrix = []
     
    
    def get_feature_names(self):
        return self.vocabulary

    
    def fit_transform(self, document):
        tmp = set()
        for elem in document:
            tmp.update(elem.lower().split())
        self.vocabulary = list(tmp)
        for elem in document:
            phrase = elem.lower().split()
            total_count=[]
            for word_vocab in self.vocabulary:
                count = 0
                for word_phrase in phrase:
                    if word_vocab == word_phrase:
                        count += 1
                total_count.append(count)
            self.matrix.append(total_count)

        return self.matrix


class TfidfTransformer():
    def __init__(self):
        self.tf_matrix = []
        self.idf_matrix = []
        self.tfidf_matrix = []

    def tf_transform(self, count_matrix):
        for count_word in count_matrix:
            self.tf_matrix.append([round(i/sum(count_word), 3) for i in count_word])
        return self.tf_matrix
    

    def idf_transform(self, count_matrix):
        self.idf_matrix = [0 for _ in range(len(count_matrix[0]))]
        for count_word in count_matrix:
            for iword, word in enumerate(count_word):
                if word != 0:
                    self.idf_matrix[iword] += 1
        self.idf_matrix = [round(math.log((len(count_matrix)+1)/(i+1)) + 1, 3) for i in self.idf_matrix]
        return self.idf_matrix


    def fit_transform(self, count_matrix): 
        self.tf_transform(count_matrix)
        self.idf_transform(count_matrix)
        for ielem, elem in enumerate(self.tf_matrix):
            tmp = []
            for i_elem, _elem in enumerate(self.idf_matrix):
                tmp.append(round(_elem*elem[i_elem],3))
            self.tfidf_matrix.append(tmp)
        return self.tfidf_matrix
    
   
class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tfidf_transformer = TfidfTransformer()
        self.tfidf_matrix = []
        self.matrix = []

    def fit_transform(self, document):
        self.matrix = super().fit_transform(document)
        self.tfidf_matrix = self.tfidf_transformer.fit_transform(self.matrix)
        return self.tfidf_matrix

