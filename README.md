# pdf2doc

Add page number to some PDF files and merge it → PERFECT DOCUMENT! ⭐️

## Install

```sh
brew tap ryuhey0123/pdf2doc
brew install pdf2doc
```

## Usage

```sh
pdf2doc [OPTIONS] [FILES]
```

- FILES : PDF files
- OPTIONS

| Options                           | Does                                                       |
| --------------------------------- | ---------------------------------------------------------- |
| `--output [str]`                  | Set output PDF file name. Default "output.pdf"             |
| `--halign [str]` `--valign [str]` | Set align. Default "center" "bottom"                       |
| `--margin [float]`                | Set margin. Default 10                                     |
| `--font [str]` `--size [int]`     | Set font name and size, Default "Helvetica" 9              |
| `--merge`                         | If set this option, merge input file and output.           |
| `--blank`                         | If set this option, add blank page at tale in odd section. |

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
