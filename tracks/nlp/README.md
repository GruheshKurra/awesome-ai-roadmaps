# Learn NLP

Goal: Go from raw text to working NLP systems: tokenization, classical models, sequence labeling, embeddings, transformers, and fine-tuning a model on a real task.

Prereqs: Python. Comfort with arrays, gradients, and a first machine-learning course (train/dev/test, overfitting, cross-entropy). You do not need a finished deep-learning track.

Status: done

Natural language processing (NLP) is how programs treat human language as data: classify it, extract structure from it, translate it, and generate it. This track is a roadmap, not a dump. Follow the stages in order. The ranked list at the bottom is the same material, numbered so you can skip around after you know the shape.

You are done with this track when you can do all of this without a tutorial open:

- Tokenize text, justify a tokenizer choice, and name what BPE is doing.
- Train a bag-of-words or logistic classifier and report a metric that matches the task (not “accuracy” by default).
- Run a spaCy pipeline for POS/NER and say where rules beat a model.
- Explain self-attention, positional encoding, and encoder vs decoder vs encoder-decoder.
- Fine-tune a pretrained transformer on a small labeled set and write down the split, metric, and failure cases.
- Read an ACL paper: task, data, baseline, claim, what would falsify it.

Budget: about 10–14 weeks at 8–12 hours a week if you do the exercises. Faster if you already write PyTorch. Slower if you skip the book chapters and only watch videos. Do not skip the book.

## Order

1. Language as data, tokens, n-grams, classification (SLP3 ch. 1–4 plus NLTK ch. 1–3, 6).
2. Industrial pipelines: tokenization, POS, NER, rules plus models (spaCy course, all four chapters).
3. Neural NLP: embeddings, then Stanford CS224N lectures and assignments through RNNs/attention.
4. Transformers: Illustrated Transformer, then Attention Is All You Need, then the Annotated Transformer notebook.
5. Pretraining and fine-tuning: D2L NLP pretraining, BERT, Hugging Face LLM course ch. 1–8, one Hub fine-tune.
6. Language modeling from the metal: Karpathy lectures 2 and 7–8 (makemore, GPT, tokenizer).
7. Research habits: CMU Advanced NLP for graduate depth, then ACL Anthology for papers you actually need.

Do not start at Hugging Face. You will get a working `pipeline()` and still not know why tokenization or class imbalance wrecks the metric.

## Stage 1: Text, tokens, n-grams, classification

Read SLP3 chapters 1–4 (introduction, words and tokens, n-gram LMs, logistic regression for text). Work NLTK book chapters 1–3 and 6 in a notebook: load a corpus, tokenize, build a frequency baseline, train a classifier.

Stop when you can answer: what is a token vs a word vs a type; why n-gram LMs fail on long context; why accuracy is the wrong metric on a 95/5 spam split.

Trap: treating NLTK as “how NLP is done in 2026.” It is how you *see* the data. Production tagging and NER come next.

## Stage 2: Pipelines you can ship

