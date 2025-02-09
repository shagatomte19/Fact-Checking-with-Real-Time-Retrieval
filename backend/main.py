from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import RobertaForSequenceClassification, RobertaTokenizer, BartForConditionalGeneration, BartTokenizer
from newsapi import NewsApiClient
import wikipediaapi
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

app = FastAPI()

# Load fine-tuned RoBERTa model
model_path = "./model/fine_tuned_roberta"
model = RobertaForSequenceClassification.from_pretrained(model_path)
tokenizer = RobertaTokenizer.from_pretrained(model_path)

# Load summarization model (BART)
summarizer = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
summarizer_tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

# Load FAISS for past fact checks
vector_index = GPTVectorStoreIndex.load_from_disk("./faiss_index")

# Initialize APIs
newsapi = NewsApiClient(api_key="d25983011bf04d0d8173ffefa50d763c")
wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent="FactChecker/1.0")

# Data model for input
class Claim(BaseModel):
    text: str

@app.post("/fact-check")
def fact_check(claim: Claim):
    query = claim.text
    
    # Fetch from Google Custom Search, Wikipedia, NewsAPI
    evidence = fetch_evidence(query)
    summarized_evidence = summarize_evidence(evidence)
    
    # Classify claim
    inputs = tokenizer(query + " " + summarized_evidence, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=-1).item()
    
    # Store fact check in FAISS
    vector_index.insert(query, summarized_evidence)
    
    return {"claim": query, "result": prediction, "evidence": summarized_evidence}

def fetch_evidence(query):
    """Retrieve relevant evidence from different sources."""
    news = newsapi.get_everything(q=query, language="en", page_size=3)
    wiki_page = wiki_wiki.page(query)
    
    evidence = [article["description"] for article in news["articles"] if article["description"]]
    if wiki_page.exists():
        evidence.append(wiki_page.summary)
    
    return " ".join(evidence)

def summarize_evidence(evidence_text):
    """Summarizes retrieved evidence."""
    inputs = summarizer_tokenizer(evidence_text, return_tensors="pt", truncation=True, padding=True, max_length=1024)
    summary_ids = summarizer.generate(inputs['input_ids'], num_beams=4, min_length=30, max_length=150, early_stopping=True)
    return summarizer_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
