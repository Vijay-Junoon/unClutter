import re
from pathlib import Path
import pandas as pd
import pymupdf as pdf
from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
import shutil

from groq import Groq

contents = []
titles = []
files = []
parent = Path("")

def createDir(data,folder_titles,parent : Path):
    for i in folder_titles:
        folder = parent / i
        folder.mkdir(parents=True,exist_ok=True)

    for i in data:
        correctFolder = parent/folder_titles[int(i)]
        for j in data[i]:
            j = Path(j)
            shutil.move(j,correctFolder)
def map_files(files,clusters):
    ffMap = dict()
    for i in range(len(files)):
        if str(clusters[i]) in ffMap:
            ffMap[str(clusters[i])].append(files[i])
        else:
            ffMap[str(clusters[i])] = [files[i]]
    return(ffMap)
    # create_directories(ffMap)

def learn(X):
    df = pd.DataFrame(X)
    df['file'] = files
    learner = DBSCAN(eps=0.7,min_samples=1,metric="cosine")
    learner.fit(X)
    df['cluster'] = learner.labels_
    print(df['cluster'].value_counts())
    folder_titles = corpus_title(df['cluster'])
    return [map_files(df['file'],df['cluster']),folder_titles]

def corpus_title(clusters):
    similar_content = []
    sett = set(clusters)
    for i in sett:
        arr = []
        for j in  range(len(clusters)):
            if clusters[j] == i:
                arr.append(contents[j][:1000])
        similar_content.append(arr)
    print(similar_content)
    client = Groq(api_key = "")
    bot = client.chat.completions.create(
        messages = [{"role": "user", "content": f"""
You are an intelligent document organizer.

You will receive a NESTED LIST of document clusters.

IMPORTANT:
- Each INNER LIST represents ONE cluster of similar documents.
- Generate EXACTLY ONE folder title for EACH inner list.
- The number of titles must equal the number of inner lists.

STRICT RULES:
1. Generate ONE title PER inner list.
2. Maximum 3 words only.
3. Acronyms are allowed and encouraged where appropriate.
   Examples:
   - Full Stack Development → FSD
   - Machine Learning → ML
   - Artificial Intelligence → AI
   - Cloud Computing → CC
4. Ignore:
   - Unit numbers
   - Faculty names
   - College names
   - "Prepared by"
   - Repeated headers
   - OCR/PDF noise
5. Choose the BROADEST common subject for the cluster.
6. Folder-safe names only:
   - No punctuation
   - No special symbols
7. No explanations.
8. Return ONLY a Python list of titles.

Example:

Input:
[
    ["React", "MongoDB", "Node.js", "Angular"],
    ["AWS", "Cloud migration", "SaaS"],
    ["Regression", "SVM", "Classification"]
]

Output:
[
    "FSD",
    "Cloud Computing",
    "ML"
]

Now generate titles for this nested list:

{similar_content}
"""}],
        model = "llama-3.3-70b-versatile",)
    folder_titles = bot.choices[0].message.content
    return folder_titles

def vectorize():
    # print(contents)
    model = SentenceTransformer( 'all-MiniLM-L6-v2')
    X = model.encode(contents)
    return learn(X)

def clean_text(text):

    text = re.sub("\n+"," ",text)
    text = re.sub(r"\s+"," ",text)
    text = re.sub('^[a-zA-Z]',"",text)
    return text

def extractCorpus():
    for item in list(parent.glob("*.pdf")):
        files.append(item)
        doc = pdf.open(item)
        temp = Path("temp.txt")
        with open(temp,"wb") as content:
            for i in range(len(doc)):
                text = doc[i].get_text().encode("utf-8")
                content.write(text)
                content.write(bytes((12,)))
        contents.append(clean_text(temp.read_text(encoding="utf-8")))
        temp.unlink()
    # print(files)
    return len(contents)