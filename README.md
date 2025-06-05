# calcylate-rate

Проект по расчёту заработной платы сотрудников.

**Технологический стек**

- Python
- Библиотека для тестирования Pytest

**Пример использования**

Пример файла

```bash

id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
3,carol@example.com,Carol Williams,Design,170,60
```

Команды запуска

- одиночный файл

  ```bash
  py main.py calc data1.csv
  ```

- несколько файлов

  ```bash
  py main.py calc data1.csv data2.csv
  ```

- вывод отчёта в файл с указанием имени
  ```bash
  py main.py calc data1.csv --report MyFile
  ```
