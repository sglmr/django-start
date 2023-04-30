class View:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


new_view = View(yup=300, hi=500)


print(new_view.yup)
