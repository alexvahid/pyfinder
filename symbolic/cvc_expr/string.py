import logging

import CVC4

from .expression import CVCExpression
from .integer import CVCInteger

log = logging.getLogger("se.cvc.string")


class CVCString(CVCExpression):
    @classmethod
    def variable(cls, name, solver):
        em = solver.getExprManager()
        expr = em.mkVar(name, em.stringType())
        return cls(expr, solver)

    @classmethod
    def constant(cls, v, solver):
        em = solver.getExprManager()

        # The CVC4 String constructor treats '' as a string of length 1 containing the null byte.
        # The empty constructor actually creates an empty string.
        if len(v) == 0:
            cvcstr = CVC4.CVC4String()
        else:
            cvcstr = CVC4.CVC4String(v)

        return cls(em.mkConst(cvcstr), solver)

    def getvalue(self):
        ce = self.solver.getValue(self.cvc_expr)
        return ce.getConstString().toString()

    def len(self):
        return CVCInteger(self.em.mkExpr(CVC4.STRING_LENGTH, self.cvc_expr), self.solver)

    def __add__(self, other):
        return CVCString(self.em.mkExpr(CVC4.STRING_CONCAT,
            self.cvc_expr, other.cvc_expr), self.solver)
