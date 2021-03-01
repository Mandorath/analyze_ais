"""Logging handling for python scripts."""

import logging
import logging.handlers
import colorlog


def init_log():
    """Create the log handler."""
    r_log = logging.getLogger()
    r_log.setLevel(logging.NOTSET)
    handle_console(r_log)

    return r_log


def handle_console(log):
    """Handle Console logging."""
    hndlr = logging.StreamHandler()
    hndlr.setLevel(logging.INFO)
    frm = logging.Formatter('%(message)s')
    hndlr.setFormatter(frm)


def handle_log(log, file):
    """Handle log file."""
    hndlr = logging.handlers.WatchedFileHandler(file)
    hndlr.setLevel(logging.DEBUG)
    frm = '%(asctime)s [%(process)d]: %(log_color)s%(bold)s%(levelname)-8s%(reset)s %(message)s'
    frmter = colorlog.ColoredFormatter(frm, '%Y-%m-%d %H:%M:%S')
    hndlr.setFormatter(frmter)

    log.addHandler(hndlr)


def set_log_level(log, lvl):
    """Set log level."""
    for hndlr in log.handlers:
        if type(hndlr) is logging.StreamHandler:
            hndlr.setLevel(lvl)
