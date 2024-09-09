# from transformers import GPT2LMHeadModel, GPT2Tokenizer
#
#
# def generate_text(prompt, max_length=200):
#     model_name = 'gpt2'
#     tokenizer = GPT2Tokenizer.from_pretrained(model_name)
#     model = GPT2LMHeadModel.from_pretrained(model_name)
#
#     inputs = tokenizer.encode(prompt, return_tensors='pt')
#     outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
#     text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return text
#
#
# prompt = "Once upon a time in a land far away,"
# print(generate_text(prompt))
from transformers import GPT2LMHeadModel, GPT2Tokenizer


def generate_text(prompt, max_length=200):
    model_name = 'gpt2'
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Encode the prompt text to tensor format
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Generate text based on the prompt
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)

    # Decode the tensor to string
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text


def main():
    prompt = input("Enter a prompt for text generation: ")
    generated_text = generate_text(prompt)
    print("\nGenerated Text:")
    print(generated_text)


if __name__ == "__main__":
    main()
