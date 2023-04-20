# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2023/2/17 10:41

import sys
import os
import logging
import logging.handlers
from colorlog import ColoredFormatter

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

from backend.config import LOG_FILE, LOG_LEVEL


def load_logfile_level():
    """
    Return the configured logging level, or throw an exception
    """
    if 'XiaoYa_MODE_TEST' in os.environ:
        return logging.DEBUG
    elif 'XiaoYa_LOGFILE_LEVEL' in os.environ:
        level = os.environ['XiaoYa_LOGFILE_LEVEL'].strip().lower()
        if level == 'debug':
            return logging.DEBUG
        elif level == 'info':
            return logging.INFO
        elif level == 'warning':
            return logging.WARNING
        elif level == 'error':
            return logging.ERROR
        elif level == 'critical':
            return logging.CRITICAL
        else:
            raise ValueError(
                'Invalid value "{}" for logfile_level. '
                'Set XiaoYa_LOGFILE_LEVEL to fix your configuration.', format(level))
    else:
        return logging.INFO


class JobIdLogger(logging.Logger):
    def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None):
        """
               Customizing it to set a default value for extra['job_id']
        """
        rv = logging.LogRecord(name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None)
        if extra is not None:
            for key in extra:
                if (key in ["message", "asctime"]) or (key in rv.__dict__):
                    raise KeyError("Attempt to overwrite %r in LogRecord" % key)
                rv.__dict__[key] = extra[key]
        if 'job_id' not in rv.__dict__:
            rv.__dict__['job_id'] = ''
        return rv


class JobIdLoggerAdapter(logging.LoggerAdapter):
    """
    Accepts an optional keyword argument: 'job_id'

    You can use this in 2 ways:
        1. On class initialization
            adapter = JobIdLoggerAdapter(logger, {'job_id': job_id})
            adapter.debug(msg)
        2. On method invocation
            adapter = JobIdLoggerAdapter(logger, {})
            adapter.debug(msg, job_id=id)
    """

    def process(self, msg, kwargs):
        if 'job_id' in kwargs:
            if 'extra' not in kwargs:
                kwargs['extra'] = {}
            kwargs['extra']['job_id'] = ' [%s]' % kwargs['job_id']
            del kwargs['job_id']
        elif 'job_id' in self.extra:
            if 'extra' not in kwargs:
                kwargs['extra'] = {}
            kwargs['extra']['job_id'] = ' [%s]' % self.extra['job_id']
        return msg, kwargs


def setup_logging():
    # Set custom logger
    logging.setLoggerClass(JobIdLogger)
    # formatter = logging.formatter()
    if "TMP_ENV" in os.environ and os.environ["TMP_ENV"] == "dev":
        log_color_set = "[%(asctime)s]%(job_id)s - %(log_color)s%(levelname).4s%(reset)s - %(message_log_color)s[%(name)s:%(lineno)d] [%(module)s %(lineno)d] - %(message_log_color)s%(message)s"
    else:
        log_color_set = "[%(asctime)s]%(job_id)s - %(levelname).4s%(reset)s - [%(name)s:%(lineno)d][pid:%(process)d]%(reset)s - %(message)s"

    formatter = ColoredFormatter(
        log_color_set,
        datefmt=DATE_FORMAT,
        # reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        },
        secondary_log_colors={
            'message': {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red',
            },
        },
        style='%',
    )

    main_logger = logging.getLogger('XiaoYa')
    main_logger.setLevel(logging.DEBUG)
    # Log to stdout
    stdoutHandler = logging.StreamHandler(sys.stdout)
    stdoutHandler.setFormatter(formatter)
    stdoutHandler.setLevel(logging.DEBUG)
    main_logger.addHandler(stdoutHandler)

    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.makedirs(os.path.dirname(LOG_FILE))

    logfile_filename = LOG_FILE
    logfile_level = LOG_LEVEL

    if logfile_filename is not None:
        webapp_logger = logging.getLogger('XiaoYa.webapp')
        webapp_logger.setLevel(logging.DEBUG)
        fileHandler = logging.handlers.RotatingFileHandler(
            logfile_filename,
            maxBytes=(1024 * 1024 * 10),  # 10 MB
            backupCount=10,
        )
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(logfile_level)
        webapp_logger.addHandler(fileHandler)
        return JobIdLoggerAdapter(webapp_logger, {})
    else:
        print('WARNING: log_file config option not found - no log file is being saved')
        return JobIdLoggerAdapter(main_logger, {})


logger = setup_logging()
