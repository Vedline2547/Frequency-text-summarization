# 📝 Frequency-Based Text Summarization using NLTK

A simple Natural Language Processing (NLP) project that automatically generates a summary from a longer piece of text using a **frequency-based extractive summarization technique**.

The program identifies important words based on their frequency, assigns scores to sentences containing those words, and selects the highest-scoring sentences to create the final summary.

## 🚀 Features

* Sentence and word tokenization using NLTK
* Removal of common English stopwords
* Word frequency calculation
* Sentence importance scoring
* Automatic selection of the most important sentences
* Extractive text summarization
* Adjustable summary length

## 🧠 How It Works

The summarization process follows these steps:

```text
Input Text
    ↓
Sentence Tokenization
    ↓
Word Tokenization
    ↓
Remove Stopwords & Punctuation
    ↓
Calculate Word Frequencies
    ↓
Score Sentences
    ↓
Rank Sentences
    ↓
Select Top Sentences
    ↓
Generate Summary
```

### 1. Tokenize the Text

The input text is divided into individual sentences and words using NLTK's tokenization functions.

### 2. Calculate Word Frequencies

Common stopwords such as `the`, `is`, `and`, and `to` are removed. The remaining words are counted based on how frequently they appear in the text.

### 3. Score Sentences

Each sentence receives a score based on the frequency of the important words it contains.

For example:

```python
sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]
```

A sentence containing several frequently occurring words will generally receive a higher score.

### 4. Select Important Sentences

The sentences are sorted according to their scores, and the highest-scoring sentences are selected for the final summary.

```python
summary_sentences = sorted(
    sentence_scores,
    key=sentence_scores.get,
    reverse=True
)[:num_sentences]
```

## 🛠️ Technologies Used

* **Python**
* **NLTK**
* **Natural Language Processing**
* **Text Summarization**

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Vedline2547/Frequency-text-summarization.git
```

Navigate into the project:

```bash
cd frequency-text-summarization
```

Install NLTK:

```bash
pip install nltk
```

Download the required NLTK resources:

```python
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

## ▶️ Usage

Run the Python script:

```bash
python main.py
```

You can control the number of sentences in the summary:

```python
summary = summarize_text(text, num_sentences=3)
```

For example, if the original text contains 8 sentences, setting `num_sentences=3` will return the 3 highest-scoring sentences.

## 📊 Example

### Input

The program can process a paragraph such as:

> Artificial Intelligence is rapidly changing the way people work, learn, and solve problems across different industries. In healthcare, AI can help doctors analyze medical images and support the development of new treatments. In education, intelligent systems can provide personalized learning experiences. Engineers are also using AI to improve designs, predict equipment failures, and optimize construction processes.

### Output

The program identifies sentences containing important and frequently occurring words and selects the highest-scoring sentences as the summary.

## 📁 Project Structure

```text
frequency-text-summarization/
│
├── main.py
├── README.md
└── requirements.txt
```

### `main.py`

Contains the text summarization algorithm.

### `requirements.txt`

Contains the required Python dependencies.

Example:

```text
nltk
```

## 🔍 Type of Summarization

This project uses **extractive summarization**.

Unlike abstractive summarization, which generates new sentences, extractive summarization selects existing sentences from the original text.

```text
Original Text
      ↓
Identify Important Words
      ↓
Score Existing Sentences
      ↓
Select Important Sentences
      ↓
Summary
```

## ⚠️ Limitations

This is a simple frequency-based approach and has some limitations:

* Frequent words are not always the most meaningful words.
* Sentence scores can be affected by the length of sentences.
* The algorithm does not understand the deeper meaning or context of the text.
* The generated summary may not always flow naturally.
* It does not generate new sentences.

## 🔮 Future Improvements

Possible improvements include:

* Sentence normalization
* TF-IDF-based sentence scoring
* TextRank summarization
* Transformer-based summarization
* BERT-based NLP models
* T5 or BART summarization
* A web interface using Flask
* Summary length controls
* Support for multiple languages

## 🎯 Learning Objectives

This project demonstrates fundamental NLP concepts including:

* Text preprocessing
* Tokenization
* Stopword removal
* Frequency analysis
* Dictionary-based word counting
* Sentence scoring
* Extractive summarization

## 👨‍💻 Author

**Vedline Ochieng**

Civil Engineering Student | ML & AI Enthusiast | Python Developer

---

⭐ If you found this project useful, consider giving the repository a star!
