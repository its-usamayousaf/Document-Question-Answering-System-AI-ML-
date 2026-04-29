from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DocumentQA:
    def __init__(self, text):
        # Split text into chunks (paragraphs)
        self.sentences = text.split("\n")

        # Remove empty lines
        self.sentences = [s.strip() for s in self.sentences if len(s.strip()) > 0]

        # Vectorize
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.X = self.vectorizer.fit_transform(self.sentences)

    def get_answer(self, query):
        query_vec = self.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.X)

        max_score = similarity.max()
        index = similarity.argmax()

        if max_score < 0.2:
            return "Sorry, no relevant information found."

        return self.sentences[index]