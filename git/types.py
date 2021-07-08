# -*- coding: utf-8 -*-
# This module is part of GitPython and is released under
# the BSD License: http://www.opensource.org/licenses/bsd-license.php

import os
import sys
from typing import Dict, Union, Any, TYPE_CHECKING


if sys.version_info[:2] >= (3, 8):
    from typing import Final, Literal, SupportsIndex, TypedDict, Protocol  # noqa: F401
else:
    from typing_extensions import Final, Literal, SupportsIndex, TypedDict, Protocol  # noqa: F401

if sys.version_info[:2] >= (3, 10):
    from typing import TypeGuard  # noqa: F401
else:
    from typing_extensions import TypeGuard  # noqa: F401


if sys.version_info[:2] < (3, 9):
    PathLike = Union[str, os.PathLike]
elif sys.version_info[:2] >= (3, 9):
    # os.PathLike only becomes subscriptable from Python 3.9 onwards
    PathLike = Union[str, 'os.PathLike[str]']  # forward ref as pylance complains unless editing with py3.9+

if TYPE_CHECKING:
    from git.objects import Commit, Tree, TagObject, Blob
    # from git.refs import SymbolicReference

TBD = Any

Tree_ish = Union['Commit', 'Tree']
Commit_ish = Union['Commit', 'TagObject', 'Blob', 'Tree']

Lit_config_levels = Literal['system', 'global', 'user', 'repository']


class Files_TD(TypedDict):
    insertions: int
    deletions: int
    lines: int


class Total_TD(TypedDict):
    insertions: int
    deletions: int
    lines: int
    files: int


class HSH_TD(TypedDict):
    total: Total_TD
    files: Dict[PathLike, Files_TD]
