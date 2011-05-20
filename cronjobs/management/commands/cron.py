import atexit
import logging
import os
import sys
import tempfile

from django.conf import settings
from django.core.management.base import BaseCommand

import cronjobs


log = logging.getLogger('cron')

LOCK = getattr(settings, 'CRONJOB_LOCK_PREFIX', 'lock')


class Command(BaseCommand):
    help = 'Run a script, often a cronjob'
    args = '[name args...]'

    def handle(self, *args, **opts):
        # Load up all the cron scripts.
        for app in settings.INSTALLED_APPS:
            try:
                __import__('%s.cron' % app)
            except ImportError:
                pass

        registered = cronjobs.registered

        if not args:
            log.error("Cron called but doesn't know what to do.")
            print 'Try one of these:\n%s' % '\n'.join(sorted(registered))
            sys.exit(1)

        script, args = args[0], args[1:]
        if script not in registered:
            log.error("Cron called with unrecognized command: %s %s" %
                      (script, args))
            print 'Unrecognized name: %s' % script
            sys.exit(1)

        # Acquire lock if needed.
        if script in cronjobs.registered_lock:
            filename = os.path.join(tempfile.gettempdir(),
                                    'django_cron.%s.%s' % (LOCK, script))
            try:
                fd = os.open(filename, os.O_CREAT|os.O_EXCL)

                def register():
                    os.close(fd)
                    os.remove(filename)

                atexit.register(register)
            except OSError:
                msg = ("Script run multiple times. If this isn't true, delete "
                       "`%s`." % filename)
                log.error(msg)
                sys.stderr.write(msg + "\n")
                sys.exit(1)

        log.info("Beginning job: %s %s" % (script, args))
        registered[script](*args)
        log.info("Ending job: %s %s" % (script, args))
