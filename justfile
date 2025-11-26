default:
    just --list

install:
    uv sync

[working-directory: "src"]
build:
    uv run ablog clean
    uv run ablog build

[working-directory: "src"]
serve:
    uv run ablog serve
