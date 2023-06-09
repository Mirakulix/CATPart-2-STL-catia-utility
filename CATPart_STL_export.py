''' Die direkte Umwandlung von .CATPRT zu .STL Dateien mit Python ist nicht möglich, da Python nicht nativ mit Catia interagieren kann. Allerdings kann Python mit Catia über die COM-Schnittstelle interagieren, um Catia zu steuern und die Umwandlung durchzuführen. '''
import win32com.client
import os

def convert_catprt_to_stl(input_file, output_file):
    # Starte Catia
    catia = win32com.client.Dispatch('catia.Application')

    # Öffne die .CATPRT Datei
    document = catia.Documents.Open(input_file)

    # Exportiere die Datei als .STL
    export_data = document.Part.ExportData(output_file, "STL")

    # Schließe das Dokument
    document.Close()

if __name__ == "__main__":
    input_directory = "C:\\path\\to\\your\\catprt\\files"
    output_directory = "C:\\path\\to\\your\\stl\\files"

    for filename in os.listdir(input_directory):
        if filename.endswith(".CATPRT"):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, filename.replace(".CATPRT", ".STL"))
            convert_catprt_to_stl(input_file, output_file)
