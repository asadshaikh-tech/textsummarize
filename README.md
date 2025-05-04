# textsummarize
#  Text Summarizer (Desktop App with spaCy)

This project is a **Text Summarizer desktop application** built using `spaCy` for NLP and `tkinter` for GUI. It extracts the most important sentences from a paragraph and displays the summary.

##  Features
- Input large text via GUI
- Summarize to 3 most relevant sentences
- Extractive summarization using word frequency

## 🛠 Tech Stack
- Python
- spaCy
  

##  Getting Started

### 1. Clone the repository

git clone https://github.com/yourusername/textsummarize.git

cd Desktop

cd text_summarizer

2. Create and activate virtual environment (optional)

python -m venv .venv

.venv\Scripts\activate  # for Windows

3. Install Dependencies
   
pip install spacy

python -m spacy download en_core_web_sm

4. Run the Summarizer
   
python summarizer_gui.py
