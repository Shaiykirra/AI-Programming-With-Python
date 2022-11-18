import argparse
import json
import numpy as np
from PIL import Image
import torch
import torchvision
import torch.nn.functional as F


# simple example
# python predict.py "flowers/test/10/image_07090.jpg" train_checkpoint.pth --gpu



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', metavar='image_path', type=str, default='flowers/test/10/image_07090.jpg')
    parser.add_argument('checkpoint', metavar='checkpoint', type=str, default='checkpoint.pth')
    parser.add_argument('--top_k', action='store', dest="top_k", type=int, default=5)
    parser.add_argument('--category_names', action='store', dest='category_names', type=str, default='cat_to_name.json')
    parser.add_argument('--gpu', action='store_true', default=False)
    return parser.parse_args()


def load_checkpoint(filepath):
    checkpoint = torch.load(filepath)
    model = torchvision.models.vgg11(pretrained=True)
    
    # freeze model parameters
    for param in model.parameters():
        param.requires_grad = False

    model.classifier = checkpoint['classifier']
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']
    
    return model


def process_image(image):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    
    # TODO: Process a PIL image for use in a PyTorch model
    image = Image.open(image_path)
    image_transform = transforms.Compose([transforms.Resize(256),
                                 transforms.CenterCrop(224),
                                 transforms.ToTensor(),
                                 transforms.Normalize([0.485, 0.456, 0.406], 
                                                      [0.229, 0.224, 0.225])])
    image = image_transform(image)
    
    return image
    process_image = process_image(image_path) # checking aginst process_image function created 
    process_image.shape #testing to see if tensor shape is correct 


def predict(image_path, model, topk=5):
    ''' Predict the class (or classes) of an image using a trained deep learning model.
    '''
    
    # TODO: Implement the code to predict the class from an image file
    model.to(device)
    model.eval()
    image = process_image(image_path).numpy()
    image = torch.from_numpy(np.array([image])).float()

    with torch.no_grad():
        output = model.forward(image.cuda())
        
    probability = torch.exp(output).data
    
    return probability.topk(topk)


def load_names(category_names_file):
    with open(category_names_file) as file:
        category_names = json.load(file)
    return category_names


def main():
    args = parse_args()
    image_path = args.image_path
    checkpoint = args.checkpoint
    top_k = args.top_k
    category_names = args.category_names
    gpu = args.gpu

    model = load_checkpoint('checkpoint.pth')

    top_p, classes, device = predict(image_path, model, top_k, gpu)

    category_names = load_names(category_names)

    labels = [category_names[str(index)] for index in classes]

    print(f"Results for your File: {image_path}")
    print(labels)
    print(top_p)
    print()

    for i in range(len(labels)):
        print("{} - {} with a probability of {}".format((i+1), labels[i], top_p[i]))


if __name__ == "__main__":
    main()