from factory import Handler

if __name__ == "__main__":
    # bug of script: it can't edit a xml file if it isn't already existed
    handler = Handler().select_editor()
    handler.editor()
