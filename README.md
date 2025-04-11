# Dlogs

A simple CLI utility for collecting statistics from your log
s

![PyPI - Version](https://img.shields.io/pypi/v/dlogs)


![DLogs help](https://raw.githubusercontent.com/Quirkink/dlogs/main/assets/help.gif)

## Install

```bash
pip install dlogs
```

## Using

It works from the command line

Analyze a single log file:
```bash
dlogs log/log_file.log
```

Analyze all logs in a directory:
```bash
dlogs logs/
```

Analyze multiple log files:
```bash
dlogs log/log_file.log log/log_file2.log
```

Analyze logs with specific handler:
```bash
dlogs log/ --report django
```

Analyze logs with specific file extension:
```bash
dlogs log/ --report django --suffix .log
```

Analyze logs with debug output:
```bash
dlogs log/ --report django --debug
```

Available options:
- `--report {django}` - specify the report type
- `--suffix SUFFIX` - filter files by extension
- `--debug` - enable debug output

