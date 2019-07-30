default: test
.PHONY: default

install_prerequisites:
	python bootstrap.py
	bin/buildout
.PHONY: install_prerequisites

generate_tests:
	hiptest-publisher -c python-unittest.conf -t "$(SECRET_TOKEN)" --without=actionwords
.PHONY: generate_tests

test: install_prerequisites
	bin/test
.PHONY: test
