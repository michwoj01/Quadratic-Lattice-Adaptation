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
    # used in defining production's left-side
    hanging_ignore: bool = False

    # compares and hashes only label
    def __eq__(self, other):
        return isinstance(other, Node) and self.label == other.label
    def __hash__(self):
        return hash(self.label)

    def get_matcher_label(self) -> dict[str, any]:
        """
        :return: GraphMatcher label, what do we care for in isomorphism matching
        For hyper-nodes: only match its tag
        For normal nodes: no not care at all (can match any node)
        """
        if self.hyper:
            # hyper-node tested here
            # not matching boundary, only tag (E/Q/...) and R property
            return { "hyper-tag": self.hyperref.tag,
                     "hyper-rip": self.hyperref.rip }
        else:
            # normal node
            if self.hanging_ignore:
                return { }
            else:
                return { "hanging": self.hanging }


    def get_display_label(self):
        """
        :return: Pretty display name, disable for debugging
        """
        if self.hyper:
            return self.hyperref.tag
            return self.label.replace("n", "").replace("m", "")

        return self.label