Complete [Advanced NLP with spaCy](https://course.spacy.io/en/). Tokenize, match, NER, custom components, then train a small entity recognizer.

Stop when you can take a folder of text, extract a typed entity list, and explain one place a matcher should override the statistical model.

Trap: jumping to transformers for NER on 200 labeled examples. spaCy plus rules will often win there.

## Stage 3: Neural NLP as a course

Use the current [Stanford CS224N](https://web.stanford.edu/class/cs224n/) site (Winter 2026 as of this writing) for the syllabus, notes, and assignments. Watch the public lecture playlist if you are not in the class. Do the assignments, not just the videos. Word vectors, then sequence models, then attention.

Stop when you can implement a batched skip-gram or an attention layer without copying a gist, and you can say what exploding/vanishing gradients look like in an RNN.

Trap: watching CS224N at 2x with no code. The assignments are the course.

## Stage 4: The Transformer, on paper and in code

Read [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) once for the picture. Then read [Attention Is All You Need](https://arxiv.org/abs/1706.03762) with a pen: residual stream, multi-head attention, positional encoding, why no recurrence. Then run the [Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) so the paper and the tensors match.

Stop when you can write the scaled-dot-product formula from memory and point to masking in the decoder.

Trap: “I understand transformers” after the blog post only. The paper’s section 3 is short. Read it.

## Stage 5: Pretrain, then fine-tune

Work [D2L: NLP pretraining](https://d2l.ai/chapter_natural-language-processing-pretraining/index.html) for word2vec, subword units, and BERT as executable chapters. Read the [BERT paper](https://arxiv.org/abs/1810.04805). Then take the free [Hugging Face LLM course](https://huggingface.co/learn/llm-course) through the tokenizer/datasets/fine-tune chapters. Fine-tune one encoder on a small classification or token-classification dataset. Write the metric, the split, and five errors.

SLP3 chapters 5–9 (embeddings, networks, transformers and pretraining, post-training, masked LMs) sit beside this stage, not instead of the code.

Stop when you can explain MLM vs causal LM, and you have a Hub or local checkpoint you trained, not only `pipeline("sentiment-analysis")`.

Trap: starting this stage before CS224N attention. The Hub will hide the model from you.

## Stage 6: Build a language model

[Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero) lectures 2 (makemore / language modeling), 7 (GPT), and 8 (tokenizer). Optional: lectures 3–5 if your PyTorch is weak.

Stop when you have sampled from a model you trained, and you can explain BPE as merge operations rather than “subwords.”

## Stage 7: Read the field

[CMU CS11-711 Advanced NLP (Fall 2024)](https://www.phontron.com/class/anlp-fall2024/) plus the lecture videos if you want graduate breadth (syntax, semantics, neural methods, a paper reimplementation). Use the [ACL Anthology](https://aclanthology.org/) as the search box for NLP papers, not a random PDF blog.

When you need a paper: task, dataset, baseline, metric, claim, compute. If you cannot name the baseline, you did not read it.

## Ranked resources

Use this order. Fifteen items. Later stages assume earlier ones.

- [Speech and Language Processing (3rd ed. draft)](https://web.stanford.edu/~jurafsky/slp3/) - Type: book. Free textbook that is still the field’s spine: tokens, n-grams, classification, embeddings, transformers, and linguistic structure, with an August 2026 draft.
- [Natural Language Processing with Python (NLTK book)](https://www.nltk.org/book/) - Type: book. Forces you to touch corpora, tokenize, and classify in Python before you hide behind a Hub pipeline.
- [Advanced NLP with spaCy](https://course.spacy.io/en/) - Type: course. Free interactive path for production tokenization, NER, rules, and training a small statistical pipeline.
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/) - Type: course. Current Stanford deep-learning NLP offering (syllabus, notes, assignments). Winter 2026 page is the live index.
- [Stanford CS224N lecture videos](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D) - Type: playlist. Public lectures for the same course when you cannot sit in NVIDIA Auditorium.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) - Type: course. One sitting visual pass over encoder, decoder, Q/K/V, and multi-head attention before the paper.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Type: paper. The architecture you will keep meeting; read section 3, not only the abstract.
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) - Type: repo. Paper lines next to a working implementation so the figures become tensors.
- [Dive into Deep Learning: NLP pretraining](https://d2l.ai/chapter_natural-language-processing-pretraining/index.html) - Type: book. Executable word2vec, subwords, and BERT chapters you can run, not only read.
- [BERT](https://arxiv.org/abs/1810.04805) - Type: paper. Why bidirectional pretraining plus a small head replaced most task-specific architectures.
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course) - Type: course. Free, no ads; Transformers, Datasets, Tokenizers, and fine-tuning. Formerly the NLP course; same stack.
- [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero) - Type: repo. Notebooks and videos that build a language model and a GPT tokenizer from scratch.
- [CMU Advanced NLP Fall 2024](https://www.phontron.com/class/anlp-fall2024/) - Type: course. Graduate NLP (CS11-711): tasks, neural methods, and a paper-style project, with public materials.
- [CMU Advanced NLP lecture videos](https://www.youtube.com/playlist?list=PL8PYTP1V4I8D4BeyjwWczukWq9d8PNyZp) - Type: playlist. Fall 2024 lecture recordings to pair with the course site.
- [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) - Type: paper. The original skip-gram / CBOW word2vec write-up; read it after SLP3 embeddings or D2L 15.1, not as your first NLP paper.

## Suggested builds (pick two)

1. News or tweet classifier: n-gram or TF-IDF baseline, then a fine-tuned encoder. Report F1, not only accuracy. Keep the baseline in the table.
2. NER on a domain you care about (resumes, medical abstracts, legal clauses): spaCy first, transformer token-classification only if the error analysis says you need it.
3. Character LM then BPE: train makemore-style, then encode the same text with a tokenizer you understand.
4. Reimplement one figure from a short ACL paper (attention heatmap, learning curve, ablation). If you cannot reproduce the number, write why.

## Out of this track

Paid Coursera certificates, “NLP in 5 hours” playlists with no syllabus, and prompt-only ChatGPT demos. Those do not replace SLP3, CS224N, or a fine-tune you ran.

LLMs as a product (agents, eval harnesses, serving) are a later track. Finish BERT and a causal LM first.
