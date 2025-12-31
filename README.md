# Img text to Clipboard (hebrew)


### Requiremenets 

- a mac 
- homebrew
- python 
- some python manager (uv , pip etc)

### Activation
```bash
git clone https://github.com/manemajef/ocr_clip ~/.ocr_clip
cd ~/.ocr_clip
brew install tesseract-lang uv
uv sync
uv run main.py
```
**for easy access**: write a zsh function:
```bash
echo "~/.ocr_clip/.venv/bin/python ~/.ocr_clip/main.py" >> ~/.zshrc 
```
