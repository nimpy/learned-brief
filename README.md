# Learned BRIEF

This repository contains the code for the *learned BRIEF* local image descriptor. In Step 1, [original BRIEF descriptor](https://www.cs.ubc.ca/~lowe/525/papers/calonder_eccv10.pdf) is implemented as a convolutional neural network (using convolutional layers to implement the average blurring and a fully-connected layer to implement BRIEF's binary pixel tests). In Step 2, this CNN is integrated to be the encoder part of an autoencoder, and the decoder is learned (trained to invert an encoding into its patch), and in Step 3, the whole autoencoder is trained. Learned BRIEF descriptor is then taken to be the encoder part of the trained autoencoder.

Trained models can be found are under [weights_pub/](https://github.com/nimpy/learned-brief/tree/master/weights_pub), both the [whole autoencoder](https://github.com/nimpy/learned-brief/blob/master/weights_pub/learned_brief_ae_20200605.h5) and only [the encoder part](https://github.com/nimpy/learned-brief/blob/master/weights_pub/learned_brief_20200605.h5) (i.e. only the descriptor).

For more details, refer to [the paper](https://ieeexplore.ieee.org/document/9287159) or [the YouTube video](https://youtu.be/xPaRN4L9eT0).

![Steps 1-3](/figures/learned_brief_steps_1-3.png)


### Additional experiments

We also provide [a notebook](https://github.com/nimpy/learned-brief/blob/master/steps_alternative__train_whole_AE_from_scratch.ipynb) for training a descriptor with the same autoencoder architecture from scratch (without the initialisation of weights to mimic BRIEF), and [the model trained using this setup](https://github.com/nimpy/learned-brief/blob/master/weights_pub/alt_learned_brief_ae.h5).
