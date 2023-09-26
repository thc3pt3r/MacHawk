# general_hawk.sh
# Modulo con funciones generales.  Las mismas pueden ser utilizadas por modulos personales

create_output_dir() {
    directory=$1
    if [ -d $directory ]; then
        echo "El directorio $directory ya existe. No se crea."
    else
        mkdir "$directory" || { echo "There was an error creating the directory."; exit 1; }
        echo "Directory '$directory' created successfully."
    fi
}

    compress_Triage_Output(){
        if [ -z "$1" ]; then
        echo "Error: Debes proporcionar un nombre de carpeta como argumento."
        return 1
        fi

        if [ ! -d "$1" ]; then
            echo "Error: La carpeta '$1' no existe."
            return 1
        fi

        zip -r -9 "$1.zip" "$1"

        if [ $? -eq 0 ]; then
            echo "Compresión exitosa: '$1.zip'"
            echo "Path completo: $(realpath "$1.zip")"
        else
            echo "Error: Ocurrió un problema durante la compresión de '$1'."
        fi
    }

    print_banner (){
        cat ./banner.txt
    }