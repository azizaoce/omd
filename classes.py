class CountVectorizer:
    def __init__(self, array):
        self.array = array
    def get_feature_names(self):
        a=set()
        for elem in self.array:
            a.update(elem.lower().split())
        return list(a)
    def fit_transform(self, mass):
        a=set()
        for elem in self.array:
            a.update(elem.lower().split())
        a=list(a)
        matrix=[]
        for i in mass:
            phrase = i.lower().split()
            b=[]
            for el in a:
                q=0
                for j in phrase:
                    if el == j:
                        q = q+1
                b.append(q)
            matrix.append(b)
                #print(b)
        return(matrix)
                                          
corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer(corpus)
print(vectorizer.get_feature_names())
print(vectorizer.fit_transform(corpus))
