from PyQt5.QtWidgets import QWidget


def manage_scroll_bar(root_component: QWidget, root_block_name: str, max_value):
    if max_value == 0:
        root_component.setProperty("class", f"{root_block_name} {root_block_name}--without-scroll-bar")
    else:
        root_component.setProperty("class", f"{root_block_name} {root_block_name}--with-scroll-bar")

    root_component.setStyleSheet("")