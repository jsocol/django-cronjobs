import sys
import logging
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand

import cronjobs

log = logging.getLogger('cron')


class Command(BaseCommand):
    help = 'Run a script, often a cronjob'
    args = '[name args...]'
    option_list = BaseCommand.option_list + tuple(
        [make_option('--%s' % rate,
                     action='store_true',
                     dest=rate,
                     default=False,
                     help='Run the %s cron jobs.' % rate)
         for rate in cronjobs.registered])

    def handle(self, *args, **opts):
        # Load up all the cron scripts.
        for app in settings.INSTALLED_APPS:
            try:
                __import__('%s.cron' % app)
            except ImportError:
                pass

        for rate in cronjobs.registered:
            ran = False
            if opts[rate]:
                ran = True
                log.info('Starting %s jobs.' % rate)
                for f in cronjobs.registered[rate]:
                    log.info('Starting job %s.' % f)
                    cronjobs.registered[rate][f](*args)
                    log.info('Finished job %s.' % f)
                log.info('Finished %s jobs.' % rate)

            if ran:
                sys.exit(0)


        registered = [f for freq in cronjobs.registered for
                      f in cronjobs.registered[freq]]

        if not args:
            log.error("Cron called but doesn't know what to do.")
            print 'Try one of these:\n%s' % '\n'.join(sorted(registered))
            print 'Or an option like --weekly, --daily, --hourly'
            sys.exit(1)

        script, args = args[0], args[1:]
        if script not in registered:
            log.error("Cron called with unrecognized command: %s %s" % (script, args))
            print 'Unrecognized name: %s' % script
            sys.exit(1)

        log.info("Beginning job: %s %s" % (script, args))
        registered[script](*args)
        log.info("Ending job: %s %s" % (script, args))
