# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta, Pool

__all__ = ['Certification']


class Certification:
    __name__ = 'project.certification'
    __metaclass__ = PoolMeta

    @classmethod
    def confirm(cls, certifications):
        Milestone = Pool().get('project.invoice_milestone')

        super(Certification, cls).confirm(certifications)

        milestones = []
        for cert in certifications:
            for x in cert.lines:
                for y in x.work.milestones:
                    milestones.append(y)
            milestones += cert.work.milestones
        if milestones:
            Milestone.check_trigger(milestones)
