import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer, CodeGenForCausalLM, AutoTokenizer

def load_model(model_name):
    """
    Load the model and tokenizer based on the model_name.
    Supports gpt2, gpt2-medium, gpt2-medium-persian
    """
    if model_name == "gpt2":
        print("Loading GPT-2 base model...")
        model = GPT2LMHeadModel.from_pretrained("./models/gpt2")
        tokenizer = GPT2Tokenizer.from_pretrained("./models/gpt2")
    elif model_name == "gpt2-medium":
        print("Loading GPT-2 medium model...")
        model = GPT2LMHeadModel.from_pretrained("./models/gpt2-medium")
        tokenizer = GPT2Tokenizer.from_pretrained("./models/gpt2-medium")
    elif model_name == "gpt2-persian":
        print("Loading GPT-2 Persian model...")
        model = GPT2LMHeadModel.from_pretrained("./models/gpt2-medium-persian")
        tokenizer = GPT2Tokenizer.from_pretrained("./models/gpt2-medium-persian")
    elif model_name == "codegen":
        print("Loading CodeGen model...")
        model = CodeGenForCausalLM.from_pretrained("./models/codegen", device_map='cpu')
        tokenizer = AutoTokenizer.from_pretrained("./models/codegen")
    elif model_name == "gpt2-large":
        print("Loading GPT2 Large Model...")
        if os.path.exists(os.path.join("./models/gpt2-large", "pytorch_model.bin")):
            model = GPT2LMHeadModel.from_pretrained("./models/gpt2-large")
        elif os.path.exists(os.path.join("./models/gpt2-large", "model.safetensors")):
            model = GPT2LMHeadModel.from_pretrained("./models/gpt2-large", from_tf=False, trust_remote_code=True)
        else:
            raise FileNotFoundError("Neither 'pytorch_model.bin' nor 'model.safetensors' found in the specified path.")      
        tokenizer = GPT2Tokenizer.from_pretrained("./models/gpt2-large") # Load Tokenizer

    # Configure the pad_token for text models
    if tokenizer:
        tokenizer.pad_token = tokenizer.eos_token
    
    return model, tokenizer
