import os
import re


def tag_checking(path, tags):
    """
    Рекурсивно ищет все HTML файлы в указанной директории и проверяет наличие меток i18n в тегах.
    """
    for root, _dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                file_in_folder = os.path.join(root, file)
                with open(file_in_folder, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for line_number, line in enumerate(lines, start=1):
                        for tag in tags:
                            pattern = fr'<{tag}(?!.*i18n).*?>'
                            if re.search(pattern, line):
                                print(
                                    f'В файле {file_in_folder} на {line_number} строке содержится тег без метки i18n: '
                                    f'{line.strip()}'
                                )
                                break


if __name__ == "__main__":
    path = '/Users/anmalevich/Downloads/test-i18n'
    tags = ['p', 'button', 'h2', 'h']
    tag_checking(path, tags)

