import random
import streamlit as st


def generate_four_arithmetic():
    while True:
        numbers = [random.randint(-40, 40) for _ in range(4)]
        operators = random.choices(['+', '-', '*'], k=3)
        
        expression = " ".join(
            f"({num})" if isinstance(num, int) and num < 0 else str(num) 
            for pair in zip(numbers, operators + [""])
            for num in pair if num != ""
        )
        
        try:
            result = eval(expression)
            return expression, result
        except ZeroDivisionError:
            continue


def generate_four_arithmetic_with_same_result(expected_result):
    while True:
        expression, result = generate_four_arithmetic()
        if result == expected_result:
            return expression, result


def generate_four_arithmetic_with_less_result(expected_result):
    while True:
        expression, result = generate_four_arithmetic()
        if expected_result - 10 <= result < expected_result:
            return expression, result


def generate_four_arithmetic_with_more_result(expected_result):
    while True:
        expression, result = generate_four_arithmetic()
        if expected_result < result <= expected_result + 10:
            return expression, result
        
    
def generate_four_arithmetic_with_double_result(expected_result):
    while True:
        expression, result = generate_four_arithmetic()
        if result == expected_result * 2:
            return expression, result


def counting_main():
    counting_types = [
        'Aritmatika 3 suku',
        'Aritmatika 4 suku',
        'Desimal',
        'Persentase',
    ]
    comparison_types = [
        '=',
        '<',
        '>'
    ]
    table_a = st.columns(3)
    table_a[0].selectbox('', ['X', '2X'], disabled=False, key='x_position')
    diferentiation = table_a[1].selectbox('', comparison_types, key='diferentiation')
    table_a[2].selectbox('', ['Y', '2Y'], disabled=False, key='y_position')
    
    table_b = st.columns(2)
    
    l_container = table_b[0].container()
    r_container = table_b[1].container()
    
    l_container.selectbox('Kolom x', counting_types)
    r_container.selectbox('Kolom y', counting_types)
    
    l_expr, l_res = generate_four_arithmetic()
    l_container.success(f'{l_expr}')
    l_container.warning(f'Hasil: {round(l_res, 2)}')
    
    if diferentiation == '=':
        r_expr, r_res = generate_four_arithmetic_with_same_result(l_res)
    if diferentiation == '<':
        r_expr, r_res = generate_four_arithmetic_with_more_result(l_res)
    if diferentiation == '>':
        r_expr, r_res = generate_four_arithmetic_with_less_result(l_res)
    
    r_container.success(f'{r_expr}')
    r_container.warning(f'Hasil: {round(r_res, 2)}')



    