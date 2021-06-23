# -*- coding: utf-8 -*-
from collections import OrderedDict as _OrderedDict
from dataclasses import asdict as _asdict
from dataclasses import dataclass as _dataclass
from enum import Enum as _Enum
from typing import List as _List

import networkx as _nx


class Category(_Enum):  # pragma: no cover
    """ISIC4 categories enum."""

    SECTION = 1
    DIVISION = 2
    GROUP = 3
    CLASS = 4


class Standards(_Enum):  # pragma: no cover
    """Industry classification standards enum."""

    ISIC3 = "ISIC3"
    ISIC31 = "ISIC31"
    ISIC4 = "ISIC4"
    NACE2 = "NACE2"
    NAICS2017 = "NAICS2017"
    TSIC2552 = "TSIC2552"
    JSIC13 = "JSIC13"


@_dataclass
class Classification:
    """Classification base object for use across standards.

    Examples:
        The NAICS2017 class "Space Research and Technology" can be represented as

        >>> Classification(
        ...     code="927110",
        ...     description="Space Research and Technology"
        ... )
        Classification(code='927110', description='Space Research and Technology', category=None)
    """

    code: str
    description: str = None
    category: Category = None

    def to_dict(self):
        """Return self as dict."""
        return _asdict(self)


class Standard(_OrderedDict):
    def __init__(self, standard: Standards, classes: _List[Classification]):
        """Industry classification standard.

        A Standard defines all classes (i.e., classifications) belonging to a
        standard.

        Args:
            standard: enum to reference standard
            classes: all included classes (i.e., codes) defined in the standard

        Examples:
            A subset of the NAICS2017 standard can be represented as

            >>> Standard(
            ...     standard=Standards.NAICS2017,
            ...     classes=[
            ...         Classification("111110", "Soybean Farming"),
            ...         Classification("111120", "Oilseed (except Soybean) Farming"),
            ...         Classification("111130", "Dry Pea and Bean Farming"),
            ...     ]
            ... )

        """
        super().__init__(self)
        self.standard = standard
        self._classes = classes

        # Add classes as key/vals and as node shortcuts
        for node in classes:
            self[node.code] = node.to_dict()

    def __repr__(self) -> str:  # pragma: no cover
        """Return repr(self)."""
        return f"StandardImpl({self.standard.value})"


class Concordance(_nx.DiGraph):
    def __init__(self, src: Standard, dst: Standard, concordances: _List[tuple]):
        """Industry classification concordance.

        Concordances define direct relationships between classification
        systems. The relationships are directed (from => to) from classes
        in a source standard to classes in a destination standard. Accordingly,
        Concordances are implemented as a directed graph.

        Given source and destination classification standards, all defined
        classes are added as nodes in the graph. Concordances are added as
        relationships between nodes in the graph.

        Concordant classes are discovered by returning all descendants of a
        given node.

        Note:
            Concordances must be directed acyclic graphs.

        Args:
            src: source standard to map concordances from
            dst: destination standard to map concordances to
            concordances: directed relationships between classes in the source
                and destination standards
        """
        super().__init__(self)
        self.src = src
        self.dst = dst
        self._concordances = concordances

        # Add all nodes to the graph
        for std in [src, dst]:
            for node in std._classes:
                self.add_node((std.standard, node.code), **node.to_dict())

        # Add all concordance edges
        self.add_edges_from(concordances)

        # Assert the resulting graph is acyclic
        # TODO: use shortest paths to handle cyclic graphs?
        assert _nx.algorithms.dag.is_directed_acyclic_graph(self)

    def __repr__(self) -> str:  # pragma: no cover
        """Return repr(self)."""
        return f"Concordance({self.src.standard.value} => {self.dst.standard.value})"

    def concordant(self, code: str) -> set:
        """Return set of concordant industry classifications (i.e., descendants).

        Args:
            code: source classification code (e.g., "927110" from NAICS2017)

        Returns:
            set: concordant (i.e., descandant) nodes from the given code

        Examples:
            >>> pyisic.NAICS2017_to_ISIC4.concordant("927110")
            {(<Standards.ISIC4: 'ISIC4'>, '5120'), (<Standards.ISIC4: 'ISIC4'>, '8413')}
        """
        try:
            nodes = {
                node
                for node in _nx.algorithms.dag.descendants(self, (self.src.standard, code))
                if node[0] == self.dst.standard
            }
        except _nx.exception.NetworkXError:
            nodes = set()
        return nodes


class ComposedGraph(_nx.DiGraph):
    def __init__(self, dst: Standard, concordances=_List[Concordance]):
        """Composed graph of industry classification concordance.

        Args:
            dst: destination standard
            concordances: iterable of concordances
        """
        super().__init__(self)
        self.dst = dst

        for cc in concordances:

            # Add all nodes to the graph
            for std in [cc.src, cc.dst]:
                for node in std._classes:
                    self.add_node((std.standard, node.code), **node.to_dict())

            # Add all concordance edges
            self.add_edges_from(cc._concordances)

    def __call__(self, code: str, src: str) -> set:
        """Return set of concordant industry classifications.

        Args:
            code: source classification code (e.g., "927110" from NAICS2017)
            src: source standard (e.g., "NAICS2017")

        Returns:
            set: concordant nodes from the given source code

        Examples:
            >>> pyisic.ToISIC4("927110", Standards.NAICS2017)
            {(<Standards.ISIC4: 'ISIC4'>, '5120'), (<Standards.ISIC4: 'ISIC4'>, '8413')}
        """
        try:
            nodes = {node for node in _nx.algorithms.dag.descendants(self, (src, code)) if node[0] == self.dst}
        except _nx.exception.NetworkXError:
            nodes = set()
        return nodes
