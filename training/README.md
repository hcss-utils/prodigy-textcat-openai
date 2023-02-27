# training

- Install `spacy-transformers` by running: `pip install -r requirements_train.txt`
- Train: `python -m spacy train configs/config.cfg --output models/ --paths.train corpus/train.spacy --paths.dev corpus/dev.spacy --nlp.lang en --gpu-id -1`
