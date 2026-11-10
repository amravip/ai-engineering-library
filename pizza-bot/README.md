# The Learning Path

Bella runs a small pizza shop, and you build her assistant one step at a time. Each step adds one idea, and each step folder is the complete project at the end of that step. Work through the steps in order, or open one folder and compare your files with it.

## The steps

### 1. First conversation (`01-first-conversation`)

Ask a local model a question, first without the menu and then with it. You see the model invent pizzas, and then answer from the menu once you give it the facts.

### 2. Tokens (`02-tokens`)

A model reads tokens, which are pieces of words, not letters. You train a small tokenizer on the menu and the reviews. Then you see why a model can miscount the letters in a word.

### 3. Embeddings (`03-embeddings`)

An embedding turns text into a list of numbers, so that similar meanings get similar lists. You search the menu by meaning, so "something meat-free" finds the vegetarian pizzas.

### 4. Attention (`04-attention`)

Each word looks at the words around it. You build attention in plain Python, and you see the word "hot" mean spicy in one sentence and warm in another.

### 5. Training (`05-training`)

A model learns from data. You build a tiny next-word model that learns by counting, and you watch its loss fall as it trains.

### 6. Fine-tuning (`06-fine-tuning`)

A model that only continues text does not answer questions. You add `chat()`, look at the chat template that wraps each message, and teach the tiny model to answer using examples.

### 7. Temperature (`07-temperature`)

Temperature controls how varied a model's words are. You see how it reshapes the probabilities, first on the tiny model and then on the real one.

### 8. Talking to models from code (`08-talking-to-models-from-code`)

A program needs data, not a paragraph. You ask the model for a fixed shape, parse three orders, and check each one against the menu. The exercise for this step is in `exercises/08-structured-output`.

### 9. The context window (`09-the-context-window`)

A model sees only the text that fits in its context window. You reproduce a bot that forgets a customer's name, then fix it by trimming the history and keeping a short summary.

### 10. Hallucination (`10-hallucination`)

A model can sound sure and still be wrong. You see an invented opening time, and then you write a checker that flags pizza names that are not on the menu.

### 11. Retrieval-augmented generation (`11-rag`)

The bot searches the shop's documents, passes the best matches to the model, and the model names the file it used. You compare keyword search with embedding search.

### 12. Tools and agents (`12-tools-and-agents`)

A tool is a function the model can ask the program to run, such as an order lookup. An agent is the loop that asks the model, runs the tool it requests, and asks again.

### 13. Shipping it (`13-shipping-it`)

A demo is not proof that the bot is right. You write an evaluation of ten questions with known answers, and you measure the tokens and seconds that each answer costs.

## Where to go next

Each step README lists its files, the commands to run, and the results to expect. Saved outputs are marked as fixed output, which must match exactly, or as real runs, where your wording will differ.
