"""
Copyright, the CVXPY authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__version__ = "1.1.0a4"

import cvxpy.interface.scipy_wrapper
from cvxpy.atoms import *
from cvxpy.constraints import NonPos, PSD, SOC, Zero
from cvxpy.error import DCPError, DGPError, DPPError, SolverError, disable_warnings, enable_warnings, warnings_enabled
from cvxpy.expressions.constants import CallbackParam, Constant, Parameter
from cvxpy.expressions.variable import Variable
from cvxpy.problems.objective import Maximize, Minimize
from cvxpy.problems.problem import Problem
from cvxpy.reductions import *
from cvxpy.reductions.solvers.defines import installed_solvers
from cvxpy.settings import (
    CBC,
    CPLEX,
    CVXOPT,
    DIFFCP,
    ECOS,
    GLPK,
    GLPK_MI,
    GUROBI,
    INFEASIBLE,
    INFEASIBLE_INACCURATE,
    MOSEK,
    NAG,
    OPTIMAL,
    OPTIMAL_INACCURATE,
    OSQP,
    ROBUST_KKTSOLVER,
    SCIP,
    SCS,
    SOLVER_ERROR,
    SUPER_SCS,
    UNBOUNDED,
    UNBOUNDED_INACCURATE,
    XPRESS,
)
from cvxpy.transforms import linearize, partial_optimize, suppfunc
