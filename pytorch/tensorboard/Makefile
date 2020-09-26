ifdef USERPROFILE
	WINPTY=winpty
else
	WINPTY=
endif

default:

run:
	$(WINPTY) python ./sample_tensorboard.py

run-tb:
	tensorboard --logdir=local/runs

view-tb:
	chrome.sh http://localhost:6006/

clean:
	rm -rf local/runs

