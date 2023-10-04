import os
# import platform
# import subprocess
# from tex import latex2pdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# def run():
#     # TeX source filename
#     print("running Compiler")
#     tex_filename = 'resume.tex'
#     filename, ext = os.path.splitext(tex_filename)
#     # the corresponding PDF filename
#     pdf_filename = filename + '.pdf'

#     # compile TeX file using the tex library
#     with open(tex_filename, 'r', encoding='utf-8') as tex_file:
#         latex_document = tex_file.read()
#         pdf = latex2pdf(latex_document)

#     # save the PDF to a file
#     with open(pdf_filename, 'wb') as pdf_file:
#         pdf_file.write(pdf.encode('latin1'))

#     # open PDF with platform-specific command
#     if platform.system().lower() == 'darwin':
#         subprocess.run(['open', pdf_filename])
#     elif platform.system().lower() == 'windows':
#         os.startfile(pdf_filename)
#     elif platform.system().lower() == 'linux':
#         subprocess.run(['xdg-open', pdf_filename])
#     else:
#         raise RuntimeError('Unknown operating system "{}"'.format(platform.system()))

# if __name__ == '__main__':
#     run()

import subprocess

tex_filename = os.path.join(BASE_DIR,'resume.tex')
pdf_filename = 'resume.pdf'

# Run pdflatex to compile the LaTeX file
subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])

# Check if PDF is successfully generated
if not os.path.exists(pdf_filename):
    raise RuntimeError('PDF output not found')
