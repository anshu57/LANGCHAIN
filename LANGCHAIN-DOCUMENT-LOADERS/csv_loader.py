from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path= '/Users/anshugangwar/Desktop/Anshu/LangChain/SeoulBikeData.csv', encoding='latin1')

docs = loader.load()

print(len(docs))
print(docs[0])
print(docs[0].metadata)