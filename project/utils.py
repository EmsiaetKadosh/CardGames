import sys
import traceback


def throw(exception: Exception):
    traceback.print_exc()


def output(head: str, *args, sep=' ', end='\n', file=sys.stdout):
    print(head, sep='', end='', file=file)
    print(*args, sep=sep, end=end, file=file)


def debug(*args, sep=' ', end='\n') -> None:
    output('[IKUN] [DEBUG] ', *args, sep=sep, end=end)


def info(*args, sep=' ', end='\n') -> None:
    output('[IKUN] [INFO]  ', *args, sep=sep, end=end)


def warn(*args, sep=' ', end='\n') -> None:
    output('[IKUN] [WARN]  ', *args, sep=sep, end=end, file=sys.stderr)


def error(*args, sep=' ', end='\n') -> None:
    output('[IKUN] [ERROR] ', *args, sep=sep, end=end, file=sys.stderr)


def traceStack(e: Exception) -> None:
    """
    建议改为调用printException()
    :param e: 被抛出的错误
    """
    result = []
    last_file = None
    last_line = None
    last_name = None
    count = 0
    traces = traceback.extract_tb(e.__traceback__)
    result.append(f'  {traces[0].line}\n')
    for frame in traces:
        if last_file is None or last_file != frame.filename or last_line is None or last_line != frame.lineno or last_name is None or last_name != frame.name:
            if count > 3:
                count -= 3
                result.append(f'  [Previous line repeated {count} more time{"s" if count > 1 else ""}]\n')
            last_file = frame.filename
            last_line = frame.lineno
            last_name = frame.name
            count = 0
        count += 1
        if count > 3:
            continue
        row = [f'  @ {frame.name} @ {frame.filename}:{frame.lineno}']
        if frame.locals:
            for name, value in sorted(frame.locals.items()):
                row.append(f'    {name} = {value}')
        row.append('\n')
        result.append(''.join(row))
    if count > 3:
        count -= 3
        result.append(f'  [Previous line repeated {count} more time{"s" if count > 1 else ""}]\n')
    for line in result:
        print(line, file=sys.stderr, end='')


def printException(e: Exception) -> None:
    """
    抛出错误时调用
    :param e: 被抛出的错误
    """
    error(f'[{type(e).__name__}] {str(e)}!! when running code:')
    traceStack(e)
