from datasets import load_dataset

ds = load_dataset("karpathy/tiny_shakespeare", split="train")

print(ds[0]["text"])


