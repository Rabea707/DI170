def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()                                  # both defaults
make_shirt("medium")                          # custom size, default text
make_shirt(size="small", text="Custom message")  # keyword arguments