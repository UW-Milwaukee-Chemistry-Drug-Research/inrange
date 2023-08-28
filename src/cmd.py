from chimerax.core.commands import CmdDesc      # Command description
from chimerax.core.commands import IntArg       # Integer argument
from chimerax.core.commands import FloatArg       # Integer argument
from chimerax.core.commands import EmptyArg     # (see below)
from chimerax.core.commands import Or # Argument modifiers
from chimerax.core.commands import run # Argument modifiers

def inrange(session, site, distance=5):
    """Report center of mass of given atoms."""

    # ``session``     - ``chimerax.core.session.Session`` instance
    # ``atoms``       - ``chimerax.atomic.Atoms`` instance or None
    # ``weighted``    - boolean, whether to include atomic mass in calculation
    # ``transformed`` - boolean, use scene rather than original coordinates

    #assemble command
    run(f"select {site} @ < {distance} ~{site}")

    session.logger.info("Processing Done")


inrange_desc = CmdDesc(required=[("site", Or(IntArg, EmptyArg))],
                    optional=[("distance", Or(IntArg, FloatArg))])
