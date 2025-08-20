# LangChain Project

This repository contains various examples and demonstrations of LangChain functionalities.


## Project Structure

- `1.LLMs/`
	- 1_llm_demo.py
- `2.ChatModels/`
	- 1_chatmodel_openai.py
	- 2_chatmodel_anthropic.py
	- 3_chatmodel_google.py
	- 4_chatmodel_hf_api.py
	- 5_chatmodel_hf_local.py
- `3.EmbeddingModels/`
	- 1_embedding_openai_query.py
	- 2_embedding_openai_docs.py
	- 3_embedding_hf_local.py
	- 4_embedding_hf_local_docs.py
	- 5_document_similarity.py
- `LANGCHAIN-CHAINS/`
	- conditional_chain.py
	- parallel_chain.py
	- sequential_chain.py
	- simple_chain.py
- `LANGCHAIN-DOCUMENT-LOADERS/`
	- directory_loader.py
	- pdf_loader.py
	- text_loader.py
- `LANGCHAIN-OUTPUT-PARSERS/`
	- JSON-PARSERS/
		- jsonoutputparser_hf_api.py
	- STRING-PARSERS/
		- stroutputparser_chain_hf_local.py
		- stroutputparser_hf_api.py
	- pydanticoutputparser.py
	- structuredoutputparsers.py
	- structuredoutputparsers_chain.py
- `LANGCHAIN-RUNNABLES/`
	- langchain_aam_zindagi.ipynb
	- langchain_mentos_zindagi.ipynb
	- pdf_reader.py
	- runnable_branch.py
	- runnable_lambda.py
	- runnable_parallel.py
	- runnable_passthrough.py
	- runnable_sequence.py
	- simple_llm_app.py
- `LANGCHAIN-STRUCTURED-OUTPUT/`
	- json_schema.json
	- pydantic_demo.py
	- typeddict_demo.py
	- with_structured_output_json.py
	- with_structured_output_pydantic.py
	- with_structured_output_typeddict.py
- `langshain_notebooks/`
	- 01_document_loading.ipynb
	- 02_document_splitting.ipynb
	- 03_vectorstores_and_embeddings.ipynb
	- 04_document_retrieval.ipynb
	- 05_question_answering.ipynb
	- 06_chat.ipynb
- `docs/`
	- cs229_lectures/
	- youtube/
- `requirements.txt`, `README.md`, `.env`, `docs.txt`, `file.pdf`

## Setup

To set up the project, install the required dependencies:

```bash
pip install -r requirements.txt
```


## Environment Variables

Create a `.env` file in the root directory and add your API keys:

```
OPENAI_API_KEY="your-openai-key"
ANTHROPIC_API_KEY="your-anthropic-key"
GOOGLE_API_KEY="your-google-key"
HUGGINGFACEHUB_API_TOKEN="your-huggingface-token"
```

## Usage

Navigate to the respective directories to run the examples. For example:

```bash
python LANGCHAIN-CHAINS/conditional_chain.py
```

## Hugging Face Model Access

If you encounter a 401 Unauthorized error when using Hugging Face models, ensure your `HUGGINGFACEHUB_API_TOKEN` is valid and set in your `.env` file.

## Troubleshooting

- For `ImportError: email-validator is not installed`, run:
	```bash
	pip install 'pydantic[email]'
	```
- For zsh users, always quote package extras (e.g., `'pydantic[email]'`).
- If you need to undo a git commit:
	```bash
	git reset --soft HEAD~1
	```
- To push to GitHub for the first time:
	```bash
	git init
	git add .
	git commit -m "Initial commit"
	git remote add origin <your-repo-url>
	git branch -M main
	git push -u origin main
	```
