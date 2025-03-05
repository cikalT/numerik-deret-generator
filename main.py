import random
import streamlit as st


option = st.selectbox(
    "Pilih Deret",
    ["Fibonacci", "Larik", "Bertingkat", "Berpola Berulang"],
    index=None,
    placeholder="Select contact method...",
)

spacer = ',    '
question_spacer = ',&nbsp;&nbsp;&nbsp;'

def convert_to_float(value):
    try:
        return round(float(value), 1)
    except ValueError:
        return None


def flatening(list):
    return [int(num) if num.is_integer() else num for num in list]


def smart_round_list(lst):
    return [round(num, 0) if isinstance(num, float) and num.is_integer() else round(num, 1) if isinstance(num, float) else num for num in lst]


def render(questions, answers):
    def randomize_list(list):
        rand = [num + random.choice([-2, -1, 0, 1, 2]) for num in list]
        return smart_round_list(rand)
    
    st.subheader(f'{question_spacer.join(map(str, smart_round_list(questions)))}, ...')
    st.write('Opsi:')
    first_line = st.columns(2)
    first_line[0].text_input(f'', value=f'a. {spacer.join(map(str, randomize_list(answers)))}', disabled=True, key='option_a')
    first_line[1].text_input(f'', value=f'b. {spacer.join(map(str, randomize_list(answers)))}', disabled=True, key='option_b')
    seconnd_line = st.columns(2)
    seconnd_line[0].text_input(f'', value=f'c. {spacer.join(map(str, randomize_list(answers)))}', disabled=True, key='option_c')
    seconnd_line[1].text_input(f'', value=f'd. {spacer.join(map(str, randomize_list(answers)))}', disabled=True, key='option_d')
    true_answer = st.columns(2)
    true_answer[0].subheader(f'{question_spacer.join(map(str, smart_round_list(answers)))}')


def render_larik(questions, answers, schemes):
    def randomize_list_larik():
        answers_options = []
        for index, s in enumerate(schemes):
            if s.startswith("+"):
                base_s = int(s[1:])
                p_a = answers[index] + random.choice(
                    [-base_s, 0, base_s, 1]
                )
            if s.startswith("-"):
                base_s = -(int(s[1:]))
                p_a = answers[index] - random.choice(
                    [-base_s, 0, base_s, 1]
                )
            if s.startswith("*"):
                base_s = int(s[1:])
                p_a = answers[index] * random.choice(
                    [-base_s, 1, base_s, 2]
                )
            answers_options.append(p_a)
        return smart_round_list(answers_options)
    
    st.subheader(f'{question_spacer.join(map(str, smart_round_list(questions)))}, ...')
    st.write('Opsi:')
    first_line = st.columns(2)
    first_line[0].text_input(f'', value=f'a. {spacer.join(map(str, randomize_list_larik()))}', disabled=True, key='option_a')
    first_line[1].text_input(f'', value=f'b. {spacer.join(map(str, randomize_list_larik()))}', disabled=True, key='option_b')
    seconnd_line = st.columns(2)
    seconnd_line[0].text_input(f'', value=f'c. {spacer.join(map(str, randomize_list_larik()))}', disabled=True, key='option_c')
    seconnd_line[1].text_input(f'', value=f'd. {spacer.join(map(str, randomize_list_larik()))}', disabled=True, key='option_d')
    true_answer = st.columns(2)
    true_answer[0].subheader(f'{question_spacer.join(map(str, smart_round_list(answers)))}')


if option == "Fibonacci":
    def generate_fibonacci(first_value, second_value, num_terms, end_count):
        fibonacci_sequence = [first_value, second_value]
        
        for i in range(2, num_terms + end_count):
            next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_value)
        
        return fibonacci_sequence[:num_terms], fibonacci_sequence[-end_count:]

    st.subheader('Fibonacci')
    col1 = st.columns(2)
    first_value = col1[0].text_input('Angka Pertama')
    second_value = col1[1].text_input('Angka Kedua')
    col2 = st.columns(2)
    num_terms = col2[0].text_input('Jumlah Suku')
    end_count = col2[1].text_input('Jumlah Suku Jawaban')

    if st.button('Buat Fibonnaci'):
        a, b = generate_fibonacci(convert_to_float(first_value), convert_to_float(second_value), int(num_terms), int(end_count))
        questions = flatening(a)
        answers = flatening(b)
        render(questions, answers)
        
        
