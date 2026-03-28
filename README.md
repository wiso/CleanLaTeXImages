# CleanLaTeXImages
Remove unused images from a LaTeX project directory.

## Usage

### With `uvx` (no installation required)

```bash
uvx clean-latex-images <latex_file> <img_folder>
```

### With `pipx` (no installation required)

```bash
pipx run clean-latex-images <latex_file> <img_folder>
```

### Install permanently with `pipx`

```bash
pipx install clean-latex-images
clean-latex-images <latex_file> <img_folder>
```

### Install with `pip`

```bash
pip install clean-latex-images
clean-latex-images <latex_file> <img_folder>
```

The tool will interactively ask whether to remove each image file found in
`<img_folder>` that is not referenced in `<latex_file>`.
