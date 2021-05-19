# LOGGING DRAFT

Run with `python -m src`. No environment is needed.

Logging here is configured to do the following:

1. Logs from the last run are saved in `logs` folder. Whereas accumulated historical logs are in `history_logs` folder.
2. Main logs are logged into `src.log` file, and logs with detailed information from auxiliary modules can be found in the correcponding `src.{module_name}.log` files. Both, main and detailed logs are streamed into `stdout`.


Followed the exampled from here https://docs.python.org/3/howto/logging-cookbook.html#using-logging-in-multiple-modules.   

Минусы этого решения:
1. В консоль печатается лог "NEW RUN" во время импорта вспомогательных модулей.
2. В файлах `.log` вспомогательных модулей не всегда на будет понятно, из какого места была вызвана функция библиотеки.