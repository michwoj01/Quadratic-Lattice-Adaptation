from dataclasses import dataclass

@dataclass(frozen=True)
class Node:
    # only for plotting, do not compare
    x: float
    y: float
    # main identification string
    label: str
    # extra args
    hanging: bool = False
    hyper: bool = False
    hyperref: any = None # type HyperEdge

    # compares and hashes only label
    def __eq__(self, other):
        return isinstance(other, Node) and self.label == other.label
    def __hash__(self):
        return hash(self.label)

    def get_matcher_label(self):
        """
        :return: GraphMatcher label, what do we care for in isomorphism matching
        For hyper-nodes: only match its tag
        For normal nodes: no not care at all (can match any node)
        """
        if self.hyper:
            return self.hyperref.tag

        return ""


    def get_display_label(self):
        """
        :return: Pretty display name, disable for debugging
        """
        if self.hyper:
            return self.hyperref.tag
            return self.label.replace("n", "").replace("m", "")

        return self.label