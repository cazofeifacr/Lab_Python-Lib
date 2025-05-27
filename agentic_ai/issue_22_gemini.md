```python
def is_palindrome(text):
    processed_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return processed_text == processed_text[::-1]
```
