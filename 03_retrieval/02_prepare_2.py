from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import SpacyTextSplitter  #← SpacyTextSplitter를 가져옴

# spacy 에서 언어 처리를 하기 위해서는 대상 언어의 "모델" 이라는 데이터를 다운로드 해야 함
# spacy download ko_core_news_sm
# 을 통해 다운로드 해야 함

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_splitter = SpacyTextSplitter(  #← SpacyTextSplitter를 초기화
    chunk_size=300,  #← 분할할 크기를 설정
    pipeline="ko_core_news_sm"  #← 분할에 사용할 언어 모델을 설정
)
splitted_documents = text_splitter.split_documents(documents) #← 문서를 분할

print(f"분할 전 문서 개수: {len(documents)}")
print(f"분할 후 문서 개수: {len(splitted_documents)}")
