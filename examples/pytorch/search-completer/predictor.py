# this is an example for cortex release 0.12 and may not deploy correctly on other releases of cortex your `cortex version`

import torch
import regex
import tqdm


class PythonPredictor:
    def __init__(self, config):
        roberta = torch.hub.load("pytorch/fairseq", "roberta.large")
        roberta.eval()
        roberta.cuda()

        self.model = roberta

    def predict(self, payload):
        predictions = self.model.fill_mask(payload["text"] + " <mask>", topk=5)
        return [prediction[0] for prediction in predictions]
