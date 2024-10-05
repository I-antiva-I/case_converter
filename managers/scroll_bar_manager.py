from PyQt5.QtWidgets import QWidget


def manage_scroll_bar(root_component: QWidget, root_block_name: str, max_value) -> None:
    """
    Manages stylesheet class of a widget with a scrollbar

    :param root_component: A widget with a scrollbar
    :param root_block_name:  Base stylesheet class of `root_component`
    :param max_value: Maximum value of a scrollbar
    """

    if max_value == 0:
        root_component.setProperty("class", f"{root_block_name} {root_block_name}--without-scroll-bar")
    else:
        root_component.setProperty("class", f"{root_block_name} {root_block_name}--with-scroll-bar")

    # Reload stylesheet
    root_component.setStyleSheet("")