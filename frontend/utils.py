
def generate_numbers():
    return list(range(1, 11))

def render_table(numbers):
    return '<table>' + ''.join([f'<tr><td>{i}</td></tr>' for i in numbers]) + '</table>'
