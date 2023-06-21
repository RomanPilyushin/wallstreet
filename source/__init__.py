from source.wallstreet import Stock, Call, Put
from pkg_resources import get_distribution, DistributionNotFound
import os.path

__all__ = ['Stock', 'Call', 'Put']

try:
    _dist = get_distribution('source')
    # Normalize case for Windows systems
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'source')):
        # not installed, but there is another version that *is*
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Please install this project with setup.py'
else:
    __version__ = _dist.version