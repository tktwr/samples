ifdef USERPROFILE
	WINPTY=winpty
else
	WINPTY=
endif

default:

run:
	$(WINPTY) python ./transfer_learning_tutorial.py -b 2 -w 2 -e 5

run-tensorboard:
	tensorboard --logdir=logs

view-tensorboard:
	chrome.sh http://localhost:6006/

get-data:
	curl -O https://download.pytorch.org/tutorial/hymenoptera_data.zip

