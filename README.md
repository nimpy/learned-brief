# Learned BRIEF

This repository contains the code for the *learned BRIEF* local image descriptor. In Step 1, [original BRIEF descriptor](https://www.cs.ubc.ca/~lowe/525/papers/calonder_eccv10.pdf) is implemented as a convolutional neural network (using convolutional layers to implement the average blurring and a fully-connected layer to implement BRIEF's binary pixel tests). In Step 2, this CNN is integrated to be the encoder part of an autoencoder, and the decoder is learned (trained to invert an encoding into its patch), and in Step 3, the whole autoencoder is trained. Learned BRIEF descriptor is then taken to be the encoder part of the trained autoencoder.

Trained models can be found are under [weights_pub/](https://github.com/nimpy/learned-brief/tree/master/weights_pub), both the [whole autoencoder](https://github.com/nimpy/learned-brief/blob/master/weights_pub/learned_brief_ae_20200605.h5) and only [the encoder part](https://github.com/nimpy/learned-brief/blob/master/weights_pub/learned_brief_20200605.h5) (i.e. only the descriptor).

![Steps 1-3](/figures/learned_brief_steps_1-3.png)
