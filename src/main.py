import streamlit as st

def formatear_numero(numero):
    return "{:,.2f}".format(numero).replace(",", "X").replace(".", ",").replace("X", ".")



def calcular_impacto_anual(carne, pollo, cerdo):
    # Supongamos que una persona come 52 semanas al año
    semanas_al_año = 52

    # Factores de conversión de gramos a kilogramos y emisiones de CO2 por kilogramo para cada tipo de carne
    factor_conversion = 0.001
    emisiones_carne = 25  # ejemplo de emisiones de CO2 por kilogramo de carne en general
    emisiones_pollo = 6.9
    emisiones_cerdo = 12.1

    # Calcular emisiones anuales
    emisiones_totales = (carne * emisiones_carne + pollo * emisiones_pollo + cerdo * emisiones_cerdo) * semanas_al_año /1000

    return emisiones_totales
def kilos_totales(carne, pollo, cerdo):
    # Supongamos que una persona come 52 semanas al año
    semanas_al_año = 52


    emisiones_carne = 25.2  # ejemplo de emisiones de CO2 por kilogramo de carne en general
    emisiones_pollo = 6.9
    emisiones_cerdo = 12.1

    # Calcular emisiones anuales
    kilos_totales = (carne  + pollo  + cerdo ) * semanas_al_año

    return kilos_totales/1000

def calcular_animales_anuales(vaca, pollo, cerdo):
    # Factores de conversión de gramos a animales
    factor_conversion_vaca = 200000  # ejemplo de cantidad de gramos de cerdo por vaca
    factor_conversion_pollo = 1500  # ejemplo de cantidad de gramos de pollo por pollo
    factor_conversion_cerdo = 50000  # ejemplo de cantidad de gramos de cerdo por cerdo

    semanas = 52

    # Calcular cantidad anual de animales consumidos
    vacas_totales = formatear_numero(vaca * semanas / factor_conversion_vaca)
    pollos_totales = formatear_numero(pollo * semanas / factor_conversion_pollo)
    cerdos_totales = formatear_numero(cerdo * semanas / factor_conversion_cerdo)

    return vacas_totales, pollos_totales, cerdos_totales

def main():
    st.title("Calculadora de Impacto de CO2 y Consumo de Animales por Carne")
    
    # Widgets para ingresar la cantidad de carne, pollo y cerdo consumidos a la semana
    carne_semana = st.number_input("Gramos de vaca a la semana:", min_value=0, max_value=3500, step=50, value=0)
    pollo_semana = st.number_input("Gramos de pollo a la semana:", min_value=0, max_value=3500, step=50, value=0)
    cerdo_semana = st.number_input("Gramos de cerdo a la semana:", min_value=0, max_value=3500, step=50, value=0)

    # Botón para calcular y mostrar el impacto anual y el consumo de animales
    if st.button("Submit"):
        impacto_anual = formatear_numero(calcular_impacto_anual(carne_semana, pollo_semana, cerdo_semana))
        vacas_totales, pollos_totales, cerdos_totales = calcular_animales_anuales(carne_semana, pollo_semana, cerdo_semana)
        kilos = formatear_numero(kilos_totales(carne_semana, pollo_semana, cerdo_semana))

        st.success(f"Tu impacto anual estimado de CO2 es de aproximadamente {impacto_anual} Toneladas.")
        st.info(f"Consumo anual estimado: {vacas_totales} vacas, {pollos_totales} pollos, {cerdos_totales} cerdos.")
        st.info(f"Consumo anual estimado: {kilos} kg de carne")
if __name__ == "__main__":
    main()
