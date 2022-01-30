all: clean data

data:
	mkdir -p _images
	./arff2png.py mnist_test.arff

clean:
	rm -f _images/*.png

train:
	./mnist_train.py $(MY_DATA)/mnist/mnist_784.arff mnist.model

test:
	./mnist_test.py mnist.model mnist_test.arff 2
	./mnist_test.py mnist.model _images/img0_5.png
