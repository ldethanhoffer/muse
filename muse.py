"""

 muse.py

Recommend similar paintings given a choice,

Uses transfer learning on the  VGG19 keras model 

code customized from A. Wong

"""
import sys, os
import numpy as np
from keras.preprocessing import image
from keras.models import Model
sys.path.append("src")

from vgg19 import VGG19
from imagenet_utils import preprocess_input
from plot_utils import plot_query_answer
from sort_utils import find_topk_unique
from kNN import kNN
from tsne import plot_tsne

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import random

def main():
    

    #Load the VVg19 model and remove the last layer for transfer learning
    print("Loading VGG19 pre-trained model...")
    
    base_model = VGG19(weights='imagenet')
    
    model = Model(input=base_model.input,
                  output=base_model.get_layer('block4_pool').output)


    # Read the images and embed into a vector space 

    imgs, filename_heads, X = [], [], []

    path = os.path.join("data", "final")
    print("Reading the images from '{}' directory...\n".format(path))
    for f in os.listdir(path):

        # Process the ilename
        filename = os.path.splitext(f)  # filename in directory
        filename_full = os.path.join(path,f)  # full path filename
        head, ext = filename[0], filename[1]
        if ext.lower() not in [".jpg", ".jpeg"]:
            continue

        # Read the image
        img = image.load_img(filename_full, target_size=(224, 224))  # load
        imgs.append(np.array(img))  # image
        filename_heads.append(head)  # filename head

        # Pre-process the image
        img = image.img_to_array(img)  # convert to array
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        features = model.predict(img).flatten()  # features
        X.append(features)  # append feature extractor

    X = np.array(X)  # the vectors
    imgs = np.array(imgs)  # the images
    print("imgs.shape = {}".format(imgs.shape))
    print("X_features.shape = {}\n".format(X.shape))


    # find the closest vectors using kNN:

    n_neighbours = 4 + 1  # +1 as itself is most similar
    knn = kNN()  # kNN model
    knn.compile(n_neighbors=n_neighbours, algorithm="brute", metric="cosine")
    knn.fit(X)


    # Plot the recommendations for each image in database

    output_rec_dir = os.path.join("output", "final_recommendations")

    n_imgs = len(imgs)
    ypixels, xpixels = imgs[0].shape[0], imgs[0].shape[1]
    for ind_query in range(n_imgs):
        
        # Find k closest image feature vectors to each vector
        print("[{}/{}] finding your recommendations: {}".format(ind_query + 1, n_imgs,
                                                                              filename_heads[ind_query]))
        distances, indices = knn.predict(np.array([X[ind_query]]))
        distances = distances.flatten()
        indices = indices.flatten()
        indices, distances = find_topk_unique(indices, distances, n_neighbours)
        
        # Plot the recommendations
        rec_filename = os.path.join(output_rec_dir, "{}_rec.png".format(filename_heads[ind_query]))
        x_query_plot = imgs[ind_query].reshape((-1, ypixels, xpixels, 3))
        x_answer_plot = imgs[indices].reshape((-1, ypixels, xpixels, 3))
        plot_query_answer(x_query=x_query_plot,
                          x_answer=x_answer_plot[1:],  # remove itself
                          filename=rec_filename)


    # finally, Plot the t-sne results for the dataset:

    output_tsne_dir = os.path.join("output")
    if not os.path.exists(output_tsne_dir):
        os.makedirs(output_tsne_dir)
    tsne_filename = os.path.join(output_tsne_dir, "tsne.png")
    print("Plotting tSNE to {}...".format(tsne_filename))
    plot_tsne(imgs, X, tsne_filename)

def get_recommendations():
    
    print("Loading the VGG19 model")
    base_model = VGG19(weights='imagenet')
    model = Model(input=base_model.input,
                  output=base_model.get_layer('block4_pool').output)


    # Read images and convert them to feature vectors

    imgs, filename_heads, X = [], [], []

    path = os.path.join("data", "processed")
    print("Reading the images from '{}' directory...\n".format(path))
    for f in os.listdir(path):

        # Process filename
        filename = os.path.splitext(f)  # filename in directory
        filename_full = os.path.join(path,f)  # full path filename
        head, ext = filename[0], filename[1]
        if ext.lower() not in [".jpg", ".jpeg"]:
            continue

        # Read image file
        img = image.load_img(filename_full, target_size=(224, 224))  # load
        imgs.append(np.array(img))  # image
        filename_heads.append(head) # filename head

        # Pre-process for model input
        img = image.img_to_array(img)  # convert to array
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        features = model.predict(img).flatten()  # features
        X.append(features)  # append feature extractor

    X = np.array(X)  # feature vectors
    imgs = np.array(imgs)  # images
    print("imgs.shape = {}".format(imgs.shape))
    print("X_features.shape = {}\n".format(X.shape))


    # Find k-nearest images to each image

    n_neighbours = 6 + 1  # +1 as itself is most similar
    knn = kNN()  # kNN model
    knn.compile(n_neighbors=n_neighbours, algorithm="brute", metric="cosine")
    knn.fit(X)

    
    # return the recommendations for each painting in the form of a dictionary

    output_rec_dir = os.path.join("output", "recommendations")

    n_imgs = len(imgs)
    ypixels, xpixels = imgs[0].shape[0], imgs[0].shape[1]
    recommendations = {}
    for ind_query in range(n_imgs):
        
        # Find k closest image feature vectors to each vector
        print("[{}/{}] finding your recommendations: {}".format(ind_query + 1, n_imgs,
                                                                              filename_heads[ind_query]))
        distances, indices = knn.predict(np.array([X[ind_query]]))
        distances = distances.flatten()
        indices = indices.flatten()
        indices, distances = find_topk_unique(indices, distances, n_neighbours)
        
        indices = indices[0][1:] #remove the first painting (as its obviously the closet one)
        wildcard = np.array([random.randrange(1, n_imgs) for _ in range(3)]) #(add 3 random paintings in the next suggestion)
        print(indices)
        print(wildcard)
        indices = np.concatenate((indices,wildcard))
        recommendations.update({ind_query:indices})    
    
    return recommendations

# Driver
if __name__ == "__main__":
    main()