from rich.layout import Layout
from uecli.logger import *
from . import themes

class SplitDirection(Enum):
    ROW = "row"
    COLUMN = "column"


@dataclass
class SplitItemOptions:
    name: str
    ratio: int


def get_child(layout: Layout, name: str) -> Layout:
    result: Layout = None
    for child in layout.children:
        if child.name == name:
            result = child
            break

    if result is None:
        raise ValueError(f"Child {name} not found")

    return result

def split_layout(layout: Layout, items: List[SplitItemOptions],
                 split_direction: SplitDirection = SplitDirection.COLUMN) -> Layout:
    item_layouts: List[Layout] = []
    for item in items:
        item_layouts.append(Layout(name=item.name, ratio=item.ratio))

    if split_direction == SplitDirection.ROW:
        layout.split_row(*item_layouts)
    elif split_direction == SplitDirection.COLUMN:
        layout.split_column(*item_layouts)
    else:
        raise ValueError("Invalid Split Direction")
    return layout


from . import screen

from . import menu_screen
from . import content_screen
from . import home_screen