import re

import pytest


def test_link_connection(
        deploy_info_file_info, deploy_info_file_content, link_key
        ):
    _, relative_path = deploy_info_file_info
    assert link_key in deploy_info_file_content, (
        f'Убедитесь, что файл `{relative_path}` содержит ключ `{link_key}`.'
    )
    link: str = deploy_info_file_content[link_key]
    assert link.startswith('https'), (
        'Убедитесь, что для проектов настроено шифрование. Ссылка под ключом '
        f'`{link_key}` в файле `{relative_path}` должна начинаться с '
        'префикса `https:`.'
    )
    link_pattern = re.compile(
        r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.'
        r'[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)&'
    )
    assert link_pattern.match(link), (
        f'Убедитесь, что ключ `{link_key}` в файле `{relative_path}` содержит '
        'корректную ссылку.'
    )


if __name__ == '__main__':
    pytest.main()
