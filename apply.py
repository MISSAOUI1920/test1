from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import streamlit as st

# Sample text for summarization
text = """
Le web scraping, parfois appelé harvesting ou en français moissonnage1, est une technique de « récupération et organisation automatisées des données Web » ; c'est la principale forme de data mining et d'extraction des données de sites web, via un script ou d'un programme. Il vise à capter des données, pour les transformer et/ou les réutiliser dans un autre contexte comme l'enrichissement de bases de données, le référencement2 ou l'exploration de données, ou l'apprentissage profond pour une intelligence artificielle. L'objectif est souvent commercial, mais parfois scientifique ou politique.
"""

# Parsing the text
parser = PlaintextParser.from_string(text, Tokenizer("french"))

# Summarizing the text
summarizer = LsaSummarizer()
summary = summarizer(parser.document, 4)  # Adjust the number of sentences

# Converting the summary to a displayable format
summary_sentences = [str(sentence) for sentence in summary]

# Displaying the summary in Streamlit
st.write("Summary:")
st.write("\n".join(summary_sentences))
