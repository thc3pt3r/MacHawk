#!/bin/bash

# Programa para realizar un triage de Incident response en equipo MacOs

#funciones
mostrar_ayuda() {
    clear
    echo " === MacHawk - Triage de equipos MacOs  by Deloitte ARG CIR TEAM === "
    echo "Uso: macHack.sh [opción]"
    echo "Opciones:"
    echo "  -h, --help          Show this help."
    echo "  -c, --complete      Run a complete IR Triage collection."
    echo "  -p, --partial       Run a partial IR Triage collection."
    echo "  -q, --quit          Exit the program."
    echo " ============================================================ "
    
}
run_complete_triage(){
    clear
    echo "Ejecutando Triage Completo"
    echo "============================================================"
    echo "Creating the Triage Folder"
    source ./hawks/general_hawk.sh
    # Get the current datetime in a specific format (e.g., YYYYMMDD_HHMMSS)
    datetime=$(date +'%Y%m%d_%H%M%S')
    parent_dir="Triage_Collection_$datetime"
    create_output_dir $parent_dir
    echo "============================================================"
    echo "Excecutando Triage de Logs"
    source ./hawks/log_hawk.sh
    run_Logs_triage $parent_dir
    echo "============================================================"
    echo "Compresing Output Directory"
    compress_Triage_Output $parent_dir
    
    exit 0
    
}
run_partial_triage(){
    clear
    echo "Ejecutando Triage Completo"
    exit 0
    
}

#loop principal
if [ "$1" == "-h" ] || [ "$1" == "--help"]; then
    mostrar_ayuda
    exit 0
fi
while true; do
    case "$1" in
        -com|--complete)
            run_complete_triage
            ;;
        -p|--partial)
            run_partial_triage
            ;;
        -q|--quit)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            mostrar_ayuda
            exit 1
            ;;
    esac
done