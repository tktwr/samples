all: build whl whl-install

build:
	python setup.py build

build-install:
	python setup.py install

build-install-user:
	python setup.py install --user

sdist:
	python setup.py sdist

whl:
	python setup.py bdist_wheel

whl-install:
	pip install --force-reinstall dist/myModule-*.whl

whl-uninstall:
	pip uninstall myModule

ver:
	pip list | grep myModule

run:
	python hello.py

clean:
	rm -rf build dist myModule.egg-info

