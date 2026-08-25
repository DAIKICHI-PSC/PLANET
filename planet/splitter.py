from .vbcommon import vbnarrow


class NC:
    __slots__ = ('command', 'value')

    def __init__(self, command=None, value=None):
        self.command = command or ['']
        self.value = value or ['']


def splitter(text_contents):
    if not text_contents:
        return None
    text_contents = text_contents.replace('\r\n', '\n').replace('\n', '\r\n')
    text_contents = text_contents.replace(';', '')
    if text_contents == '':
        return None
    if text_contents[-1] != '\n':
        text_contents += '\r\n'
    text_contents = text_contents.replace('\r\n', ';\r\n')
    text_contents = text_contents.upper()
    text_contents = vbnarrow(text_contents)

    contents_lines = text_contents.split('\r\n')
    nc_lines = []

    for individual_line in contents_lines:
        commands = ['']
        values = ['']
        current_position = 0
        command_number_counter = 0

        n = len(individual_line)
        while True:
            if current_position >= n:
                break
            nc_command = individual_line[current_position]
            if nc_command == ';':
                break
            elif nc_command == '':
                break
            elif ('A' <= nc_command <= 'Z') or nc_command in ',#(/':
                nc_command_value = ''
                if nc_command == '(':
                    current_position += 1
                    while True:
                        if current_position >= n:
                            break
                        tmp_str = individual_line[current_position]
                        if tmp_str == ';':
                            current_position -= 1
                            break
                        elif tmp_str == ')':
                            nc_command_value += tmp_str
                            break
                        nc_command_value += tmp_str
                        current_position += 1
                else:
                    while True:
                        current_position += 1
                        if current_position >= n:
                            break
                        tmp_str = individual_line[current_position]
                        if ('A' <= tmp_str <= 'Z') or tmp_str == ',' or tmp_str == '(' or nc_command == '/' or tmp_str == ';':
                            current_position -= 1
                            break
                        elif tmp_str == ' ':
                            break
                        nc_command_value += tmp_str

                command_number_counter += 1
                commands.append('')
                values.append('')
                commands[command_number_counter - 1] = nc_command
                values[command_number_counter - 1] = nc_command_value
            else:
                pass

            current_position += 1

        nc_lines.append(NC(commands, values))

    return nc_lines
