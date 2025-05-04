import spacy
from collections import Counter
import tkinter as tk
from tkinter import scrolledtext

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def summarize_text(text, num_sentences=3):
    doc = nlp(text)
    words = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    word_freq = Counter(words)
    sentence_scores = {}

    for sent in doc.sents:
        for token in sent:
            if token.text.lower() in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[token.text.lower()]
    
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join([sent.text for sent in summary_sentences])
    return summary

def run_summarizer():
    input_text = input_box.get("1.0", tk.END).strip()
    if input_text:
        summary = summarize_text(input_text, num_sentences=3)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, summary)

# GUI setup
window = tk.Tk()
window.title("Text Summarizer")
window.geometry("700x500")

# Input label and box
tk.Label(window, text="Enter your paragraph:", font=("Arial", 14)).pack()
input_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=10, font=("Arial", 12))
input_box.pack(padx=10, pady=10)

# Summarize button
tk.Button(window, text="Summarize", command=run_summarizer, font=("Arial", 12), bg="lightblue").pack(pady=10)

# Output label and box
tk.Label(window, text="Summary:", font=("Arial", 14)).pack()
output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=6, font=("Arial", 12))
output_box.pack(padx=10, pady=10)

# Run the app
window.mainloop()
