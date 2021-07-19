# Mnist-Anomaly-detection

## Goal
The Goal of this notebook is to identify anomalies in given dataset.

## Data
the dataset contains 100 images.
90 from mnist, 10 from other dataset

## Method
I used pre-trained VAE that as been trained on mnist dataset to generates new images.

In variational autoencoders, inputs are mapped to a probability distribution over latent vectors, and a latent vector is then sampled from that distribution. The decoder becomes more robust at decoding latent vectors as a result.

So, if i will have data from diffrenet distrabution, the VAE wont succed to reconstruct the image.
And my loss will be big.

Like that I can find anomalies if their loss will be bigger than normal data.

## Pre-Trained
I Used pre-trained NN that i found here https://github.com/csinva/gan-vae-pretrained-pytorch
