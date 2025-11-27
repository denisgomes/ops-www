default:
    just --list

install:
    uv sync

clean: clean-ablog
    -rm -r build

[working-directory: "source"]
clean-ablog:
    -rm -r _website
    -rm -r __pycache__
    -rm -r .doctrees
    -rm -r jupyter_execute

build: clean
    uv run make clean
    uv run make html

deploy: build
    uv run make github

[working-directory: "source"]
serve: clean
    uv run ablog build
    uv run ablog serve
