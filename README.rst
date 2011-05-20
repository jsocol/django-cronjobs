===============
Django Cronjobs
===============

django-cronjobs is a simple Django app that runs registered cron jobs via a
management command.


Installing
==========

To install django-cronjobs, first install via pip or easy_install, then just
add ``cronjobs`` to your ``INSTALLED_APPS``.


Registering a cron job
======================

django-cronjobs includes a decorator to register a cronjob, and discovers
registered jobs in the module ``<appname>.cron``.

For example::

    # myapp/cron.py
    import cronjobs

    @cronjobs.register
    def periodic_task():
        pass

django-cronjobs will then recognize ``periodic_task`` as a valid job.


Running a cron job
==================

To run a registered cron job, use the ``cron`` management command::

    $ ./manage.py cron <job_name>

So to run ``periodic_task`` from above, you could use::

    $ ./manage.py cron periodic_task

Additional arguments can be passed after the name of the task.


Locks
=====

By default, cron jobs are locked so that only one copy of a given job can be
running at a time. If you need to override this behavior, you can pass the
``lock`` kwarg to ``register``::

    from cronjobs import register
    @register(lock=False)
    def my_cron_job():
        # Multiple instances of me can run simultaneously.

If you run multiple sets of cronjobs on the same file system and need the locks
to not collide, set ``CRONJOB_LOCK_PREFIX`` to something unique in your Django
settings.
