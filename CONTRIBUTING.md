# Contributing

## Быстрый старт

```bash
git clone https://github.com/kozandlov/avito-python-sdk.git
cd avito-python-sdk
pip install -e .[dev]
```

## Локальная проверка

```bash
pytest -q
python -m build
```

## Стандарт изменений

- Делайте небольшие PR с четким scope.
- Обновляйте README/USAGE, если меняется публичное поведение.
- Для багфиксов добавляйте тест или сценарий воспроизведения.

## Коммиты

Рекомендуемый формат:

- `feat: ...`
- `fix: ...`
- `docs: ...`
- `ci: ...`
- `chore: ...`
