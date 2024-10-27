from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
from datetime import datetime
from builtins import print as builtins_print

from string import Formatter as _PyFormatter
import rich

@dataclass
class LogSeverityElementOptions:
    name: str
    color: str

    def __str__(self):
        return f"{self.name}"


class LogSeverity(Enum):
    DEBUG = LogSeverityElementOptions("DEBUG", "blue")
    INFO = LogSeverityElementOptions("INFO", "green")
    WARNING = LogSeverityElementOptions("WARNING", "yellow")
    ERROR = LogSeverityElementOptions("ERROR", "red")
    CRITICAL = LogSeverityElementOptions("CRITICAL", "bold red")


G_MSG_FMT: str = "{time} [{level}] {message}"


@dataclass
class LogMessage:
    class LoggerKwargsFormatter(_PyFormatter):
        def get_value(self, key, args, kwds):
            if isinstance(key, str):
                return kwds.get(key, f"{{{key}}}")  # Return placeholder if key is missing
            return super().get_value(key, args, kwds)

    formatter = LoggerKwargsFormatter()

    @staticmethod
    def _make_msg(msg, *args, **kwargs) -> str:
        """
        Format a message string with arguments
        :param msg: The message to format
        :param args: The arguments to format the message with
        :param kwargs: The keyword arguments to format the message with
        :return: The formatted message
        """
        # Format with keyword arguments if provided

        if args:
            try:
                msg = msg % args
            except TypeError:
                raise ValueError("Mismatch between positional placeholders and args")

        msg = LogMessage.formatter.format(msg, **kwargs)

        return msg

    def __init__(self, message: str,
                 severity: LogSeverity,
                 date_time: datetime = datetime.now(),
                 *args, **kwargs):
        """
        Initialize a new log message
        :param message: The message to log
        :param severity: The severity level of the message
        :param date_time: The time the message was logged
        """
        self.message: str = message
        self.log_severity: LogSeverity = severity
        self.time: datetime = date_time

        # copy the args and kwargs
        self.args = args
        self.kwargs = kwargs.copy()
        self.formatted_msg = self._make_msg(message, *args, **kwargs)

    def __str__(self):
        """
        Format the log message as a string
        :return:  The formatted log message
        """
        return G_MSG_FMT.format(
            time=self.time.strftime("%Y-%m-%d %H:%M:%S"), level=self.log_severity.value.name, message=self.formatted_msg)


class Logger:
    def __init__(self, name: str):
        self.name = name
        self.messages: Dict[LogSeverity, List[LogMessage]] = {
            LogSeverity.INFO: [],
            LogSeverity.WARNING: [],
            LogSeverity.ERROR: [],
            LogSeverity.CRITICAL: []
        }
        self.print_log_to_builtins: bool = False

    @property
    def all_messages(self) -> List[LogMessage]:
        """
        Get all messages
        :return: A list of all messages
        """
        return [msg for msgs in self.messages.values() for msg in msgs]

    @property
    def all_logs(self) -> List[str]:
        """
        Get all logs
        :return: A list of all logs
        """
        return [str(msg) for msg in self.all_messages]

    def log(self, msg: str, severity: LogSeverity, *args, **kwargs):  # known special case of debug
        """
        Log a message with a given severity level
        :param msg: The message to log
        :param severity: The severity level of the message
        :return: None
        """
        log_message = LogMessage(message=msg, severity=severity, *args, **kwargs)
        self.messages[severity].append(log_message)

        if self.print_log_to_builtins:
            builtins_print(log_message)

    def info(self, msg: str, *args, **kwargs):  # known special case of info
        """
        Log 'msg % args' with severity 'INFO'.
        :param msg:
        :param args:
        :param kwargs:
        :return:
        """
        self.log(msg, LogSeverity.INFO, *args, **kwargs)

    def debug(self, msg: str, *args, **kwargs):  # known special case of debug
        """
        Log 'msg % args' with severity 'DEBUG'.
        :param msg: the message to log
        :param args: the arguments to format the message with
        :param kwargs: additional keyword arguments
        :return: None
        """
        self.log(msg, LogSeverity.DEBUG, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):  # known special case of warning
        """
        Log 'msg % args' with severity 'WARNING'.
        :param msg: the message to log
        :param args: the arguments to format the message with
        :param kwargs: additional keyword arguments
        :return: None
        """
        self.log(msg, LogSeverity.WARNING, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs):  # known special case of error
        """
        Log 'msg % args' with severity 'ERROR'.
        :param msg:  the message to log
        :param args:  the arguments to format the message with
        :param kwargs:  additional keyword arguments
        :return:   None
        """
        self.log(msg, LogSeverity.ERROR, *args, **kwargs)


"""
Global logger
"""
G_LOGGER = Logger("Global Logger")


def g_info(msg: str, *args, **kwargs):  # known special case of info
    """
    Log 'msg % args' to the global logger with severity 'INFO'.
    :param msg: the message to log
    :param args: the arguments to format the message with
    :param kwargs: additional keyword arguments
    """
    global G_LOGGER
    G_LOGGER.info(msg, *args, **kwargs)


def print(*args, sep: str= ' ', end: str = '\n', file: str = None) \
        -> None:  # known special case of print
    """
    Print a message to the global logger
    :param args: The arguments to print
    :param sep: The separator to use between arguments
    :param end: The end character to use
    :param file: The file to print to
    :return: None
    """
    msg: str = sep.join(map(str, args)) + end
    global G_LOGGER
    G_LOGGER.info(msg)

    if file is not None:
        G_LOGGER.warning("File argument is not implemented in the uecli print function. Ignoring.")
