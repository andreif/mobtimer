.PHONY: clean
clean:
	rm -rf build dist


.PHONY: publish
publish: clean
	python ./setup.py sdist bdist_wheel
	twine check dist/*
	twine upload dist/*
