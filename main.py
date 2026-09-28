# Import necesary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
# Download stopwords
nltk.download('stopwords')
nltk.download('punkt')
# Example sentence for summarization
text = """Artificial Intelligence is rapidly changing the way people work, learn, and solve problems across different industries. 
In healthcare, AI can help doctors analyze medical images, identify patterns in patient data, and support the development of new treatments. 
In education, intelligent systems can provide personalized learning experiences by adapting lessons and exercises to the needs of individual students. 
Engineers are also using AI to improve the design of buildings, predict equipment failures, optimize construction processes, and analyze large amounts of technical data. 
In transportation, AI is being used to improve traffic management, optimize routes, and develop technologies for autonomous vehicles. 
Businesses are adopting AI to automate repetitive tasks, understand customer behavior, detect fraud, and improve decision-making.
Despite these benefits, the growing use of AI also creates challenges involving privacy, security, bias, employment, and the responsible use of automated systems. 
As AI continues to develop, researchers and organizations must focus on creating systems that are reliable, transparent, and beneficial to society."""
# Function to generate a frequency based summary
def summarize_text(text,num_sentences=2):
    # Tokenize text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    # Filter out stopwords and non-alphabetic words
    stop_words = set(stopwords.words("english"))
    word_frequencies = {}
    for word in words:
        if word.isalpha() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word,0) + 1
    # Score each sentence based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence,0) + word_frequencies[word]
    # Sort sentences by score and select the top 'num_sentences
    summary_sentences = sorted(sentence_scores,key=sentence_scores.get,reverse=True)[:num_sentences]
    summary = " ".join(summary_sentences)
    return summary
# Generate and print the summary
summary = summarize_text(text,num_sentences=2)
print("Original Text:\n",text)
print("Summary:\n ",summary)