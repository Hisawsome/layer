import base64

# Define the encoded data and key
encoded_data = base64.b64decode(
    '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'
)
key = [98, 111, 115, 115, 50, 52, 54, 55]

# Decode the data using the XOR key
decoded_data = bytes([b ^ key[i % len(key)] for i, b in enumerate(encoded_data)])

# Display the decoded result
decoded_data.decode(errors='ignore')
