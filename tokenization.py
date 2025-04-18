import tiktoken

encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")

print ("Vocab size: ", encoder.n_vocab)

text = "Hello, world! This is a test sentence."
tokens = encoder.encode(text)
print ("Tokens: ", tokens)

print ("Decoded: ", encoder.decode(tokens))
print ("Token count: ", len(tokens))