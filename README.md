# scripts
Various small python scripts making life easier. 

## Available scripts:

- cleanup.py
    - Cleans up current or specified directory after LaTex compilations
    - `python cleanup.py` cleans current directory
    - `python cleanup.py exampleDir` cleans ./exampleDir/
- buildMarkdownFiles.py
    - Compiles all markdown files in directory using pandoc
    - `python buildMarkdownFiles.py` compiles markdown files in current directory
    - `python buildMarkdownFiles.py exampleDir` build markdown files in ./exampleDir/

## Efficient usage

Use aliases to execute scripts in any directory.

`alias buildMarkdownFiles = "python /pathToScript/buildMarkdownFiles.py"`
