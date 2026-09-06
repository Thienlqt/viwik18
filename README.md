# Set up
## Create dataset ready dir
cd viwik18
mkdir -p dataset_ready
## Merge to single file
    $ cat dataset/viwik18_* > dataset_ready/viwik18.txt

## Build dataset
```bash
python utils/build_dataset.py
```

Use Python 3.11. Run these commands from the project directory (macOS/Linux):

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\activate` instead. The patch script
builds for the current machine and needs a C compiler (Xcode Command Line Tools
on macOS, GCC on Linux, or compatible MSVC Build Tools on Windows). This setup
has been tested on macOS ARM64 with Python 3.11; other platforms are unverified.

# Train

```bash
source .venv/bin/activate
mkdir -p models/sgns
mkdir -p models/cbow
python train.py
```

`main.py` currently trains SGNS using
`dataset_compressed/viwik18_lineSentences.txt` and saves to
`models/sgns/word2vec_sgns.model`. Full training may take a long time.

# Inference

```bash
source .venv/bin/activate
python inference.py
```

`inference.py` currently loads `models/sgns/word2vec_sgns.model`.
To query the CBOW model produced by `main.py`, change its load path to
`model/cbow/word2vec_cbow.model`. Keep each model's accompanying `.npy` files
next to its `.model` file.
