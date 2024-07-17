from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import streamlit as st
import nltk

nltk.download('punkt')
# Sample text for summarization
text = """
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites.[1] Web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. It is a form of copying in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis."""

# Parsing the text
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Summarizing the text
summarizer = LsaSummarizer()
summary = summarizer(parser.document, 4)  # Adjust the number of sentences

# Converting the summary to a displayable format
summary_sentences = [str(sentence) for sentence in summary]

# Displaying the summary in Streamlit
st.write("Summary:")
st.write("\n".join(summary_sentences))
