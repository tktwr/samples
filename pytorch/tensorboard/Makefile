ifdef USERPROFILE
	WINPTY=winpty
else
	WINPTY=
endif

default:

run:
	$(WINPTY) python ./sample_tensorboard.py

run-tensorboard:
	tensorboard --logdir=runs

