all:

clean_all: clean_data clean_model

clean_data:
	rm -rf _images

clean_model:
	rm -f mnist.model

data:
	mkdir -p _images
	./arff2png.py mnist_test.arff

train:
	./mnist_train.py $(MY_DATA)/mnist/mnist_784.arff mnist.model

test:
	./mnist_test.py mnist.model mnist_test.arff 2
	./mnist_test.py mnist.model _images/img0_5.png
