import os
from docx2pdf import convert

# Caminho para o arquivo DOCX de entrada
docx_file = "./CERTIFICADO_DEUDA_AL_DIA_1.docx"

# Caminho para o arquivo PDF de saída
pdf_file = "output.pdf"

# Converter o arquivo DOCX para PDF
convert(docx_file, pdf_file)

# Definir permissões de acesso para o arquivo PDF (por exemplo, 0o777 para conceder acesso a todos)
os.chmod(pdf_file, 0o777)
