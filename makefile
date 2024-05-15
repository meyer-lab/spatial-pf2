SHELL := /bin/bash

.PHONY: clean test

flist = $(wildcard spatialpf2/figures/figure*.py)
allOutput = $(patsubst spatialpf2/figures/figure%.py, output/figure%.svg, $(flist))

all: $(allOutput)

output/figure%.svg: spatialpf2/figures/figure%.py
	@ mkdir -p ./output
	poetry run fbuild $*

test:
	poetry run pytest -s -x -v

coverage.xml:
	poetry run pytest --cov=spatialpf2 --cov-report=xml

clean:
	rm -rf output profile profile.svg
	rm -rf factor_cache

testprofile:
	poetry run python3 -m cProfile -o profile -m pytest -s -v -x
	gprof2dot -f pstats --node-thres=5.0 profile | dot -Tsvg -o profile.svg

mypy:
	poetry run mypy --install-types --non-interactive --ignore-missing-imports --check-untyped-defs spatialpf2
