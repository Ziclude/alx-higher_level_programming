#!/usr/bin/python3
if __name__ == "__main__":
    """print all hidden names in hidden_4 module."""
    import hidden_4
    nms = dir(hidden_4)
    for name in nms:
        if name[:2] != "__":
            print(name)
