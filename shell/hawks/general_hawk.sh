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
        cat<<EOF
        888b     d888                   888    888                        888                       888b     d888                         .d88888b.                8888888888                888         88888888888      d8b                            
        8888b   d8888                   888    888                        888                       8888b   d8888                        d88P" "Y88b               888                       888             888          Y8P                            
        88888b.d88888                   888    888                        888                       88888b.d88888                        888     888               888                       888             888                                         
        888Y88888P888  8888b.   .d8888b 8888888888  8888b.  888  888  888 888  888                  888Y88888P888  8888b.   .d8888b      888     888 .d8888b       8888888  8888b.  .d8888b  888888          888  888d888 888  8888b.   .d88b.   .d88b.  
        888 Y888P 888     "88b d88P"    888    888     "88b 888  888  888 888 .88P                  888 Y888P 888     "88b d88P"         888     888 88K           888         "88b 88K      888             888  888P"   888     "88b d88P"88b d8P  Y8b 
        888  Y8P  888 .d888888 888      888    888 .d888888 888  888  888 888888K       888888      888  Y8P  888 .d888888 888           888     888 "Y8888b.      888     .d888888 "Y8888b. 888             888  888     888 .d888888 888  888 88888888 
        888   "   888 888  888 Y88b.    888    888 888  888 Y88b 888 d88P 888 "88b                  888   "   888 888  888 Y88b.         Y88b. .d88P      X88      888     888  888      X88 Y88b.           888  888     888 888  888 Y88b 888 Y8b.     
        888       888 "Y888888  "Y8888P 888    888 "Y888888  "Y8888888P"  888  888                  888       888 "Y888888  "Y8888P       "Y88888P"   88888P'      888     "Y888888  88888P'  "Y888          888  888     888 "Y888888  "Y88888  "Y8888  
                                                                                                                                                                                                                                            888          
                                                                                                                                                                                                                                    Y8b d88P          
                                                                                                                                                                                                                                        "Y88P"
EOF
    }