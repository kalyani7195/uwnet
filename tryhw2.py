from uwnet import *
def conv_net_bn():
    l = [   make_convolutional_layer(32, 32, 3, 8, 3, 2),
            make_batchnorm_layer(8),
            make_activation_layer(RELU),
            make_maxpool_layer(16, 16, 8, 3, 2),
            make_convolutional_layer(8, 8, 8, 16, 3, 1),
            make_batchnorm_layer(16),
            make_activation_layer(RELU),
            make_maxpool_layer(8, 8, 16, 3, 2),
            make_convolutional_layer(4, 4, 16, 32, 3, 1),
            make_batchnorm_layer(32),
            make_activation_layer(RELU),
            make_connected_layer(512, 10),
            make_activation_layer(SOFTMAX)]
    return make_net(l)


def conv_net():
    l = [   make_convolutional_layer(32, 32, 3, 8, 3, 2),
            make_activation_layer(RELU),
            make_maxpool_layer(16, 16, 8, 3, 2),
            make_convolutional_layer(8, 8, 8, 16, 3, 1),
            make_activation_layer(RELU),
            make_maxpool_layer(8, 8, 16, 3, 2),
            make_convolutional_layer(4, 4, 16, 32, 3, 1),
            make_activation_layer(RELU),
            make_connected_layer(512, 10),
            make_activation_layer(SOFTMAX)]



    return make_net(l)


print("loading data...")
train = load_image_classification_data("cifar/cifar.train", "cifar/cifar.labels")
test  = load_image_classification_data("cifar/cifar.test",  "cifar/cifar.labels")
print("done")
print

print("making model...")
batch = 128
iters = 500
rate = .01
momentum = .9
decay = .005

#m = conv_net()
m = conv_net_bn()
print("training...")
#train_image_classifier(m, train, batch, iters, rate, momentum, decay)
train_image_classifier(m, train, batch, iters, 0.0, momentum, decay)
print("done")
print

print("evaluating model...")
print("training accuracy: %f", accuracy_net(m, train))
print("test accuracy:     %f", accuracy_net(m, test))

# 7.6 Question: What do you notice about training the convnet with/without batch normalization? How does it affect convergence? How does it affect what magnitude of learning rate you can use? Write down any observations from your experiments:
# TODO: Your answer

#Without BN
#('training accuracy: %f', 0.39851999282836914)
#('test accuracy:     %f', 0.400299996137619)

#With BN
#('training accuracy: %f', 0.5585799813270569)
#('test accuracy:     %f', 0.5461000204086304)

# With LR schedule
# iter < 300; rate = 0.1
# iter < 400: rate = 0.01
# iter <=500: rate = 0.001 
# ('training accuracy: %f', 0.5635600090026855)
# ('test accuracy:     %f', 0.5507000088691711)


# Model converges faster when we add batch normalization. We think this is because, 
# when using mini-batch, the input data distribution to the layers change with each
# mini-batch. With batch normalization, we normalize the input to each layer. The 
# inputs will then be zero mean and unit variance, thereby eliminating vanishing gradient. 
# This also reduces the Internal Covariance Shift (distribution of netorwk activations) 
# and hence helps the model to converge faster.