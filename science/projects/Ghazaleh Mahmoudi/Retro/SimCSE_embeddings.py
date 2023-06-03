import torch
from scipy.spatial.distance import cosine
from transformers import AutoModel, AutoTokenizer

class SimCSEChunkEmbeddings:
    def __init__(self, device: torch.device):
        
        self.device = device
        
        self.tokenizer = AutoTokenizer.from_pretrained("model_checkpoint/")
        self.model = AutoModel.from_pretrained("model_checkpoint/")

        self.model.to(self.device)

    def __call__(self, sentences: list[str]):
        # Tokenize input texts

        inputs = self.tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

        inputs = inputs.to(self.device)
        
        # Get the embeddings
        with torch.no_grad():
            embeddings = self.model(**inputs, output_hidden_states=True, return_dict=True).pooler_output

        return  embeddings
    
def test():

    simcse_embedding = SimCSEChunkEmbeddings('cuda:0')

    texts = [
    "دانش آموزان در حال آماده کردن خود برای امتحان هستند",
    # "دانش آموزان فردا امتحان میان ترم دارند",
    "هوا تهران امروز ابری است",
    "آزمون میان ترم سخت است"
    ]

    embeddings = simcse_embedding(texts)

    print(embeddings.shape)
    print(embeddings)



    # Calculate cosine similarities
    # Cosine similarities are in [-1, 1]. Higher means more similar
    cosine_sim_0_1 = 1 - cosine(embeddings[0].cpu() , embeddings[1].cpu() )
    cosine_sim_0_2 = 1 - cosine(embeddings[0].cpu() , embeddings[2].cpu() )


    print("Cosine similarity between \"%s\" and \"%s\" is: %.3f" % (texts[0], texts[1], cosine_sim_0_1))
    print("Cosine similarity between \"%s\" and \"%s\" is: %.3f" % (texts[0], texts[2], cosine_sim_0_2))


if __name__ == '__main__':
    test()