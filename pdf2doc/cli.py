import os

from click import Path, Choice, IntRange
from click import command, argument, option, echo
from send2trash import send2trash

from .addpage import Margin
from .addpage import paged_pdfs_writer, concat_pdfs_merger


cwd = os.getcwd()

PDF2DOC_FONT = "Helvetica"
PDF2DOC_FONTSIZE = 9
PDF2DOC_FORMAT = "{0} - {1}"
PDF2DOC_SUFFIX = '_paged'

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def validate_file_args(ctx, param, value):
    if not value:
        echo(ctx.get_help())
        ctx.exit()
    return value


@command(context_settings=CONTEXT_SETTINGS)
@argument('files', nargs=-1, type=Path(exists=True), callback=validate_file_args)
@option('--output', '-o', default='output.pdf', type=str, help='Set output file name.')
@option('--halign', '-h', default='center', type=Choice(['left', 'center', 'right']), help='Set horizon position.')
@option('--valign', '-v', default='bottom', type=Choice(['top', 'center', 'bottom']), help='Set vertical position.')
@option('--margin', '-m', default=10, type=IntRange(0, 100), help='Set mergin.')
@option('--font', '-f', default=PDF2DOC_FONT, help='Set font name.')
@option('--size', '-s', default=PDF2DOC_FONTSIZE, help='Set font size.')
@option('--merge', is_flag=True, help='Merge document.')
@option('--blank', is_flag=True, help='Add blank page for double print.')
def cli(files, output, halign, valign, margin, font, size, merge, blank):
    """ ⭐️ Add pages to PDFs and merge(optional) -> PERFECT DOCUMENT! 📑"""

    file_paths = [os.path.join(cwd, file) for file in files]

    output_paths = []
    for path in file_paths:
        root, ext = os.path.splitext(path)
        output_paths.append(root + PDF2DOC_SUFFIX + ext)

    output_writers = paged_pdfs_writer(
        files=file_paths,
        h_align=halign,
        v_align=valign,
        margin=Margin(all=margin),
        font=font,
        font_size=size,
        format=PDF2DOC_FORMAT,
        add_blank=blank
    )

    echo('Temporary saving file...')
    for writer, path in zip(output_writers, output_paths):
        with open(path, 'wb') as f:
            writer.write(f)

    echo('Merging PDFs...')
    if merge:
        echo('  Merge pages...')
        merger = concat_pdfs_merger(output_paths)
        merger.write(output)
        merger.close()
        for path in output_paths:
            send2trash(path)

    echo('')
    echo('      ⭐️⭐️⭐️ All Done! ⭐⭐️⭐️️')