if option == "Larik":
    st.subheader('Larik')
    lar = st.columns(3)
    line_numbers = lar[0].text_input('Jumlah Larik')
    scheme_number = lar[1].text_input('Jumlah Deret per Larik')
    if line_numbers.isdigit() and scheme_number.isdigit():
        lar[2].text_input('Jumlah Suku', value=f'{int(line_numbers) * int(scheme_number)}', disabled=True)
    answer_lengths = st.text_input('Jumlah Suku Jawaban', value=line_numbers, disabled=True)
    if line_numbers.isdigit() and scheme_number.isdigit() and answer_lengths.isdigit():
        pattern_count = int(line_numbers)
        number_count = int(scheme_number)
        answer_length = int(answer_lengths)
        
        schemes = []
        first_values = []
        results = []
        final_list = []
        
        for i in range(pattern_count):
            larik = st.columns(2)
            value_first = larik[0].text_input(f'Angka Pertama {i+1}')
            first_values.append(value_first)
            value_scheme = larik[1].text_input(f'Pola Larik {i+1} (+5 atau -3 atau *2)')
            schemes.append(value_scheme)
            
        
        if st.button('Buat Larik'):
            for i in range(pattern_count):
                first_value = convert_to_float(first_values[i])
                scheme = schemes[i]
                results.append(first_value)
            
            for i in range(pattern_count):
                if schemes[i].startswith("+"):
                    results.append(convert_to_float(first_values[i]) + int(schemes[i][1:]))
                if schemes[i].startswith("-"):
                    results.append(convert_to_float(first_values[i]) - int(schemes[i][1:]))
                if schemes[i].startswith("*"):
                    results.append(convert_to_float(first_values[i]) * int(schemes[i][1:]))
            final_list.extend(results)
            
            appended_list = []
            for j in range(number_count - 1):
                for i in range(len(schemes)):
                    if schemes[i].startswith("+"):
                        appended_list.append(
                            convert_to_float(results[-(len(schemes) - i)]) + int(schemes[i][1:])
                        )
                    if schemes[i].startswith("-"):
                        appended_list.append(
                            convert_to_float(results[-(len(schemes) - i)]) - int(schemes[i][1:])
                        )
                    if schemes[i].startswith("*"):
                        appended_list.append(
                            convert_to_float(results[-(len(schemes) - i)]) * int(schemes[i][1:])
                        )
                results.extend(appended_list)
        
            final_list.extend(appended_list)
            jawaban = final_list[-answer_length:]
            del final_list[-answer_length:]
            
            questions = flatening(final_list)
            answers = flatening(jawaban)
            render_larik(questions, answers, schemes)


if option == "Bertingkat":
    st.subheader('Bertingkat')
    def generate_sequence(a, b, c, d, e):
        questions = []
        answers = []
        
        next_value = a+b
        for i in range(d+1):
            if i == 0:
                questions.append(a)
            elif i == 1:
                questions.append(next_value)
            elif i == 2:
                next_value = next_value + b+c
                questions.append(next_value)
            else:
                next_value = questions[-1] + (b + ((i-1)*c))
                questions.append(next_value)
        
        answers.append(questions[-1])
        for i in range(e):
            next_index = d + 1 + i
            next_value = answers[-1] + (b + ((next_index-1)*c))
            answers.append(next_value)
            
        answers.pop(0)
        return questions, answers

    col1 = st.columns(3)
    a = col1[0].text_input('Angka Pertama')
    b = col1[1].text_input('Beda 1')
    c = col1[2].text_input('Beda 2')
    col2 = st.columns(2)
    d = col2[0].text_input('Jumlah Suku')
    e = col2[1].text_input('Jumlah Suku Jawaban')
    if st.button('Buat Bertingkat'):
        questions, answers = generate_sequence(convert_to_float(a), convert_to_float(b), convert_to_float(c), int(d), int(e))
        questions = flatening(questions)
        answers = flatening(answers)
        
        render(questions, answers)


if option == "Berpola Berulang":
    col1 = st.columns(2)
    a = col1[0].text_input('Jumlah Pola')
    b = col1[1].text_input('Jumlah Kelipatan Pola Suku')
    col2 = st.columns(2)
    c = col2[0].text_input('Jumlah Total Suku', value=f'{int(a)*int(b) + 1}', disabled=True)
    d = col2[1].text_input('Jumlah Suku Jawaban')
    
    if a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit():
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = st.text_input('Angka Pertama')
        e = convert_to_float(e)
        
        questions = []
        questions.append(e)
        
        schemes = []
        for i in range(a):
            value_scheme = st.text_input(f'Pola Angka {i+1} (+5 atau -3 atau *2)')
            schemes.append(value_scheme)
        
        if st.button('Buat Berpola Berhitung'):
            for i in range(b):
                for idx, sch in enumerate(schemes):
                    last_number = questions[-1]
                    if sch.startswith("+"):
                        rb = last_number + float(sch[1:])
                    if sch.startswith("-"):
                        rb = last_number - float(sch[1:])
                    if sch.startswith("*"):
                        rb = last_number * float(sch[1:])
                    questions.append(rb)
            
            answers = []
            answers.append(questions[-1])
            for i in range(d):
                for idx, sch in enumerate(schemes):
                    last_number = answers[-1]
                    if sch.startswith("+"):
                        rb = last_number + float(sch[1:])
                    if sch.startswith("-"):
                        rb = last_number - float(sch[1:])
                    if sch.startswith("*"):
                        rb = last_number * float(sch[1:])
                    answers.append(rb)
            
            del answers[0]
            del answers[-d:]
            
            questions = flatening(questions)
            answers = flatening(answers)
            render(questions, answers)