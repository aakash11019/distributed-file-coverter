# Document conversion module enhanced with logging and validation by Aakash Sharma

import os
import subprocess


def convert(input_path, target_format):
    """
    Convert document files using LibreOffice (soffice).
    Supports: docx→pdf, txt→pdf, odt→pdf, etc.
    """

    target_format = target_format.lower().strip('.')
    output_dir = os.path.dirname(input_path) or "."

    print("[DOC CONVERTER] Starting document conversion...")
    print(f"[DOC CONVERTER] Input file: {input_path}")
    print(f"[DOC CONVERTER] Target format: {target_format}")

    # Validate input file existence
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    cmd = [
        "soffice", "--headless",
        "--convert-to", target_format,
        "--outdir", output_dir,
        input_path
    ]

    print(f"[DOC CONVERTER] Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("[DOC CONVERTER] Conversion failed.")
        raise RuntimeError(f"LibreOffice error: {result.stderr}")

    base = os.path.splitext(input_path)[0]
    output_path = f"{base}.{target_format}"

    if not os.path.exists(output_path):
        raise FileNotFoundError(f"Converted file not found: {output_path}")

    print(f"[DOC CONVERTER] Conversion successful: {input_path} → {output_path}")
    return output_path


def can_handle(input_path, target_format):
    doc_formats = {'pdf', 'docx', 'odt', 'txt', 'html', 'rtf'}
    ext = os.path.splitext(input_path)[1].lower().strip('.')
    return ext in doc_formats and target_format.lower() in doc_formats
